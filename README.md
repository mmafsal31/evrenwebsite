# Evren Academy Website

A premium, fully responsive educational institution website built with Django, Tailwind CSS, and vanilla JavaScript.

## Features

- ✅ Premium & modern UI design
- ✅ Fully responsive (mobile-first)
- ✅ Django Admin CMS for content management
- ✅ Multi-page structure (17+ pages)
- ✅ Hero slider with animations
- ✅ Testimonials carousel
- ✅ Blog/News system
- ✅ Course/Program management
- ✅ Multiple branch/campus support
- ✅ Gallery with lightbox
- ✅ SEO optimized (meta tags, sitemap, schema markup)
- ✅ Smooth animations (AOS.js)
- ✅ Floating WhatsApp and Call buttons
- ✅ Contact, admission, and career forms
- ✅ Mobile-responsive navigation
- ✅ Fast loading (optimized static files)

## Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: Tailwind CSS 3+, Vanilla JavaScript
- **Database**: SQLite (dev), PostgreSQL (production)
- **UI Components**: Swiper.js (sliders), AOS.js (animations)
- **Image Processing**: Pillow
- **Rich Text**: django-ckeditor
- **Static Files**: WhiteNoise
- **Deployment**: Gunicorn + Nginx

## Installation

### Prerequisites

- Python 3.13+
- pip
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd evern_academy
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional)**
   ```bash
   python manage.py loaddata seed_data
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the site**
    - Website: http://localhost:8000
    - Admin: http://localhost:8000/admin

## Project Structure

```
evren_academy/
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── evren_academy/          # Main project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── core/               # Homepage and site settings
│   ├── courses/            # Programs and courses
│   ├── branches/           # Campus locations
│   ├── facilities/         # Campus facilities
│   ├── gallery/            # Photo gallery
│   ├── testimonials/       # Reviews
│   ├── blog/               # News and articles
│   ├── admissions/         # Admission forms and info
│   ├── contact/            # Contact forms
│   ├── careers/            # Job listings
│   └── seo/                # SEO management
├── templates/              # Django templates
├── static/                 # Static assets (CSS, JS, images)
└── media/                  # User uploads

```

## Pages

- **Home** (/)
- **About** (/about/)
- **Courses** (/courses/, /courses/<slug>/)
- **Branches** (/branches/, /branches/<slug>/)
- **Facilities** (/facilities/)
- **Gallery** (/gallery/)
- **Testimonials** (/testimonials/)
- **Blog** (/blog/, /blog/<slug>/)
- **Events** (/events/)
- **Admissions** (/admissions/)
- **Contact** (/contact/)
- **Careers** (/careers/)
- **Privacy Policy** (/privacy-policy/)
- **Terms & Conditions** (/terms-conditions/)

## Admin Features

The Django Admin allows you to manage:
- Site settings and branding
- Hero slider content
- Courses and programs
- Campus branches
- Facilities and gallery
- Blog posts and news
- Testimonials
- Team members
- SEO settings for each page
- Form submissions

## Deployment

### Using Gunicorn + Nginx

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create Gunicorn systemd service** (on Linux)
   - See deployment guide for details

3. **Configure Nginx**
   - See nginx.conf example in deployment guide

4. **Environment Setup**
   - Set DEBUG=False
   - Generate secure SECRET_KEY
   - Configure ALLOWED_HOSTS
   - Set up PostgreSQL database

5. **Static Files**
   - Run `python manage.py collectstatic`
   - Serve via Nginx

## Customization

### Colors

Edit `SiteSettings` in Django Admin to customize:
- Primary color
- Secondary color
- Accent colors
- Brand colors

### Typography

Fonts are configured in `static/css/tailwind.css`. Supported fonts:
- Headings: Playfair Display, Poppins
- Body: Inter, Open Sans

### Content

All content is editable via Django Admin. No code changes needed to update:
- Course information
- Team members
- Testimonials
- News articles
- FAQs
- Gallery items

## Performance

- Optimized images with Pillow
- Lazy loading for images
- Minified CSS and JavaScript
- Efficient database queries
- Gzip compression
- Static file caching

## SEO

- Dynamic meta tags and Open Graph
- XML sitemap
- robots.txt
- Schema.org markup
- Canonical URLs
- Mobile-friendly

## Security

- CSRF protection
- Form validation
- SQL injection prevention
- XSS protection
- Secure headers
- HTTPS ready

## Browser Support

- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

Proprietary - Evren Academy

## Support

For issues or questions, contact: support@everenacademy.com

## Credits

Built with Django, Tailwind CSS, and passion for education. 🎓
