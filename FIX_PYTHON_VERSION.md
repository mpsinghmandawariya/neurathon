# Fix Render Python Version Error

## Problem
Render is using Python 3.14 (too new) which breaks pydantic-core

## Solution

### Step 1: Add These Files (Already Done)
- ✅ `runtime.txt` - Specifies Python 3.11
- ✅ `.python-version` - Backup version file
- ✅ Updated `render.yaml` - Added PYTHON_VERSION

### Step 2: Push to GitHub
```bash
cd ps2-business-agent
git add .
git commit -m "Fix Python version for Render"
git push
```

### Step 3: Redeploy on Render
1. Go to your Render dashboard
2. Click your service
3. Click "Manual Deploy" → "Deploy latest commit"
4. Wait 2-3 minutes
5. Done! ✅

---

## Alternative: Set Python Version in Render Dashboard

If files don't work:

1. Go to Render dashboard
2. Click your service
3. Go to "Environment" tab
4. Add environment variable:
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.11.0`
5. Click "Save Changes"
6. Service will auto-redeploy

---

## Quick Commands

```bash
# Push fix to GitHub
git add runtime.txt .python-version render.yaml
git commit -m "Fix Python version"
git push

# Check Render logs
# Go to dashboard → Your service → Logs
```

---

## Expected Result

Build logs should show:
```
✓ Using Python 3.11.0
✓ Installing dependencies
✓ Build succeeded
```

Your app will be live! 🚀
