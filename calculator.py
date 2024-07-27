import tkinter as tk
from tkinter import ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Kalkulator")
root.geometry("350x500")
root.configure(bg='#f0f0f0')

# Gaya ttk
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Arial', 18), padding=10)

# Display untuk menampilkan input dan hasil
display_frame = ttk.Frame(root)
display_frame.pack(pady=20)

display_var = tk.StringVar()
display = ttk.Entry(display_frame, textvariable=display_var, font=(
    'Arial', 24), justify='right', state='readonly')
display.pack(ipady=10, fill='x', padx=10)

# Frame untuk tombol
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=10)

# Tombol angka dan operator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 0
col = 0
for button in buttons:
    def action(x=button): return button_click(x)
    ttk.Button(buttons_frame, text=button, command=action).grid(
        row=row, column=col, sticky='nsew', padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Menambahkan konfigurasi grid untuk tombol
for i in range(4):
    buttons_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    buttons_frame.grid_rowconfigure(i, weight=1)

# Fungsi untuk menghandle klik tombol


def button_click(value):
    current = display_var.get()
    if value == '=':
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set('Error')
    elif value == 'C':
        display_var.set('')
    else:
        display_var.set(current + value)


# Menambahkan tombol Clear
clear_button = ttk.Button(root, text='C', command=lambda: button_click('C'))
clear_button.pack(pady=10, fill='x', padx=10)

# Menjalankan Aplikasi
root.mainloop()
