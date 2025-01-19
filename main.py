import tkinter as tk

# Main periodic table data
main_elements = [
    ["H", 1, "Hydrogen", "Nonmetal", 1.008, "Gas", 2.20], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ["He", 2, "Helium", "Noble Gas", 4.0026, "Gas", None],
    ["Li", 3, "Lithium", "Alkali Metal", 6.94, "Solid", 0.98], ["Be", 4, "Beryllium", "Alkaline Earth Metal", 9.0122, "Solid", 1.57], None, None, None, None, None, None, None, None, None, None, ["B", 5, "Boron", "Metalloid", 10.81, "Solid", 2.04], ["C", 6, "Carbon", "Nonmetal", 12.011, "Solid", 2.55], ["N", 7, "Nitrogen", "Nonmetal", 14.007, "Gas", 3.04], ["O", 8, "Oxygen", "Nonmetal", 15.999, "Gas", 3.44], ["F", 9, "Fluorine", "Halogen", 18.998, "Gas", 3.98], ["Ne", 10, "Neon", "Noble Gas", 20.180, "Gas", None],
    ["Na", 11, "Sodium", "Alkali Metal", 22.990, "Solid", 0.93], ["Mg", 12, "Magnesium", "Alkaline Earth Metal", 24.305, "Solid", 1.31], None, None, None, None, None, None, None, None, None, None, ["Al", 13, "Aluminium", "Post-Transition Metal", 26.982, "Solid", 1.61], ["Si", 14, "Silicon", "Metalloid", 28.085, "Solid", 1.90], ["P", 15, "Phosphorus", "Nonmetal", 30.974, "Solid", 2.19], ["S", 16, "Sulfur", "Nonmetal", 32.06, "Solid", 2.58], ["Cl", 17, "Chlorine", "Halogen", 35.45, "Gas", 3.16], ["Ar", 18, "Argon", "Noble Gas", 39.948, "Gas", None],
    ["K", 19, "Potassium", "Alkali Metal", 39.098, "Solid", 0.82], ["Ca", 20, "Calcium", "Alkaline Earth Metal", 40.078, "Solid", 1.00], ["Sc", 21, "Scandium", "Transition Metal", 44.956, "Solid", 1.36], ["Ti", 22, "Titanium", "Transition Metal", 47.867, "Solid", 1.54], ["V", 23, "Vanadium", "Transition Metal", 50.942, "Solid", 1.63], ["Cr", 24, "Chromium", "Transition Metal", 51.996, "Solid", 1.66], ["Mn", 25, "Manganese", "Transition Metal", 54.938, "Solid", 1.55], ["Fe", 26, "Iron", "Transition Metal", 55.845, "Solid", 1.83], ["Co", 27, "Cobalt", "Transition Metal", 58.933, "Solid", 1.88], ["Ni", 28, "Nickel", "Transition Metal", 58.693, "Solid", 1.91], ["Cu", 29, "Copper", "Transition Metal", 63.546, "Solid", 1.90], ["Zn", 30, "Zinc", "Transition Metal", 65.38, "Solid", 1.65], ["Ga", 31, "Gallium", "Post-Transition Metal", 69.723, "Solid", 1.81], ["Ge", 32, "Germanium", "Metalloid", 72.63, "Solid", 2.01], ["As", 33, "Arsenic", "Metalloid", 74.922, "Solid", 2.18], ["Se", 34, "Selenium", "Nonmetal", 78.971, "Solid", 2.55], ["Br", 35, "Bromine", "Halogen", 79.904, "Liquid", 2.96], ["Kr", 36, "Krypton", "Noble Gas", 83.798, "Gas", 3.00],
    ["Rb", 37, "Rubidium", "Alkali Metal", 85.468, "Solid", 0.82], ["Sr", 38, "Strontium", "Alkaline Earth Metal", 87.62, "Solid", 0.95], ["Y", 39, "Yttrium", "Transition Metal", 88.906, "Solid", 1.22], ["Zr", 40, "Zirconium", "Transition Metal", 91.224, "Solid", 1.33], ["Nb", 41, "Niobium", "Transition Metal", 92.906, "Solid", 1.6], ["Mo", 42, "Molybdenum", "Transition Metal", 95.95, "Solid", 2.16], ["Tc", 43, "Technetium", "Transition Metal", 98, "Solid", 1.9], ["Ru", 44, "Ruthenium", "Transition Metal", 101.07, "Solid", 2.2], ["Rh", 45, "Rhodium", "Transition Metal", 102.91, "Solid", 2.28], ["Pd", 46, "Palladium", "Transition Metal", 106.42, "Solid", 2.2], ["Ag", 47, "Silver", "Transition Metal", 107.87, "Solid", 1.93], ["Cd", 48, "Cadmium", "Transition Metal", 112.41, "Solid", 1.69], ["In", 49, "Indium", "Post-Transition Metal", 114.82, "Solid", 1.78], ["Sn", 50, "Tin", "Post-Transition Metal", 118.71, "Solid", 1.96], ["Sb", 51, "Antimony", "Metalloid", 121.76, "Solid", 2.05], ["Te", 52, "Tellurium", "Metalloid", 127.6, "Solid", 2.1], ["I", 53, "Iodine", "Halogen", 126.90, "Solid", 2.66], ["Xe", 54, "Xenon", "Noble Gas", 131.29, "Gas", 2.6],
    ["Cs", 55, "Cesium", "Alkali Metal", 132.91, "Solid", 0.79], ["Ba", 56, "Barium", "Alkaline Earth Metal", 137.33, "Solid", 0.89], None, ["Hf", 72, "Hafnium", "Transition Metal", 178.49, "Solid", 1.3], ["Ta", 73, "Tantalum", "Transition Metal", 180.95, "Solid", 1.5], ["W", 74, "Tungsten", "Transition Metal", 183.84, "Solid", 2.36], ["Re", 75, "Rhenium", "Transition Metal", 186.21, "Solid", 1.9], ["Os", 76, "Osmium", "Transition Metal", 190.23, "Solid", 2.2], ["Ir", 77, "Iridium", "Transition Metal", 192.22, "Solid", 2.2], ["Pt", 78, "Platinum", "Transition Metal", 195.08, "Solid", 2.28], ["Au", 79, "Gold", "Transition Metal", 196.97, "Solid", 2.54], ["Hg", 80, "Mercury", "Transition Metal", 200.59, "Liquid", 2.00], ["Tl", 81, "Thallium", "Post-Transition Metal", 204.38, "Solid", 1.62], ["Pb", 82, "Lead", "Post-Transition Metal", 207.2, "Solid", 2.33], ["Bi", 83, "Bismuth", "Post-Transition Metal", 208.98, "Solid", 2.02], ["Po", 84, "Polonium", "Metalloid", 209, "Solid", 2.0], ["At", 85, "Astatine", "Halogen", 210, "Solid", 2.2], ["Rn", 86, "Radon", "Noble Gas", 222, "Gas", None],
    ["Fr", 87, "Francium", "Alkali Metal", 223, "Solid", 0.7], ["Ra", 88, "Radium", "Alkaline Earth Metal", 226, "Solid", 0.9], None, ["Rf", 104, "Rutherfordium", "Transition Metal", 267, "Solid", None], ["Db", 105, "Dubnium", "Transition Metal", 270, "Solid", None], ["Sg", 106, "Seaborgium", "Transition Metal", 271, "Solid", None], ["Bh", 107, "Bohrium", "Transition Metal", 274, "Solid", None], ["Hs", 108, "Hassium", "Transition Metal", 277, "Solid", None], ["Mt", 109, "Meitnerium", "Unknown", 278, "Solid", None], ["Ds", 110, "Darmstadtium", "Unknown", 281, "Solid", None], ["Rg", 111, "Roentgenium", "Unknown", 282, "Solid", None], ["Cn", 112, "Copernicium", "Unknown", 285, "Liquid", None], ["Nh", 113, "Nihonium", "Unknown", 286, "Solid", None], ["Fl", 114, "Flerovium", "Unknown", 289, "Solid", None], ["Mc", 115, "Moscovium", "Unknown", 290, "Solid", None], ["Lv", 116, "Livermorium", "Unknown", 293, "Solid", None], ["Ts", 117, "Tennessine", "Halogen", 294, "Solid", None], ["Og", 118, "Oganesson", "Noble Gas", 294, "Gas", None],
]


lanthanides = [
    ["La", 57, "Lanthanum", "Lanthanide", 138.91, "Solid", 1.1],
    ["Ce", 58, "Cerium", "Lanthanide", 140.12, "Solid", 1.12],
    ["Pr", 59, "Praseodymium", "Lanthanide", 140.91, "Solid", 1.13],
    ["Nd", 60, "Neodymium", "Lanthanide", 144.24, "Solid", 1.14],
    ["Pm", 61, "Promethium", "Lanthanide", 145, "Solid", None],
    ["Sm", 62, "Samarium", "Lanthanide", 150.36, "Solid", 1.17],
    ["Eu", 63, "Europium", "Lanthanide", 151.96, "Solid", None],
    ["Gd", 64, "Gadolinium", "Lanthanide", 157.25, "Solid", 1.2],
    ["Tb", 65, "Terbium", "Lanthanide", 158.93, "Solid", None],
    ["Dy", 66, "Dysprosium", "Lanthanide", 162.5, "Solid", 1.22],
    ["Ho", 67, "Holmium", "Lanthanide", 164.93, "Solid", 1.23],
    ["Er", 68, "Erbium", "Lanthanide", 167.26, "Solid", 1.24],
    ["Tm", 69, "Thulium", "Lanthanide", 168.93, "Solid", 1.25],
    ["Yb", 70, "Ytterbium", "Lanthanide", 173.04, "Solid", None],
    ["Lu", 71, "Lutetium", "Lanthanide", 174.97, "Solid", 1.27],
]

actinides = [
    ["Ac", 89, "Actinium", "Actinide", 227, "Solid", None],
    ["Th", 90, "Thorium", "Actinide", 232.04, "Solid", 1.3],
    ["Pa", 91, "Protactinium", "Actinide", 231.04, "Solid", 1.5],
    ["U", 92, "Uranium", "Actinide", 238.03, "Solid", 1.38],
    ["Np", 93, "Neptunium", "Actinide", 237, "Solid", 1.36],
    ["Pu", 94, "Plutonium", "Actinide", 244, "Solid", 1.28],
    ["Am", 95, "Americium", "Actinide", 243, "Solid", 1.13],
    ["Cm", 96, "Curium", "Actinide", 247, "Solid", None],
    ["Bk", 97, "Berkelium", "Actinide", 247, "Solid", None],
    ["Cf", 98, "Californium", "Actinide", 251, "Solid", None],
    ["Es", 99, "Einsteinium", "Actinide", 252, "Solid", None],
    ["Fm", 100, "Fermium", "Actinide", 257, "Solid", None],
    ["Md", 101, "Mendelevium", "Actinide", 258, "Solid", None],
    ["No", 102, "Nobelium", "Actinide", 259, "Solid", None],
    ["Lr", 103, "Lawrencium", "Actinide", 262, "Solid", None],
]


# Function to display element details
def show_element_details(symbol, atomic_number, name, category, atomic_mass, state, electronegativity):
    details = (
        f"Symbol: {symbol}\n"
        f"Atomic Number: {atomic_number}\n"
        f"Name: {name}\n"
        f"Category: {category}\n"
        f"Atomic Mass: {atomic_mass} u\n"
        f"State at Room Temperature: {state}\n"
        f"Electronegativity: {electronegativity if electronegativity else 'N/A'}"
    )
    details_label.config(text=details)

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
    if element and len(element) < 7:
        element.append("N/A")
    if element:
        symbol, atomic_number, name, category, atomic_mass, state, electronegativity = element
        button = tk.Button(
            table_frame,
            text=symbol,
            width=box_width,
            height=box_height,
            bd=border_width,
            fg="white",
            bg="black",
            command=lambda s=symbol, a=atomic_number, n=name, c=category, m=atomic_mass, st=state, e=electronegativity:
            show_element_details(s, a, n, c, m, st, e),
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
    symbol, atomic_number, name, category, atomic_mass, state, electronegativity = element
    button = tk.Button(
        lanthanide_frame,
        text=symbol,
        width=box_width,
        height=box_height,
        bd=border_width,
        fg="white",
        bg="black",
        command=lambda s=symbol, a=atomic_number, n=name, c=category, m=atomic_mass, st=state, e=electronegativity:
        show_element_details(s, a, n, c, m, st, e),
    )
    button.config(font=("Cascadia Code", 10))
    button.grid(row=0, column=i, padx=2, pady=2)

# Add Actinides
actinide_frame = tk.Frame(root, background="black")
actinide_frame.pack()
for i, element in enumerate(actinides):
    symbol, atomic_number, name, category, atomic_mass, state, electronegativity = element
    button = tk.Button(
        actinide_frame,
        text=symbol,
        width=box_width,
        height=box_height,
        bd=border_width,
        fg="white",
        bg="black",
        command=lambda s=symbol, a=atomic_number, n=name, c=category, m=atomic_mass, st=state, e=electronegativity:
        show_element_details(s, a, n, c, m, st, e),
    )
    button.config(font=("Cascadia Code", 10))
    button.grid(row=0, column=i, padx=2, pady=2)

# Label for displaying element details
details_label = tk.Label(root, background="black", fg="white", text="Click an element for details", font=("Cascadia Code", 14), highlightthickness=1, highlightbackground="white")
details_label.pack(pady=10)

# Run the application

root.mainloop()