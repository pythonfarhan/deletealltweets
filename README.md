# Delete All Tweets

Sebuah *Automation Script* yang berfungsi untuk menghapus
semua tweet pada akun twitter anda secar otomatis dan berkala --satu minggu sekali--. Script ini ditulis menggunakan 
**Python 3.x**.

# How to use
- Silahkan download script terlebih dahulu:
```
$ git clone https://github.com/pythonfarhan/deletealltweets.git
$ cd deletealltweets
```
- Jika anda belum memiliki **token key** dan **consumer key**
 twitter, silahkan daftarkan akun anda di [https://apps.twitter.com](https://apps.twitter.com).
 
 - Kemudian, masukan **token key** dan **consumer key**
 akun twitter anda di dalam variabel yang dibutuhkan, seperti
hari, variabel ini berfungsi untuk menentukan tiap hari
apa akun anda akan dibersihkan.
  di file **_constants.py**
 
 - Install *dependencies* dengan:
 ```
 $ pip install -r requirements.txt
 ```
 
 - Jalankan script dengan:
 ```
 $ python app.py
 ```