# inventory

Link Adaptable: none (Error)

## Cara implementasi poin-poin pada tugas

### Prosedur pembuatan Proyek Django

1. Membuat repositori lokal "inventory" dan menginisiasinya dengan command 'git init' pada cmd.
2. Mengatur username dan email yang digunakan untuk repositori ini ('git config user.name "____"' dan 'git config user.email "____"').
3. Membuat repositori GitHub dengan nama "inventory".
4. Membuat README.md file di direktori lokal.
5. Melakukan add dan commit pada direktori lokal ('git add .' dan 'git commit -m "____"')
6. Membuat branch utama baru dengan nama "main" ('git branch -M main')
7. Menghubukan repositori lokal dengan repositori GitHub ('git remote add origin https://github.com/WinotoHasyim/inventory.git')
8. Melakukan push pada direktori lokal ke branch "main"('git push -u origin main')
9. Membuat virtual environment pada direktori lokal guna mengisolasi package dan dependencies ('python -m venv env')
10. Mengaktifkan virtual environment. Akan muncul tanda (env) sebagai indikator aktifnya virtual environment ('env\Scripts\activate.bat')
11. Membuat file requirements.txt berisi beberapa dependencies
12. Memasang dependencies pada direktori lokal ('pip install -r requirements.txt')
13. Membuat proyek django "inventory" ('django-admin startproject inventory .')
14. Pada settings.py, menambahkan "*" pada ALLOWED_HOSTS (semua host bisa mengakses aplikasi)
15. Menambahkan file .gitignore berisi beberapa berkas konfigurasi. Berkas-berkas yang ada dalam file akan diabaikan oleh git

### Membuat aplikasi "main" pada proyek Django

1. Menjalankan command 'python manage.py startapp main'
2. Menambahkan 'main' pada INSTALLED_APPS di settings.py

### Melakukan routing pada proyek untuk aplikasi "main"

1. Di file urls.py direktori utama, import function 'include' dari django.urls 
2. Menambahkan path('main/', include('main.urls')) ke dalam list urlpatterns

### Membuat model pada aplikasi "main" dengan nama "Item"

1. Di file models.py aplikasi "main", menambahkan class Item(models.Model)
2. Menambahkan atribut name, amount, dan description pada class tersebut dengan tipe CharField, IntegerField, dan TextField masing-masing
3. Migrasi model ('python manage.py makemigrations' dan 'python manage.py migrate')

### Membuat function pada views.py agar bisa menampilkan html

1. Membuat folder "templates" pada aplikasi "main" dan kemudian membuat html file di dalam folder tersebut yang akan menampilkan nama aplikasi, nama pribadi, dan kelas PBP pribadi
2. Di views.py, import render dari django.shortcuts dan membuat sebuah function bernama show_main yang menerima request.
3. Membuat dictionary berisi nama aplikasi, nama pribadi, dan kelas PBP pribadi
4. Function tersebut akan mengembalikan response berdasarkan request, template, dan dictionarynya (return menggunakan function render)

### Membuat routing urls.py pada aplikasi "main"

1. Membuat file urls.py pada aplikasi "main"
2. Import path dari django.urls dan import function yang ada di views.py
3. Membuat string bernama app_name yang berisi nama aplikasinya untuk membuat pola URL unik
3. Membuat list bernama urlpatterns dan mengisinya dengan path dengan argumen function yang di import dari views.py

### Melakukan deployment ke Adaptable

1. Pergi ke link Adaptable.io
2. Click App Dashboard
3. Click new app untuk membuat aplikasi baru. Pilih 'connect an existing repository'
4. Pilih repository yang ingin kita pakai. Disini, saya memakai repository 'inventory'
5. Pilih branch untuk dipakai. Disini, saya memakai 'main'
6. Pilih Python App Template sebagai deploy template
7. Pilih PostgreSQL sebagai Database type
8. Pilih python version yang dipakai. Disini, sayamemakai python versi 3.10
9. Edit Start command menjadi 'python manage.py migrate && gunicorn inventory.wsgi'
10. Tentukan nama appnya
11. Centan HTTP Listenenr on PORT
12. Click Deploy App

## Request client ke web aplikasi berbasis Django beserta responnya

![Alt text](https://i.imgur.com/lwxXRhS.jpg)
Gambar Bagan: https://i.imgur.com/lwxXRhS.jpg
Kaitan urls.py, views.py, models.py, dan berkas html:
1. urls.py akan menyocokkan pola URL yang kemudian dari pola tersebut akan diketahui function yang mana yang akan diproses dari views.py
2. views.py dapat berinteraksi dengan model agar bisa menyimpan atau mengambil data untuk ditampilkan nanti
3. function yang diproses pada views.py akan menggunakan template (berkas html) yang sesuai. Nantinya template tersebut akan ditampilkan dalam browser

## Mengapa menggunakan virtual environment?

Virtual environment membantu kita untuk mengisolasi dependencies atau versi python (atau mungkin bahasa pemrograman yang lain) antara suatu proyek dengan proyek yang lain. Dengan ini, kita dapat menyertakan dependencies atau memakai versi python yang berbeda pada setiap proyek yang kita buat.

## Apakah tetap bisa membuat proyek Django tanpa virtual environment?

Bisa, tapi sangat tidak dianjurkan karena berpotensi menyebabkan konflik pada dependencies di setiap proyek

## Apa itu MVC, MVT, MVVM? Apa perbedaannya?

Ketiganya adalah konsep arsitektur dengan penjelasan sebagai berikut:
- MVC (Model-View-Controller) = Konsep arsitektur dengan model yang merupakan komponen untuk mengelola data, view untuk menampilkan tampilan kepada pengguna, dan controller sebagai penghubung antara model dan view (menerima input dari view, memprosesnya dengan model, dan menampilkan kembali hasilnya lewat view)
- MVT (Model-View-Template) = Konsep arsitekstur dengan model sebagai komponen yang bertanggung jawab mengelola data, view untuk mengatur tampilan pada template berdasarkan data pada model, dan template untuk menentukan tampilan antarmuka pengguna
- MVVM (Model-View-ViewModel) = Konsep arsitektur dengan model sebagai komponen untuk mengelola data, view untuk tampilan antarmuka pengguna, ViewModel sebagai perantara antara model dan view yang bertugas untuk meneruskan data yang diperoleh dari model ke view, atau menerima input dari view untuk diteruskan/diproses oleh model

Perbedaan dari ketiga konsep arsitektur ini adalah MVC dan MVVM menggunakan view sebagai komponen untuk menampilkan tampilan kepada pengguna, sementara MVT menggunakan template untuk menampilkan tampilannya. Selain itu, Controller dan ViewmModel pada MVC dan MVVM berperan sebagai perantara antara view dengan model, sedangkan MVT menggunakan view sebagai perantara antara template dan model.

## Implementasi test lain pada tests.py

Di dalam tests.py, ada tambahan test yang dilakukan. Test tersebut bernama test_name_is_exist_in_main_template. Test ini bertujuan untuk mengecek apakah string "Name:" Muncul pada konten yang sedang ditampilkan