# 🚀 Deployment Guide - PythonAnywhere

## Step-by-Step Deployment Instructions

This guide will help you deploy the updated Evren Academy website to PythonAnywhere with mobile responsive features.

---

## 📋 Prerequisites

- ✅ PythonAnywhere account (created)
- ✅ Git repository uploaded (already done)
- ✅ Latest code changes (mobile responsive updates)
- ✅ Local git repository configured

---

## 🔄 Step 1: Push Latest Changes to Git

### From Your Computer Terminal/PowerShell

```bash
# Navigate to your project
cd c:\Users\dell\Desktop\evern website

# Check git status
git status

# Add all changes
git add .

# Commit with message
git commit -m "feat: Deploy mobile responsive website to PythonAnywhere"

# Push to remote repository
git push origin main
```

**Expected Output:**
```
[main xxxxx] feat: Deploy mobile responsive website...
 8 files changed, 1695 insertions(+)
...
Counting objects: XX...
Compressing objects: XX...
Writing objects: XX...
Delta compression using up to 8 threads...
To github.com:mmafsal31/evrenwebsite.git
   main -> main
```

✅ **Success**: If you see "main -> main" at the end

---

## 🌐 Step 2: Pull Changes on PythonAnywhere

### Access Your PythonAnywhere Bash Console

1. **Login to PythonAnywhere**
   - Go to: https://www.pythonanywhere.com
   - Sign in with your account
   - Go to: Dashboard → Consoles → Bash

2. **Navigate to Your Project**
   ```bash
   cd /home/yourusername/evrenwebsite
   ```
   Replace `yourusername` with your actual PythonAnywhere username

3. **Pull Latest Changes**
   ```bash
   git pull origin main
   ```

4. **Verify Changes**
   ```bash
   git log --oneline -5
   ```
   You should see your latest commits

**Expected Output:**
```
2c23e4e docs: Add main README for mobile responsive
2f6905b docs: Add comprehensive mobile responsiveness checklist
93612b8 feat: Make website fully mobile responsive
...
```

---

## 📦 Step 3: Install/Update Dependencies (if needed)

```bash
# Activate virtual environment
source /home/yourusername/evrenwebsite/venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

---

## 🗂️ Step 4: Collect Static Files

Static files (CSS, JavaScript, images) need to be collected for serving.

```bash
# Activate virtual environment
source /home/yourusername/evrenwebsite/venv/bin/activate

# Collect static files
python manage.py collectstatic --noinput

# Output will show collected files
```

**Expected Output:**
```
...
Copying '/home/yourusername/evrenwebsite/static/css/mobile-optimized.css'
...
123 static files copied to '/home/yourusername/evrenwebsite/static/', ...
```

---

## ⚙️ Step 5: Apply Database Migrations

```bash
# Activate virtual environment
source /home/yourusername/evrenwebsite/venv/bin/activate

# Apply migrations
python manage.py migrate

# Output
Operations to perform:
  Apply all migrations: ...
Running migrations:
  ...
```

---

## 🔄 Step 6: Reload Your Web App

### From PythonAnywhere Dashboard

1. **Go to Web Tab**
   - Dashboard → Web

2. **Find Your App**
   - Look for your app in the list (should be evrenwebsite.pythonanywhere.com or similar)

3. **Reload Button**
   - Click the green "Reload" button
   - Wait 10-20 seconds for reload to complete

4. **Check Status**
   - Should see "Last reload: XX seconds ago"
   - Status should show as running

### Or Use Command Line

```bash
# From PythonAnywhere bash console
touch /home/yourusername/mysite/mysite/wsgi.py
```

This triggers a reload by updating the WSGI file timestamp.

---

## ✅ Step 7: Verify Deployment

### Test Your Website

1. **Open in Browser**
   - Go to: https://yourusername.pythonanywhere.com

2. **Test Mobile Responsiveness**
   - Open DevTools (F12)
   - Click mobile icon (📱)
   - Select different device sizes
   - Verify layout responds correctly

3. **Test Key Features**
   - ✅ Navigation menu (check hamburger on mobile)
   - ✅ Forms (fill out admission form)
   - ✅ Links and buttons (click several)
   - ✅ Images (scroll and view)
   - ✅ Responsive layout (try different sizes)

4. **Check Styling**
   - Mobile-optimized CSS should load
   - Colors should be correct
   - Buttons should be styled
   - No broken styling

---

## 🔍 Troubleshooting

### Issue: Static Files Not Showing (CSS/JS Missing)

**Solution:**
```bash
# SSH into PythonAnywhere
source /home/yourusername/evrenwebsite/venv/bin/activate

# Clear and re-collect
rm -rf /home/yourusername/evrenwebsite/static/
python manage.py collectstatic --noinput

# Reload web app
touch /home/yourusername/mysite/mysite/wsgi.py
```

### Issue: Website Shows Errors

**Check Logs:**
```bash
# Error log location
/var/log/yourusername.pythonanywhere.com.error.log

# View errors
tail -f /var/log/yourusername.pythonanywhere.com.error.log
```

### Issue: Changes Not Appearing

**Solution:**
```bash
# Make sure you're on main branch
git status

# Pull latest changes
git pull origin main

# Collect static files again
python manage.py collectstatic --noinput

# Reload web app
# Go to Dashboard → Web → Click Reload
```

### Issue: Database Errors

**Solution:**
```bash
# Run migrations
python manage.py migrate

# Check for issues
python manage.py check
```

---

## 🎯 Complete Deployment Checklist

After deployment, verify:

- [ ] Website loads without errors
- [ ] Mobile menu works (hamburger icon)
- [ ] Navigation links work
- [ ] Forms are functional
- [ ] Images display correctly
- [ ] CSS/styling applied (colors, fonts)
- [ ] Buttons are styled and clickable
- [ ] Layout responsive on mobile (use F12)
- [ ] No console errors (F12 → Console tab)
- [ ] Page loads quickly

---

## 📊 Verify File Changes on PythonAnywhere

Check that new files are present:

```bash
# List CSS files
ls -la /home/yourusername/evrenwebsite/static/css/

# Should include:
# - mobile-optimized.css (NEW)
# - responsive.css (UPDATED)
# - style.css (UPDATED)

# List documentation files
ls -la /home/yourusername/evrenwebsite/*.md

# Should include:
# - README_MOBILE_RESPONSIVE.md (NEW)
# - MOBILE_RESPONSIVE_GUIDE.md (NEW)
# - MOBILE_RESPONSIVE_SUMMARY.md (NEW)
```

---

## 🚀 Quick Deployment Commands Summary

```bash
# 1. On your computer - commit and push
cd c:\Users\dell\Desktop\evern website
git add .
git commit -m "Deploy mobile responsive updates"
git push origin main

# 2. On PythonAnywhere - pull and deploy
cd /home/yourusername/evrenwebsite
git pull origin main
python manage.py collectstatic --noinput
python manage.py migrate

# 3. Reload web app from Dashboard
# OR: touch /home/yourusername/mysite/mysite/wsgi.py
```

---

## 📝 Environment Variables (if needed)

If you need to set environment variables on PythonAnywhere:

**Web tab → Edit WSGI file:**
```python
import os
import sys

# Add path
path = '/home/yourusername/evrenwebsite'
if path not in sys.path:
    sys.path.append(path)

# Set environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'evren_academy.settings'

# Load application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

---

## 🔒 Security Check

- ✅ DEBUG = False in production settings
- ✅ ALLOWED_HOSTS includes your domain
- ✅ SECRET_KEY is set (don't commit to git)
- ✅ Database is configured
- ✅ CSRF protection enabled
- ✅ HTTPS enabled (PythonAnywhere provides)

---

## 📈 Monitoring

After deployment, monitor:

1. **Website Status**
   - Check: yourusername.pythonanywhere.com
   - Verify it loads

2. **Errors**
   - Watch error log for issues
   - Check Django logs

3. **Performance**
   - Monitor page load time
   - Check for slow queries

4. **User Activity**
   - Forms being submitted
   - Navigation working

---

## 🎓 Additional Resources

- **PythonAnywhere Help**: https://help.pythonanywhere.com/
- **Django Deployment**: https://docs.djangoproject.com/en/stable/howto/deployment/
- **Git Documentation**: https://git-scm.com/doc/

---

## ✨ Success Criteria

Your deployment is successful when:

✅ Website is accessible at yourusername.pythonanywhere.com  
✅ Mobile responsive CSS is loaded  
✅ All pages display correctly  
✅ Forms are functional  
✅ No console errors (F12)  
✅ Mobile menu works  
✅ Images display  
✅ Links work  

---

## 🎉 Next Steps

1. **Test on Mobile**: Open on your phone and verify
2. **Share URL**: Website is now live online!
3. **Monitor**: Keep an eye on error logs
4. **Update**: Push new changes using the same process

---

**Deployment Date**: 2026-05-19  
**Status**: Ready to Deploy  
**Quality**: Production Ready

---

## 🆘 Need Help?

If something goes wrong:

1. **Check logs**: `/var/log/yourusername.pythonanywhere.com.error.log`
2. **Re-pull code**: `git pull origin main`
3. **Collect static**: `python manage.py collectstatic --noinput`
4. **Reload app**: Click reload button
5. **Check website**: yourusername.pythonanywhere.com

**Contact PythonAnywhere support if issues persist!**
