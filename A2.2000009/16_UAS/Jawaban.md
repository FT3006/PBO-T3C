Soal :

1. Apa itu class?
2. Apa itu instance?
3. Apa hubungan antara class dan instance?
4. Apa sintaks Python yang digunakan untuk menentukan class baru?
5. Apa konvensi ejaan untuk nama class?
6. Bagaimana Anda memberi instantiate, atau membuat instance dari, sebuah class?
7. Bagaimana Anda mengakses atribut dan perilaku instance class?
8. Apa itu metode?
9. Apa tujuannya self?
10. Apa tujuan dari _init_metode ini?
11. Jelaskan bagaimana pewarisan membantu mencegah duplikasi kode.
12. Dapatkah class child menimpa sifat parents?

Jawaban :

1. Class adalah mekanisme yang digunakan untuk membuat struktur data pengguna baru yang ditentukan. Ini berisi data serta metode yang digunakan untuk memproses data tersebut.

2. Instance adalah salinan class dengan nilai sebenarnya , secara harfiah merupakan objek class tertentu.

3. Sementara class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut.

4. Dengan menulis "class" diawal, kemudian diikuti dengan  nama kelasnya dan diakhiri dengan titik dua. 
   Contoh : class Hero:

5. Ditulis dengan notasi CamelCase, dimulai dengan huruf Kapital. 
   Contoh : HeroGenshinImpact()

6. Dengan menggunakan tanda kurung () setelah nama classnya. 
   Contoh : hero = Ayaka()

7. Dengan notasi titik — misalnya, instance_name.attribute_name

8. Sebuah fungsi yang didefinisikan di dalam class.

9. Argumen pertama dari setiap metode merujuk pada instance class saat ini, yang menurut konvensi, diberi nama self. Dalam _initmetode ini, selfmengacu pada objek yang baru dibuat; sementara dalam metode lain, selfmengacu pada contoh yang metode namanya disebut. Untuk lebih lanjut tentang __init_vs self, lihat artikel ini .

10. _init_Metode menginisialisasi sebuah instance dari class.

11. class child mewarisi semua atribut dan perilaku parents.

12. Iya betul.