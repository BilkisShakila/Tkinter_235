import tkinter as tk                  #import tkinter module dengan alias tk
import tkinter.messagebox as msg       # import modul messagebox dengan alias msg
top = tk.Tk()                          #membuat objek window utama

# Fungsi ketika tombol ditekan
def prediksi_prodi():                       #membuat fungsi prediksi_prodi
        msg.showinfo("Prediksi Prodi","Hasil Prediksi: Teknologi Informasi")     #menampilkan message box dengan judul dan isi pesan

top.title("Aplikasi prediksi Prodi Pilihan")
top.geometry("800x600")
top.configure(bg="white")
def tampilkanPrediksi():

#label judul
    msg.showinfo("Prediksi Prodi","Hasil Prediksi: Teknologi Informasi")
tombol = tk.Button(top, text="Aplikasi prediksi Prodi Pilihan", command=tampilkanPrediksi, bg="lightblue")
tombol.pack(pady=20)      

# Frame untuk input nilai
input_frame = tk.Frame(top)    #membuat frame untuk input nilai
input_frame.pack(pady=10)      #menempatkan frame di window utama #10  dari atas
entries = [] #menyimpan state dari input nilai mata pelajaran.

# Membuat 10 input nilai mata pelajaran dalam 1 kolom
for i in range(10):
    label = tk.Label(input_frame, text=f"Nilai MP {i+1}:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
    
    entry = tk.Entry(input_frame, width=10)  #Setiap tk.Entry adalah widget yang menyimpan state dari input nilai mata pelajaran.
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

#membuat 1 button hasil prediksi
prediksi_button = tk.Button(top, text="Hasil Prediksi", command=prediksi_prodi, bg="lightblue")
prediksi_button.pack(pady=20)   

#membuat label hasil prediksi
hasil_label = tk.Label(top, text="Hasil Prediksi: ", fg="black")    
hasil_label.pack(pady=10)

#menjalankan aplikasi
top.mainloop() #menjalankan loop utama aplikasi tkinter