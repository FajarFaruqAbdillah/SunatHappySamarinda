from urllib.parse import quote

from django.shortcuts import redirect, render


def home(request):
    contacts = [
        {"name": "Arif", "phone": "0812 5868 203", "wa": "628125868203"},
        {"name": "Hamid", "phone": "0813 4750 2281", "wa": "6281347502281"},
        {"name": "Yudi", "phone": "0821 5425 0353", "wa": "6282154250353"},
    ]

    context = {
        "primary_wa": "628125868203",
        "map_url": "https://maps.app.goo.gl/LFjScP7CVBtvsXwf7",
        "map_embed_url": (
            "https://www.google.com/maps"
            "?q=Rumah%20Sunat%20Happy%20Samarinda%2C%20Jl.%20Wahid%20Hasim%202"
            "%20Ruko%20Green%20City%20No.%2004%2C%20Sempaja%2C%20Samarinda"
            "&output=embed"
        ),
        "contacts": contacts,
        "methods": [
            {
                "name": "Konvensional",
                "desc": "Pilihan prosedur standar dengan pendampingan tenaga berpengalaman.",
            },
            {
                "name": "Laser / Flascutter",
                "desc": "Metode modern untuk tindakan yang lebih cepat dan perawatan praktis.",
            },
            {
                "name": "Super Ring",
                "desc": "Metode tanpa jahit yang banyak dipilih untuk anak aktif.",
            },
            {
                "name": "Tabung",
                "desc": "Pilihan nyaman dengan perlindungan area tindakan selama pemulihan.",
            },
            {
                "name": "Stapler",
                "desc": "Teknik rapi untuk kebutuhan tertentu, termasuk pasien dewasa.",
            },
            {
                "name": "Lem",
                "desc": "Pendekatan minim jahitan untuk hasil yang lebih estetis.",
            },
        ],
        "benefits": [
            "Bius tanpa jarum suntik untuk pengalaman yang minim nyeri.",
            "Banyak pilihan metode sesuai usia, kondisi, dan kenyamanan keluarga.",
            "Pendampingan kontrol langsung maupun via WhatsApp sampai sembuh.",
            "Melayani bayi, anak, dewasa, serta kerja sama kegiatan sunat massal.",
        ],
        "steps": [
            {
                "title": "Konsultasi",
                "text": "Diskusikan usia, kondisi, dan metode yang paling cocok melalui WhatsApp.",
            },
            {
                "title": "Tindakan Nyaman",
                "text": "Tim membantu anak lebih tenang dengan pendekatan ramah dan sugesti positif.",
            },
            {
                "title": "Kontrol Pemulihan",
                "text": "Keluarga tetap didampingi sampai proses penyembuhan selesai.",
            },
        ],
        "testimonials": [
            {
                "quote": "Pelayanan ramah, anak jadi lebih tenang, dan kontrol setelah tindakan sangat membantu.",
                "name": "Orang tua pasien",
            },
            {
                "quote": "Pilihan metodenya jelas, konsultasi cepat, dan prosesnya terasa profesional.",
                "name": "Keluarga pasien",
            },
        ],
        "faqs": [
            {
                "question": "Apakah bisa konsultasi dulu sebelum menentukan metode?",
                "answer": "Bisa. Tim akan membantu menjelaskan metode yang sesuai dengan usia dan kebutuhan pasien.",
            },
            {
                "question": "Apakah melayani sunat dewasa?",
                "answer": "Ya, Rumah Sunat Happy melayani bayi, anak, dan dewasa.",
            },
            {
                "question": "Bagaimana kontrol setelah tindakan?",
                "answer": "Kontrol bisa dilakukan dengan datang langsung atau melalui WhatsApp sampai pemulihan selesai.",
            },
        ],
    }
    return render(request, "marketing/home.html", context)


def lead(request):
    if request.method != "POST":
        return redirect("marketing:home")

    name = request.POST.get("name", "").strip() or "Calon pasien"
    phone = request.POST.get("phone", "").strip() or "-"
    need = request.POST.get("need", "").strip() or "Konsultasi metode sunat"
    message = (
        "Halo Rumah Sunat Happy, saya ingin konsultasi.\n"
        f"Nama: {name}\n"
        f"No. WhatsApp: {phone}\n"
        f"Kebutuhan: {need}"
    )
    return redirect(f"https://wa.me/628125868203?text={quote(message)}")
