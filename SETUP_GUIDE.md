# 🎤 BHARAT BIZ-AGENT - SETUP GUIDE

## Quick Start

### Windows Users
```batch
# Double-click run.bat
run.bat
```

Server will start at: **http://localhost:8000**

### Mac/Linux Users
```bash
# Install dependencies
python -m pip install -r requirements.txt

# Initialize database
cd backend
python -c "from db import init_db; init_db()"

# Start server
python -m uvicorn main:app --reload --port 8000
```

---

## Features Implemented ✓

###🎤 Voice & Multilingual Support
- ✓ Speech-to-Text (Browser API + Whisper API ready)
- ✓ Hindi/Hinglish/English recognition
- ✓ Text-to-Speech in multiple languages
- ✓ Code-mixed language handling (e.g., "2 kg chawal 60 rupaye")

### 💰 Billing & Finance
- ✓ Automatic item extraction from voice
- ✓ GST calculation (5% for food, 18% for general, 28% for luxury)
- ✓ UPI string generation
- ✓ **UPI QR Code generation** (embedded in PDF)
- ✓ Professional PDF invoice generation
- ✓ Customer mobile tracking

### 🤖 Agentic AI
- ✓ Intent detection (greeting, billing, payment, etc.)
- ✓ Draft action generation
- ✓ **Human-in-the-loop confirmation** (Confirm/Cancel)
- ✓ Structured data extraction
- ✓ GPT integration (optional, fallback regex available)

### 💾 Database & Records
- ✓ SQLite database with full schema
- ✓ Invoice storage and retrieval
- ✓ Customer management
- ✓ Payment tracking
- ✓ Product catalog (50+ items)

### 📊 Business Intelligence
- ✓ Today's sales summary
- ✓ Customer statistics
- ✓ Payment pending tracking
- ✓ Customer loyalty tracking

### 🔒 Safety & Confirmation
- ✓ Draft-based approach (no actions without confirmation)
- ✓ Multi-language confirmation (Yes/No/Cancel)
- ✓ Edit capability before confirmation
- ✓ Transaction logging

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Frontend UI |
| `/health` | GET | Health check |
| `/chat` | POST | Process voice/text input |
| `/confirm` | POST | Confirm draft actions |
| `/invoice/{id}` | GET | Download invoice PDF |
| `/summary` | GET | Business summary |
| `/customers` | GET | List customers |
| `/invoices` | GET | List invoices |
| `/transcribe` | POST | Transcribe audio (Whisper) |
| `/upload` | POST | Upload bill screenshot |

---

## Configuration

### Optional: Use OpenAI Features

1. Create `.env` file from `.env.example`
2. Add your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Server will automatically use GPT for better Hinglish extraction

### Without OpenAI
- System uses regex-based extraction (works great!)
- Supports 50+ common items in database
- Falls back gracefully for unknown items

---

## Example Voice Commands

### Hindi/Hinglish
- **"2 kilo chawal 60 rupaye, 1 kilo tel 150"**
- **"GST add kar do"** (not needed - automatic)
- **"Aaj ka sales dikha"** (Show today's sales)
- **"Customer mobile 9876543210"**

### English (India-English)
- **"2 kg rice at 60, 1 kg oil at 150"**
- **"Show today's sales"**
- **"Record payment of 500 rupees via UPI"**

### Code-Mixed (Recommended - Most Natural)
- **"2 kg chawal 60 rupaye, 1 bottle tel 150"**
- **"Make bill for 3 pieces eggs 6 rupaye per piece"**

---

## Usage Workflow

1. **Start talking**: Press 🎤 or type a message
2. **Agent extracts items**: Automatically parses quantities, prices, units
3. **Draft created**: Shows what will be billed
4. **Confirm**: Select ✓ Confirm or ✗ Cancel
5. **Invoice generated**: PDF with QR code created
6. **Download**: Click 📄 Download Invoice PDF
7. **Database updated**: Customer record stored

---

## Troubleshooting

### Server won't start
```
Error: Port 8000 in use
→ Change in run.bat: --port 8001
```

### Database errors
```
Error: Database locked
→ Delete backend/billing.db and restart
→ System will recreate it automatically
```

### Voice not working
```
Chrome: Make sure microphone permission is granted
Firefox: Same as Chrome
Safari: Enable Microphone permission in Settings
IE: Not supported - use modern browser
```

### Missing modules
```
pip install -r requirements.txt
# or
python -m pip install qrcode[pil] openai reportlab fastapi uvicorn
```

---

## System Architecture

```
Voice Input (Hindi/Hinglish/English)
         ↓
Speech-to-Text (Browser API / Whisper)
         ↓
Agent Brain (GPT / Regex Extraction)
         ↓
Item Extraction → GST Calculation → Total Amount
         ↓
Draft Action (Human Review)
         ↓
Confirm / Cancel (User Input)
         ↓
PDF Generator + QR Code + Database Storage
         ↓
Invoice Ready + Download Link
```

---

## Technology Stack

**Frontend:**
- HTML5 + CSS3
- Vanilla JavaScript
- Speech Recognition API (Web API)
- Speech Synthesis API (Web API)

**Backend:**
- FastAPI (Python web framework)
- Uvicorn (ASGI server)
- SQLite (Database)
- ReportLab (PDF generation)
- QRCode (QR code generation)
- OpenAI API (Optional - Whisper, GPT)
- Pillow (Image processing)

---

## Features for Judges

✓ **Not just chat** - Real PDF generation + QR codes
✓ **India-first** - GST + UPI + Mobile tracking
✓ **Multilingual** - Hindi, Hinglish, English
✓ **Agentic** - Executes actions, not just talks
✓ **Safe** - Human confirmation required
✓ **Extensible** - Ready for inventory, credit tracking, WhatsApp

---

## Support

For issues or questions:
1. Check troubleshooting section above
2. Verify Python 3.10+ installed
3. Run: `python -m pip install -r requirements.txt`
4. Check logs in terminal

---

**Built with ❤️ for Indian businesses**
Bharat Biz-Agent v1.0.0
