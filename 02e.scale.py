import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Scale
label_scale = tk.Label(root, text="Pilih nilai:")
label_scale.pack(pady=5)
scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
scale.pack(pady=5)


# Menjalankan Aplikasi
root.mainloop()
