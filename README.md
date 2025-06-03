# 🏨 Hotel – Django aplikace

Tento projekt je webová aplikace napsaná v Pythonu pomocí virtuálního prostředí django.

Slouží k recepci pro monitorování hostů v pokojích.

---

## ✅ Požadavky

- Python 3.8 nebo novější
- `pip` (správce balíčků)
- Virtuální prostředí (`venv`)

---

## 🚀 Instalace a spuštění

1. **Klonování repozitáře a přechod do složky:**

    ```bash
    git clone https://github.com/AdamVehovsky/hotel.git
    cd hotel
    ```

2. **Aktivace virtuálního prostředí:**

    - **Windows:**
        ```
        hotel\Scripts\activate
        ```

3. **Instalace requirements:**

    ```
    pip install -r requirements.txt
    ```

4. **Migrace databáze (volitelné):**

    ```
    python manage.py migrate
    ```

5. **(Volitelné) Vytvoření superuživatele:**
   Mělo by fungovat jméno a heslo pro přihlašení do django-admin, které jsem nastavil: adam, adam

    ```
    python manage.py createsuperuser
    ```

7. **Spuštění serveru:**

    ```
    python manage.py runserver
    ```

    Aplikace poběží na: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Struktura projektu

- `manage.py` – hlavní spouštěcí skript
- `hotel/` – hlavní konfigurační složka projektu
- `requirements.txt` – seznam Python požadavků

---

## 🛠️ Použité technologie

- Python
- Django
