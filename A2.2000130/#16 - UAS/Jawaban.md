1. Apa itu class?
class adalah cetak biru atau prototipe dari objek dimana kita mendefinisikan atribut dari suatu objek. Atribut ini terdiri dari data member (variabel) dan fungsi (metode).
2. Apa itu intance?
Objek individu dari kelas tertentu. Obyek obj yang termasuk dalam Lingkaran kelas, misalnya, adalah turunan dari Lingkaran kelas.
3. Apa hubungan antara class dan instance?
Class adalah rancangan atau blue print dari sebuah objek. Sedangkan objek adalah sebuah variabel yang merupakan instance atau perwujudan dari Class. Instance bisa diartikan sebagai wujud dari class. Class berisi definisi variabel dan fungsi yang menggambarkan sebuah objek.
4. Apa sintaks python yang digunakan untuk menentukan class baru?
class PythonclassName:
5. Apa konvensi ejaan untuk nama class?
CamelCase notasi, dimulai dengan huruf kapital -> PythonclassName()
6. Bagaimana Anda mengakses atribut dan perilaku instance class?
Menggunakan nama class, diikuti dengan tanda kurung. Jadi jika nama classnya Dog(), contoh Dognya adalah - my_class = Dog().
7. Bagaimana Anda mengakses atribut dan perilaku instance class?
Dengan notasi titik contohnya, instance_name.attribute_name
8. Apa itu metode?
Metode adalah fungsi yang didefinisikan di dalam suatu kelas
9. Apa tujuan self?
Keyword self digunakan untuk merepresentasikan setiap objek yang dibuat.
10. Apa tujuan dari __init__ metode ini?
Metode __init__() adalah metode konstruktor, yaitu metode khusus yang digunakan Python untuk menginisialisasi pembuatan objek dari kelas tersebut.
11. Jelaskan bagaimana pewarisan membantu mencegah duplikasi kode!
Kita bisa menurunkan karakteristik sebuah kelas ke kelas baru, dibandingkan dengan membuat kelas baru dari awal. Turunannya disebut kelas anak (child class) dan yang mewariskannya disebut kelas induk (parent class).

Kelas anak mewarisi atribut dari kelas induk, dan kita bisa menggunakan atribut tersebut seolah atribut itu didefinisikan juga di dalam kelas anak. Kelas anak juga bisa menimpa (override) data dan metode dari induknya dengan data dan metodenya sendiri.

Satu kelas anak bisa mewarisi karakteristik dari satu atau beberapa kelas induk.
12. Dapatkah class child menimpa sifat parents?
Kelas anak juga bisa menimpa (override) data dan metode dari induknya dengan data dan metodenya sendiri.