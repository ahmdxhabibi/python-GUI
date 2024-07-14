import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Spinbox
label_spinbox = tk.Label(root, text="Pilih angka:")
label_spinbox.pack(pady=5)
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=5)


# Menjalankan Aplikasi
root.mainloop()
