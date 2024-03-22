import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_errors = 3
errors = 0 # Variable que cuenta los fallos del jugador
vowels = "aeiou"
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
valid_difficulty = 0 # Variable usada para asegurar que se elija una dificultad valida
# Eleccion de dificultad
while valid_difficulty == 0:
    difficulty = input("Elija nivel de dificultad(facil, medio, dificil): ").lower()
    if difficulty == "facil":
        guessed_letters = ["a", "e", "i", "o", "u"] # Agrega las vocales a las letras adivinadas
        word_displayed = "".join(char if char in vowels else "_" for char in secret_word) # Muestra solo las vocales de la palabra
        print(f"Palabra: {word_displayed}")
        valid_difficulty = 1
    elif difficulty == "medio":
        word_displayed = f"{secret_word[0]}{'_' * (len(secret_word) - 2)}{secret_word[-1]}" # Muestra solo la 1ra y ultima letra de la palabra
        guessed_letters = [secret_word[0], secret_word[-1]] 
        print(f"Palabra: {word_displayed}")
        valid_difficulty = 1
    elif difficulty == "dificil":
        print(f"Palabra: {word_displayed}")
        valid_difficulty = 1
    else:
        print("No se ha elegido dificultad, vuelva a intentar")
while max_errors != errors:
     # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verifica que no se haya ingresado un string vacio
    if letter == "" or letter == " ":
        print("No se ha ingresado una letra, vuelve a intentar")
        continue
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.") # Mostrar la palabra parcialmente adivinada
        errors += 1
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has llegado a {max_errors} errores.")
    print(f"La palabra secreta era: {secret_word}")