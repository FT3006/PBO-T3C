Apa itu clas ? class pada python bisa dikatakan sebabagai sebua buleprint (cetakan) dari objek yang ingin kita buat. Class juga bisa di sebut sebuah mekanisme yang digunakan unyuk membuat struktur data pengguna baru yang ditentukan. Ini oberisi data serta metode yang digunakan untuk memproses data tersebut.

Apa itu instance? Instance adalah istilah lain dari objek suatu kelas. Sebuah objek yang dibuat dari prototipe kelas Lingkaran misalnya disebut sebagai instance dari kelas tersebut. Atau bisa juga disebut instance adalah salinan class dengan nilai sebenarnya, secara harfiah merupakan objek class tertentu.

Apa hubungan antara class dan instance? sementara class adalah cetak biru yang digunkan menggambarkan bagaimana membuat sesuatu, sedangkan instance adalah obejk yang dibuat dari cetak biru tersebut. jadi secara singkat class bisa disebut sebagai cetakannya atau definisinya sedangkan objek (atau instance) adalah ibjek nyatanya.

Apa sintaks Python yang digunakan untuk menentukan class baru? class pythonclassName:

Apa konvensi ejaan untuk nama class? konvensi penmaan untuk variabel dan nama metode biasanya camelCase notasi,atau pascalCase dimulai dengan huruf kapital -yaitu, PythonclassName()

Bagaimana Anda memberi instantiate, atau membuat instance dari, sebuah class? Jika menggunakan nama class, diikitu dengan tanda kurung.Jadi jika nama classnya Dog(), contoh Dognya adalah - my_class = Dog ()

Bagaimana Anda mengakses atribut dan perilaku instance class? Denagn notasi titik-misalnya, instance_name.attribute_name

Apa itu metode? Metode atau fungsi ii merupakan sebuah kumpulan code program yang digunakan untuk melakukan suatu perintah jadi dapat disimpulkan bahwa kode adalah Sebuah fungsi yang didefinisikan di dalam class.

Apa tujuannya self? Argumen pertama dari setiap metode merujuk pada instance class saat ini, yang menurut konvensi, diberi nama self. Dalam __init__ metode ini, self mengacu pada objek yang baru dibuat, sementara dalam metode lain, self mengcu pada contoh yang metode namanya disebut. Untuk lebih lanjut tentang __init__ vs self.

Apa tujuan dari init metode ini? __init__ Metode menginisialisasi sebuah instance dari class

Jelaskan bagaimana pewarisan membantu mencegah duplikasi kode? Kita bisa menurunkan karakteristik sebuah kelas ke kelas baru, dibanding dengan membuat kelas dari awal. Turunannya kelas anak (child class) dan yang mewarisikannya disebut kelas induk (parent class) kelas anak mewarisi atribut dari kelas induk, dan kita bisa menggunakan atribut tersebut seolah atribut itu didefinisikan juga didalam kelas anak. Kelas anak juga bisa menimpa (override) data danmetode dari induknya dengan data dan metodenya sendiri. Secara singkat dapat diartikan bahwa class cild mwarisi semua artibut dan perilaku parents.

Dapatkah class child menimpa sifat parents? Iya class child bisa menimpa sifat parents  