# Aplikasi
Aplikasi dari Katalog terdapat dalam link: [https://eda-pbp-tugas-2.herokuapp.com/todolist/]

# Tugas 6

### Perbedaan Asynchronus Programmming dengan Synchronus Programming
Perbedaan antara keduanya yaitu pada responses. Jika terdapat suatu event, Synchronus programming mengharuskan user untuk menunggu response yang diberikan browser, sementara asynchronus programming tidak harus menunggu dan user dapat melakukan hal-hal yang lain.

#### Event Driven Programming
Yaitu sebuah paradigma dimana jalannya sebuah program ditentukan oleh 'event' bukan secara sequential. Contoh penerapan Event Driven Programming adalah adanya method click untuk mengsubmit form yang ada. Dengan kata lain, jika event click tersebut ditrigger, maka akan ada perintah-perntah yang akan dijalankan.

#### Penerapan Asynchronus Programming pada AJAX
Penerapan AJAX memungkinkan user untuk dapat melakukan aktivitas-aktivitas lain pada website tanpa diharuskan untuk mereload website.

#### Implementasi
1. Menambahkankan path baru pada urls.py
2. Membuat dua fungsi baru pada views.py
3. Membuat file html baru
4. Menerapkan boostrap pada file html tersebut
5. Membuat fungsi AJAX get untuk mendapatkan data dari server
6. Membuat modal
7. Membuat fungsi AJAX post untuk mensubmit form secara asynchronus dan diimplementasikan pada modal
8. Menyambungkan fungsi pada views.py dan todolist