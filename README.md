# Rumah Sunat Happy Marketing Website

Website Django modern untuk kebutuhan marketing Rumah Sunat Happy Samarinda.

## Menjalankan Project

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py runserver
```

Buka `http://127.0.0.1:8000/`.

## Deploy ke Railway

Project ini sudah disiapkan untuk Railway:

- `Procfile` menjalankan Gunicorn.
- `railway.json` menjalankan `collectstatic` saat build.
- WhiteNoise menyajikan static files Django.

Environment variable yang disarankan di Railway:

```text
DEBUG=False
SECRET_KEY=<isi-dengan-secret-key-kuat>
ALLOWED_HOSTS=.up.railway.app,sunatmoderensamarinda.com,www.sunatmoderensamarinda.com
```

## Struktur

- `sunat_happy/` konfigurasi utama Django.
- `marketing/` aplikasi landing page.
- `marketing/templates/marketing/home.html` halaman utama.
- `marketing/static/marketing/css/styles.css` styling modern.
