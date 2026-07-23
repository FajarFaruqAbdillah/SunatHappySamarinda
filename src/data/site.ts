export const site = {
  name: "Rumah Sunat Happy Samarinda",
  shortName: "Rumah Sunat Happy",
  url: "https://sunathappy.com",
  primaryWhatsapp: "628125868203",
  address:
    "Jl. Wahid Hasim 2, Ruko Green City No. 04, Sempaja, Samarinda, Kalimantan Timur",
  mapUrl: "https://maps.app.goo.gl/LFjScP7CVBtvsXwf7",
  mapEmbedUrl:
    "https://www.google.com/maps?q=Rumah%20Sunat%20Happy%20Samarinda%2C%20Jl.%20Wahid%20Hasim%202%20Ruko%20Green%20City%20No.%2004%2C%20Sempaja%2C%20Samarinda&output=embed",
};

export const contacts = [
  { name: "Arif", phone: "0812 5868 203", wa: "628125868203" },
  { name: "Hamid", phone: "0813 4750 2281", wa: "6281347502281" },
  { name: "Yudi", phone: "0821 5425 0353", wa: "6282154250353" },
];

export const methods = [
  {
    name: "Konvensional",
    description:
      "Pilihan prosedur standar dengan pendampingan tenaga berpengalaman.",
  },
  {
    name: "Laser / Flascutter",
    description:
      "Metode modern untuk tindakan yang lebih cepat dan perawatan praktis.",
  },
  {
    name: "Super Ring",
    description:
      "Metode tanpa jahit yang banyak dipilih untuk anak aktif.",
  },
  {
    name: "Tabung",
    description:
      "Pilihan nyaman dengan perlindungan area tindakan selama pemulihan.",
  },
  {
    name: "Stapler",
    description:
      "Teknik rapi untuk kebutuhan tertentu, termasuk pasien dewasa.",
  },
  {
    name: "Lem",
    description:
      "Pendekatan minim jahitan untuk hasil yang lebih estetis.",
  },
];

export const benefits = [
  "Bius tanpa jarum suntik untuk pengalaman yang minim nyeri.",
  "Banyak pilihan metode sesuai usia, kondisi, dan kenyamanan keluarga.",
  "Pendampingan kontrol langsung maupun via WhatsApp sampai sembuh.",
  "Melayani bayi, anak, dewasa, serta kerja sama kegiatan sunat massal.",
];

export const steps = [
  {
    title: "Konsultasi",
    description:
      "Diskusikan usia, kondisi, dan metode yang paling cocok melalui WhatsApp.",
  },
  {
    title: "Tindakan Nyaman",
    description:
      "Tim membantu anak lebih tenang dengan pendekatan ramah dan sugesti positif.",
  },
  {
    title: "Kontrol Pemulihan",
    description:
      "Keluarga tetap didampingi sampai proses penyembuhan selesai.",
  },
];

export const testimonials = [
  {
    quote:
      "Pelayanan ramah, anak jadi lebih tenang, dan kontrol setelah tindakan sangat membantu.",
    name: "Orang tua pasien",
  },
  {
    quote:
      "Pilihan metodenya jelas, konsultasi cepat, dan prosesnya terasa profesional.",
    name: "Keluarga pasien",
  },
];

export const faqs = [
  {
    question: "Apakah bisa konsultasi dulu sebelum menentukan metode?",
    answer:
      "Bisa. Tim akan membantu menjelaskan metode yang sesuai dengan usia dan kebutuhan pasien.",
  },
  {
    question: "Apakah melayani sunat dewasa?",
    answer: "Ya, Rumah Sunat Happy melayani bayi, anak, dan dewasa.",
  },
  {
    question: "Bagaimana kontrol setelah tindakan?",
    answer:
      "Kontrol bisa dilakukan dengan datang langsung atau melalui WhatsApp sampai pemulihan selesai.",
  },
];

export function whatsappUrl(message: string) {
  return `https://wa.me/${site.primaryWhatsapp}?text=${encodeURIComponent(message)}`;
}
