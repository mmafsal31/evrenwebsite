from django.contrib import admin
from django.utils.html import format_html

from .models import SiteSettings, HeroSlide, Statistic, InstitutionProfile, TeamMember


# ==========================================
# Site Settings Admin
# ==========================================
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'site_name',
                'tagline',
                'logo',
                'favicon',
            )
        }),
        ('Contact Information', {
            'fields': (
                'phone',
                'whatsapp',
                'email',
                'address',
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
            )
        }),
        ('Footer & Announcement', {
            'fields': (
                'footer_text',
                'announcement',
                'show_announcement',
            )
        }),
    )

    def has_add_permission(self, request):
        # Allow only one Site Settings object
        return not SiteSettings.objects.exists()


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
            ),
            'description': (
                'Choose Image or Video. '
                'For video, upload an MP4 file or provide an external MP4 URL.'
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
        'name',
        'title',
        'role',
        'image_preview',
        'order',
    )
    list_editable = ('order',)
    list_filter = ('role',)
    search_fields = (
        'name',
        'title',
    )
    ordering = ('order',)

    readonly_fields = ('image_preview',)

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'title',
                'role',
                'image',
                'image_preview',
                'bio',
                'order',
            )
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '''
                <img src="{}"
                     width="120"
                     height="120"
                     style="object-fit: cover;
                            border-radius: 50%;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
                ''',
                obj.image.url
            )
        return "No image"

    image_preview.short_description = 'Preview'
