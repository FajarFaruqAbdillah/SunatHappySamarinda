# Rumah Sunat Happy Samarinda

Website marketing statis untuk [sunathappy.com](https://sunathappy.com), dibuat
dengan Astro. Hasil build berupa HTML, CSS, JavaScript, dan gambar yang dapat
langsung diunggah ke `public_html` Biznet Gio.

## Menjalankan Project

Persyaratan: Node.js 22.12 atau lebih baru.

```powershell
pnpm install
pnpm dev
```

Buka alamat yang ditampilkan Astro, biasanya `http://localhost:4321`.

## Pemeriksaan dan Build

```powershell
pnpm check
pnpm build
pnpm preview
```

Hasil website statis berada di folder `dist/`.

## Deploy ke Biznet Gio

1. Jalankan `pnpm build`.
2. Unggah seluruh isi folder `dist/` ke folder `public_html` melalui File
   Manager atau FTP.
3. Pastikan file `index.html` berada langsung di dalam `public_html`, bukan di
   dalam subfolder `dist`.
4. Aktifkan SSL gratis untuk `sunathappy.com` dan `www.sunathappy.com`.
5. Buka domain dan periksa tombol WhatsApp serta Google Maps.

Arsip siap unggah juga dapat dibuat dari isi `dist/`:

```powershell
New-Item -ItemType Directory -Path deploy -Force
Compress-Archive -Path dist\* -DestinationPath deploy\sunathappy-public_html.zip -Force
```

## Struktur

- `src/components/` komponen tiap bagian halaman.
- `src/data/site.ts` konten, nomor WhatsApp, dan alamat.
- `src/layouts/BaseLayout.astro` metadata SEO dan JavaScript global.
- `src/pages/` halaman yang dibangun Astro.
- `src/styles/global.css` tampilan responsif.
- `public/` gambar, favicon, sitemap, robots, dan konfigurasi hosting.
