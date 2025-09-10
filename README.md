Tautan: https://jessevan-gerard-sigmashop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Pertama-tama, saya mengikuti setiap langkah-langkah yang penting mengikuti tutorial yang diberikan kemarin, sembari mengikut tutorial, saya mengubah beberapa variabel seperti yang diminta dalam tugas kali ini, contohnya membuat model pada aplikasi main dengan nama "Product", bukan "News", lalu menambahkan atribut-atribut yang diminta seperti name, price, description, thumbnail, category, dan is_featured. Lalu menyelesaikan langkah-langkah berikutnya seperti pada tutorial kemarin.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    - Berikut bagan singkat mengenai request client ke web aplikasi berbasis Django beserta responnya:
        Klien (Peramban Web)
            |
            | Permintaan URL (mis. /produk/1)
            v
        -----------------
        |  urls.py      |  <-- Pemetaan URL
        -----------------
            |
            | Mengarahkan permintaan ke fungsi yang sesuai
            v
        -----------------
        |  views.py     |  <-- Logika Bisnis
        -----------------
            |
            | Membutuhkan data?
            v
            |------------------------------------
            |              Ya                  |
            |              v                   |
        -----------------      |
        |  models.py    |  <-- Interaksi Basis Data
        -----------------      |
            |              |
            | Mengambil/Mengubah Data
            v
        -----------------      |
        |  views.py     |  <-- Mendapatkan Data
        -----------------
            |
            | Merender template dengan data
            v
        -----------------
        |  Berkas HTML  |  <-- Tampilan Antarmuka (Templat)
        -----------------
            |
            | Mengirim tanggapan HTML yang sudah dirender
            v
        -----------------
        |  Klien        |
        -----------------
    Kaitan yang bisa dijelaskan berdasarkan alur di atas:

    urls.py: Berkas ini berperan sebagai pemeta atau dispatcher URL. Ketika permintaan masuk dari klien, Django pertama kali melihat urls.py untuk mencocokkan URL yang diminta (/produk/1/) dengan pola yang sudah didefinisikan. Jika ada kecocokan, ia akan mengarahkan permintaan tersebut ke fungsi atau kelas yang spesifik di dalam berkas views.py.

    views.py: Ini adalah pusat logika bisnis dari aplikasi Django Anda. Setelah urls.py mengarahkan permintaan, fungsi atau kelas di views.py akan dieksekusi. Tugasnya adalah memproses permintaan, mengambil data yang diperlukan (jika ada) dari models.py, dan memutuskan template HTML mana yang akan ditampilkan. Fungsi inilah yang bertugas mengumpulkan semua komponen yang dibutuhkan untuk membuat tanggapan.

    models.py: Berkas ini mendefinisikan struktur data aplikasi Anda (seperti tabel di database). Django menggunakan ORM (Object-Relational Mapper) yang memungkinkan Anda berinteraksi dengan database menggunakan objek Python biasa, bukan perintah SQL. views.py akan memanggil objek dan fungsi dari models.py saat perlu mengambil, menyimpan, memperbarui, atau menghapus data di database.

    Berkas HTML (Templat): Ini adalah tampilan atau antarmuka yang akan dilihat oleh pengguna. Berkas ini berisi kode HTML statis, namun juga bisa menerima data dinamis yang dikirimkan oleh views.py. views.py akan "merender" berkas HTML ini dengan data yang relevan, mengubahnya menjadi tanggapan HTML yang lengkap dan siap dikirimkan kembali ke klien.

3. Jelaskan peran settings.py dalam proyek Django!
    - Peran settings.py dalam proyek Django adalah sebagai file konfigurasi utama yang mengatur semua aspek operasional aplikasi Django. Ibaratnya, settings.py adalah otak dari proyek Django, yang memberi tahu kerangka kerja bagaimana harus berperilaku, berinteraksi dengan basis data, mengelola file statis, dan banyak lagi.

4. Bagaimana cara kerja migrasi database di Django?
    - Migrasi database di Django adalah cara untuk mengubah skema database Anda tanpa perlu menghapus data yang ada. Ini memungkinkan Anda memodifikasi model Django (di models.py) dan secara otomatis menerjemahkan perubahan tersebut menjadi perintah SQL untuk database.

    Proses migrasi Django bekerja dalam dua langkah utama:

    1. Membuat Migrasi (makemigrations)
    Saat Anda membuat perubahan pada file models.py (misalnya, menambahkan model baru, mengubah nama field, atau menambahkan field), Anda harus menjalankan perintah ini di terminal:

    python manage.py makemigrations

    Perintah ini tidak benar-benar mengubah database Anda. Sebaliknya, ia menganalisis perbedaan antara model saat ini dan versi model terakhir yang ada di file migrasi. Django kemudian akan membuat file migrasi baru (di dalam folder migrations aplikasi Anda) yang berisi instruksi Python untuk melakukan perubahan tersebut. File migrasi ini berfungsi sebagai "cetak biru" yang mendeskripsikan perubahan yang diperlukan.

    2. Menerapkan Migrasi (migrate)
    Setelah file migrasi dibuat, Anda harus menerapkannya ke database dengan perintah berikut:

    python manage.py migrate

    Perintah ini akan mengeksekusi semua file migrasi yang belum diterapkan. Django akan membaca instruksi dari file migrasi yang telah dibuat sebelumnya dan menerjemahkannya menjadi perintah SQL yang sesuai dengan jenis database Anda (misalnya, SQLite, PostgreSQL). Perintah-perintah SQL ini kemudian dijalankan pada database, mengubah skema tabel sesuai dengan perubahan yang Anda buat pada model.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Berikut adalah beberapa alasan dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak menurut saya:
    1. Django adalah Full-Stack Framework
    Lengkap: Django menyediakan semua yang dibutuhkan dalam satu paket — routing, views, ORM (akses database), admin panel, template engine, dll. Tidak perlu install banyak library eksternal untuk mulai membangun aplikasi. Artinya: Mahasiswa bisa langsung belajar konsep "end-to-end" dari backend hingga frontend tanpa ribet setup awal.

    2. Berbasis Python
    Python dikenal sebagai bahasa yang mudah dibaca dan ditulis, cocok untuk pemula. Banyak mahasiswa sudah belajar Python di awal kuliah (misalnya dari DDP1/DDP2 di Fasilkom UI), jadi lebih mudah memahami alur logika Django.

    3. Konsep MVT yang Jelas
    Django mengajarkan arsitektur perangkat lunak yang baik:
    Model → struktur data (berbasis database)
    View → logika bisnis
    Template → tampilan antarmuka

    Hal ini mempersiapkan mahasiswa mengenal praktik terbaik dalam desain perangkat lunak dan melatih mindset pemisahan tanggung jawab (separation of concerns).

    4. Dokumentasi yang Sangat Baik
    Dokumentasi resmi Django sangat lengkap dan mudah dipahami, bahkan menyediakan tutorial langkah demi langkah bagi pemula. Banyak sumber belajar tersedia: buku, video, artikel, dan course online, sehingga mahasiswa dapat belajar mandiri dengan lebih mudah.

    5. Community Support Besar
    Karena Django populer, komunitasnya aktif. Mudah menemukan solusi kalau mengalami error, karena kemungkinan besar orang lain pernah mengalami hal serupa.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    - Mantap, asisten dosen tutorial 1 kemarin sangat membantu dan informatif terkait permasalahan yang saya hadapi selama tutorial kemarin dan membantu menyelesaikan permasalahan yang ada.