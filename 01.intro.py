import tkinter as tk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Tkinter Dasar")
root.geometry("400x300")

# Menambahkan Label dengan Pack
label = tk.Label(root, text="Halo, Dunia!", font=('Arial', 18))
label.pack(pady=20)

# Fungsi Callback untuk Button


def on_button_click():
    print("Tombol diklik!")


# Menambahkan Button dengan Event Handler
button = tk.Button(root, text="Klik Saya", font=(
    'Arial', 14), command=on_button_click)
button.pack(pady=10)

# Menjalankan Aplikasi
root.mainloop()
