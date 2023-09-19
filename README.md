# inventoryge

Link Adaptable: none (Error)

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

![XML](https://imgur.com/a/f6PRQWW)

### XML by ID

![XML by ID](https://imgur.com/a/rNtW4EB)

### JSON

![JSON](https://imgur.com/a/VZhetb7)

### JSON by ID

![JSON by ID](https://imgur.com/a/cswJkXI)

### HTML

![HTML](https://imgur.com/a/ifFnSRt)

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