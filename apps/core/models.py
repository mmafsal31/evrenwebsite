from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
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

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    primary_color = models.CharField(max_length=7, default='#0B5D3B')
    secondary_color = models.CharField(max_length=7, default='#D4AF37')

    footer_text = RichTextUploadingField(blank=True, null=True)

    announcement = models.CharField(max_length=500, blank=True)
    show_announcement = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name


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

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='faculty')

    image = models.ImageField(
        upload_to='team/',
        blank=True,
        null=True
    )

    bio = RichTextUploadingField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name
