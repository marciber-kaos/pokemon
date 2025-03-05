import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
from io import BytesIO

def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "Nombre": data["name"].capitalize(),
            "ID": data["id"],
            "Altura": data["height"],
            "Peso": data["weight"],
            "Tipos": [t["type"]["name"].capitalize() for t in data["types"]],
            "Imagen": data["sprites"]["front_default"]
        }
        return pokemon_info
    else:
        return None

def buscar_pokemon():
    nombre = entry.get()
    pokemon_data = get_pokemon_data(nombre)

    if pokemon_data:
        info_text.set(
            f"Nombre: {pokemon_data['Nombre']}\n"
            f"ID: {pokemon_data['ID']}\n"
            f"Altura: {pokemon_data['Altura']} dm\n"
            f"Peso: {pokemon_data['Peso']} hg\n"
            f"Tipo(s): {', '.join(pokemon_data['Tipos'])}"
        )

        # Cargar y mostrar la imagen
        img_url = pokemon_data["Imagen"]
        img_response = requests.get(img_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data = img_data.resize((150, 150), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_data)
        label_img.config(image=img_tk)
        label_img.image = img_tk
    else:
        info_text.set("Pokémon no encontrado. Inténtalo de nuevo.")

# Crear ventana
root = tk.Tk()
root.title("Pokédex")
root.geometry("300x400")

# Entrada de texto
entry = Entry(root)
entry.pack(pady=10)

# Botón de búsqueda
button = Button(root, text="Buscar Pokémon", command=buscar_pokemon)
button.pack()

# Etiqueta para mostrar la información
info_text = tk.StringVar()
label_info = Label(root, textvariable=info_text, justify="left")
label_info.pack(pady=10)

# Etiqueta para la imagen del Pokémon
label_img = Label(root)
label_img.pack()

# Ejecutar la ventana
root.mainloop()
