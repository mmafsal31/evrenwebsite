import re

from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
    HERO_MEDIA_FIT_CHOICES = (
        ('cover', 'Fill hero area (recommended)'),
        ('contain', 'Show full media without cropping'),
    )

    site_name = models.CharField(max_length=255, default='Evren Academy')
    tagline = models.CharField(max_length=255, blank=True)

    logo = models.ImageField(
        upload_to='site/',
        blank=True,
        null=True
    )
    favicon = models.ImageField(
        upload_to='site/',
        blank=True,
        null=True
    )

    phone = models.CharField(max_length=20, default='+92 300 1234567')
    whatsapp = models.CharField(max_length=20, default='+92 300 1234567')
    email = models.EmailField(default='info@evrenacademy.com')
    address = models.TextField(blank=True)
    google_map_embed = models.TextField(
        blank=True,
        help_text='Optional Google Maps iframe embed code for the contact page.'
    )

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    primary_color = models.CharField(max_length=7, default='#0B5D3B')
    secondary_color = models.CharField(max_length=7, default='#D4AF37')
    hero_autoplay_ms = models.PositiveIntegerField(
        default=5500,
        help_text='Hero slide autoplay delay in milliseconds.'
    )
    hero_transition_ms = models.PositiveIntegerField(
        default=1400,
        help_text='Hero dissolve transition speed in milliseconds.'
    )
    hero_overlay_opacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.55,
        help_text='Dark overlay strength from 0.00 to 1.00.'
    )
    hero_media_fit = models.CharField(
        max_length=10,
        choices=HERO_MEDIA_FIT_CHOICES,
        default='cover',
        help_text='Choose how hero images and videos should fill the slide.'
    )

    footer_about = models.TextField(
        blank=True,
        default='Premium educational institution dedicated to excellence in education.'
    )
    footer_text = RichTextUploadingField(blank=True, null=True)
    copyright = models.CharField(
        max_length=255,
        blank=True,
        default='Copyright (c) Evren Academy. All rights reserved.'
    )

    announcement = models.CharField(max_length=500, blank=True)
    show_announcement = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    @staticmethod
    def _digits(value):
        return re.sub(r'\D+', '', value or '')

    @property
    def whatsapp_digits(self):
        digits = self._digits(self.whatsapp)
        if len(digits) == 10:
            return f'91{digits}'
        return digits

    @property
    def phone_digits(self):
        return self._digits(self.phone)

    @property
    def whatsapp_url(self):
        if not self.whatsapp_digits:
            return ''
        return f'https://wa.me/{self.whatsapp_digits}'

    @property
    def tel_url(self):
        if not self.phone_digits:
            return ''
        return f'tel:+{self.phone_digits}'


class HeroSlide(models.Model):
    MEDIA_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_CHOICES,
        default='image'
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)

    label = models.CharField(
        max_length=100,
        blank=True,
        help_text='Small text above the main heading'
    )

    image = models.ImageField(
        upload_to='hero/images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='hero/videos/',
        blank=True,
        null=True,
        help_text='Upload MP4 video file'
    )

    video_url = models.URLField(
        blank=True,
        null=True,
        help_text='Optional MP4 video URL'
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        default='Learn More'
    )

    button_link = models.CharField(
        max_length=255,
        blank=True
    )

    content = RichTextUploadingField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Hero Slide'
        verbose_name_plural = 'Hero Slides'

    def __str__(self):
        return self.title


class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return f"{self.label}: {self.value}"


class CTASection(models.Model):
    title = models.CharField(max_length=255, default='Ready to begin your learning journey?')
    subtitle = models.CharField(max_length=500, blank=True)
    button_text = models.CharField(max_length=100, default='Apply for Admission')
    button_link = models.CharField(max_length=255, default='/admissions/')
    image = models.ImageField(upload_to='cta/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'CTA Section'
        verbose_name_plural = 'CTA Section'

    def __str__(self):
        return self.title


class Popup(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='popups/', blank=True, null=True)
    button_text = models.CharField(max_length=100, blank=True, default='Learn More')
    button_url = models.CharField(max_length=255, blank=True)
    show_on_homepage = models.BooleanField(default=True)
    show_once_per_session = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-updated_at']
        verbose_name = 'Popup'
        verbose_name_plural = 'Popups'

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        now = timezone.now()
        if not self.is_active:
            return False
        if self.start_date and self.start_date > now:
            return False
        if self.end_date and self.end_date < now:
            return False
        return True


class InstitutionProfile(models.Model):
    title = models.CharField(max_length=255, default='About Evren Academy')
    intro = RichTextUploadingField(blank=True, null=True)
    mission = RichTextUploadingField(blank=True, null=True)
    vision = RichTextUploadingField(blank=True, null=True)
    history = RichTextUploadingField(blank=True, null=True)
    admission_overview = RichTextUploadingField(blank=True, null=True)
    eligibility = RichTextUploadingField(blank=True, null=True)
    career_overview = RichTextUploadingField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Institution Profile'
        verbose_name_plural = 'Institution Profile'

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    ROLE_CHOICES = (
        ('associate', 'Associate'),
        ('advisory_board', 'Advisory Board'),
        ('faculty', 'Faculty'),
        ('principal', 'Principal'),
    )

    TEAM_CATEGORY_CHOICES = (
        ('advisory', 'Advisory Board'),
        ('management', 'Management Team'),
        ('faculty', 'Faculty Team'),
        ('staff', 'Staff'),
    )

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='faculty')
    full_name = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    team_category = models.CharField(max_length=30, choices=TEAM_CATEGORY_CHOICES, default='faculty')

    image = models.ImageField(
        upload_to='team/',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='team/',
        blank=True,
        null=True
    )

    bio = RichTextUploadingField(
        blank=True,
        null=True
    )
    short_bio = RichTextUploadingField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'order']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.display_name

    @property
    def display_name(self):
        return self.full_name or self.name

    @property
    def display_designation(self):
        return self.designation or self.title

    @property
    def display_photo(self):
        return self.photo or self.image

    @property
    def display_bio(self):
        return self.short_bio or self.bio
