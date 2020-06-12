from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
import random

# Definimos la ventana
ventana = Tk()
ventana.minsize(400, 200)
ventana.title("Adivinanzas")
ventana.iconbitmap(r"D:\Python\Proyectos\Juegos\Adivinanzas\pedro.ico")

# Variables 
guess = IntVar()
guess.set("")
guessed = []
secret_number = random.randint(1, 10)
count = 0

# Pantallas
def home():
	#Poner pantalla
	home_label.config(
		fg = "white",
		bg = "lightgrey",
		font = ("Arial", 30),
		padx = 200
		)
	home_label.grid(row = 0)

	add_frame.grid(row = 1, column = 0)
	add_game_label.grid(row = 1)
	add_game_entry.grid(row = 2)
	Label(add_frame).grid(row = 3)
	button_game.grid(row = 4)

	# Ocultar otras pantallas
	info_label.grid_remove()

def info():
	info_label.config(
		fg = "white",
		bg = "lightgrey",
		font = ("Arial", 30),
		padx = 100
		)
	info_label.grid(row = 0)
	
	# Ocultar otras pantallas
	home_label.grid_remove()
	add_frame.grid_remove()

def reset():
	global count 
	global guess
	global guessed

	guess.set("")
	guessed = []
	count = 0

def takeGuess():
	global count
	global guessed

	count += 1

	try:
		if guess.get() >= 1 and guess.get() <= 10:

			if count == 1:
				if guess.get() == secret_number:
					messagebox.showinfo("Ganaste!", "Felicidades! Gnaste.")
					reset()
				else: 
					messagebox.showerror("Sigue intentando!", f"Ese no es, te quedan {3 - count} intentos.")
					guessed.append(guess.get())
					guess.set("")			
					home()

			elif count == 2:
				if guess.get() == secret_number:
					messagebox.showinfo("Ganaste!", "Felicidades! Gnaste.")
					reset()
				else:
					if guess.get() not in guessed:
						messagebox.showerror("Sigue intentando!", f"Ese no es, te queda {3 - count} intentos.")
						guessed.append(guess.get())
						guess.set("")
					else:
						messagebox.showerror("Error", "Ese ya lo intentaste!")
						count -= 1

			elif count == 3:
				if guess.get() == secret_number:
					messagebox.showinfo("Ganaste!","Felicidades! Gnaste.")
					reset()
				else: 
					if guess.get() not in guessed:
						messagebox.showerror("Perdiste!", f"Ese no era! Estaba pensando en {secret_number}.")
						reset()
					else:
						messagebox.showerror("Error", "Ese ya lo intentaste!")
						guess.set("")
						count -= 1
		else:
			messagebox.showerror("Error", "Eso no es valido!")
			count -= 1
			guess.set("")

	except:
		messagebox.showerror("Error", "El número debe estar entre 1 y 10!")
		count -= 1
		guess.set("")

# Menu
menu_superior = Menu(ventana)
ventana.config(menu = menu_superior)

menu_inicio = Menu(menu_superior, tearoff = 0)
menu_inicio.add_command(label = "Continuar", command = home)
menu_inicio.add_separator()
menu_inicio.add_command(label = "Reiniciar", command = reset)

menu_superior.add_cascade(label = "Inicio", menu = menu_inicio)
menu_superior.add_command(label = "Información", command = info)
menu_superior.add_command(label = "Salir", command = ventana.quit)


# Campos (Titulos) de pantalla 
home_label = Label(ventana, text = "¡A JUGAR!")
info_label = Label(ventana, text = "Información")

# Formulario del juego
add_frame = Frame(ventana)
add_game_label = Label(add_frame, text = "Estoy pensando en un número entre el 1 y el 10! \n¿Podras adivinar cuál es?")
add_game_entry = Entry(add_frame, textvariable = guess, justify = "center")

button_game = Button(add_frame, text = "Adivinar", command = takeGuess)

# Cargamos la ventana
home()
ventana.mainloop()