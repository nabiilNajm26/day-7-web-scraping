# day-7-web-scraping
Deskripsi tugas:
- Tujuan: Membuat program untuk melakukan web scraping pada halaman web yang mengandung kutipan, penulis, dan tag-tag yang terkait dengan kutipan tersebut. Data hasil scraping akan disimpan dalam format CSV.
- Sumber Data: Halaman web yang berisi kutipan beserta informasi penulis dan tag-tag terkait.
- Tools yang Digunakan: Python, library BeautifulSoup untuk melakukan web scraping, library Pandas untuk manipulasi dan penyimpanan data dalam format CSV.
- Langkah-langkah:
  1. Menggunakan library requests, mengirim permintaan GET ke URL halaman web yang berisi kutipan.
  2. Menggunakan library BeautifulSoup, mengekstrak data kutipan, penulis, dan tag-tag terkait dari struktur HTML halaman web.
  3. Menyimpan data yang telah diekstrak ke dalam struktur data yang sesuai (misalnya, list atau DataFrame).
  4. Menggunakan library Pandas, menyimpan data ke dalam file CSV dengan menggunakan metode `to_csv()`.
- Output: File CSV yang berisi data kutipan, penulis, dan tag-tag terkait.
- Validasi: Melakukan pengecekan bahwa data yang telah diekstrak sesuai dengan struktur yang diharapkan dan bahwa file CSV telah berhasil dibuat dan berisi data yang benar.
- Kesimpulan: Setelah menjalankan program, data kutipan, penulis, dan tag-tag terkait telah berhasil diambil dari halaman web dan disimpan dalam file CSV, siap digunakan untuk analisis lebih lanjut atau tujuan lainnya.
