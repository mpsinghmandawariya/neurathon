# Quick Deployment Options

## 🏠 Local Network (Recommended for Shops)
**Already configured in run.bat!**

```bash
run.bat
```

Access from any device on WiFi: `http://YOUR_IP:8000`

Find your IP: `ipconfig` (look for IPv4)

✅ Free
✅ Fast
✅ Offline
✅ No setup needed

---

## ☁️ Cloud Hosting

### Railway (Easiest)
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### Render (Free)
1. Push to GitHub
2. Connect on render.com
3. Auto-deploys

### Heroku
```bash
heroku create voicebillingai
git push heroku main
```

### Docker
```bash
docker build -t voicebillingai .
docker run -p 8000:8000 voicebillingai
```

---

## 📱 Access URLs

**Local:** http://localhost:8000
**Network:** http://YOUR_IP:8000
**Cloud:** Provided by hosting service

---

## 🎯 Best Choice

**For small shops:** Local Network (run.bat)
**For online access:** Railway or Render
**For production:** AWS EC2 + Nginx

See DEPLOYMENT.md for detailed instructions.
