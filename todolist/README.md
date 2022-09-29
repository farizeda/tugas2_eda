# Aplikasi
Aplikasi dari Katalog terdapat dalam link: [https://eda-pbp-tugas-2.herokuapp.com/todolist/]

# Jawaban

### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

csrf_token adalah potongan kode rahasia yang digenerate server dalam permintaan HTTP yang dibuat oleh user. Token ini disediakan oleh Django untuk melindungi resources CSRF dari serangan-serangan jahat. Jika token ini ditiadakan, maka resources yang menggunakan token ini akan error di project kita.


### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.


Bisa, form-form seprti form-form dapat dibuat manual dengan memasukkan isi dari tag-tag secara manual sebagai input.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


1. User membuat sebuah request (POST)  yang nantinya akan diterima
2. Data-data pada request akan di check validitasnya dan dihandle oleh functions yand terdapat pada views.py
3. ika valid, data akan disimpan pada database
4. Data akan dipass ke HTML yang sesuai melewati functions
5. Data muncul dalam HTML



### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. UMembuat aplikasi todolist dengan menjalankan python manage.py startapp todolist
2. Menambahkan todolist pada settings.py dan menghubungkan url todolist pada folder django_app
3. Membuat data types & variables sesuai dengan atribut-atribute sebuah list dalam models.py
4. Mengimplementasikan business logic di function-function pada views.py (login, logout, register, dll) 
5. Menambahkan layer security dngan @login_required dan penggunaan cookies
6. Membuat path-path yang dibutuhkan pada urls.py
7.  Membuat file-file HTML  yang berisi informasi yang dibutuhkan serta implementasi komponen-komponennya.
8. Melakukan git add, commit, push dan deployment pada heroku



