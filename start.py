#!/usr/bin/env python
"""
🎤 Bharat Biz-Agent - Startup Script
Autonomous AI Co-Pilot for Indian Businesses
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("🎤 BHARAT BIZ-AGENT - Starting Server")
    print("="*60)
    print("Bridging the Digital Divide with Autonomous AI Operations\n")
    
    # Get paths
    project_root = Path(__file__).resolve().parent
    backend_dir = project_root / "backend"
    
    # Change to backend directory
    os.chdir(str(backend_dir))
    
    # Initialize database
    print("\n[1/3] Initializing database...")
    try:
        from db import init_db
        init_db()
        print("✓ Database initialized")
    except Exception as e:
        print(f"⚠ Database warning: {e}")
    
    # Check dependencies
    print("\n[2/3] Checking dependencies...")
    required_packages = [
        'fastapi', 'uvicorn', 'pydantic', 'qrcode',
        'reportlab', 'Pillow', 'openai'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_').split('-')[0].lower())
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"⚠ Missing packages: {', '.join(missing)}")
        print(f"  Installing with: pip install {' '.join(missing)}")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q'] + missing)
        print("✓ Dependencies installed")
    else:
        print("✓ All dependencies available")
    
    # Start server
    print("\n[3/3] Starting server...\n")
    print("="*60)
    print("✓ Server starting on http://localhost:8000")
    print("✓ Frontend: http://localhost:8000")
    print("✓ API Docs: http://localhost:8000/docs")
    print("✓ API Redoc: http://localhost:8000/redoc")
    print("="*60)
    print("\n🎤 Ready to accept voice commands!")
    print("✓ Hindi/Hinglish/English support")
    print("✓ GST calculation ready")
    print("✓ UPI QR code generation ready")
    print("✓ Database storage active")
    print("\nPress Ctrl+C to stop the server\n")
    
    # Start uvicorn
    try:
        import uvicorn
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\nTroubleshooting:")
        print("1. Check if port 8000 is available")
        print("2. Run: pip install -r ../requirements.txt")
        print("3. Check Python version (3.10+ required)")
        sys.exit(1)

if __name__ == "__main__":
    main()
