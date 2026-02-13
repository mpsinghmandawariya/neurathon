# VoiceBillingAI - Offline Voice Billing Assistant

Offline voice-powered billing assistant with **PDF download button**, GST compliance, and instant UPI payment.

## Features

✓ **Download Button** - Click to download invoice PDF after confirmation
✓ **PDF Invoice Generation** - Professional PDF invoices
✓ **Multiple Items at Once** - Add multiple items in one command
✓ **Voice Input** - Hindi, English, Hinglish support
✓ **Offline Operation** - Works without internet (except UPI)
✓ **GST Compliant** - Automatic tax calculation by category
✓ **Instant UPI** - Generate payment QR codes
✓ **Local Storage** - SQLite database

## Quick Start

```bash
run.bat
```

Open: http://localhost:8000

## Usage Flow

1. **Say items**: "2 kg rice at 60, 1 kg sugar at 42, 3 piece soap at 30"
2. **System shows**: Bill with 3 items, Total: Rs 276.3
3. **Click**: "Confirm" button
4. **Download button appears**: "📄 Download Invoice PDF"
5. **Click download**: PDF opens in new tab
6. **Done**: Invoice saved in database and as PDF

## Voice Commands

### Multiple Items
```
"2 kg rice at 60, 1 kg sugar at 42, 3 piece soap at 30"
"1 liter oil at 150 and 2 kg wheat at 45"
"5 piece biscuit at 20, 1 kg tea at 250, 2 liter milk at 55"
```

### With Customer
```
"2 kg rice at 60, 1 kg sugar at 42 customer 9876543210"
```

## UI Features

- **Chat Interface** - User-friendly conversation
- **Confirm Button** - Approve draft invoices
- **Download Button** - Green button to download PDF
- **Voice Input** - Microphone support (browser-dependent)

## API Response

After confirmation:
```json
{
  "response": "Invoice INV20260212235530 generated successfully!",
  "invoice_id": "INV20260212235530",
  "download_url": "/invoice/INV20260212235530"
}
```

Frontend displays download button using the `download_url`.

## API Endpoints

- `POST /chat` - Voice/text input
- `POST /confirm` - Confirm and get download URL
- `GET /invoice/{invoice_id}` - Download PDF invoice
- `GET /summary` - Daily summary

## PDF Invoice Format

Professional A4 format with:
- Invoice ID, date, time
- Customer mobile
- Itemized list with GST
- Subtotal, GST, Grand Total
- UPI payment string

## Tech Stack

- FastAPI (Backend)
- ReportLab (PDF Generation)
- SQLite (Database)
- JavaScript (Frontend)
- Regex NLP (Offline parsing)

## File Structure

```
ps2-business-agent/
├── backend/
│   ├── agent.py           # Main agent
│   ├── voice_agent.py     # Billing engine
│   ├── pdf_generator.py   # PDF creation
│   ├── db.py              # Database
│   ├── main.py            # API server
│   ├── billing.db         # SQLite DB
│   └── invoices/          # Generated PDFs
├── frontend/
│   ├── index.html         # UI
│   ├── app.js             # Logic + Download button
│   └── styles.css         # Styling
└── run.bat                # Startup script
```

## Test Results

✅ Multiple items extraction
✅ GST calculation
✅ PDF generation
✅ Download button appears after confirm
✅ PDF opens in new tab
✅ Database storage
