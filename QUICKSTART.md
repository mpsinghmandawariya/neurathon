# Quick Start Guide - Bharat Biz-Agent

## Running the Application

### Option 1: Using Batch File (Windows)
```bash
start.bat
```

### Option 2: Manual Start
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

Then open: http://localhost:8000

## Sample Commands to Try

### Bills
- "Create bill for 2kg rice at 60, 1kg sugar at 42 with GST"
- "Generate bill for 5 packets biscuits at 30"
- "Bill for customer 9876543210: 3kg wheat at 45"

### Products
- "Add product Rice price 60 stock 100 category Groceries"
- "Check low stock items"
- "Show all products"

### Customers
- "Add customer Ramesh mobile 9876543210"
- "Show top customers"

### Payments
- "Record payment of Rs 1500 from Ramesh via UPI today"
- "Payment received Rs 2000 reference UPI123456"

### Expenses
- "Add expense Rs 5000 for rent"
- "Record expense Rs 2500 for electricity"

### Reports & Analytics
- "Show today's sales report"
- "What are today's sales?"
- "Show sales trend"

### Reminders
- "Remind me to call supplier tomorrow"
- "Set reminder to follow up with Priya"

## API Endpoints

### Main Endpoints
- POST /chat - Send messages to agent
- POST /confirm - Confirm draft actions
- GET /summary - Dashboard data

### Data Endpoints
- GET /products - List all products
- GET /customers - List all customers
- GET /analytics/sales - Sales analytics
- GET /analytics/trend - Sales trend

## Database Location
`backend/ledger.db`

## Sample Data
Run `python seed_data.py` to populate with sample data:
- 8 products
- 5 customers
- 2 bills
- Sample payments, expenses, reminders

## Features
✓ Multi-language support (Hindi/English/Hinglish)
✓ GST calculation
✓ UPI payment strings
✓ Inventory tracking
✓ Customer management
✓ Expense tracking
✓ Business analytics
✓ Voice input/output
✓ OCR for screenshots
