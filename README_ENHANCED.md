# Bharat Biz-Agent - Complete Business Management System

An advanced India-first business agent with comprehensive features for managing bills, inventory, customers, expenses, and analytics.

## 🚀 Features

### Core Features
- **Smart Bill Generation**: Create bills from Hindi/Hinglish/English with automatic GST calculation
- **UPI Payment Integration**: Generate UPI payment strings for instant collection
- **Customer Management**: Track customer purchases and history
- **Product & Inventory**: Manage stock levels with low-stock alerts
- **Expense Tracking**: Record and categorize business expenses
- **Payment Recording**: Log payments with multiple modes (UPI/NEFT/IMPS)
- **Reminders**: Set reminders for follow-ups and payments
- **Analytics Dashboard**: Sales trends, profit/loss, and business insights

### Advanced Capabilities
- OCR for UPI screenshot extraction
- Voice input/output (Hindi/English)
- Human-in-the-loop confirmation
- SQLite database with full audit trail
- Real-time stock tracking
- Customer purchase history
- Multi-language support

## 📊 Database Schema

### Tables
- **customers**: Customer profiles with purchase history
- **products**: Product catalog with inventory tracking
- **bills**: Complete bill records with GST
- **payments**: Payment transactions
- **reminders**: Task and payment reminders
- **expenses**: Business expense tracking
- **inventory_logs**: Stock movement audit trail
- **business_settings**: Configurable business settings

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR (for screenshot processing)

### Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Tesseract OCR:**
   - Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
   - Add to PATH

3. **Run the server:**
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

4. **Access the app:**
```
http://localhost:8000
```

## 📝 Usage Examples

### Create a Bill
```
"Create bill for 2kg rice at 60, 1kg dal at 120 with GST"
```

### Add Product
```
"Add product Rice price 60 stock 100 category Groceries"
```

### Record Payment
```
"Record payment of Rs 1500 from Ramesh via UPI today"
```

### Add Expense
```
"Add expense Rs 5000 for rent"
```

### Check Stock
```
"Show low stock items"
```

### Sales Report
```
"Show today's sales report"
```

## 🔌 API Endpoints

### Chat & Actions
- `POST /chat` - Main chat interface
- `POST /confirm` - Confirm draft actions
- `POST /upload` - Upload UPI screenshots

### Data Management
- `GET /summary` - Dashboard summary
- `GET /products` - List all products
- `GET /customers` - List all customers

### Analytics
- `GET /analytics/sales` - Sales summary
- `GET /analytics/trend` - Sales trend (7 days)

## 🏗️ Project Structure

```
ps2-business-agent/
├── backend/
│   ├── agent.py          # Main agent logic
│   ├── bill.py           # Bill generation
│   ├── customers.py      # Customer management
│   ├── products.py       # Inventory management
│   ├── expenses.py       # Expense tracking
│   ├── analytics.py      # Business analytics
│   ├── ledger.py         # Transaction ledger
│   ├── parser.py         # Text parsing
│   ├── intent.py         # Intent detection
│   ├── ocr.py            # OCR processing
│   ├── db.py             # Database setup
│   ├── main.py           # FastAPI server
│   └── ledger.db         # SQLite database
├── frontend/
│   ├── index.html        # Web interface
│   ├── app.js            # Frontend logic
│   └── styles.css        # Styling
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🔐 Security & Compliance

- Human-in-the-loop for all database writes
- Draft-first workflow prevents accidental changes
- Complete audit trail in SQLite
- Data minimization principles
- No automatic LLM-driven database modifications

## 🌐 Environment Variables

```bash
OPENAI_API_KEY=your_key          # Optional: For intent detection
MERCHANT_UPI_ID=merchant@upi     # Your UPI ID
```

## 🐳 Docker Deployment

```bash
docker build -t bharat-biz-agent .
docker run -p 8000:8000 bharat-biz-agent
```

## 📈 Business Insights

The system provides:
- Daily/weekly/monthly sales trends
- Top customers by purchase value
- Low stock alerts
- Expense categorization
- Profit/loss calculations
- Payment mode analysis

## 🤝 Contributing

This is a production-ready business management system. Contributions welcome!

## 📄 License

MIT License - Free for commercial use
