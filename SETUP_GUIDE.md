# Evren Academy Django Website - Setup Guide

## 🎓 Project Overview

A complete, premium Django-based educational institution website for Evren Academy featuring:
- ✅ Responsive design with Bootstrap 5 & custom CSS
- ✅ Django Admin CMS for content management
- ✅ 17+ pages (homepage, courses, branches, blog, etc.)
- ✅ Animated components (Swiper.js, AOS.js)
- ✅ SEO optimization (meta tags, sitemap, robots.txt)
- ✅ Floating WhatsApp and Call buttons
- ✅ Contact, admission, and career forms
- ✅ Multi-branch support
- ✅ Blog/News system
- ✅ Testimonials carousel
- ✅ Gallery with lightbox
- ✅ Team member management

---

## 📋 Prerequisites

### System Requirements
- **OS**: Windows 10+, macOS, or Linux
- **Python**: 3.13+
- **Browser**: Chrome, Firefox, Safari, Edge (latest versions)
- **Storage**: 500MB minimum
- **RAM**: 2GB minimum

### Required Software
1. **Python 3.13+**
   - Download from: https://www.python.org/downloads/
   - ✅ Check "Add Python to PATH" during installation

2. **Git** (Optional but recommended)
   - Download from: https://git-scm.com/

3. **Text Editor** (VS Code recommended)
   - Download from: https://code.visualstudio.com/

---

## 🚀 Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd "c:\Users\dell\Desktop\evern website"
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

**Activate Virtual Environment:**

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

### Step 3: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Django 5.0+
- Pillow (image processing)
- django-ckeditor (rich text editor)
- WhiteNoise (static files)
- python-decouple (environment variables)
- And more...

### Step 5: Configure Environment Variables

Copy `.env.example` to `.env`:

**Windows:**
```bash
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

Edit `.env` file and customize:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
SITE_NAME=Evren Academy
WHATSAPP_NUMBER=+92 300 1234567
PHONE_NUMBER=+92 (0) 123 456 789
```

### Step 6: Run Initial Setup Scripts

**Generate Project Structure:**
```bash
python COMPLETE_BUILD.py
```

This creates all models, views, URLs, admin configurations, and app structure.

### Step 7: Create Databases

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the SQLite database and all tables.

### Step 8: Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email: admin@example.com
Password: (enter your secure password)
```

### Step 9: Generate Templates and Static Files

```bash
python BUILD_TEMPLATES.py
```

This creates all HTML templates, CSS, and JavaScript files.

### Step 10: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 11: Run Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## 🌐 Access Your Website

### Frontend
- **Homepage**: http://localhost:8000
- **Courses**: http://localhost:8000/courses/
- **Branches**: http://localhost:8000/branches/
- **Blog**: http://localhost:8000/blog/
- **Contact**: http://localhost:8000/contact/

### Admin Panel
- **Admin Login**: http://localhost:8000/admin
- **Username**: admin (or your superuser username)
- **Password**: (your chosen password)

---

## 📝 Managing Content via Admin

### Adding a Hero Slide
1. Login to admin panel
2. Navigate to **Core > Hero Slides**
3. Click **Add Hero Slide**
4. Fill in:
   - **Title**: e.g., "Welcome to Evren Academy"
   - **Subtitle**: Your subtitle
   - **Image**: Upload hero image
   - **Button Text**: e.g., "Learn More"
   - **Button Link**: e.g., "/courses/"
5. Click **Save**

### Adding a Course
1. Login to admin panel
2. Navigate to **Courses > Courses**
3. Click **Add Course**
4. Fill in:
   - **Name**: Course title
   - **Category**: Select or create category
   - **Short Description**: Brief overview
   - **Description**: Full course details (with rich text editor)
   - **Image**: Course image
   - **Duration**: e.g., "6 months"
   - **Eligibility**: Requirements
5. Click **Save**

### Managing Site Settings
1. Login to admin panel
2. Navigate to **Core > Site Settings**
3. Edit:
   - **Site Name**: "Evren Academy"
   - **Logo**: Upload logo
   - **Phone/WhatsApp**: Contact numbers
   - **Colors**: Primary, secondary, accent
   - **Social Media**: Links to social profiles
   - **Address**: Full address
4. Click **Save**

### Adding Blog Posts
1. Login to admin panel
2. Navigate to **Blog > Blog Posts**
3. Click **Add Blog Post**
4. Fill in:
   - **Title**: Post title
   - **Category**: Select category
   - **Excerpt**: Short summary
   - **Content**: Full article (with rich text editor)
   - **Image**: Featured image
5. Click **Save**

---

## 📂 Project Structure

```
evren_academy/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (created)
├── db.sqlite3               # Database (created)
│
├── evren_academy/           # Main project folder
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # Production WSGI
│   └── asgi.py              # ASGI configuration
│
├── apps/                    # Django applications
│   ├── core/                # Homepage and site settings
│   ├── courses/             # Program management
│   ├── branches/            # Campus locations
│   ├── facilities/          # Campus facilities
│   ├── gallery/             # Photo gallery
│   ├── testimonials/        # Reviews
│   ├── blog/                # News and articles
│   ├── admissions/          # Admission forms
│   ├── contact/             # Contact forms
│   ├── careers/             # Job listings
│   └── seo/                 # SEO management
│
├── templates/               # HTML templates
│   ├── base.html           # Master template
│   ├── includes/           # Reusable components
│   ├── core/               # Homepage templates
│   ├── courses/            # Course templates
│   ├── blog/               # Blog templates
│   ├── errors/             # Error pages (404, 500)
│   └── pages/              # Static pages
│
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── images/            # Website images
│   └── vendors/           # Third-party libraries
│
└── media/                  # User uploads
    ├── uploads/
    ├── courses/
    ├── branches/
    ├── blog/
    └── team/
```

---

## 🎨 Customization

### Changing Colors
1. Admin panel → Core → Site Settings
2. Edit:
   - **Primary Color**: Main brand color (currently #0B5D3B)
   - **Secondary Color**: Accent color (currently #D4AF37)
   - **Accent Color**: Light background (currently #F8F5EE)

### Changing Fonts
Edit `static/css/style.css`:
```css
h1, h2, h3, h4, h5, h6 {
    font-family: 'Your Font', serif;
}

body {
    font-family: 'Your Body Font', sans-serif;
}
```

### Custom Logo
1. Go to Admin → Core → Site Settings
2. Upload your logo image
3. Save

### Custom Homepage
Edit `templates/core/index.html` to modify homepage layout and sections.

---

## 🔒 Security Settings

### For Production:
Edit `evren_academy/settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'generate-a-secure-key'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
```

### Generate Secret Key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 🚀 Deployment

### Using Heroku

1. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli

2. **Create Procfile**:
```
web: gunicorn evren_academy.wsgi
```

3. **Create requirements.txt** (already created)

4. **Deploy**:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Using DigitalOcean / AWS

1. **Install Gunicorn**: `pip install gunicorn`

2. **Create Nginx config** (nginx.conf)

3. **Create systemd service**

4. **Use supervisor** for process management

---

## 🐛 Troubleshooting

### Issue: "No module named 'django'"
**Solution**: Make sure virtual environment is activated
```bash
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### Issue: "Port 8000 already in use"
**Solution**: Use different port
```bash
python manage.py runserver 8001
```

### Issue: "ModuleNotFoundError: No module named 'apps'"
**Solution**: Run from project root directory and ensure apps/ folder exists

### Issue: Database errors
**Solution**: Reset database
```bash
python manage.py migrate --plan
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic --clear --noinput
```

---

## 📚 Common Commands

```bash
# Start development server
python manage.py runserver

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Shell (interactive Python)
python manage.py shell

# Check for issues
python manage.py check

# Create app
python manage.py startapp appname

# Dump data
python manage.py dumpdata > data.json

# Load data
python manage.py loaddata data.json
```

---

## 📞 Support & Resources

### Django Documentation
- https://docs.djangoproject.com/

### Bootstrap Documentation
- https://getbootstrap.com/docs/

### Swiper Documentation
- https://swiperjs.com/

### AOS Documentation
- https://michalsnik.github.io/aos/

---

## 📝 License

Proprietary - Evren Academy

---

## ✅ Checklist Before Launch

- [ ] Update site settings (name, logo, colors, contact info)
- [ ] Add hero slides
- [ ] Add courses with descriptions
- [ ] Add branches with contact info
- [ ] Add team members
- [ ] Add testimonials
- [ ] Add blog posts
- [ ] Configure contact forms
- [ ] Set up WhatsApp and phone numbers
- [ ] Add social media links
- [ ] Test on mobile devices
- [ ] Check SEO settings
- [ ] Verify all forms work
- [ ] Test navigation and links
- [ ] Optimize images
- [ ] Set SECRET_KEY for production
- [ ] Set DEBUG=False for production
- [ ] Configure email backend
- [ ] Set up SSL certificate (production)
- [ ] Configure database for production
- [ ] Set up backups

---

## 🎉 You're All Set!

Your Evren Academy website is now ready. Customize the content, design, and settings to match your institution's brand and needs.

For questions or issues, refer to the Django documentation or contact support.

Happy coding! 🚀
