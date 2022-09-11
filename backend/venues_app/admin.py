from django.contrib import admin

from venues_app.models import Venue, SeatSection, Seat, VenueEmployee


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "postal_code", "owner", "established", "max_capacity")
    raw_id_fields = ("owner",)
    search_fields = (
        "name", 
        "city", 
        "postal_code", 
        "owner__username", 
        "owner__first_name", 
        "owner__last_name", 
        "owner__email", 
        "owner__phone_primary",
    )
    ordering = ("name", "city", "-created")

@admin.register(SeatSection)
class SeatSectionAdmin(admin.ModelAdmin):
    list_display = ("name", "venue", "total_seats", "price_per_seat")
    raw_id_fields = ("venue",)
    search_fields = (
        "name",
        "venue__name",
        "venue__city", 
        "venue__postal_code", 
        "venue__owner__username", 
        "venue__owner__first_name", 
        "venue__owner__last_name", 
        "venue__owner__email", 
        "venue__owner__phone_primary",
    )
    ordering = ("venue", "name")

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat_number", "section", "status", "price")
    raw_id_fields = ("section",)
    search_fields = (
        "seat_number",
        "section__name",
        "section__venue__name",
        "section__venue__city", 
        "section__venue__postal_code", 
        "section__venue__owner__username", 
        "section__venue__owner__first_name", 
        "section__venue__owner__last_name", 
        "section__venue__owner__email", 
        "section__venue__owner__phone_primary",
    )
    ordering = ("section", "seat_number")


@admin.register(VenueEmployee)
class VenueEmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee", "venue", "employee_type", "contract_type")
    raw_id_fields = ("employee", "venue")
    search_fields = (
        "employee__username",
        "employee__first_name",
        "employee__last_name",
        "employee__email",
        "employee_phone_primary",
        "venue__name",
        "venue__city"
    )
    ordering = ("venue", "employee", "-created")

