import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk memuat data
@st.cache
def load_data():
    return pd.read_csv("ecommerce.csv")

# Fungsi untuk analisis data
def data_analysis(df):
    # Analisis data
    st.write("## Analisis Data E-Commerce")

    # Pertanyaan 1: AOV untuk semua pembayaran
    total_sales_all_payments = df['payment_value'].sum()
    total_transactions_all_payments = len(df)
    aov_all_payments = total_sales_all_payments / total_transactions_all_payments

    # Pertanyaan 2: AOV berdasarkan metode pembayaran
    payment_stats = df.groupby('payment_type')['payment_value'].agg(['sum', 'count'])
    payment_stats['aov'] = payment_stats['sum'] / payment_stats['count']
    st.write("### AOV Berdasarkan Metode Pembayaran")
    st.bar_chart(payment_stats['aov'])

    # Pertanyaan 3: Jumlah Transaksi berdasarkan Metode Pembayaran
    st.write("### Jumlah Transaksi berdasarkan Metode Pembayaran")
    st.bar_chart(payment_stats['count'])



# Layout header
def header():
    st.write("# Analisis Data E-Commerce")
    st.write("Selamat datang di aplikasi analisis data")

# Layout footer
def footer():
    st.write("Terima kasih telah menggunakan aplikasi ini. ")

# Main function (recommended for clarity)
def main():
    # Layout header
    header()

    # Sidebar
    st.sidebar.title("Pilihan")
    menu = st.sidebar.radio("Pilih menu:", ("Analisis Data", "Tentang"))

    # Load data (load only once on the first run)
    df = load_data()

    # Tampilkan halaman berdasarkan opsi yang dipilih
    if menu == "Analisis Data":
        data_analysis(df)
    elif menu == "Tentang":
        st.write("# Tentang Aplikasi")
        st.write("Aplikasi ini dibuat dengan Streamlit.")
        st.write("Digunakan untuk menganalisis data transaksi e-commerce.")

    # Layout footer
    footer()

if __name__ == "__main__":
    main()
