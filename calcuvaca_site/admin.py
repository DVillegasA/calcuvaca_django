from django.contrib import admin
from calcuvaca_site.models import Employ, VacationTaken

class EmployAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_date', 'created_at', 'modified_at')

class VacationTakenAdmin(admin.ModelAdmin):
    list_display = ('employ', 'vacation_days', 'vacation_date')

admin.site.register(Employ, EmployAdmin)
admin.site.register(VacationTaken, VacationTakenAdmin)
