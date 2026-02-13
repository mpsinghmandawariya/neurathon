# Deploy in 3 Steps

## Your code is on GitHub ✓

Now deploy to a hosting service:

## Option 1: Render (Recommended)

1. Go to: https://render.com
2. Sign in with GitHub
3. Click: "New +" → "Web Service"
4. Select your repo: `ps2-business-agent`
5. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `cd backend && python -c "from db import init_db; init_db()" && uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click: "Create Web Service"
7. Wait 2 minutes
8. Get your URL!

## Option 2: Railway (CLI)

```bash
npm i -g @railway/cli
cd ps2-business-agent
railway login
railway up
railway domain
```

## Option 3: Replit (No CLI)

1. Go to: https://replit.com
2. Import from GitHub
3. Click "Run"
4. Get URL

## Why GitHub URL doesn't work?

GitHub = Code storage only
Render/Railway = Live hosting

You need BOTH:
- GitHub: Store code ✓
- Render: Host live app ← Do this now

## Quick Test

After deploying to Render, your URL will be:
`https://voicebillingai.onrender.com`

Test it!
