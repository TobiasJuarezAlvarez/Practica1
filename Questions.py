import random
import sys

score = 0

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Se escoge 3 preguntas de manera aleaotoria (Las preguntas pueden repertirse)
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, answers, correct_answer in questions_to_ask:
    print(question)
    
    for i, options in enumerate(answers):
        print(f"{i+1}. {options}")


    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):     
        user_answer = (input("Respuesta: ")) 

        if not user_answer.isdigit() or ((int(user_answer)-1) < 0) or ((int(user_answer)-1) >= len(answers)):
            print("Respuesta no valida")
            sys.exit(1)

        user_answer = int(user_answer) -1

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            score += 1
            print("¡Correcto!")
            break
        else:
            score -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_answer])

    # Se imprime un blanco al final de la pregunta
    print()

print(f"Puntaje final =  {score} ") #Imprime en pantalla el puntaje total del jugador