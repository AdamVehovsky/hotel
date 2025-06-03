from django.contrib import admin
from datetime import timedelta
from .models import Host, Pokoj, Rezervace, Platba

class RezervaceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Calculate "Cena celkem" (total price)
        if obj.datum_prijezdu and obj.datum_odjezdu and obj.pokoj:
            nights = (obj.datum_odjezdu - obj.datum_prijezdu).days
            obj.cena_celkem = obj.pokoj.cena_za_noc * nights
        obj.clean()
        super().save_model(request, obj, form, change)

admin.site.register(Host)
admin.site.register(Pokoj)
admin.site.register(Rezervace, RezervaceAdmin)
admin.site.register(Platba)