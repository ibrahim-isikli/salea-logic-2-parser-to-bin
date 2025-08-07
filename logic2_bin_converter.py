import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def convert_csv_to_bin():
    csv_filename = filedialog.askopenfilename(
        title="Please select parsed .csv file",
        filetypes=[("CSV files", "*.csv")]
    )

    if not csv_filename:
        return  

    binary_data = []

    try:
        with open(csv_filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for cell in row:
                    cell = cell.strip()
                    if cell.startswith("0x") and len(cell) == 4:
                        try:
                            value = int(cell, 16)
                            binary_data.append(value)
                        except ValueError:
                            pass

        
        output_filename = os.path.splitext(csv_filename)[0] + "_for_imhex.bin"
        with open(output_filename, "wb") as f:
            f.write(bytearray(binary_data))

        messagebox.showinfo("successed", f"binary created:\n{output_filename}")

    except Exception as e:
        messagebox.showerror("error", f"error: please check the file location. Files must be same location\n{e}")


root = tk.Tk()
root.title("logic2 parsed csv to bin")
root.geometry("650x250")
root.resizable(False, False)


info_label = tk.Label(
    root,
    text = "Logic2_parser programindan aldiginiz .csv dosyasini secin. Secili dosya parse'lanmis olmalidir. Cikan bin dosyasini imhex editorune atin",
    font = ("Arial", 11),
    justify = "center",
    wraplength = 600,
    fg = "black"
)
info_label.pack(pady=(20, 10))

info_label_eng = tk.Label(
    root,
    text = "Select the .csv file from Logic2_parser program. The selected file must be parsed. Insert the resulting bin file into imhex.",
    font = ("Arial",11), 
    justify ="center",
    wraplength = 600,
    fg = "black"
)
info_label_eng.pack(pady=(40,10))

convert_button = tk.Button(root, text="CSV Dosyasini Secin ve BIN'e Donusturun", command=convert_csv_to_bin, font=("Arial", 9))
convert_button.pack(pady=20)


root.mainloop()
