from django.contrib import admin

from .models import Advisor, Donation, Member, PresidentMessage, Project, VicePresidentMessage


@admin.register(PresidentMessage)
class PresidentMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "designation", "message")


@admin.register(VicePresidentMessage)
class VicePresidentMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "designation", "message")


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_active", "ordering")
    list_editable = ("ordering",)
    list_filter = ("is_active",)
    search_fields = ("name", "designation", "message")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "whatsapp_number", "ordering")
    list_editable = ("ordering",)
    search_fields = ("name", "designation", "bio", "whatsapp_number")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "project_date", "ordering")
    list_editable = ("ordering",)
    search_fields = ("title", "description")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "donation_date", "ordering")
    list_editable = ("ordering",)
    search_fields = ("title", "description", "amount")
