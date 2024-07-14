import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Tkinter Dasar")
root.geometry("400x300")

# Menambahkan Label dengan Pack
label = tk.Label(root, text="Halo, Dunia!", font=('Arial', 18))
label.pack(pady=20)
root.mainloop()
