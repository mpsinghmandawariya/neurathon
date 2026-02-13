# How to Run VoiceBillingAI

## Method 1: Double-click run.bat
1. Go to folder: `ps2-business-agent`
2. Double-click: `run.bat`
3. Browser opens automatically at http://localhost:8000

## Method 2: Command Line
```bash
cd ps2-business-agent
run.bat
```

## Method 3: Manual
```bash
cd ps2-business-agent\backend
python -m uvicorn main:app --reload --port 8000
```

Then open: http://localhost:8000

## What Happens
- Database initializes
- Server starts on port 8000
- Frontend loads
- Ready to use!

## Test It
1. Type: "2 kg rice at 60, 1 kg sugar at 42"
2. Click: "Confirm"
3. Click: "📄 Download Invoice PDF"
4. PDF opens!
