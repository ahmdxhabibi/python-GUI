import tkinter as tk
from tkinter import ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Combobox
label_combobox = tk.Label(root, text="Pilih item:")
label_combobox.pack(pady=5)
combobox = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combobox.pack(pady=5)


# Menjalankan Aplikasi
root.mainloop()
