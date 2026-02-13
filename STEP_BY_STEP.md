# Step-by-Step Deployment Guide

## Method 1: Render.com (Easiest - Recommended)

### Step 1: Push Your Code to GitHub
```bash
cd ps2-business-agent
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Go to Render.com
1. Open browser
2. Go to: **https://render.com**
3. Click: **"Get Started for Free"** (top right)

### Step 3: Sign Up with GitHub
1. Click: **"Sign in with GitHub"**
2. Authorize Render to access your GitHub
3. You'll be redirected to Render dashboard

### Step 4: Create New Web Service
1. Click: **"New +"** button (top right)
2. Select: **"Web Service"**
3. You'll see "Create a new Web Service" page

### Step 5: Connect Your Repository
1. Find your repo: **"ps2-business-agent"** in the list
2. Click: **"Connect"** button next to it
3. If you don't see it, click **"Configure account"** and give access

### Step 6: Configure Service Settings
Fill in these fields:

**Name:**
```
voicebillingai
```

**Region:**
```
Singapore (or closest to you)
```

**Branch:**
```
main
```

**Root Directory:**
```
(leave empty)
```

**Runtime:**
```
Python 3
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
cd backend && python -c "from db import init_db; init_db()" && uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:**
```
Free
```

### Step 7: Deploy
1. Scroll down
2. Click: **"Create Web Service"** (blue button)
3. Wait 2-3 minutes while it deploys
4. You'll see logs scrolling

### Step 8: Get Your URL
1. Once deployed, you'll see: **"Live"** with green dot
2. Your URL will be at top: `https://voicebillingai.onrender.com`
3. Click the URL to open your app!

### Step 9: Test
1. Open the URL
2. Type: "2 kg rice at 60, 1 kg sugar at 42"
3. Click: "Confirm"
4. Click: "Download Invoice PDF"
5. Done! ✅

---

## Method 2: Railway.app (Fastest)

### Step 1: Install Railway CLI
Open Command Prompt:
```bash
npm install -g @railway/cli
```

### Step 2: Login
```bash
railway login
```
Browser will open, click "Authorize"

### Step 3: Navigate to Your Project
```bash
cd ps2-business-agent
```

### Step 4: Initialize Railway
```bash
railway init
```
- Enter project name: `voicebillingai`
- Press Enter

### Step 5: Deploy
```bash
railway up
```
Wait 1-2 minutes

### Step 6: Add Domain
```bash
railway domain
```
You'll get URL like: `https://voicebillingai-production.up.railway.app`

### Step 7: Test
Open the URL in browser!

---

## Method 3: Replit (No Installation)

### Step 1: Go to Replit
1. Open: **https://replit.com**
2. Sign up/Login with GitHub

### Step 2: Import from GitHub
1. Click: **"Create Repl"**
2. Select: **"Import from GitHub"**
3. Paste your GitHub repo URL
4. Click: **"Import from GitHub"**

### Step 3: Configure
1. Replit will detect Python
2. It will install dependencies automatically

### Step 4: Run
1. Click: **"Run"** button (top)
2. Wait for server to start
3. You'll see URL in the output window

### Step 5: Open
Click the URL that appears!

---

## Troubleshooting

### Issue: "Build failed"
**Fix:** Make sure `requirements.txt` is in root folder

### Issue: "Port already in use"
**Fix:** Render/Railway handle ports automatically, no action needed

### Issue: "Module not found"
**Fix:** Check that all files are pushed to GitHub:
```bash
git status
git add .
git commit -m "Add missing files"
git push
```

### Issue: "Database error"
**Fix:** The database will be created automatically on first run

---

## What You'll Get

After deployment:
- ✅ Live URL (e.g., `https://voicebillingai.onrender.com`)
- ✅ Works on any device with internet
- ✅ Auto-updates when you push to GitHub
- ✅ Free hosting (Render/Railway free tier)
- ✅ HTTPS enabled automatically

---

## Quick Comparison

| Method | Time | Difficulty | Free Tier |
|--------|------|------------|-----------|
| Render | 5 min | Easy | Yes (750 hrs/month) |
| Railway | 2 min | Easiest | Yes (500 hrs/month) |
| Replit | 3 min | Easy | Yes (limited) |

**Recommended:** Start with Render (most reliable free tier)

---

## Next Steps After Deployment

1. **Test the URL** - Make sure it works
2. **Share the URL** - Give it to users
3. **Monitor** - Check Render dashboard for logs
4. **Update** - Push to GitHub, auto-deploys

---

## Need Help?

If stuck at any step:
1. Check the error message in Render logs
2. Make sure all files are on GitHub
3. Verify `requirements.txt` has all dependencies
4. Try Railway if Render doesn't work

Your app will be live in 5 minutes! 🚀
