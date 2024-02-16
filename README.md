## README.md - Aplikasi Analisis Data E-Commerce dengan Streamlit

**Aplikasi ini memungkinkan Anda untuk menganalisis data transaksi e-commerce dan mendapatkan wawasan berharga.** Dibangun dengan Streamlit, Pandas, dan Matplotlib.

### Cara Penggunaan

1. **Pastikan Python dan library yang dibutuhkan terinstal:**

```bash
pip install streamlit
pip install -r requirements.txt
```

**Persyaratan:**

- Python 3.7+
- Streamlit ([https://docs.streamlit.io/get-started/installation](https://docs.streamlit.io/get-started/installation))
- Pandas ([https://pandas.pydata.org/docs/getting_started/install.html](https://pandas.pydata.org/docs/getting_started/install.html))
- Matplotlib ([https://matplotlib.org/](https://matplotlib.org/))

2. **Clone atau unduh repository ini.**

3. **Buka command prompt atau terminal di direktori repository.**

4. **Jalankan aplikasi dengan perintah berikut:**

```bash
streamlit run ecommerce.py
```

5. **Buka browser Anda.**

6. **Pilih menu "Analisis Data" untuk melihat analitik.**

**Fitur:**

- Menghitung AOV (Average Order Value) untuk semua pembayaran dan berdasarkan metode pembayaran.
- Menampilkan visualisasi AOV dan jumlah transaksi berdasarkan metode pembayaran dalam bentuk bar chart.
- Menampilkan dataframe transaksi lengkap.

7. **Pilih menu "Tentang" untuk informasi aplikasi.**

### Persyaratan Data

- Aplikasi ini membutuhkan file CSV bernama "ecommerce.csv" yang berisi data transaksi e-commerce.
- Pastikan file tersebut berada di direktori yang sama dengan kode aplikasi.

### Fitur Tambahan

- Anda dapat memodifikasi kode untuk menambah fitur seperti:

  - Filter data berdasarkan tanggal, produk, atau kategori lainnya.
  - Tambah visualisasi data lainnya seperti line chart atau pie chart.
  - Buat widget interaktif untuk mengontrol analisis.

### Sumber Kode

- Kode aplikasi tersedia di repository ini.
- Dokumentasi Streamlit: [https://docs.streamlit.io/knowledge-base/tutorials](https://docs.streamlit.io/knowledge-base/tutorials)
- Dokumentasi Pandas: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- Dokumentasi Matplotlib: [https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)

### Kontribusi

Silahkan ajukan issue atau pull request di repository ini jika Anda ingin berkontribusi dalam pengembangan aplikasi.
