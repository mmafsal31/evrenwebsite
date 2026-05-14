#!/usr/bin/env python3
"""
EVREN ACADEMY - TEMPLATES & STATIC FILES BUILDER
Run after: python COMPLETE_BUILD.py && python manage.py migrate
Run: python BUILD_TEMPLATES.py
"""

from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).parent

def write(rel_path, content, silent=False):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content), encoding='utf-8')
    if not silent:
        print(f"  ✓ {rel_path}")

print("\n" + "╔" + "═" * 80 + "╗")
print("║" + "PHASE 3: TEMPLATES & STATIC FILES".center(80) + "║")
print("╚" + "═" * 80 + "╝\n")

print("📝 Creating base template...")

# BASE.HTML - Master Template
write('templates/base.html', '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{% block meta_description %}{{ site_settings.tagline }}{% endblock %}">
    <title>{% block title %}{{ site_settings.site_name }}{% endblock %}</title>
    <link rel="icon" type="image/x-icon" href="{% if site_settings.favicon %}{{ site_settings.favicon.url }}{% else %}/static/images/favicon.ico{% endif %}">
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Swiper CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css">
    <!-- AOS CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
    
    <link rel="stylesheet" href="/static/css/style.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Top Announcement Bar -->
    {% if site_settings.show_announcement %}
    <div class="announcement-bar bg-dark text-white py-2">
        <div class="container text-center">
            <p class="mb-0">📢 {{ site_settings.announcement }}</p>
        </div>
    </div>
    {% endif %}

    <!-- Header -->
    {% include 'includes/header.html' %}

    <!-- Main Content -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    {% include 'includes/footer.html' %}

    <!-- Floating Buttons -->
    <a href="https://wa.me/{{ site_settings.whatsapp|slice:'1:' }}" class="whatsapp-btn" title="WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>
    <a href="tel:{{ site_settings.phone }}" class="call-btn" title="Call">
        <i class="fas fa-phone"></i>
    </a>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <!-- AOS JS -->
    <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
    
    <script src="/static/js/main.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
''')

print("📝 Creating include templates...")

# HEADER
write('templates/includes/header.html', '''
<header class="navbar navbar-expand-lg navbar-light bg-white sticky-top shadow-sm">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'core:home' %}">
            {% if site_settings.logo %}
            <img src="{{ site_settings.logo.url }}" alt="{{ site_settings.site_name }}" height="50">
            {% else %}
            <strong>{{ site_settings.site_name }}</strong>
            {% endif %}
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'core:home' %}">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'core:home' %}#about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'courses:list' %}">Courses</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'branches:list' %}">Branches</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'blog:list' %}">Blog</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'contact:list' %}">Contact</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link btn btn-primary text-white ms-2" href="{% url 'admissions:list' %}">
                        Apply Now
                    </a>
                </li>
            </ul>
        </div>
    </div>
</header>
''')

# FOOTER
write('templates/includes/footer.html', '''
<footer class="bg-dark text-white py-5">
    <div class="container">
        <div class="row">
            <div class="col-md-4 mb-4">
                <h5>About {{ site_settings.site_name }}</h5>
                <p>Premium educational institution dedicated to excellence in education.</p>
                <div class="social-links">
                    {% if site_settings.facebook %}<a href="{{ site_settings.facebook }}" target="_blank" class="text-white me-2"><i class="fab fa-facebook"></i></a>{% endif %}
                    {% if site_settings.twitter %}<a href="{{ site_settings.twitter }}" target="_blank" class="text-white me-2"><i class="fab fa-twitter"></i></a>{% endif %}
                    {% if site_settings.instagram %}<a href="{{ site_settings.instagram }}" target="_blank" class="text-white me-2"><i class="fab fa-instagram"></i></a>{% endif %}
                    {% if site_settings.linkedin %}<a href="{{ site_settings.linkedin }}" target="_blank" class="text-white me-2"><i class="fab fa-linkedin"></i></a>{% endif %}
                </div>
            </div>

            <div class="col-md-4 mb-4">
                <h5>Quick Links</h5>
                <ul class="list-unstyled">
                    <li><a href="{% url 'courses:list' %}" class="text-white-50">Courses</a></li>
                    <li><a href="{% url 'branches:list' %}" class="text-white-50">Branches</a></li>
                    <li><a href="{% url 'admissions:list' %}" class="text-white-50">Admissions</a></li>
                    <li><a href="{% url 'careers:list' %}" class="text-white-50">Careers</a></li>
                </ul>
            </div>

            <div class="col-md-4 mb-4">
                <h5>Contact Us</h5>
                <p class="mb-2">
                    <i class="fas fa-phone"></i> <a href="tel:{{ site_settings.phone }}" class="text-white-50">{{ site_settings.phone }}</a>
                </p>
                <p class="mb-2">
                    <i class="fas fa-envelope"></i> <a href="mailto:{{ site_settings.email }}" class="text-white-50">{{ site_settings.email }}</a>
                </p>
                <p class="mb-2">
                    <i class="fas fa-map-marker-alt"></i> {{ site_settings.address|truncatewords:5 }}
                </p>
            </div>
        </div>

        <hr class="bg-white-50">
        <div class="text-center text-white-50">
            <p class="mb-0">{{ site_settings.copyright }}</p>
        </div>
    </div>
</footer>
''')

print("📝 Creating page templates...")

# HOMEPAGE
write('templates/core/index.html', '''
{% extends "base.html" %}

{% block title %}Home - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<!-- Hero Slider -->
<div class="hero-slider">
    <div class="swiper">
        <div class="swiper-wrapper">
            {% for slide in hero_slides %}
            <div class="swiper-slide" style="background: url('{{ slide.image.url }}') center/cover;">
                <div class="hero-content">
                    <h1 class="display-4" data-aos="fade-up">{{ slide.title }}</h1>
                    <p class="lead" data-aos="fade-up" data-aos-delay="100">{{ slide.subtitle }}</p>
                    {% if slide.button_link %}
                    <a href="{{ slide.button_link }}" class="btn btn-primary btn-lg" data-aos="fade-up" data-aos-delay="200">
                        {{ slide.button_text }}
                    </a>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-button-next"></div>
    </div>
</div>

<!-- Statistics Section -->
<section class="py-5 bg-light">
    <div class="container">
        <div class="row text-center">
            {% for stat in statistics %}
            <div class="col-md-3 mb-4" data-aos="fade-up">
                <h3 class="counter">{{ stat.value }}</h3>
                <p class="text-muted">{{ stat.label }} {{ stat.unit }}</p>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Featured Courses -->
<section class="py-5">
    <div class="container">
        <h2 class="text-center mb-5" data-aos="fade-up">Our Courses</h2>
        <div class="row">
            {% load static %}
            {% for course in courses %}
            <div class="col-md-4 mb-4" data-aos="fade-up">
                <div class="card h-100">
                    <img src="{{ course.image.url }}" class="card-img-top" alt="{{ course.name }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ course.name }}</h5>
                        <p class="card-text">{{ course.short_description }}</p>
                    </div>
                    <div class="card-footer bg-transparent">
                        <a href="{% url 'courses:detail' course.slug %}" class="btn btn-outline-primary">Learn More</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Team Section -->
<section class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-5" data-aos="fade-up">Our Leadership</h2>
        <div class="row">
            {% for member in team_members %}
            <div class="col-md-4 mb-4" data-aos="fade-up">
                <div class="text-center">
                    <img src="{{ member.image.url }}" class="rounded-circle mb-3" width="200" height="200" alt="{{ member.name }}">
                    <h5>{{ member.name }}</h5>
                    <p class="text-muted">{{ member.title }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
''')

# 404 PAGE
write('templates/errors/404.html', '''
{% extends "base.html" %}

{% block title %}Page Not Found{% endblock %}

{% block content %}
<div class="container py-5 text-center">
    <h1 class="display-1">404</h1>
    <h2>Page Not Found</h2>
    <p class="lead mb-4">Sorry, the page you are looking for doesn't exist.</p>
    <a href="{% url 'core:home' %}" class="btn btn-primary">Go Home</a>
</div>
{% endblock %}
''')

# 500 PAGE
write('templates/errors/500.html', '''
{% extends "base.html" %}

{% block title %}Server Error{% endblock %}

{% block content %}
<div class="container py-5 text-center">
    <h1 class="display-1">500</h1>
    <h2>Server Error</h2>
    <p class="lead mb-4">Something went wrong on our end. Please try again later.</p>
    <a href="{% url 'core:home' %}" class="btn btn-primary">Go Home</a>
</div>
{% endblock %}
''')

# COURSES LIST
write('templates/courses/course_list.html', '''
{% extends "base.html" %}

{% block title %}Courses - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">Our Courses</h1>

    <div class="row">
        <div class="col-md-3 mb-4">
            <h5>Filter by Category</h5>
            <div class="list-group">
                <a href="{% url 'courses:list' %}" class="list-group-item{% if not selected_category %} active{% endif %}">
                    All Courses
                </a>
                {% for category in categories %}
                <a href="?category={{ category.slug }}" class="list-group-item{% if category.slug == selected_category %} active{% endif %}">
                    {{ category.name }}
                </a>
                {% endfor %}
            </div>
        </div>

        <div class="col-md-9">
            <div class="row">
                {% for course in courses %}
                <div class="col-md-6 mb-4">
                    <div class="card h-100">
                        <img src="{{ course.image.url }}" class="card-img-top" alt="{{ course.name }}">
                        <div class="card-body">
                            <span class="badge bg-primary">{{ course.category.name }}</span>
                            <h5 class="card-title">{{ course.name }}</h5>
                            <p class="card-text">{{ course.short_description }}</p>
                            {% if course.duration %}<p class="text-muted"><i class="fas fa-clock"></i> {{ course.duration }}</p>{% endif %}
                        </div>
                        <div class="card-footer bg-transparent">
                            <a href="{% url 'courses:detail' course.slug %}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
                {% empty %}
                <p class="text-muted">No courses found.</p>
                {% endfor %}
            </div>

            <!-- Pagination -->
            {% if is_paginated %}
            <nav aria-label="Page navigation">
                <ul class="pagination justify-content-center">
                    {% if page_obj.has_previous %}
                    <li class="page-item">
                        <a class="page-link" href="?page=1">First</a>
                    </li>
                    {% endif %}
                    
                    {% for num in page_obj.paginator.page_range %}
                    <li class="page-item {% if page_obj.number == num %}active{% endif %}">
                        <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                    </li>
                    {% endfor %}
                    
                    {% if page_obj.has_next %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
                    </li>
                    {% endif %}
                </ul>
            </nav>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
''')

# BRANCHES LIST
write('templates/branches/branch_list.html', '''
{% extends "base.html" %}

{% block title %}Branches - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">Our Branches</h1>

    <div class="row">
        {% for branch in branches %}
        <div class="col-md-4 mb-4">
            <div class="card h-100" data-aos="fade-up">
                <img src="{{ branch.image.url }}" class="card-img-top" alt="{{ branch.name }}">
                <div class="card-body">
                    <h5 class="card-title">{{ branch.name }}</h5>
                    <p class="card-text"><strong>{{ branch.city }}</strong></p>
                    <p class="card-text text-muted">{{ branch.address|truncatewords:10 }}</p>
                    <p class="mb-2">
                        <i class="fas fa-phone"></i> <a href="tel:{{ branch.phone }}">{{ branch.phone }}</a>
                    </p>
                    <p class="mb-2">
                        <i class="fas fa-envelope"></i> <a href="mailto:{{ branch.email }}">{{ branch.email }}</a>
                    </p>
                </div>
                <div class="card-footer bg-transparent">
                    <a href="{% url 'branches:detail' branch.slug %}" class="btn btn-primary">View Details</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
''')

# CONTACT PAGE
write('templates/contact/contact.html', '''
{% extends "base.html" %}

{% block title %}Contact Us - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row">
        <div class="col-md-6 mb-4">
            <h2>Get in Touch</h2>
            <form method="post">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Name</label>
                    <input type="text" class="form-control" name="name" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" class="form-control" name="email" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Subject</label>
                    <input type="text" class="form-control" name="subject" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Message</label>
                    <textarea class="form-control" name="message" rows="5" required></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Send Message</button>
            </form>
        </div>

        <div class="col-md-6">
            <h2>Contact Information</h2>
            <div class="mb-4">
                <h5><i class="fas fa-phone"></i> Phone</h5>
                <p><a href="tel:{{ site_settings.phone }}">{{ site_settings.phone }}</a></p>
            </div>
            <div class="mb-4">
                <h5><i class="fas fa-envelope"></i> Email</h5>
                <p><a href="mailto:{{ site_settings.email }}">{{ site_settings.email }}</a></p>
            </div>
            <div class="mb-4">
                <h5><i class="fas fa-map-marker-alt"></i> Address</h5>
                <p>{{ site_settings.address }}</p>
            </div>
            <div>
                <h5><i class="fab fa-whatsapp"></i> WhatsApp</h5>
                <p><a href="https://wa.me/{{ site_settings.whatsapp|slice:'1:' }}">{{ site_settings.whatsapp }}</a></p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''')

# ADMISSIONS PAGE
write('templates/admissions/admission.html', '''
{% extends "base.html" %}

{% block title %}Admissions - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">Admissions</h1>

    <div class="row">
        <div class="col-md-6 mb-4">
            <h2>Apply Now</h2>
            <form method="post">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Full Name</label>
                    <input type="text" class="form-control" name="name" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" class="form-control" name="email" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Phone</label>
                    <input type="tel" class="form-control" name="phone" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Course of Interest</label>
                    <input type="text" class="form-control" name="course">
                </div>
                <div class="mb-3">
                    <label class="form-label">Message</label>
                    <textarea class="form-control" name="message" rows="4"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit Application</button>
            </form>
        </div>

        <div class="col-md-6">
            <h2>Admission Information</h2>
            <h5>Admission Requirements</h5>
            <ul>
                <li>Valid educational qualifications</li>
                <li>Completed application form</li>
                <li>Entrance test (if applicable)</li>
                <li>Interview</li>
            </ul>

            <h5 class="mt-4">Admission Timeline</h5>
            <div class="timeline">
                <div class="timeline-item">
                    <h6>Application Submission</h6>
                    <p class="text-muted">Open throughout the year</p>
                </div>
                <div class="timeline-item">
                    <h6>Document Verification</h6>
                    <p class="text-muted">Within 5 business days</p>
                </div>
                <div class="timeline-item">
                    <h6>Entrance Exam</h6>
                    <p class="text-muted">Scheduled based on applications</p>
                </div>
                <div class="timeline-item">
                    <h6>Interview & Result</h6>
                    <p class="text-muted">Within 2 weeks of exam</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''')

# PRIVACY POLICY
write('templates/pages/privacy_policy.html', '''
{% extends "base.html" %}

{% block title %}Privacy Policy - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-4">Privacy Policy</h1>
    
    <div class="row">
        <div class="col-md-8">
            <h3>Introduction</h3>
            <p>{{ site_settings.site_name }} ("we", "our", or "us") operates the website. This page informs you of our policies regarding the collection, use, and disclosure of personal data when you use our service and the choices you have associated with that data.</p>

            <h3 class="mt-4">Data Collection</h3>
            <p>We collect personal information you voluntarily provide when you submit forms on our website, such as your name, email, phone number, and course preferences.</p>

            <h3 class="mt-4">Data Usage</h3>
            <p>We use the collected data to respond to your inquiries, process applications, send educational materials, and improve our services.</p>

            <h3 class="mt-4">Security</h3>
            <p>We implement appropriate security measures to protect your personal information. However, no method of transmission over the Internet is 100% secure.</p>

            <h3 class="mt-4">Contact Us</h3>
            <p>If you have questions about this Privacy Policy, please contact us at <a href="mailto:{{ site_settings.email }}">{{ site_settings.email }}</a>.</p>
        </div>
    </div>
</div>
{% endblock %}
''')

# TERMS & CONDITIONS
write('templates/pages/terms.html', '''
{% extends "base.html" %}

{% block title %}Terms & Conditions - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-4">Terms & Conditions</h1>
    
    <div class="row">
        <div class="col-md-8">
            <h3>Agreement to Terms</h3>
            <p>By accessing and using this website, you accept and agree to be bound by the terms and provision of this agreement.</p>

            <h3 class="mt-4">Use License</h3>
            <p>Permission is granted to temporarily download one copy of the materials (information or software) on {{ site_settings.site_name }}'s website for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:</p>
            <ul>
                <li>Modify or copy the materials</li>
                <li>Use the materials for any commercial purpose or for any public display</li>
                <li>Attempt to decompile or reverse engineer any software contained on the website</li>
                <li>Remove any copyright or other proprietary notations from the materials</li>
            </ul>

            <h3 class="mt-4">Disclaimer</h3>
            <p>The materials on {{ site_settings.site_name }}'s website are provided on an 'as is' basis. {{ site_settings.site_name }} makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>

            <h3 class="mt-4">Limitations</h3>
            <p>In no event shall {{ site_settings.site_name }} or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on {{ site_settings.site_name }}'s website.</p>

            <h3 class="mt-4">Accuracy of Materials</h3>
            <p>The materials appearing on {{ site_settings.site_name }}'s website could include technical, typographical, or photographic errors. {{ site_settings.site_name }} does not warrant that any of the materials on its website are accurate, complete, or current.</p>
        </div>
    </div>
</div>
{% endblock %}
''')

# SITEMAP.XML
write('templates/sitemap.xml', '''
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{{ site_url }}</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{{ site_url }}/courses/</loc>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{{ site_url }}/branches/</loc>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{{ site_url }}/blog/</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>{{ site_url }}/admissions/</loc>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>{{ site_url }}/contact/</loc>
        <priority>0.8</priority>
    </url>
    {% for course in courses %}
    <url>
        <loc>{{ site_url }}/courses/{{ course.slug }}/</loc>
        <priority>0.7</priority>
    </url>
    {% endfor %}
    {% for post in blog_posts %}
    <url>
        <loc>{{ site_url }}/blog/{{ post.slug }}/</loc>
        <priority>0.6</priority>
    </url>
    {% endfor %}
</urlset>
''')

print("📝 Creating static CSS...")

# MAIN CSS
write('static/css/style.css', '''
:root {
    --primary: #0B5D3B;
    --secondary: #D4AF37;
    --accent: #F8F5EE;
    --dark: #222222;
    --light: #F5F5F5;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', 'Open Sans', sans-serif;
    color: var(--dark);
    background: #fff;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', 'Poppins', serif;
    color: var(--dark);
    font-weight: 600;
}

/* Hero Slider */
.hero-slider {
    position: relative;
    height: 600px;
    overflow: hidden;
}

.hero-slider .swiper-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    background-size: cover;
    background-position: center;
    position: relative;
}

.hero-slider .swiper-slide::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.4);
}

.hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
}

.swiper-button-next, .swiper-button-prev {
    color: white;
}

.swiper-pagination-bullet-active {
    background-color: white;
}

/* Navbar */
.navbar {
    z-index: 1000;
}

.navbar-brand img {
    max-height: 50px;
}

.navbar-nav .nav-link {
    font-weight: 500;
    margin: 0 10px;
    transition: color 0.3s ease;
}

.navbar-nav .nav-link:hover {
    color: var(--primary) !important;
}

/* Cards */
.card {
    border: none;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

/* Buttons */
.btn-primary {
    background-color: var(--primary);
    border-color: var(--primary);
}

.btn-primary:hover {
    background-color: #084b2d;
    border-color: #084b2d;
}

.btn-outline-primary {
    color: var(--primary);
    border-color: var(--primary);
}

.btn-outline-primary:hover {
    background-color: var(--primary);
}

/* Floating Buttons */
.whatsapp-btn, .call-btn {
    position: fixed;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: white;
    text-decoration: none;
    z-index: 999;
    animation: pulse 2s infinite;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.whatsapp-btn {
    background-color: #25d366;
    bottom: 80px;
    right: 20px;
}

.call-btn {
    background-color: var(--primary);
    bottom: 20px;
    right: 20px;
}

.whatsapp-btn:hover, .call-btn:hover {
    transform: scale(1.1);
    text-decoration: none;
    color: white;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

/* Counter Animation */
.counter {
    font-size: 2.5rem;
    font-weight: bold;
    color: var(--primary);
}

/* Footer */
footer {
    margin-top: 5rem;
    padding: 3rem 0 1rem;
}

footer a {
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}

/* Announcement Bar */
.announcement-bar {
    background-color: #333;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-slider {
        height: 400px;
    }

    .hero-content h1 {
        font-size: 1.8rem;
    }

    .whatsapp-btn, .call-btn {
        width: 50px;
        height: 50px;
        font-size: 20px;
    }
}
''')

print("📝 Creating static JS...")

# MAIN JS
write('static/js/main.js', '''
// Initialize Swiper
const heroSwiper = new Swiper('.hero-slider .swiper', {
    slidesPerView: 1,
    spaceBetween: 0,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: false,
});

// Counter Animation
function animateCounter() {
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = parseInt(counter.textContent);
        const increment = target / 100;
        let current = 0;
        
        const updateCount = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current) + '+';
                setTimeout(updateCount, 20);
            } else {
                counter.textContent = target + '+';
            }
        };
        
        updateCount();
    });
}

// Trigger counter animation when visible
window.addEventListener('load', () => {
    const counterSection = document.querySelector('.counter');
    if (counterSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter();
                    observer.unobserve(entry.target);
                }
            });
        });
        observer.observe(counterSection);
    }
});

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Navbar toggler
document.addEventListener('click', function (e) {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbar = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbar && !navbarToggler.contains(e.target) && !navbar.contains(e.target)) {
        if (navbar.classList.contains('show')) {
            navbarToggler.click();
        }
    }
});

// Form handling
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function (e) {
        console.log('Form submitted');
    });
});

// Lazy loading images
if ('IntersectionObserver' in window) {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.src = entry.target.dataset.src;
                observer.unobserve(entry.target);
            }
        });
    });
    images.forEach(img => imageObserver.observe(img));
}

console.log('✓ Evren Academy site initialized');
''')

print("\n" + "═" * 80)
print("✅ PHASE 3 COMPLETE - Templates & Static Files Created!")
print("═" * 80)

print("\n📋 Summary of Generated Files:")
print("  ✓ Base template (base.html)")
print("  ✓ Header and Footer components")
print("  ✓ Homepage template with sliders")
print("  ✓ Course listing and detail pages")
print("  ✓ Branch listing pages")
print("  ✓ Contact, Admission, and Career pages")
print("  ✓ Privacy Policy and Terms & Conditions")
print("  ✓ Responsive CSS (Bootstrap + Custom)")
print("  ✓ JavaScript with animations (Swiper, AOS)")

print("\n🚀 TO LAUNCH YOUR SITE:\n")
print("1. In project directory, activate venv:")
print("   venv\\\\Scripts\\\\activate\n")

print("2. Run migrations:")
print("   python manage.py makemigrations")
print("   python manage.py migrate\n")

print("3. Create superuser:")
print("   python manage.py createsuperuser\n")

print("4. Collect static files:")
print("   python manage.py collectstatic --noinput\n")

print("5. Run development server:")
print("   python manage.py runserver\n")

print("6. Access in browser:")
print("   Website: http://localhost:8000")
print("   Admin: http://localhost:8000/admin\n")

print("═" * 80)
