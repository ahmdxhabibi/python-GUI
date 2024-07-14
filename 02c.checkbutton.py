import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Komponen Input pada Tkinter")
root.geometry("500x400")

# Checkbutton
label_check = tk.Label(root, text="Pilih opsi:")
label_check.pack(pady=5)
var_check = tk.IntVar()
check = tk.Checkbutton(root, text="Saya setuju", variable=var_check)
check.pack(pady=5)


# Menjalankan Aplikasi
root.mainloop()
