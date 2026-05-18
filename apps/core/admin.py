from django.contrib import admin
from django.utils.html import format_html

from .models import (
    CTASection,
    HeroSlide,
    InstitutionProfile,
    Popup,
    SiteSettings,
    Statistic,
    TeamMember,
)


# ==========================================
# Site Settings Admin
# ==========================================
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone', 'whatsapp_link', 'email', 'show_announcement')
    readonly_fields = ('logo_preview', 'favicon_preview', 'whatsapp_link')

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'site_name',
                'tagline',
                'logo',
                'logo_preview',
                'favicon',
                'favicon_preview',
            )
        }),
        ('Contact Information', {
            'fields': (
                'phone',
                'whatsapp',
                'whatsapp_link',
                'email',
                'address',
                'google_map_embed',
            )
        }),
        ('Social Media Links', {
            'fields': (
                'facebook',
                'twitter',
                'instagram',
                'linkedin',
                'youtube',
            )
        }),
        ('Design Settings', {
            'fields': (
                'primary_color',
                'secondary_color',
                'hero_autoplay_ms',
                'hero_transition_ms',
                'hero_overlay_opacity',
                'hero_media_fit',
            )
        }),
        ('Footer & Announcement', {
            'fields': (
                'footer_about',
                'footer_text',
                'copyright',
                'announcement',
                'show_announcement',
            )
        }),
    )

    def has_add_permission(self, request):
        # Allow only one Site Settings object
        return not SiteSettings.objects.exists()

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 70px; width: auto;" />', obj.logo.url)
        return 'No logo uploaded'

    def favicon_preview(self, obj):
        if obj.favicon:
            return format_html('<img src="{}" style="height: 32px; width: 32px; object-fit: contain;" />', obj.favicon.url)
        return 'No favicon uploaded'

    def whatsapp_link(self, obj):
        if obj and obj.whatsapp_url:
            return format_html('<a href="{}" target="_blank" rel="noopener">Open WhatsApp</a>', obj.whatsapp_url)
        return 'Add a WhatsApp number'

    logo_preview.short_description = 'Logo preview'
    favicon_preview.short_description = 'Favicon preview'
    whatsapp_link.short_description = 'WhatsApp test link'


# ==========================================
# Hero Slide Admin
# ==========================================
@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'media_type',
        'preview',
        'is_active',
        'order',
    )
    list_editable = (
        'is_active',
        'order',
    )
    list_filter = (
        'media_type',
        'is_active',
    )
    list_per_page = 25
    search_fields = (
        'title',
        'subtitle',
        'label',
    )
    ordering = ('order',)

    fieldsets = (
        ('Slide Content', {
            'fields': (
                'title',
                'subtitle',
                'label',
                'content',
            )
        }),
        ('Media Settings', {
            'fields': (
                'media_type',
                'image',
                'video',
                'video_url',
                'preview',
            ),
            'description': (
                'Choose Image or Video. '
                'For best quality use 1920x900 or larger images and optimized MP4 videos.'
            )
        }),
        ('Button Settings', {
            'fields': (
                'button_text',
                'button_link',
            )
        }),
        ('Display Settings', {
            'fields': (
                'is_active',
                'order',
            )
        }),
    )

    readonly_fields = ('preview',)

    def preview(self, obj):
        # Uploaded video preview
        if obj.media_type == 'video' and obj.video:
            return format_html(
                '''
                <video width="250" controls muted
                       style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                    <source src="{}" type="video/mp4">
                </video>
                ''',
                obj.video.url
            )

        # Image preview
        if obj.image:
            return format_html(
                '''
                <img src="{}"
                     width="250"
                     style="border-radius: 8px;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
                ''',
                obj.image.url
            )

        # External video URL
        if obj.media_type == 'video' and obj.video_url:
            return format_html(
                '<a href="{}" target="_blank">Open Video URL</a>',
                obj.video_url
            )

        return "No media uploaded"

    preview.short_description = 'Preview'


# ==========================================
# Statistic Admin
# ==========================================
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'value',
        'unit',
        'order',
    )
    list_editable = ('order',)
    search_fields = ('label',)
    ordering = ('order',)
    list_per_page = 50


@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    readonly_fields = ('updated_at', 'image_preview')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'image', 'image_preview')
        }),
        ('Button', {
            'fields': ('button_text', 'button_link')
        }),
        ('Display', {
            'fields': ('is_active', 'updated_at')
        }),
    )

    def has_add_permission(self, request):
        return not CTASection.objects.exists()

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 260px; border-radius: 8px;" />', obj.image.url)
        return 'No image uploaded'


@admin.register(Popup)
class PopupAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_on_homepage', 'show_once_per_session', 'is_active', 'start_date', 'end_date', 'display_order')
    list_editable = ('show_on_homepage', 'show_once_per_session', 'is_active', 'display_order')
    list_filter = ('is_active', 'show_on_homepage', 'show_once_per_session')
    search_fields = ('title', 'description')
    readonly_fields = ('updated_at', 'image_preview')
    ordering = ('display_order', '-updated_at')
    fieldsets = (
        ('Popup Content', {
            'fields': ('title', 'description', 'image', 'image_preview')
        }),
        ('Action Button', {
            'fields': ('button_text', 'button_url')
        }),
        ('Display Rules', {
            'fields': ('show_on_homepage', 'show_once_per_session', 'is_active', 'start_date', 'end_date', 'display_order', 'updated_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 260px; border-radius: 8px;" />', obj.image.url)
        return 'No image uploaded'


@admin.register(InstitutionProfile)
class InstitutionProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('About Page', {
            'fields': ('title', 'intro', 'mission', 'vision', 'history')
        }),
        ('Admission Page', {
            'fields': ('admission_overview', 'eligibility')
        }),
        ('Career Page', {
            'fields': ('career_overview',)
        }),
    )

    def has_add_permission(self, request):
        return not InstitutionProfile.objects.exists()


# ==========================================
# Team Member Admin
# ==========================================
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'display_designation',
        'team_category',
        'is_active',
        'image_preview',
        'display_order',
    )
    list_editable = ('team_category', 'is_active', 'display_order')
    list_filter = ('team_category', 'is_active')
    search_fields = (
        'name',
        'title',
        'full_name',
        'designation',
    )
    ordering = ('display_order', 'order')

    readonly_fields = ('image_preview',)

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'full_name',
                'designation',
                'team_category',
                'photo',
                'image_preview',
                'short_bio',
            )
        }),
        ('Social Links', {
            'fields': (
                'linkedin_url',
                'facebook_url',
                'instagram_url',
            )
        }),
        ('Legacy Content', {
            'classes': ('collapse',),
            'fields': (
                'name',
                'title',
                'role',
                'image',
                'bio',
                'order',
            )
        }),
        ('Display Controls', {
            'fields': (
                'display_order',
                'is_active',
            )
        }),
    )

    def image_preview(self, obj):
        image = obj.display_photo
        if image:
            return format_html(
                '''
                <img src="{}"
                     width="120"
                     height="120"
                     style="object-fit: cover;
                            border-radius: 50%;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
                ''',
                image.url
            )
        return "No image"

    image_preview.short_description = 'Preview'
