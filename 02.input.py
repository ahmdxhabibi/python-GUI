import tkinter as tk
from tkinter import ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x600")

# Entry
label_entry = tk.Label(root, text="Masukkan teks:")
label_entry.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Text
label_text = tk.Label(root, text="Masukkan teks panjang:")
label_text.pack(pady=5)
text = tk.Text(root, height=5, width=30)
text.pack(pady=5)

# Checkbutton
label_check = tk.Label(root, text="Pilih opsi:")
label_check.pack(pady=5)
var_check = tk.IntVar()
check = tk.Checkbutton(root, text="Saya setuju", variable=var_check)
check.pack(pady=5)

# Radiobutton
label_radio = tk.Label(root, text="Pilih satu:")
label_radio.pack(pady=5)
var_radio = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Opsi 1", variable=var_radio, value=1)
radio2 = tk.Radiobutton(root, text="Opsi 2", variable=var_radio, value=2)
radio1.pack(pady=5)
radio2.pack(pady=5)

# Scale
label_scale = tk.Label(root, text="Pilih nilai:")
label_scale.pack(pady=5)
scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
scale.pack(pady=5)

# Spinbox
label_spinbox = tk.Label(root, text="Pilih angka:")
label_spinbox.pack(pady=5)
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=5)

# Combobox
label_combobox = tk.Label(root, text="Pilih item:")
label_combobox.pack(pady=5)
combobox = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combobox.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()
