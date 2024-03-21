import tkinter as tk

def contar_caracteres(event=None):
    input_text = entrada_texto.get()
    caracteres = len(input_text)
    resultado.set(f"{input_text} has {caracteres} characters.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Contador de Caracteres")

# Crear etiqueta de entrada
etiqueta = tk.Label(ventana, text="What is the input string?")
etiqueta.pack()

# Crear campo de entrada de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

# Variable para almacenar el resultado
resultado = tk.StringVar()

# Mostrar resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

# Llamar a la función contar_caracteres cada vez que se presione una tecla
entrada_texto.bind("<KeyRelease>", contar_caracteres)

# Llamar a la función contar_caracteres al inicio
contar_caracteres()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
