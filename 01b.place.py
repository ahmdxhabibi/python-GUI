import tkinter as tk

root_place = tk.Tk()
root_place.title("Contoh Place")
root_place.geometry("400x300")

# Menggunakan Place untuk Tata Letak
label1 = tk.Label(root_place, text="Label 1", bg="red", width=15)
label2 = tk.Label(root_place, text="Label 2", bg="green", width=15)
label3 = tk.Label(root_place, text="Label 3", bg="blue", width=15)

label1.place(x=50, y=50)
label2.place(x=150, y=100)
label3.place(x=250, y=150)

# Menjalankan Aplikasi Place
root_place.mainloop()
