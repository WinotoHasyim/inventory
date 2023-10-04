# inventoryge

Link Adaptable: none (Error)

<details>
<summary>Tugas 5 PBP</summary>
<br>

## Cara implementasi poin-poin pada tugas

1. Menambahkan 
```html
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
/>
```
pada `base.html` jika belum.

2. Untuk menggunakan bootstrap, tambahkan kode ini dibawah elemen `meta`:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
<style>
    main {
        max-width: 1200px;
        width: 100%;
        margin: 0 auto;
        padding: 4rem 4rem;
        flex: 1;

        display: flex;
        align-items: center;
        flex-direction:column; justify-content:center;
        min-height:100vh;
    }
</style>
```
style disini digunakan untuk menerapkan styling pada elemen `main` pada HTML. Styling digunakan hanya untuk meng-align webpage menjadi centered

3. Untuk setiap file HTML pada folder `main/templates`, tambakan elemen `<main>` pada awal-awal block content dan tutup elemen tersebut di akhir-akhir block content. 

4. Pada file `login.html`, gunakan login button berikut:
```html
<tr>
    <td></td>
    <td><input type="submit" class="btn btn-outline-success" value="login"></td>
</tr>
```

5. Pada file `register.html`, gunakan button berikut:
```html
<tr>  
    <td></td>
    <td><input class="btn btn-outline-primary" type="submit" name="submit" value="Daftar"/></td>  
</tr>  
```

6. Buka file `main.html`. Sebelum elemen `<main>`, tambahkan elemen `<header>` untuk menambahkan header yang akan dipakai sebagai navigation bar. Kode akan menjadi seperti berikut:
```html
<header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand">{{ app }}</a>
            </div>
            <button class="navbar-toggler order-first" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <ul class="navbar-nav ms-auto">
                    <div class="row">
                        <div class="col">
                            <a class="nav-link">Welcome, {{ name }} from {{ class }}</a>
                        </div>
                    </div>
                    <li class="nav-item">
                        <form class="d-flex" role="logout">
                            <a href="{% url 'main:logout' %}" class="btn btn-info btn-lg">
                                <span class="glyphicon glyphicon-log-out"></span> Log out
                            </a>
                        </form>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>
<main>
    ...
```
ada konten yang menggunakan class navbar collapse agar ketika size dari web tidak mencukupi, teks welcome user dan logout button ada di dalam collapse tersebut. Disini juga digunakan header yang menampilkan nama app

7. (Termasuk Penjelasan Bonus) Dalam elemen `<main>`, ubah kode sehingga menjadi seperti berikut:
```html
<main>
    <h3>Kamu menyimpan {{ total_item }} item pada aplikasi ini</h3>
    <div class="row">
        {% for item in items %}
        <div class="card {% if forloop.last %}bg-info{% endif %}" style="width: 20rem; margin: 1rem; background-color: rgb(171, 170, 172);">
            <div class="card-body">
                <h5 class="card-title">{{ item.name }}</h5>
                <p class="card-text">{{ item.description }}</p>
                <p class="card-text">Amount: {{ item.amount }}</p>
                <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
                    <div class="btn-group" role="group">
                        <form method="POST" action="{% url 'main:increase_amount' item.id %}">{% csrf_token %}<button type="submit" class="btn btn-success">+</button></form>
                        <form method="POST" action="{% url 'main:decrease_amount' item.id %}">{% csrf_token %}<button type="submit" class="btn btn-danger">-</button></form>
                    </div>
                    <form method="POST" action="{% url 'main:remove_item' item.id %}">{% csrf_token %}<button type="submit" class="btn btn-dark">Remove</button></form>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

    <h5>Sesi terakhir login: {{ last_login }}</h5>
</main>
```
Disini tabel tidak dipakai lagi untuk menampilkan daftar item, tetapi memakai card. Kode yang digunakan untuk membuat background color dari item terakhir berbeda dengan background color item yang lain adalah `{% if forloop.last %}bg-info{% endif %}` yang berada pada atribut class.

### add-commit-push

Jalankan command berikut:
```
git add .
```
```
git commit -m "<message>"
```
```
git push origin main
```

## Pertanyaan

### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

- Universal selector = Memilih semua elemen pada halaman web untuk diatur stylingnya. biasanya digunakan untuk sizing seperti `box-sizing: border-box;`, atau memberikan style yang bersifat umum pada semua elemen.

- Type Selector = Memilih semua elemen dengan jenis tertentu (`h1`, `p`, dll.) untuk diatur stylingnya. Dipakai ketika mau menerapkan style pada jenis elemen yang sama pada suatu file html

- Class Selector = Memilih elemen yang mempunyai atribut class tertentu. Dipakai ketika kita mau menerapkan styling pada elemen dengan class yang sama, tanpa melihat jenis elemen apa yang memakai class tersebut

- ID Selector = Memilih elemen yang mempunyai ID tertentu. Biasanya setiap id itu unik, jadi ID selector dipakai untuk menerapkan styling pada elemen yang unik.

### Jelaskan HTML5 Tag yang kamu ketahui.

- `<header>`: Digunakan untuk mengelompokkan elemen-elemen yang berada di dalam bagian atas halaman atau elemen tertentu yang merupakan bagian judul atau kepala dokumen

- `<nav>`: Mendefinisikan bagian navigasi dalam dokumen. Ini sering digunakan untuk membuat menu navigasi

- `<main>`: Menunjukkan konten utama dokumen. Hanya ada satu elemen `<main>` dalam satu halaman

- `<footer>`: Digunakan untuk mengelompokkan elemen-elemen yang berada di bagian bawah halaman atau elemen tertentu yang merupakan bagian penutup atau kaki dokumen

- `<p>`: Merupakan teks paragraf

- `<a>`: Digunakan untuk menghubungkan suatu page dengan yang lain

- `<h1>`: Merupakan judul. Terdapat tag `<h1>` sampai `<h6>`, semakin kecil angkanya, semakin kecil ukuran judulnya

- `<body>`: Isi utama dari HTML-nya

- `<ul>`: Unordered list (Menggunakan dot)

- `<ol>`: Ordered list (Menggunakan nomor atau alfabet)

- `<li>`: list dalam `<ul>` ataupun `<ol>`

- `div`: Mengelompokkan konten

- `<form>`: Formulir untuk mengumpulkan data dari user

### Jelaskan perbedaan antara margin dan padding.

Margin merupakan area yang dikosongkan di luar border dan bersifat transparan, sedangkan padding merupakan area yang dikosongkan dari luar content sampai border dan juga bersifat transparan. Padding mengatur jarak content dengan bordernya sedangkan margin mengatur jarak antar-elemen

### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

- Tailwind:
    - Membangun tampilan dengan menggunakan kelas-kelas utilitas yang sudah didefinisikan
    - Ukuran berkas nya lebih ringan karena hanya memuat kelas-kelas utilitas yang ada
    - Fleksibilitasnya tinggi, yang artinya kita bisa mendesain web dengan gaya kita sendiri
    - Memakan waktu yang lama untuk dipelajari karena memerlukan pemahaman terhadap kelas-kelas utilitas yang ada

- Bootstrap:
    - Memiliki komponen siap pakai yang desainnya sudah ditentukan
    - Ukuran berkasnya lebih besar karena memiliki banyak komponen dan gaya bawaan
    - Biasanya menghasilkan tampilan yang konsisten tetapi cenderung sulit untuk disesuaikan dengan gaya yang diinginkan
    - Memakan waktu yang cepat untuk dipelajari karena kita hanya memakai komponen yang sudah ada

Bootstraps sebaiknya digunakan jika kita mau mengembangkan suatu web dengan waktu yang relatif cepat. Ini cocok untuk proyek-proyek yang memerlukan konsistensi desain dengan menggunakan komponen bawaan

Tailwind CSS sebaiknya digunakan jika ingin fleksibilitas dalam desain dan bersedia menghabiskan waktu lebih banyak untuk menyesuaikan tampilan sesuai gaya sendiri. Ini cocok untuk proyek-proyek yang ingin tampilan yang unik atau jika pengembang ingin mengutamakan ukuran berkas yang lebih kecil

</details>

<details>
<summary>Tugas 4 PBP</summary>
<br>

## Cara implementasi poin-poin pada tugas

Pertama-tama, nyalakan virtual environment di `cmd` pada local repo dengan perintah berikut.
```
env\Scripts\activate.bat
```

### Implementasi fungsi registrasi, login, dan logout

1. Buka file `views.py` pada direktori `main` dan tambahkan import-import berikut:
```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
UserCreationForm dapat membantu membuat formulir pendaftaran user pada aplikasi sehingga kita tidak perlu menulis kode dari awal lagi.

2. Tambahkan function:
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Function tersebut berfungsi untuk menerima request dan membuat form dari request tersebut menggunakan UserCreationForm. Jika berhasil, kita akan diarahkan ke page login.

3. Buat file `register.html` pada folder `main/templates` dan isi file tersebut dengan kode:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

4. Buka `urls.py` pada subdirektori `main` dan tambahkan import register dari main.views:
```python
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register
```
Setelah itu, buka urls.py pada subdirektori yang sama dan tambahkan path url dari function yang diimpor tadi ke dalam list `urlpatterns`:
```python
...
path('register/', register, name='register'),
...
```

5. Buka `views.py` lagi dan import:
```python
from django.contrib.auth import authenticate, login
```
Kedua function di atas berfungsi untuk proses autentikasi dan login user.

6. Tambahkan fungsi seperti berikut pada `views.py`:
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

7. Buat file `login.html` pada folder `main/templates` dan isi file tersebut dengan kode:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

8. Buka `urls.py` pada subdirektori `main` dan import fungsi `login_user`:
```python
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user
```
Setelah itu, buka urls.py pada subdirektori yang sama dan tambahkan path url dari function yang diimpor tadi ke dalam list `urlpatterns`:
```python
...
path('login/', login_user, name='login'),
...
```

9. Buka `views.py` pada subdirektori `main` dan tambahkan import logout seperti berikut:
```python
from django.contrib.auth import authenticate, login, logout
```

10. Buat function di dalam `views.py`:
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Function `logout` yang diimpor tadi digunakan untuk menghapus session user yang sedang login. Setelah itu, web akan menampilkan halaman login.

11. Tambahkan isi file `main.html` yang ada pada folder `main/templates` dengan kode berikut di bagian bawah Add New Item:
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

12. Buka `urls.py` pada subdirektori `main` dan kemudian tambahkan import function `logout_user` dari `main.views`:
```python
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user
```
Setelah itu, buka `urls.py` pada subdirektori `main` dan tambahkan path url untuk mengakses fungsi yang diimpor tadi:
```python
...
path('logout/', logout_user, name='logout'),
...
```

13. Buka kembali `views.py` dan tambahkan import berikut:
```python
from django.contrib.auth.decorators import login_required
```
Decorator tersebut berfungsi untuk merestriksi akses suatu halaman web jika pengguna belum login.

14. Tambahkan kode seperti berikut di atas function `show_main`:
```python
...
@login_required(login_url='/login')
def show_main(request):
...
```
Hal ini dilakukan guna merestriksi halaman main jika pengguna belum melakukan login

### Menampilkan detail informasi pengguna, menerapkan cookies, dan menghubungkan model Item dengan User

1. Buka `views.py` yang ada pada subdirektori `main` dan import beberapa function berikut:
```python
import datetime
from django.http import HttpResponseRedirect # Import kalau belum
from django.urls import reverse
```

2. Di function `login_user`, ubahlah sebagian kode menjadi seperti berikut:
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
Perbedaannya dari kode sebelumnya ialah response yang dihasilkan akan di-set cookienya menjadi last_login

3. Pada function `show_main`, tambahkan key `last_login` pada dictionary `context`. Contohnya:
```python
context = {
        'app': 'Inventoryge',
        'name': 'Winoto Hasyim',
        'class': 'PBP C',
        'items': items,
        'last_login': request.COOKIES['last_login'],
        'total_item': total_item,
    }
```
Value dari `last_login` ini berfungsi untuk menambahkan cookie last_login pada response.

4. Ubah function `logout_user` sehingga menjadi:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Perbedaannya dari kode sebelumnya yaitu response yang nanti dihasilkan akan di-delete cookie last_login-nya terlebih dahulu.

5. Buka file `main.html` pada folder `main/templates` dan tambahkan kode berikut sebelum endblock content:
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

6. Bukalah `models.py` pada subdirektori `main` dan lakukan import:
```python
...
from django.contrib.auth.models import User
...
```
Kemudian, pada model `Item` yang sudah didefinisikan, tambahkan kode berikut:
```python
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Potongan kode yang ditambahkan pada model berfungsi untuk menghubungkan Item dengan User-nya sehingga setiap User yang terdaftar dapat memiliki Item yang berbeda.

7. Buka `views.py` pada subdirektori `main` dan ubahlah sebagian kode dari function `create_item` menjadi seperti berikut:
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
```
Disini, `commit=False` bertujuan agar form tidak di-save langsung ke database sehingga kita bisa mengedit formnya terlebih dahulu. Kemudian kita akan meng-edit field `user` dari variabel `item` menjadi `request.user` untuk menunjukkan bahwa item yang dibuat itu dimiliki oleh user yang sedang login

8. Ubah sebagian kode pada function `show_main` menjadi seperti berikut:
```python
def show_main(request):
    items = Item.objects.filter(user=request.user)
    total_item = len(items)

    context = {
        'app': 'Inventoryge',
        'name': request.user.username,
    ...
...
```
Function `show_main` akan memperoleh objek `Item` yang dimiliki oleh user yang sedang login (`request.user`). Function tersebut juga akan mengubah value dari key `name` pada dictionary `context` menjadi `request.user.username`. Hal ini bertujuan untuk menampilkan nama user yang sedang login.

9. Laukan migrasi model dengan command berikut:
```
python manage.py makemigrations
```
Nantinya, akan muncul error saat melakukan migrasi. Pilih `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data
![Error](https://cdn.discordapp.com/attachments/923523971226435584/1152471335080046712/image.png)

Ketik angka `1` lagi untuk menetapkan user dengan ID 1 pada model yang sudah ada
![Default value](https://cdn.discordapp.com/attachments/923523971226435584/1152471372988170310/image.png)

Jika sudah, jalankan command berikut untuk mengaplikasikan migrasi:
```
python manage.py migrate
```

### Membuat dua akun pengguna dengan masing-masing tiga dummy data

1. Jalankan command `python manage.py runserver` dan bukalah http://localhost:8000/ di browser. 

2. Klik Register Now
![](https://cdn.discordapp.com/attachments/872295244811620402/1156331836688060426/image.png?ex=65149571&is=651343f1&hm=82a70e542336faa466b401b21b81d3bbf0cf84c088636ca3ae5093b07c53edc6&)

3. Isi field-fieldnya dan klik tombol Daftar
![](https://cdn.discordapp.com/attachments/872295244811620402/1156332413694267493/image.png?ex=651495fb&is=6513447b&hm=214c38e3534e65a5dc5c532beee14e587f11b2d515eaf2e4111abb3cfccab514&)

4. Login dengan username dan password yang sudah dicantumkan pada form registrasi tadi. Kemudian, klik Login
![](https://cdn.discordapp.com/attachments/872295244811620402/1156333059621269504/image.png?ex=65149695&is=65134515&hm=a0d738738cde8ba6fb41dc697d38a2cedfe34d6bd98b828a5c162ecce0e0f3db&)

5. Klik tombol Add New Item, dan isi field-fieldnya dengan informasi item yang ingin ditambahkan ke inventory
![](https://cdn.discordapp.com/attachments/872295244811620402/1156333540473045002/image.png?ex=65149707&is=65134587&hm=01d4de7e2ef96ec79a397b7009a6b1c4110aac61aeca3504e64655b518127054&)

6. Ulangi step ke-5 sebanyak 2 kali lagi.

7. Jika sudah mempunyai 3 Item, klik tombol Logout (Gambar hanya contoh user yang memiliki 6 jenis Item)
![](https://cdn.discordapp.com/attachments/872295244811620402/1156334192456638494/image.png?ex=651497a3&is=65134623&hm=9dce6d436752e383beec04001492a4c65f9f9408eec9fa7d04a4430b73a808e3&)

8. Ulangi step ke-2 sampai ke-7.

### add-commit-push

Jalankan command berikut:
```
git add .
```
```
git commit -m "<message>"
```
```
git push origin main
```

## Pertanyaan

### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah suatu form bawaan yang disediakan oleh Django. Form ini digunakan untuk memudahkan developer dalam pembuatan user baru sehingga developer tidak perlu membuat kode dari awal lagi.

Kelebihan UserCreationForm:
- Ready-to-use form untuk diimplementasikan, sehingga Proses pengembangan proyek Django menjadi lebih sederhana dan cepat
- Dapat mengecek apakah password yang ditentukan untuk suatu user sudah sesuai dengan kebijakan keamanan yang ditetapkan atau belum
- Bekerja dengan baik dengan `User` model-nya Django
- Bisa di kustomisasi sesuai keinginan (cth. menambah field)

Kekurangan UserCreationForms:
- Bentuk default nya sangat minimalis. Jika ada banyak informasi yang harus diinput untuk suatu user, maka fieldnya juga harus ditambah
- Tampilannya yang default tidak memakai styling apa pun
- Untuk field selain password (atau password itu sendiri) mungkin harus ditambahi validasi custom jika diinginkan sehingga dapat merepotkan

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses untuk memverifikasi identitas seseorang, sedangkan Otorisasi adalah proses untuk memverifikasi apakah seseorang yang telah diautentikasi memiliki akses ke suatu hal atau tidak (hak akses pengguna ke berbagai bagian aplikasi). Otorisasi biasanya dilakukan setelah autentikasi. Keduanya penting untuk memastikan keamanan dan privasi dari user. Contohnya, Autentikasi membantu melindungi user dari pengaksesan yang tidak sah, sedangkan otorisasi mengelola apa saja yang dapat dilakukan oleh user sehingga user hanya dapat melakukan tindakan tertentu saja dan bukan tindakan lain yang dapat merugikan user. 

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah sebuah teks file berukuran kecil yang ditransfer dari website yang dikunjungi ke browser kita. Cookies digunakan untuk menyimpan informasi user seperti preferensi user, search history, dan lain-lain. Cookies juga digunakan dalam proses autentikasi user. 

Django mengunakan cookie bernama session id untuk menyimpan session key yang nantinya akan dipakai untuk mengakses session data user pada database. Nantinya, setiap kali user membuat request ke server, cookienya akan dikirim kembali ke server. Django menggunakan cookie yang berisi session id ini untuk mengidentifikasi pengguna dan mengaitkannya dengan session data yang sesuai di server

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Terdapat risiko potensial yang harus diwaspadai dalam penggunaan cookies, contohnya:
- Informasi pribadi user seperti informasi login atau detail kartu kredit yang disimpan dalam cookie mempunyai risiko merugikan privasi pengguna dan dapat disalahgunakan orang lain
- Penggunaan cookie yang lemah seperti cookie yang tidak memiliki atribut HttpOnly dapat dieksploitasi oleh serangan XSS
- Cookies dapat digunakan untuk melacak perilaku user

## Implementasi fitur bonus

1. Pada file `main.html` di folder main/templates, buatlah table data seperti berikut pada table item:
```python
...
<td><form method="POST" action="{% url 'main:increase_amount' item.id %}">{% csrf_token %}<button type="submit">+</button></form></td>
<td><form method="POST" action="{% url 'main:decrease_amount' item.id %}">{% csrf_token %}<button type="submit">-</button></form></td>
<td><form method="POST" action="{% url 'main:remove_item' item.id %}">{% csrf_token %}<button type="submit">Remove</button></form></td>
...
```
Menggunakan method POST untuk mentransfer data. Form akan meneruskan argumen item.id

2. Buka file `views.py` dan lakukan import:
```python
from django.shortcuts import get_object_or_404, render, redirect # Import get_object_or_404
```
`get_object_or_404` digunakan untuk mendapatkan objek `Item` dan kalau objeknya itu tidak ada maka akan mereturn 404 response

3. Buatlah function-function dalam `views.py`:
```python
def increase_amount(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_amount(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        if item.amount > 1:
            item.amount -= 1
            item.save()
        else:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_item(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

4. Buka file `urls.py` pada subdirektori `main` dan tambahkan routing berikut pada list `urlpatterns`:
```python
...
path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
path('decrease_amount/<int:id>/', decrease_amount, name='decrease_amount'),
path('remove_item/<int:id>/', remove_item, name='remove_item'),
...
```

</details>

<details>
<summary>Tugas 3 PBP</summary>
<br>

## Cara implementasi poin-poin pada tugas

Pertama-tama, nyalakan virtual environment di `cmd` pada local repo dengan perintah berikut.
```
env\Scripts\activate.bat
```

1. Buat file `forms.py` pada direktori `main`. Isi file tersebut dengan kode:
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
Ini akan membuat form untuk objek `Item` dengan `fields` seperti yang dispesifikasikan di kode tersebut

2. Buka `views.py` pada direktori `main` dan tambahkan kode ini untuk menambahkan beberapa import:
```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```

3. Buat function baru bernama `create_item` yang menerima parameter `request` seperti kode berikut:
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)
```
Function ini akan digunakan untuk membuat variable `form` dan kemudian jika `form` tersebut valid dan mendapatkan input dari user melalui metode `POST`, maka dia akan kembali ke halaman utama. Jika tidak, dia akan ke halaman lain untuk mengisi informasi tentang item yang ingin ditambahkan.

4. Ubah function `show_main` pada `views.py` sehingga menjadi seperti berikut:
```python
def show_main(request):
    items = Item.objects.all()
    total_item = len(items) # Ini untuk BONUS

    context = {
        'app': 'Inventoryge',
        'name': 'Winoto Hasyim',
        'class': 'PBP C',
        'items': items,
        'total_item': total_item, # Ini untuk BONUS
    }

    return render(request, "main.html", context)
```
Kita tambahkan variable `items` untuk mendapatkan informasi dari semua objek `Item` pada database.
(Untuk BONUS, itu hanya untuk mengitung berapa jenis item yang didaftarkan)

5. Buka `urls.py` pada folder `main` dan import function `create_item`:
```python
from main.views import show_main, create_item
```
Tambahkan juga path url ke dalam list `urlpatterns`-nya:
```python
path('create-item', create_item, name='create_item'),
```

6. Buat folder baru bernama `templates` pada root folder dan buatlah file bernama `base.html` di dalam folder baru tersebut. Isi filenya dengan kode seperti berikut:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
Ini dilakukan untuk membuat kerangka dari file-file html yang akan kita buat nantinya.
Kemudian, buka `settings.py` pada subdirektori `inventory` dan cari list `TEMPLATES`. Isi key `'DIRS'` dengan value berikut:
```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    }
]
...
```

7. Buatlah file `create_item.html` pada direktori `main/templates` dan tambahkan kode berikut:
```html

{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
File html ini akan mengextend kerangka file html tadi yaitu `base.html` dan mengisi bagian kontennya. File ini juga berisi form dengan metode `POST` yang di dalam block tersebut akan dibuat tombol submit untuk mengirim request ke `create_item(request)`

8. Ubah isi file `main.html` pada direktori `main/templates`:
```html
{% extends 'base.html' %}

{% block content %}

    <h1>{{ app }}</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>

    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
        </tr>
        
        <h3>Kamu menyimpan {{ total_item }} item pada aplikasi ini</h3>
        {% for item in items %}
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.amount }}</td>
                <td>{{ item.description }}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Product
        </button>
    </a>

{% endblock content %}
```

9. Buka `views.py` yang ada di folder `main` dan lakukan import sehingga kode akan menjadi seperti berikut:
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.core import serializers
```

10. Buatlah function-function yang berfungsi untuk mengembalikan data dalam bentuk XML dan JSON, dan juga function untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON:
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
`serializers` ini digunakan untuk men-translate objek model menjadi format lain seperti XML atau JSON.

11. Buka `urls.py` pada folder `main`. Lakukan import seperti berikut:
```python
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id
```
Kemudian, isi list `urlpatterns` sehingga keseluruhan isi list tersebut adalah:
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

12. Lakukan `add`, `commit`, dan `push`:
```
git add .
```
```
git commit -m "<message>"
```
```
git push origin main
```

## Pertanyaan

1. Apa perbedaan antara form POST dan form GET dalam Django?
    GET biasanya digunakan untuk request yang tidak memengaruhi sistem, sedangkan POST biasanya digunakan untuk request yang melakukan perubahan pada sistem. Selain itu, GET tidak terlalu cocok untuk dipakai sebagai password form karena password tersebut akan tampil pada URL. Oleh karena itu, POST lebih cocok untuk password form karena passwordnya tidak ditampilkan pada URL. GET biasanya dipakai agar URL bisa dibookmark karena data ditampilkan pada URL. Terakhir, GET request mengembalikan HTTP status code 200 jika data berhasil diperoleh/dikirim dari/ke server, sedangkan POST request mengembalikan HTTP status code 201.
2.  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    XML digunakan jika melibatkan data yang sangat terstruktur. JSON biasanya dipakai untuk web development dan juga JSON lebih ringan dan mudah untuk dilihat strukturnya. HTML digunakan untuk membuat tampilan halaman web.
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    Karena ringan, mudah dibaca oleh manusia, data struktur yang fleksibel, disupport oleh banyak bahasa pemrograman, dan juga memiliki kemampuan untuk mem-parsing data yang dibutuhkan saja tanpa harus mem-parsing seluruh dokumen JSON

## Foto Postman

### XML

![XML](https://i.imgur.com/2EjJ0U5.png)

### XML by ID

![XML by ID](https://i.imgur.com/w5FFzzN.png)

### JSON

![JSON](https://i.imgur.com/yw2WQAj.png)

### JSON by ID

![JSON by ID](https://i.imgur.com/Ehr0I4n.png)

### HTML

![HTML](https://i.imgur.com/xXHXHhj.png)

</details>

<details>
<summary>Tugas 2 PBP</summary>
<br>

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

Gambar Bagan:
![Bagan](https://i.imgur.com/lwxXRhS.jpg)
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
</details>
