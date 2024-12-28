import tkinter as tk
from tkinter import messagebox

def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        conversion_factors_length = {
            'метры': 1,
            'километры': 1000,
            'миль': 1609.34,
            'футы': 0.3048,
            'сантиметры': 0.01,
            'миллиметры': 0.001,
            'ярды': 0.9144,
            'дюймы': 0.0254
        }

        conversion_factors_mass = {
            'килограммы': 1,
            'граммы': 0.001,
            'фунты': 0.453592,
            'унции': 0.0283495,
            'тонны': 1000
        }

        conversion_factors_volume = {
            'литры': 1,
            'миллилитры': 0.001,
            'галлионы': 3.78541,
            'кубические метры': 1000,
            'пинты': 0.473176,
            'кубические сантиметры': 0.001,
            'кубические дюймы': 0.0163871
        }

        conversion_factors_temperature = {
            'цельсий': 0,
            'фаренгейт': 32,
            'кельвин': 273.15
        }

        conversion_factors_speed = {
            'метры в секунду': 1,
            'километры в час': 0.277778,
            'миль в час': 0.44704,
            'футы в секунду': 0.3048
        }

        if from_unit in conversion_factors_length and to_unit in conversion_factors_length:
            result = value * conversion_factors_length[from_unit] / conversion_factors_length[to_unit]
        elif from_unit in conversion_factors_mass and to_unit in conversion_factors_mass:
            result = value * conversion_factors_mass[from_unit] / conversion_factors_mass[to_unit]
        elif from_unit in conversion_factors_volume and to_unit in conversion_factors_volume:
            result = value * conversion_factors_volume[from_unit] / conversion_factors_volume[to_unit]
        elif from_unit in conversion_factors_temperature and to_unit in conversion_factors_temperature:
            if from_unit == 'цельсий':
                result = value + conversion_factors_temperature['фаренгейт'] - conversion_factors_temperature[from_unit]
                if to_unit == 'фаренгейт':
                    result = (result * 9/5) + 32
                elif to_unit == 'кельвин':
                    result = result + 273.15
            elif from_unit == 'фаренгейт':
                result = (value - 32) * (5/9)
                if to_unit == 'цельсий':
                    result = result
                elif to_unit == 'кельвин':
                    result = result + 273.15
            elif from_unit == 'кельвин':
                result = value - conversion_factors_temperature['кельвин']
                if to_unit == 'цельсий':
                    result = result
                elif to_unit == 'фаренгейт':
                    result = (result * 9/5) + 32
        elif from_unit in conversion_factors_speed and to_unit in conversion_factors_speed:
            result = value * conversion_factors_speed[from_unit] / conversion_factors_speed[to_unit]
        else:
            raise ValueError("Неизвестная или несовместимая единица измерения")

        formatted_result = f"{result:.4f}"
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, formatted_result)

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", "Произошла ошибка при конверсии")

window = tk.Tk()
window.title("Конвертер единиц")
window.geometry("500x600")

font_style = ("Arial", 12)

label_value = tk.Label(window, text="Введите значение:", font=font_style)
label_value.pack(pady=10)
entry_value = tk.Entry(window, font=font_style)
entry_value.pack(pady=10)

from_unit_var = tk.StringVar(window)
from_unit_var.set('метры')
to_unit_var = tk.StringVar(window)
to_unit_var.set('метры')

length_units = ['метры', 'километры', 'миль', 'футы', 'сантиметры', 'миллиметры', 'ярды', 'дюймы']
mass_units = ['килограммы', 'граммы', 'фунты', 'унции', 'тонны']
volume_units = ['литры', 'миллилитры', 'галлионы', 'кубические метры', 'пинты', 'кубические сантиметры', 'кубические дюймы']
temperature_units = ['цельсий', 'фаренгейт', 'кельвин']
speed_units = ['метры в секунду', 'километры в час', 'миль в час', 'футы в секунду']

def update_units(event):
    unit_type = unit_type_var.get()
    if unit_type == "Длина":
        from_unit_var.set(length_units[0])
        to_unit_var.set(length_units[0])
        update_menu(from_unit_menu, length_units, from_unit_var)
        update_menu(to_unit_menu, length_units, to_unit_var)
    elif unit_type == "Масса":
        from_unit_var.set(mass_units[0])
        to_unit_var.set(mass_units[0])
        update_menu(from_unit_menu, mass_units, from_unit_var)
        update_menu(to_unit_menu, mass_units, to_unit_var)
    elif unit_type == "Объем":
        from_unit_var.set(volume_units[0])
        to_unit_var.set(volume_units[0])
        update_menu(from_unit_menu, volume_units, from_unit_var)
        update_menu(to_unit_menu, volume_units, to_unit_var)
    elif unit_type == "Температура":
        from_unit_var.set(temperature_units[0])
        to_unit_var.set(temperature_units[0])
        update_menu(from_unit_menu, temperature_units, from_unit_var)
        update_menu(to_unit_menu, temperature_units, to_unit_var)
    elif unit_type == "Скорость":
        from_unit_var.set(speed_units[0])
        to_unit_var.set(speed_units[0])
        update_menu(from_unit_menu, speed_units, from_unit_var)
        update_menu(to_unit_menu, speed_units, to_unit_var)

def update_menu(menu, options, var):
    menu['menu'].delete(0, 'end')
    for unit in options:
        menu['menu'].add_command(label=unit, command=tk._setit(var, unit))

unit_type_var = tk.StringVar(window)
unit_type_var.set('Длина')
unit_type_menu = tk.OptionMenu(window, unit_type_var, "Длина", "Масса", "Объем", "Температура", "Скорость", command=update_units)
unit_type_menu.config(font=font_style)
unit_type_menu.pack(pady=10)

from_unit_menu = tk.OptionMenu(window, from_unit_var, *length_units)
from_unit_menu.config(font=font_style)
from_unit_menu.pack(pady=10)

to_unit_menu = tk.OptionMenu(window, to_unit_var, *length_units)
to_unit_menu.config(font=font_style)
to_unit_menu.pack(pady=10)

button_convert = tk.Button(window, text="Конвертировать", command=convert_units, font=font_style)
button_convert.pack(pady=20)

label_result = tk.Label(window, text="Результат:", font=font_style)
label_result.pack(pady=10)
entry_result = tk.Entry(window, font=font_style)
entry_result.pack(pady=10)

window.mainloop()