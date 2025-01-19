import tkinter as tk

# Main periodic table data (symbol, atomic number, name, category)
main_elements = [
    ["H", 1, "Hydrogen", "Nonmetal"], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,["He", 2, "Helium", "Noble Gas"],
    ["Li", 3, "Lithium", "Alkali Metal"], ["Be", 4, "Beryllium", "Alkaline Earth Metal"], None, None, None, None, None, None, None, None, None, None, ["B", 5, "Metalloid"], ["C", 6, "Nonmetal"], ["N", 7, "Nonmetal"], ["O", 8, "Nonmetal"], ["F", 9, "Halogen"], ["Ne", 10, "Noble Gas"],
    ["Na", 11, "Sodium", "Alkali Metal"], ["Mg", 12, "Magnesium", "Alkaline Earth Metal"], None, None, None, None, None, None, None, None, None, None, ["Al", 13, "Post-Transition Metal"], ["Si", 14, "Metalloid"], ["P", 15, "Nonmetal"], ["S", 16, "Nonmetal"], ["Cl", 17, "Halogen"], ["Ar", 18, "Noble Gas"],
    ["K", 19, "Potassium", "Alkali Metal"], ["Ca", 20, "Calcium", "Alkaline Earth Metal"], ["Sc", 21, "Transition Metal"], ["Ti", 22, "Transition Metal"], ["V", 23, "Transition Metal"], ["Cr", 24, "Transition Metal"], ["Mn", 25, "Transition Metal"], ["Fe", 26, "Iron", "Transition Metal"], ["Co", 27, "Cobalt", "Transition Metal"], ["Ni", 28, "Nickel", "Transition Metal"], ["Cu", 29, "Copper", "Transition Metal"], ["Zn", 30, "Zinc", "Transition Metal"], ["Ga", 31, "Post-Transition Metal"], ["Ge", 32, "Metalloid"], ["As", 33, "Metalloid"], ["Se", 34, "Nonmetal"], ["Br", 35, "Halogen"], ["Kr", 36, "Noble Gas"],
    ["Rb", 37, "Rubidium", "Alkali Metal"], ["Sr", 38, "Strontium", "Alkaline Earth Metal"], ["Y", 39, "Transition Metal"], ["Zr", 40, "Zirconium", "Transition Metal"], ["Nb", 41, "Niobium", "Transition Metal"], ["Mo", 42, "Molybdenum", "Transition Metal"], ["Tc", 43, "Technetium", "Transition Metal"], ["Ru", 44, "Ruthenium", "Transition Metal"], ["Rh", 45, "Rhodium", "Transition Metal"], ["Pd", 46, "Palladium", "Transition Metal"], ["Ag", 47, "Silver", "Transition Metal"], ["Cd", 48, "Cadmium", "Transition Metal"], ["In", 49, "Post-Transition Metal"], ["Sn", 50, "Tin", "Post-Transition Metal"], ["Sb", 51, "Metalloid"], ["Te", 52, "Metalloid"], ["I", 53, "Halogen"], ["Xe", 54, "Noble Gas"],
    ["Cs", 55, "Cesium", "Alkali Metal"], ["Ba", 56, "Barium", "Alkaline Earth Metal"], None, ["Hf", 72, "Hafnium", "Transition Metal"], ["Ta", 73, "Tantalum", "Transition Metal"], ["W", 74, "Tungsten", "Transition Metal"], ["Re", 75, "Rhenium", "Transition Metal"], ["Os", 76, "Osmium", "Transition Metal"], ["Ir", 77, "Iridium", "Transition Metal"], ["Pt", 78, "Platinum", "Transition Metal"], ["Au", 79, "Gold", "Transition Metal"], ["Hg", 80, "Mercury", "Transition Metal"], ["Tl", 81, "Post-Transition Metal"], ["Pb", 82, "Post-Transition Metal"], ["Bi", 83, "Post-Transition Metal"], ["Po", 84, "Metalloid"], ["At", 85, "Halogen"], ["Rn", 86, "Noble Gas"],
    ["Fr", 87, "Francium", "Alkali Metal"], ["Ra", 88, "Radium", "Alkaline Earth Metal"], None, ["Rf", 104, "Rutherfordium", "Transition Metal"], ["Db", 105, "Dubnium", "Transition Metal"], ["Sg", 106, "Seaborgium", "Transition Metal"], ["Bh", 107, "Bohrium", "Transition Metal"], ["Hs", 108, "Hassium", "Transition Metal"], ["Mt", 109, "Meitnerium", "Transition Metal"], ["Ds", 110, "Darmstadtium", "Transition Metal"], ["Rg", 111, "Roentgenium", "Transition Metal"], ["Cn", 112, "Copernicium", "Transition Metal"], ["Nh", 113, "Post-Transition Metal"], ["Fl", 114, "Post-Transition Metal"], ["Mc", 115, "Post-Transition Metal"], ["Lv", 116, "Post-Transition Metal"], ["Ts", 117, "Halogen"], ["Og", 118, "Noble Gas"],
]

# Lanthanides and Actinides
lanthanides = [
    ["La", 57, "Lanthanum", "Lanthanide"], ["Ce", 58, "Cerium", "Lanthanide"], ["Pr", 59, "Praseodymium", "Lanthanide"],
    ["Nd", 60, "Neodymium", "Lanthanide"], ["Pm", 61, "Promethium", "Lanthanide"], ["Sm", 62, "Samarium", "Lanthanide"],
    ["Eu", 63, "Europium", "Lanthanide"], ["Gd", 64, "Gadolinium", "Lanthanide"], ["Tb", 65, "Terbium", "Lanthanide"],
    ["Dy", 66, "Dysprosium", "Lanthanide"], ["Ho", 67, "Holmium", "Lanthanide"], ["Er", 68, "Erbium", "Lanthanide"],
    ["Tm", 69, "Thulium", "Lanthanide"], ["Yb", 70, "Ytterbium", "Lanthanide"], ["Lu", 71, "Lutetium", "Lanthanide"],
]

actinides = [
    ["Ac", 89, "Actinium", "Actinide"], ["Th", 90, "Thorium", "Actinide"], ["Pa", 91, "Protactinium", "Actinide"],
    ["U", 92, "Uranium", "Actinide"], ["Np", 93, "Neptunium", "Actinide"], ["Pu", 94, "Plutonium", "Actinide"],
    ["Am", 95, "Americium", "Actinide"], ["Cm", 96, "Curium", "Actinide"], ["Bk", 97, "Berkelium", "Actinide"],
    ["Cf", 98, "Californium", "Actinide"], ["Es", 99, "Einsteinium", "Actinide"], ["Fm", 100, "Fermium", "Actinide"],
    ["Md", 101, "Mendelevium", "Actinide"], ["No", 102, "Nobelium", "Actinide"], ["Lr", 103, "Lawrencium", "Actinide"],
]

# Color mapping for element categories
category_colors = {
    "Nonmetal": "lightgreen",
    "Noble Gas": "cyan",
    "Alkali Metal": "lightpink",
    "Alkaline Earth Metal": "lightyellow",
    "Metalloid": "orange",
    "Halogen": "lightblue",
    "Transition Metal": "lightgray",
    "Post-Transition Metal": "beige",
    "Lanthanide": "violet",
    "Actinide": "gold",
}

# Function to display element details
def show_element_details(symbol, atomic_number, name, category):
    details_label.config(
        text=f"Symbol: {symbol}\nAtomic Number: {atomic_number}\nName: {name}\nCategory: {category}"
    )

# Create main window
root = tk.Tk()
root.title("Periodic Table")
root.geometry("1200x800")
root.config(bg="black")


# Frame for periodic table
table_frame = tk.Frame(root, background="black")
table_frame.pack(pady=20)

# Create periodic table grid
row = 0
col = 0
border_width = 2
box_width= 5
box_height= 2

for element in main_elements:
    if element and len(element) < 4:
        element.append("Unknown")
    if element:
        symbol, atomic_number, name, category = element
        button = tk.Button(
            table_frame,
            text=symbol,
            width=box_width,
            height=box_height,
            bd=border_width,
            fg="white",
            bg="black",
            command=lambda s=symbol, a=atomic_number, n=name, c=category: show_element_details(s, a, n, c),
        )
        button.config(font=("Cascadia Code", 10))
        button.grid(row=row, column=col, padx=2, pady=2)
    else:
        placeholder = tk.Label(table_frame, text="", width=box_width, height=box_height, bd=border_width, fg="white", bg="black")
        placeholder.grid(row=row, column=col),
    

    col += 1
    if col > 17:  
        col = 0
        row += 1

# Add Lanthanides
lanthanide_frame = tk.Frame(root, background="black")
lanthanide_frame.pack()
for i, element in enumerate(lanthanides):
    symbol, atomic_number, name, category = element
    button = tk.Button(
        lanthanide_frame,
        text=symbol,
        width=box_width,
        height=box_height,
        bd=border_width,
        fg="white",
        bg="black",
        command=lambda s=symbol, a=atomic_number, n=name, c=category: show_element_details(s, a, n, c),
    )
    button.config(font=("Cascadia Code", 10))
    button.grid(row=0, column=i, padx=2, pady=2)

# Add Actinides
actinide_frame = tk.Frame(root, background="black")
actinide_frame.pack()
for i, element in enumerate(actinides):
    symbol, atomic_number, name, category = element
    button = tk.Button(
        actinide_frame,
        text=symbol,
        width=box_width,
        height=box_height,
        bd=border_width,
        fg="white",
        bg="black",
        command=lambda s=symbol, a=atomic_number, n=name, c=category: show_element_details(s, a, n, c),
    )
    button.config(font=("Cascadia Code", 10))
    button.grid(row=0, column=i, padx=2, pady=2)

# Label for displaying element details
details_label = tk.Label(root, background="black", fg="white", text="Click an element for details", font=("Cascadia Code", 14), highlightthickness=1, highlightbackground="white")
details_label.pack(pady=10)

# Run the application

root.mainloop()