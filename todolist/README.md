# Aplikasi
Aplikasi dari Katalog terdapat dalam link: [https://eda-pbp-tugas-2.herokuapp.com/todolist/]

# Tugas 5

### Apa perbedaan dari inline, internal, dan external CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

#### Inline: 
Pengaplikasian CSS ditulis di dalam inline tag suatu komponen HTML

Kelebihan:
- Request HTTP lebih kecil
- Mudah untuk bereksperimen dengan style
- Berguna untuk quick fix

Kekurangan:
- Harus diterapkan satu persatu pada setiap elemen.

#### Internal
Pengaplikasian CSS ditulis di file HTML, biasanya di bagian bawah dan di dalam tag <style> </style>

Kelebihan:
- Perubahan untuk 1 halaman saja
- Dapat menggunakan element, class, dan id selector
- HTML dan CSS berada di file yang sama

Kekurangan:
- Meningkatkan waktu akses website
- Tidak efisien jika terdapat banyak file HTML yang ingin diterapkan CSS.

#### External
Pengaplikasian CSS ditulis di file yang berbeda dengan file HTML dan biasanya diletakan setelah bagian <head> (reccomended)

Kelebihan:
- Kecepatan loading lebih cepat
- Dapat digunakan di halaman  yang banyak
- ukuran file HTML menjadi kecil dan strukturnya lebih rapih

Kekurangan:
- Halaman harus menunggu CSS terpanggil untuk tampil secara sempurna.


### Jelaskan tag HTML5 yang kamu ketahui.

* <header> : merepresentasikan header sebuah dokumen atau bagian
* <nav>	: mendefinisi sebuah bagian untuk navigation lins
* <picture> : mendefinisi seebuah container untuk sumber-sumber gambar 
* <section> : mendefinisi sebuah section sebuah dokument, seperti heade, footer, etc
* <source> : alternatif untuk medefinisikan sumber media seperti <audio> atau <video>
* <aside> :  mendefinisikan konten yang berhubungan dengan konten halaman
* <footer>: merepresentasikan sebuah footer dari dokumen
* <article>: mendefinisikan sebuah article

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Element Selector: Selector tanpa diawali dengan # atau .

	Selector yang berkorespondensi dengan tipe elemen HTML nya.

	Contoh : jika kita mengubah h1 menjadi warna hijau, maka semua h1 pada HTML akan berubah hijau.


2. Class Selector: Selector diawali dengan .

    Mirip dengan Id selector, perbedaannya adalah meskipun ID tertentu hanya boleh ditetapkan ke satu elemen, kita dapat menetapkan kelas yang sama ke elemen sebanyak yang kita inginkan.

    Contoh : dua elemen h1 memiliki class yang sama, maka hanya dua elemen h1 itu saja yang CSS targetkan, tidak semuanya.

3. ID Selector: Selector diawali dengan #

    Selector yang menargetkan elemen yang memiliki id yang unik.
    
    Contoh: jika kita memiliki elemen h1 dengan suatu id, maka CSS hanya menargetkan elemen h1 tersebut saja.


### Jelaskan bagaimana car akamu mengimplementasikan checklist di atas.

1. Menyantumkan bootstrap pada masing-masing file HTML
2. Brainstorming atas konsep web desain yang diinginakn
3. Mencari elemen-elemen yang tepat untuk dimasukkan
4. Mengaplikasikan elemen-elemen tersebut, terutama cards pada to do list




# Tugas 4

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




