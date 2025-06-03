# 🏨 Hotel – Django webová aplikace

Tento projekt je webová aplikace napsaná v Pythonu pomocí frameworku **Django**.

Slouží k recepci pro monitorování hostů v pokojích.

---

## ✅ Požadavky

- Python 3.8 nebo novější
- `pip` (správce balíčků)
- Doporučeno: virtuální prostředí (`venv`)

---

## 🚀 Instalace a spuštění

1. **Klonování repozitáře a přechod do složky:**

    ```bash
    git clone https://github.com/AdamVehovsky/hotel.git
    cd hotel
    ```

2. **Vytvoření a aktivace virtuálního prostředí:**

    - **Windows:**
        ```bash
        python -m venv venv
        hotel\Scripts\activate
        ```

3. **Instalace závislostí:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Aplikace migrací databáze:**

    ```bash
    python manage.py migrate
    ```

5. **(Volitelné) Vytvoření superuživatele:**
   Mělo by fungovat jméno a heslo pro přihlašení do django-admin, které jsem nastavil: adam, adam

    ```bash
    python manage.py createsuperuser
    ```

7. **Spuštění vývojového serveru:**

    ```bash
    python manage.py runserver
    ```

    Aplikace poběží na: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Struktura projektu

- `manage.py` – hlavní spouštěcí skript
- `hotel/` – hlavní konfigurační složka projektu
- `requirements.txt` – seznam Python závislosti

---

## 🛠️ Použité technologie

- Python
- Django
