import random

# Establecemos el número a adivinar
secret_number = random.randint(1, 10)

# Establecemos las variables globales (parámetros)
count = 0
limit = 3

guess = ''
guessed = []

while count <= limit:
    # Si es numérico
    try:
        guess = int(input("Adivina: "))
        count += 1
        # Para el primer y segundo intento
        if count < limit:
            # si el número está entre el 1 y el 10
            if 10 >= guess >= 1:
                if guess != secret_number:
                    # Si ya lo intentaste
                    if guess in guessed:
                        print('Ese ya lo intentaste! Intenta de nuevo...')
                        count -= 1
                    else:
                        print('Ese no es! Intenta de nuevo...')
                        guessed.append(guess)
                else:
                    print('Ese era! ¡FELICIDADES!')
                    break
            # Si no
            else:
                print('Debes escribir un número entero entre el 1 y el 10')
                count -= 1

        # Si estas en el 3er intento
        else:
            # si el número está entre el 1 y el 10
            if 10 >= guess >= 1:
                if guess != secret_number:
                    # Si ya lo intentaste
                    if guess in guessed:
                        print('Ese ya lo intentaste! Intenta de nuevo...')
                        count -= 1
                    else:
                        print(f'Ese no es! El número era {secret_number}...')
                        break
                else:
                    print('Le atinaste! ¡FELICIDADES!')
                    break
            # Si no
            else:
                print('Debes escribir un número entero entre el 1 y el 10')
                count -= 1

    # Si no lo es
    except ValueError:
        print('Debes adivinar un número...')
        continue
