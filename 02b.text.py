import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Text
label_text = tk.Label(root, text="Masukkan teks panjang:")
label_text.pack(pady=5)
text = tk.Text(root, height=5, width=30)
text.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()
