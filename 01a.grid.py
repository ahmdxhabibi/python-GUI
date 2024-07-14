import tkinter as tk
# Contoh terpisah untuk Grid
root_grid = tk.Tk()
root_grid.title("Contoh Grid")
root_grid.geometry("400x300")

# Menggunakan Grid untuk Tata Letak
label1 = tk.Label(root_grid, text="Label 1", bg="red", width=15)
label2 = tk.Label(root_grid, text="Label 2", bg="green", width=15)
label3 = tk.Label(root_grid, text="Label 3", bg="blue", width=15)

label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
label3.grid(row=0, column=2, padx=5, pady=5)

# Menjalankan Aplikasi Grid
root_grid.mainloop()
