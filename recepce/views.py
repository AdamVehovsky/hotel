from django.shortcuts import render, get_object_or_404
from .models import Rezervace, Pokoj
from django.utils.timezone import now
import openpyxl
from django.http import HttpResponse

def index(request):
    today = now().date()
    rezervace_list = Rezervace.objects.select_related('host', 'pokoj').order_by('id')

    expired_rezervace = list(rezervace_list.filter(datum_odjezdu__lt=today))
    active_rezervace = list(rezervace_list.filter(datum_prijezdu__lte=today, datum_odjezdu__gte=today))
    future_rezervace = list(rezervace_list.filter(datum_prijezdu__gt=today))

    # Calculate cena_celkem for each reservation in each list
    for rezervace in expired_rezervace + active_rezervace + future_rezervace:
        nights = (rezervace.datum_odjezdu - rezervace.datum_prijezdu).days
        rezervace.cena_celkem = rezervace.pokoj.cena_za_noc * nights if nights > 0 else 0

    volne_pokoje = Pokoj.objects.filter(stav='volny').exclude(
        id__in=Rezervace.objects.filter(
            datum_prijezdu__lte=today,
            datum_odjezdu__gte=today
        ).values_list('pokoj_id', flat=True)
    )
    obsazene_pokoje = Pokoj.objects.filter(
        id__in=Rezervace.objects.filter(
            datum_prijezdu__lte=today,
            datum_odjezdu__gte=today
        ).values_list('pokoj_id', flat=True)
    )
    return render(request, 'index.html', {
        'expired_rezervace': expired_rezervace,
        'active_rezervace': active_rezervace,
        'future_rezervace': future_rezervace,
        'volne_pokoje': volne_pokoje,
        'obsazene_pokoje': obsazene_pokoje,
    })

def rezervace_list(request):
    rezervace_list = Rezervace.objects.select_related('host', 'pokoj').order_by('-datum_prijezdu')
    return render(request, 'rezervace_list.html', {
        'rezervace_list': rezervace_list
    })

def rezervace_detail(request, rezervace_id):
    rezervace = get_object_or_404(Rezervace, id=rezervace_id)
    return render(request, 'rezervace_detail.html', {
        'rezervace': rezervace
    })

def pokoje_list(request):
    pokoje = Pokoj.objects.all().order_by('cislo')
    return render(request, 'pokoje_list.html', {
        'pokoje': pokoje
    })



def export_rezervace_to_excel(request):
    # Vytvoření nového Excel souboru
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Rezervace"

    # Přidání hlaviček
    sheet.append([
        "ID", "Host", "Telefon", "Email", "Národnost", "Pokoj", "Druh pokoje",
        "Datum příjezdu", "Datum odjezdu", "Cena celkem", "Počet nocí",
        "Stav rezervace", "Speciální požadavky", "Datum platby", "Způsob platby"
    ])

    # Načtení dat z databáze
    rezervace_list = Rezervace.objects.select_related('host', 'pokoj').all()

    for rezervace in rezervace_list:
        # Výpočet ceny celkem a počtu nocí
        if rezervace.datum_prijezdu and rezervace.datum_odjezdu:
            nights = (rezervace.datum_odjezdu - rezervace.datum_prijezdu).days
            cena_celkem = rezervace.pokoj.cena_za_noc * nights if nights > 0 else 0
        else:
            nights = 0
            cena_celkem = 0

        # Získání dat o platbě (pokud existují)
        platba = rezervace.platba_set.first()  # Předpokládáme, že rezervace má vztah k platbám
        datum_platby = platba.datum_platby if platba else "Není zaplaceno"
        zpusob_platby = platba.zpusob if platba else "Neuvedeno"

        # Přidání dat do Excelu
        sheet.append([
            rezervace.id,
            rezervace.host.jmeno if rezervace.host else "N/A",
            rezervace.host.telefon if rezervace.host else "N/A",
            rezervace.host.email if rezervace.host else "N/A",
            rezervace.host.narodnost if rezervace.host else "N/A",
            rezervace.pokoj.cislo if rezervace.pokoj else "N/A",
            rezervace.pokoj.typ_pokoje if rezervace.pokoj else "N/A",
            rezervace.datum_prijezdu,
            rezervace.datum_odjezdu,
            cena_celkem,
            nights,
            rezervace.stav,
            rezervace.specialni_pozadavky if rezervace.specialni_pozadavky else "Žádné",
            datum_platby,
            zpusob_platby
        ])

    # Nastavení odpovědi pro stažení souboru
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=rezervace.xlsx'

    # Uložení Excel souboru do odpovědi
    workbook.save(response)
    return response