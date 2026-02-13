# Deployment Guide - VoiceBillingAI

## Option 1: Railway (Easiest - Free Tier)

1. **Install Railway CLI:**
```bash
npm install -g @railway/cli
```

2. **Login:**
```bash
railway login
```

3. **Deploy:**
```bash
cd ps2-business-agent
railway init
railway up
```

4. **Get URL:**
```bash
railway domain
```

## Option 2: Render (Free Tier)

1. **Create `render.yaml`:**
```yaml
services:
  - type: web
    name: voicebillingai
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. **Push to GitHub**
3. **Connect to Render.com**
4. **Deploy automatically**

## Option 3: Heroku

1. **Create `Procfile`:**
```
web: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. **Deploy:**
```bash
heroku login
heroku create voicebillingai
git push heroku main
```

## Option 4: AWS EC2 (Production)

1. **Launch Ubuntu EC2 instance**

2. **SSH and setup:**
```bash
sudo apt update
sudo apt install python3-pip nginx -y
git clone <your-repo>
cd ps2-business-agent
pip3 install -r requirements.txt
```

3. **Run with systemd:**
```bash
sudo nano /etc/systemd/system/voicebilling.service
```

```ini
[Unit]
Description=VoiceBillingAI
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/ps2-business-agent/backend
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable voicebilling
sudo systemctl start voicebilling
```

4. **Configure Nginx:**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Option 5: Docker (Any Platform)

1. **Build:**
```bash
docker build -t voicebillingai .
```

2. **Run:**
```bash
docker run -p 8000:8000 voicebillingai
```

3. **Deploy to any cloud with Docker support**

## Option 6: Local Network Access

**Already configured in run.bat!**

Your `run.bat` uses `--host 0.0.0.0` which means:
- Access from same computer: `http://localhost:8000`
- Access from other devices on network: `http://YOUR_IP:8000`

**Find your IP:**
```bash
ipconfig
```
Look for IPv4 Address (e.g., 192.168.1.100)

**Access from phone/tablet:**
```
http://192.168.1.100:8000
```

## Recommended for Small Business

**Option 6 (Local Network)** - Already working!
- Free
- Fast
- No internet needed
- Access from any device on WiFi
- Perfect for shop/office

**Just run:**
```bash
run.bat
```

Then access from any device: `http://YOUR_IP:8000`

## Environment Variables

For production, set:
```bash
MERCHANT_UPI_ID=yourshop@paytm
```

## Database Backup

```bash
# Backup
copy backend\billing.db backup\billing_backup.db

# Restore
copy backup\billing_backup.db backend\billing.db
```

## Quick Deploy Commands

**Railway:**
```bash
railway up
```

**Render:**
- Push to GitHub
- Connect on render.com

**Local Network:**
```bash
run.bat
# Access: http://YOUR_IP:8000
```
