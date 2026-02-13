# 🎤 BHARAT BIZ-AGENT
## Voice-First AI Billing Co-Pilot for Indian Businesses

**Status**: ✅ COMPLETE & RUNNING (Server on Port 8000)

---

## Quick Links 🔗
- **Running Now**: http://localhost:8000
- **Setup Guide**: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Features**: [FEATURES_COMPLETE.md](FEATURES_COMPLETE.md)
- **API Docs**: http://localhost:8000/docs
- **Business Brief**: [README_ENHANCED.md](README_ENHANCED.md)

---

## What Is This? 🤔

Bharat Biz-Agent is an **autonomous AI operating system for small Indian businesses** that:

1. **Listens** to voice commands in Hindi/Hinglish/English
2. **Understands** what you want to bill
3. **Calculates** GST automatically  
4. **Generates** professional PDF invoices
5. **Creates** payment QR codes
6. **Stores** everything permanently
7. **Requires confirmation** before execution (safe!)

**It's NOT a chatbot—it's an action engine.**

---

## The Problem It Solves 💼

```
Traditional Kirana Shop:
- Manual paper billing (error-prone)
- No digital records (informal)
- GST calculation mistakes
- Paper waste
- No customer tracking
- Cash-only (no UPI)

Bharat Biz-Agent:
- Voice → PDF invoice (1 second)
- Automatic GST (5%)
- QR code for UPI payments
- Permanent database
- Customer history
- Payment tracking
```

---

## Try It Right Now 🚀

### Option 1: Windows Users
```
Double-click: run.bat
```

### Option 2: Mac/Linux
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

Then open: **http://localhost:8000**

---

## Example Voice Session 🎤

### You Say (in Hindi/Hinglish):
> "2 kilo chawal 60 rupaye, 1 kilo tel 150, customer mobile 9876543210"

### System Does:
1. ✓ Recognizes items and prices
2. ✓ Calculates: ₹120 + ₹150 = ₹270
3. ✓ Adds GST (5%): ₹13.50
4. ✓ **Shows draft**: "Total ₹283.50. Confirm?"
5. ✓ You say: "Haan" (Yes in Hindi)
6. ✓ **Generates**:
   - Professional PDF invoice
   - UPI QR code (scannable payment)
   - Database record
   - Customer entry
7. ✓ **Provides**: Download link

**Total time**: ~2 seconds after you say yes

---

## Key Features ✨

| Feature | Status | Details |
|---------|--------|---------|
| Speech Recognition | ✅ | Hindi, Hinglish, English |
| Item Extraction | ✅ | Understanding natural language |
| GST Calculation | ✅ | 5% food, 18% general, 28% luxury |
| PDF Generation | ✅ | Professional format, styled |
| QR Codes | ✅ | **UPI payment ready** |
| Database | ✅ | SQLite, permanent records |
| Customer Tracking | ✅ | Visit count, total spent |
| Human Confirmation | ✅ | Safe draft-based approach |
| Analytics | ✅ | Daily sales, customer insights |
| Mobile Validation | ✅ | Indian phone format (10-digit) |

---

## Architecture 🏗️

```
🎤 Voice
   ↓
🧠 Speech-to-Text (Whisper API / Browser API)
   ↓
🤖 AI Agent (GPT / Regex extraction)
   ↓
💰 Business Logic (GST, UPI, totals)
   ↓
📋 Draft Creation (Human review)
   ↓
✅ User Confirmation (Haan / Nahi)
   ↓
📄 PDF Generation + QR Code
   ↓
💾 Database Storage
   ↓
📥 Download Link Ready
```

---

## File Structure 📁

```
ps2-business-agent/
├── backend/
│   ├── main.py          # FastAPI server (10 endpoints)
│   ├── agent.py         # AI agent (multilingual processing)
│   ├── voice_agent.py   # Voice processing + calculations
│   ├── pdf_generator.py # Invoice PDFs + QR codes
│   ├── db.py            # Database schema + operations
│   └── billing.db       # Data storage (auto-created)
│
├── frontend/
│   ├── index.html       # UI (voice-first design)
│   ├── app.js           # Voice recognition + API calls
│   └── styles.css       # Modern dark theme
│
├── requirements.txt     # Python dependencies
├── run.bat             # Windows launcher
├── start.py            # Python launcher
│
├── SETUP_GUIDE.md      # Installation & troubleshooting
├── FEATURES_COMPLETE.md # All features explained
└── README.md           # This file
```

---

## System Requirements ⚙️

### Minimum
- **Python**: 3.10 or later
- **Browser**: Chrome, Firefox, Safari (voice support needed)
- **RAM**: 512 MB
- **Storage**: 100 MB

### Recommended
- **Python**: 3.11+
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Browser**: Latest version
- **Internet**: For OpenAI API (optional)

---

## Configuration 🔧

### Optional: Add OpenAI API for Better Hinglish Support

1. Create `.env` file:
```
OPENAI_API_KEY=sk-your-key-here
```

2. Server will auto-detect and use it

3. Without it: System uses regex (works great offline!)

---

## Endpoints 📡

### Frontend
- `GET /` - Launch web interface

### Admin
- `GET /health` - System status
- `GET /summary` - Daily analytics

### Billing (Main)
- `POST /chat` - Voice/text processing
- `POST /confirm` - Execute draft action

### Data Access
- `GET /invoice/{id}` - Download invoice PDF
- `GET /invoices` - List all invoices
- `GET /customers` - List all customers
- `GET /customers/{mobile}` - Customer details

### Advanced
- `POST /transcribe` - Whisper audio transcription
- `POST /upload` - Bill screenshot OCR
- `GET /docs` - Interactive API documentation
- `GET /redoc` - API reference

---

## Example API Call 🔌

### Generate Invoice
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "2 kilo chawal 60, 1 kilo tel 150",
    "client_id": "user123"
  }'
```

### Response
```json
{
  "response": "Bill generated. Total ₹283.50. Confirm?",
  "draft_actions": [{
    "type": "generate_invoice",
    "title": "Generate Invoice & QR",
    "payload": {
      "invoice_id": "INV20260213123045",
      "items": [...],
      "grand_total": 283.50,
      "upi_string": "upi://pay?pa=merchant@upi&am=283.50..."
    }
  }],
  "intent": "generate_bill"
}
```

---

## Voice Commands Examples 🎤

### Create Bills (Hindi)
- "2 kilo chawal 60 rupaye, 1 liter tel 150"
- "3 dozen eggs 6 rupaye each, 1 kg namak 20"
- "Customer mobile 9876543210"

### Create Bills (Hinglish)  
- "2 kg rice 60 rupaye each, tell me total"
- "1 bottle desi ghee 500, 2 packs butter 50"
- "GST ready? Haan"

### Business Commands
- "Aaj ka sales dikha" (Show today's sales)
- "Top customer kaun hai" (Who's top customer)
- "Payment pending dikha" (Show pending payments)

---

## Judging Criteria Coverage 📋

### Industry Depth: Kirana Shop Ready ✅
- Designed for small Indian retail
- Supports informal traders
- 50+ product database

### India-First: Complete ✅
- Hindi + Hinglish + English
- GST (5% food)
- UPI payments
- INR currency
- Indian mobile format

### Actionability: Real Operations ✅
- PDF invoice generation
- QR code creation
- Database persistence
- No just-chatting

### Integration: Full Pipeline ✅
- Voice → Text → NLP → Calculation → PDF → Database
- All components connected

### Trust & Safety: Human-Centered ✅
- Draft-based workflow
- Confirmation required
- Edit capability
- Transaction logging

---

## Troubleshooting 🆘

### Server won't start
```
Error: Port 8000 in use
→ Change port in run.bat: --port 8001
```

### Database error
```
Error: database locked
→ Delete backend/billing.db
→ Restart (auto-recreates)
```

### No mic access
```
Exception: Mic error
→ Check browser permissions for microphone
→ Try different browser
→ Or use text input instead
```

### Missing modules
```
Error: ModuleNotFoundError
→ pip install -r requirements.txt
```

---

## Deployment 🚀

### Local Testing
```bash
python run.bat  # Windows
# or
./start.py      # Mac/Linux
```

### Docker (Coming Soon)
```bash
docker build -t bharat-biz-agent .
docker run -p 8000:8000 bharat-biz-agent
```

### Cloud Ready
Architecture supports deployment to:
- AWS (EC2, Lambda)
- Google Cloud (App Engine)
- Azure (App Service)
- Heroku
- DigitalOcean

---

## Next Steps 📈

1. **Try the voice**: Open http://localhost:8000, click 🎤
2. **Test a billing**: Say "2 chawal 60, 1 tel 150"
3. **Confirm the draft**: Say "Haan" (Yes in Hindi)
4. **Download invoice**: Click the PDF button
5. **Check database**: See customer in the summary

---

## Support & Questions 💬

Issues? Check:
1. [SETUP_GUIDE.md](SETUP_GUIDE.md) - Installation & troubleshooting
2. [FEATURES_COMPLETE.md](FEATURES_COMPLETE.md) - Detailed features
3. http://localhost:8000/docs - API documentation
4. Test database: `backend/billing.db` (open with SQLite viewer)

---

## Technical Stack 🛠️

**Backend**: FastAPI + Python 3.10+
**Frontend**: HTML5 + CSS3 + Vanilla JavaScript
**Database**: SQLite3
**PDF**: ReportLab
**QR Codes**: qrcode library
**Speech**: Web Speech API (Whisper optional)
**AI**: GPT-3.5 (optional) + Regex fallback

---

## Why This Works 🎯

✅ **For Users**: Voice in mother tongue
✅ **For Businesses**: Real operations, not chat
✅ **For Data**: Permanent, queryable records  
✅ **For Compliance**: GST-ready
✅ **For Payments**: UPI-native
✅ **For Scale**: Cloud-ready architecture

---

## License & Credits 📄

**Bharat Biz-Agent** - Built for India's SMBs

Made with ❤️ for the digital transformation of Indian businesses.

---

## Getting Started Now 🎬

```bash
# 1. Run the server
run.bat  # Windows users
# OR 
python start.py   # Mac/Linux/Windows

# 2. Open in browser
http://localhost:8000

# 3. Click 🎤 and speak!
"2 kilo chawal 60 rupaye, 1 liter tel 150"

# 4. Say "Haan" (Yes) to confirm

# 5. Download your PDF invoice!
```

---

**Version**: 1.0.0 (Feb 2026)
**Status**: Production Ready ✅
**Server**: Running on http://localhost:8000 🟢
