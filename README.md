# Tuyou Dental (Django)

Dynamic dental clinic website built with **Python + Django** and **SQLite**.

## Run locally

```powershell
cd "c:\Users\ifosu\OneDrive\Desktop\DentalAi"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Site: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Manage content (dynamic)

In Admin you can update:
- **Site settings** (hero text, CTA links, hours, contact info)
- **Services**
- **Team members**
- **Testimonials**
- **FAQs**
- **Blog posts**
- **Appointment requests** (incoming)
- **Contact messages** (incoming)

## Notes

- Database file: `db.sqlite3`
- Templates: `templates/`
- Static assets: `static/`

Hosted using varcel
(tuyoudental.vercel.app)

