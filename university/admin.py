from django.contrib import admin

from .models import (
    University,
    City,
    StateAndPaidInfo,
    BenefitsBoolean,
    Hostel
)

admin.site.register(City)

class StateAndPaidInfo(admin.StackedInline):
    model = StateAndPaidInfo

class BenefitsBoolean(admin.StackedInline):
    model = BenefitsBoolean

class Hostel(admin.StackedInline):
    model = Hostel

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [
        StateAndPaidInfo,
        BenefitsBoolean,
        Hostel,
    ]
