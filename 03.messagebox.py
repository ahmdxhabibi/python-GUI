import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Tkinter Lanjut")
root.geometry("600x400")

# Fungsi Message Box


def show_message():
    messagebox.showinfo("Informasi", "Ini adalah message box informasi")


def show_warning():
    messagebox.showwarning("Peringatan", "Ini adalah message box peringatan")


def show_error():
    messagebox.showerror("Error", "Ini adalah message box error")


def ask_question():
    result = messagebox.askquestion(
        "Pertanyaan", "Apakah Anda ingin melanjutkan?")
    print("Hasil pertanyaan:", result)


# Menambahkan tombol untuk menampilkan message box
button_info = tk.Button(root, text="Tampilkan Info", command=show_message)
button_info.pack(pady=5)

button_warning = tk.Button(
    root, text="Tampilkan Peringatan", command=show_warning)
button_warning.pack(pady=5)

button_error = tk.Button(root, text="Tampilkan Error", command=show_error)
button_error.pack(pady=5)

button_question = tk.Button(
    root, text="Ajukan Pertanyaan", command=ask_question)
button_question.pack(pady=5)

# Menubar


def about():
    messagebox.showinfo("Tentang", "Ini adalah aplikasi contoh dengan menubar")


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Baru")
filemenu.add_command(label="Buka")
filemenu.add_command(label="Simpan")
filemenu.add_separator()
filemenu.add_command(label="Keluar", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Tentang", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Pop-Up


def get_input():
    user_input = simpledialog.askstring("Input", "Masukkan sesuatu:")
    if user_input:
        messagebox.showinfo("Informasi", f"Anda memasukkan: {user_input}")


button_popup = tk.Button(root, text="Tampilkan Pop-Up", command=get_input)
button_popup.pack(pady=5)

# Multiple Window


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Jendela Baru")
    new_window.geometry("300x200")
    label = tk.Label(
        new_window, text="Ini adalah jendela baru", font=('Arial', 14))
    label.pack(pady=20)


button_new_window = tk.Button(
    root, text="Buka Jendela Baru", command=open_new_window)
button_new_window.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()
