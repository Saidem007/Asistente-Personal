import tkinter as tk
import kalvin  # Importa el módulo kalvin


# Función para iniciar el asistente
def iniciar_asistente():
        return kalvin.verificador(kalvin.convertidor())  # Llama a las funciones de kalvin
           

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Asistente Personal")  # Título de la ventana
ventana.geometry("300x200")  # Tamaño de la ventana

# Etiqueta de bienvenida
etiqueta = tk.Label(ventana, text="Hola,soy Kelvin", font=("Arial", 12))
etiqueta.pack(pady=20)

# Botón para iniciar el asistente
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar_asistente, font=("Arial", 10), bg="green", fg="white")
boton_iniciar.pack(pady=20)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
