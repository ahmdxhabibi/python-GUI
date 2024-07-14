import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Radiobutton
label_radio = tk.Label(root, text="Pilih satu:")
label_radio.pack(pady=5)
var_radio = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Opsi 1", variable=var_radio, value=1)
radio2 = tk.Radiobutton(root, text="Opsi 2", variable=var_radio, value=2)
radio1.pack(pady=5)
radio2.pack(pady=5)


# Menjalankan Aplikasi
root.mainloop()
