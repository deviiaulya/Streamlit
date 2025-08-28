import streamlit as st

st.set_page_config(page_title="Aplikasi Multi-Fitur", layout="centered")

st.title("Aplikasi Perhitungan")

# Pilihan menu
menu = st.sidebar.radio("Pilih Fitur:", ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

# Kalkulator
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)
    operator = st.selectbox("Pilih operator", ["+", "-", "×", "÷"])

    if st.button("Hitung"):
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "×":
            hasil = a * b
        elif operator == "÷":
            hasil = a / b if b != 0 else "Tak terdefinisi (bagi 0)"
        st.info(f"Hasil: {hasil}")

# Konversi Suhu
elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")
    nilai = st.number_input("Masukkan nilai suhu", value=0.0)
    asal = st.selectbox("Dari satuan:", ["Celcius", "Reamur", "Fahrenheit"])
    tujuan = st.selectbox("Ke satuan:", ["Celcius", "Reamur", "Fahrenheit"])

    if st.button("Konversi"):
        hasil = None
        if asal == tujuan:
            hasil = nilai
        elif asal == "Celcius":
            if tujuan == "Reamur":
                hasil = (4/5) * nilai
            elif tujuan == "Fahrenheit":
                hasil = (9/5) * nilai + 32
        elif asal == "Reamur":
            if tujuan == "Celcius":
                hasil = (5/4) * nilai
            elif tujuan == "Fahrenheit":
                hasil = (9/4) * nilai + 32
        elif asal == "Fahrenheit":
            if tujuan == "Celcius":
                hasil = (5/9) * (nilai - 32)
            elif tujuan == "Reamur":
                hasil = (4/9) * (nilai - 32)

        st.info(f"Hasil: {hasil:.2f} {tujuan}")

#Deret Fibonacci
elif menu == "Deret Fibonacci":
    st.header("Deret Fibonacci")
    n = st.number_input("Masukkan jumlah bilangan (n)", min_value=1, step=1)

    if st.button("Generate"):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        fib = fib[:n]
        st.info(f"Deret Fibonacci ({n} bilangan):")
        st.write(fib)
