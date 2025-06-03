from django.db import models

class Host(models.Model):
    jmeno = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    narodnost = models.CharField(max_length=50)

    def __str__(self):
        return self.jmeno


class Pokoj(models.Model):
    TYP_POKOJE_CHOICES = [
        ('jednoluzkovy', 'Jednolůžkový'),
        ('dvouluzkovy', 'Dvoulůžkový'),
        ('apartma', 'Apartmá'),
    ]

    cislo = models.IntegerField(unique=True)
    typ_pokoje = models.CharField(max_length=20, choices=TYP_POKOJE_CHOICES)
    stav = models.CharField(max_length=20, choices=[('volny', 'Volný'), ('obsazeny', 'Obsazený')])
    cena_za_noc = models.DecimalField(max_digits=8, decimal_places=2)
    kapacita = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cislo} - {self.get_typ_pokoje_display()}"


class Rezervace(models.Model):
    STAV_REZERVACE_CHOICES = [
        ('potvrzeno', 'Potvrzeno'),
        ('ceka_na_potvrzeni', 'Čeká na potvrzení'),
        ('zruseno', 'Zrušeno'),
    ]

    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    pokoj = models.ForeignKey(Pokoj, on_delete=models.CASCADE)
    datum_prijezdu = models.DateField()
    datum_odjezdu = models.DateField()
    pocet_osob = models.PositiveIntegerField()
    stav = models.CharField(max_length=30, choices=STAV_REZERVACE_CHOICES)
    specialni_pozadavky = models.TextField(blank=True)

    def __str__(self):
        return f"Rezervace {self.id} - {self.host}"


class Platba(models.Model):
    ZPUSOB_PLATBY_CHOICES = [
        ('hotove', 'Hotově'),
        ('kartou', 'Kartou'),
        ('prevodem', 'Převodem'),
    ]

    rezervace = models.ForeignKey(Rezervace, on_delete=models.CASCADE)
    zpusob = models.CharField(max_length=20, choices=ZPUSOB_PLATBY_CHOICES)
    castka = models.DecimalField(max_digits=10, decimal_places=2)
    datum_platby = models.DateField(null=True, blank=True)
    stav = models.CharField(max_length=30, choices=[
        ('zaplaceno', 'Zaplaceno'),
        ('ceka_na_uhradu', 'Čeká na úhradu'),
        ('nezaplaceno', 'Nezaplaceno'),
    ])

    def __str__(self):
        return f"Platba {self.id} - {self.rezervace}"
