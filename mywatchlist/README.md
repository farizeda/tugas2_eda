# Aplikasi
Aplikasi dari Katalog terdapat dalam link: [https://eda-pbp-tugas-2.herokuapp.com/mywatchlist/]

# Jawaban

### 1.Jelaskan perbedaan antara JSON, XML, dan HTML! 

XML
* Merupakan eXtensible Markup Language
* Memiliki ekstensi file .xml
* Mempunyai start & end tags yang case sensitive
* Tidak mendukung array
* Mendukung namespace
* Lebih aman dibanding JSON
* Mendukung berbagai macam encoding

JSON
* Merupakan JavaScript Object Notation
* Memiliki ekstensi file .json
* Tidak memiliki end tags
* Mendukung array
* Tidak mendukung namespace
* Kurang aman
* Hanya mendukung encoding UTF-8

HTML
* Singkatan dari Hypertext Markup Language
* Merupakan bahasa standar programming dalam pembuatan website


### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery merupakan suatu aspek yang krusial dalam implementasi sebuah plarform. Seorang user yang mengakses suatu website dan merequest informasi tentu butuh suatu “jawaban” atau respons dari website tersebut. Untuk tugas ini, website dapat memberikan respons dalam bentuk halaman HTML, JSON, atau XML yang berisi informasi-informasi yang dibutuhkan oleh user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

1. Menjalankan command startapp aplikasi baru bernama mywatchlist
2. Menyambungkan urls aplikasi mywatchlist di urls project_django
3. Menambahkan nama aplikasi mywatchlist di INSTALLED_APPS di settings.py
4. Membuat path yang tepat di urlpatterns pada file urls.py di folder mywatchlist
5. Menciptakan class MyWatchList di models.py yang berisi atribut-atribut yang diminta
6. Mengimplementasi logic di views.py dengan menambahkan function-function yang diperlukan dengan soal (render HTML  & HttpResponse JSON & XML)
7. Menyambungkan antara views, models, dan urls
8. Mengisi data-data film pada file initial_watchlist_data.json sesuai dengan atribut-atribut di model
9. Membuat file mywatchlist.html untuk tampilan dalam website
10. Melakukan loaddata atas file initial_watchlist_data.json
11. Melakukan git add, commit, dan push ke github yang nantinya akan auto-deploy di heroku
