import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Entry
label_entry = tk.Label(root, text="Masukkan teks:")
label_entry.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()
