1. Class merupakan cetak biru (blue print) dari objek atau dengan kata lain sebuah Class menggambarkan ciri-ciri objek secara umum. Class digunakan hanya untuk membuat kerangka dasar. 

2. Instance adalah istilah lain dari objek suatu kelas. Sebuah objek yang dibuat dari prototipe kelas Lingkaran misalnya disebut sebagai instance dari kelas tersebut.

3. Class dan objek memang memiliki hubungan yang erat. Class adalah spesifikasi/desain dari objek,    sedangkan objek sendiri adalah instance (perwujudan) dari class. Alasan ini juga yang menyebabkan kata instance sering digunakan sebagai ganti dari objek karena memiliki arti yang sama.

4. Dengan menulis "class" diawal, kemudian diikuti dengan nama kelasnya dan diakhiri dengan titik dua.
   Contoh penulisannya : 
   class Hero:


5. Ditulis dengan notasi CamelCase, dimulai dengan huruf Kapital.
   Contoh penulisannya :
   Hero()


6. Dengan menggunakan nama class, lalu diikuti tanda kurung.\
   Misal, nama classnya `Hero`, maka penulisannya : 
   my_hero = Hero()

7. Dengan menambahkan titik ( . )\
   Misal, `nama_instance.nama_atribut`

8. Metode adalah fungsi yang didefinisikan di dalam suatu kelas.

9. Self digunakan untuk menampung dirinya sendiri, maksudnya self ini adalah argumen pertama dari setiap metode merujuk pada instance class saat ini.

10.  `__init__` Metode menginisialisasi sebuah instance dari class.

11. Karena konsep Inheritance diturunkan, maka semua kode yang telah dibuat sebelumnya (didalam class) dapat dipakai kembali di class lain sebagai class turunannya. Dengan begitu code yang sama tidak perlu dibuat berulang kali, dan alhasil bisa mencegah duplikasi code.

12. Bisa