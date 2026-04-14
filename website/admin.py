from django.contrib import admin

from .models import (
    AppointmentRequest,
    BlogPost,
    ContactMessage,
    FAQ,
    GalleryImage,
    Service,
    SiteSettings,
    TeamMember,
    Testimonial,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone", "email", "updated_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "sort_order", "updated_at")
    list_filter = ("featured",)
    search_fields = ("title", "short_description", "description")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "active", "sort_order", "updated_at")
    list_filter = ("active",)
    search_fields = ("name", "role", "bio")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "rating", "approved", "featured", "sort_order", "created_at")
    list_filter = ("approved", "featured", "rating")
    search_fields = ("author_name", "quote")
    list_editable = ("approved", "featured")
    actions = ("approve_selected", "unapprove_selected")

    @admin.action(description="Approve selected testimonials")
    def approve_selected(self, request, queryset):
        queryset.update(approved=True)

    @admin.action(description="Unapprove selected testimonials")
    def unapprove_selected(self, request, queryset):
        queryset.update(approved=False)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "active", "sort_order", "updated_at")
    list_filter = ("active",)
    search_fields = ("question", "answer")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "active", "sort_order", "updated_at")
    list_filter = ("active",)
    search_fields = ("title", "caption", "image_url")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "published_at", "updated_at")
    list_filter = ("published",)
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "service", "preferred_date", "status", "created_at")
    list_filter = ("status", "service")
    search_fields = ("full_name", "phone", "email", "message")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("full_name", "email", "subject", "message")
