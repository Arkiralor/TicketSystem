from django.contrib import admin

from user_app.models import User, UserProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "regnal_number","email", "phone_primary", "is_active")
    search_fields = ("username", "first_name", "last_name", "regnal_number","email", "phone_primary", "date_joined")
    ordering = ("-date_joined", "username")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "birthday", "location")
    search_fields = (
        "user__username", 
        "user__first_name", 
        "user__last_name", 
        "user__regnal_number", 
        "user__email", 
        "user__phone_primary", 
        "user__date_joined"
    )
    ordering = ("-created",)