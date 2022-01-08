1. Apa itu class?
   Class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan.
   Ini berisi data serta metode yang digunakan untuk memproses data tersebut.

2. Apa itu instance?
   Instance adalah salinan class dengan nilai sebenarnya , secara harfiah merupakan objek class tertentu.

3. Apa hubungan antara class dan instance?
   Class dan objek memang memiliki hubungan yang erat. Class adalah spesifikasi/desain dari objek, sedangkan 
   objek sendiri adalah instance (perwujudan) dari class. Alasan ini juga yang menyebabkan kata instance 
   sering digunakan sebagai ganti dari objek karena memiliki arti yang sama

4. Apa sintaks Python yang digunakan untuk menentukan class baru?
   Menulis "class" diawal, kemudian diikuti dengan  nama kelasnya dan diakhiri dengan titik dua. 
   Contoh : class Angka:

5. Apa konvensi ejaan untuk nama class?
   Ditulis dengan notasi CamelCase, dimulai dengan huruf Kapital. 
   Contoh : NilaiAkhir()

6. Bagaimana Anda memberi instantiate, atau membuat instance dari, sebuah class?
   Dengan menggunakan tanda kurung () setelah nama classnya. 
   Contoh : nama = Udin()

7. Bagaimana Anda mengakses atribut dan perilaku instance class?
   Dengan menggunakan notasi titik. 
   Contoh : instance_name.atribut_name

8. Apa itu metode?
   Sebuah fungsi yang didefinisikan di dalam class.

9. Apa tujuannya self?
   Fungsi Self adalah sebagai sebuah variabel yang menyatakan kelas itu sendiri. Jika kita ingin memanggil
   sebuah variabel atau metode di dalam sebuah class, dan metode yang akan kita panggil ada di class itu 
   juga, maka kita memakai kata “self” di depan nama variabel atau metodenya.

10. Apa tujuan dari _init_metode ini?
    _init_Metode menginisialisasi sebuah instance dari class.

11. Jelaskan bagaimana pewarisan membantu mencegah duplikasi kode!
    Karena konsep Inheritance diturunkan, maka semua kode yang telah dibuat sebelumnya (didalam class) 
    dapat dipakai kembali di class lain sebagai class turunannya. Dengan begitu code yang sama tidak
    perlu dibuat berulang kali, dan alhasil bisa mencegah duplikasi code.

12. Dapatkah class child menimpa sifat parents?
    Bisa.