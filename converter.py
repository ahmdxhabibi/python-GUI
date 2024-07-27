import tkinter as tk
from tkinter import ttk, messagebox

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Konversi Satuan")
root.geometry("400x400")
root.configure(bg='#f0f0f0')

# Gaya ttk
style = ttk.Style()
style.theme_use('clam')

# Frame untuk input nilai
frame_input = tk.Frame(root, bg='#f0f0f0')
frame_input.pack(pady=10)

label_input = tk.Label(frame_input, text="Masukkan nilai:",
                       bg='#f0f0f0', font=('Arial', 12))
label_input.pack(side=tk.LEFT, padx=5)

value_entry = ttk.Entry(frame_input, width=20)
value_entry.pack(side=tk.LEFT, padx=5)

# Frame untuk pilihan satuan
frame_units = tk.Frame(root, bg='#f0f0f0')
frame_units.pack(pady=10)

label_from_unit = tk.Label(frame_units, text="Dari:",
                           bg='#f0f0f0', font=('Arial', 12))
label_from_unit.pack(side=tk.LEFT, padx=5)

from_unit_combobox = ttk.Combobox(frame_units, values=[
                                  "Meter", "Kilometer", "Mil", "Yard", "Gram", "Kilogram", "Ons", "Pon", "Celsius", "Fahrenheit", "Kelvin"])
from_unit_combobox.pack(side=tk.LEFT, padx=5)

label_to_unit = tk.Label(frame_units, text="Ke:",
                         bg='#f0f0f0', font=('Arial', 12))
label_to_unit.pack(side=tk.LEFT, padx=5)

to_unit_combobox = ttk.Combobox(frame_units, values=[
                                "Meter", "Kilometer", "Mil", "Yard", "Gram", "Kilogram", "Ons", "Pon", "Celsius", "Fahrenheit", "Kelvin"])
to_unit_combobox.pack(side=tk.LEFT, padx=5)

# Frame untuk tombol konversi dan hasil
frame_result = tk.Frame(root, bg='#f0f0f0')
frame_result.pack(pady=10)


def convert_units():
    try:
        value = float(value_entry.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()
        if from_unit and to_unit:
            result = convert(value, from_unit, to_unit)
            result_label.config(text=f"Hasil: {result} {to_unit}")
        else:
            messagebox.showwarning(
                "Peringatan", "Pilih satuan asal dan tujuan!")
    except ValueError:
        messagebox.showwarning("Peringatan", "Masukkan nilai yang valid!")


def convert(value, from_unit, to_unit):
    # Konversi panjang
    if from_unit in ["Meter", "Kilometer", "Mil", "Yard"] and to_unit in ["Meter", "Kilometer", "Mil", "Yard"]:
        return convert_length(value, from_unit, to_unit)
    # Konversi berat
    elif from_unit in ["Gram", "Kilogram", "Ons", "Pon"] and to_unit in ["Gram", "Kilogram", "Ons", "Pon"]:
        return convert_weight(value, from_unit, to_unit)
    # Konversi suhu
    elif from_unit in ["Celsius", "Fahrenheit", "Kelvin"] and to_unit in ["Celsius", "Fahrenheit", "Kelvin"]:
        return convert_temperature(value, from_unit, to_unit)
    else:
        raise ValueError("Konversi tidak didukung!")


def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Mil": 1609.34,
        "Yard": 0.9144
    }
    return value * length_units[from_unit] / length_units[to_unit]


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Gram": 1,
        "Kilogram": 1000,
        "Ons": 28.3495,
        "Pon": 453.592
    }
    return value * weight_units[from_unit] / weight_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32


convert_button = ttk.Button(
    frame_result, text="Konversi", command=convert_units)
convert_button.pack(pady=5)

result_label = tk.Label(frame_result, text="Hasil: ",
                        bg='#f0f0f0', font=('Arial', 12))
result_label.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()
