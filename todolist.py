import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Pengelola Tugas")
root.geometry("500x500")
root.configure(bg='#f0f0f0')

# Gaya ttk
style = ttk.Style()
style.theme_use('clam')

# Entry untuk input tugas baru
frame_entry = tk.Frame(root, bg='#f0f0f0')
frame_entry.pack(pady=10)

task_entry_label = tk.Label(
    frame_entry, text="Masukkan tugas:", bg='#f0f0f0', font=('Arial', 12))
task_entry_label.pack(side=tk.LEFT, padx=5)

task_entry = ttk.Entry(frame_entry, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_task_button = ttk.Button(
    frame_entry, text="Tambah Tugas", command=lambda: add_task())
add_task_button.pack(side=tk.LEFT, padx=5)

# Listbox untuk menampilkan tugas dengan scrollbar
frame_listbox = tk.Frame(root, bg='#f0f0f0')
frame_listbox.pack(pady=10)

task_listbox = tk.Listbox(
    frame_listbox, selectmode=tk.SINGLE, width=40, height=15, font=('Arial', 12))
task_listbox.pack(side=tk.LEFT)

scrollbar = ttk.Scrollbar(
    frame_listbox, orient="vertical", command=task_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill="y")
task_listbox.config(yscrollcommand=scrollbar.set)

# Fungsi untuk menambah tugas


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Masukkan tugas terlebih dahulu!")

# Fungsi untuk menghapus tugas


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# Fungsi untuk menandai tugas sebagai selesai


def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} ✔")
    except IndexError:
        messagebox.showwarning(
            "Peringatan", "Pilih tugas yang ingin ditandai sebagai selesai!")

# Fungsi untuk menyimpan tugas


def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        with open(save_path, 'w') as file:
            for task in tasks:
                file.write(f"{task}\n")

# Fungsi untuk membuka tugas


def open_tasks():
    open_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if open_path:
        task_listbox.delete(0, tk.END)
        with open(open_path, 'r') as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

# Menubar


def about():
    messagebox.showinfo(
        "Tentang", "Aplikasi Pengelola Tugas\nDibuat dengan Tkinter")


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Simpan", command=save_tasks)
filemenu.add_command(label="Buka", command=open_tasks)
filemenu.add_separator()
filemenu.add_command(label="Keluar", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Tentang", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Menambahkan tombol operasi tugas
frame_buttons = tk.Frame(root, bg='#f0f0f0')
frame_buttons.pack(pady=10)

delete_task_button = ttk.Button(
    frame_buttons, text="Hapus Tugas", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)

mark_task_button = ttk.Button(
    frame_buttons, text="Tandai Selesai", command=mark_task_completed)
mark_task_button.pack(side=tk.LEFT, padx=5)

# Menjalankan Aplikasi
root.mainloop()
