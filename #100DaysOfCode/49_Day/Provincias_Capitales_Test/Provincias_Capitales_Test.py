#! python3

# Provincias_Capitales_Test.py, es una aplicacion para generar examenes de provincias y
# capitales de Argentina de manera random, según la cantidad de participantes en el juego.

# Importing librares and modules

import random

# Defining global variables

capitales = None
quiz_File = None
quiz_Number = 0
exams_For_Pupil = 0
answers_Quantity = 0

# Datos de los examenes, Keys son provincias y Values son sus capitales

capitales = {'Buenos Aires':'La Plata',
            'Catamarca':  'San Fernando del Valle de Catamarca',
            'Chaco':  'Resistencia',
            'Chubut': 'Rawson',
            'Cordoba': 'Cordoba',
            'Corrientes': 'Corrientes',
            'Entre Rios': 'Parana',
            'Formosa': 'Formosa',
            'Jujuy': 'San Salvador de Jujuy',
            'La Pampa': 'Santa Rosa',
            'La Rioja': 'La Rioja',
            'Mendoza': 'Mendoza',
            'Misiones': 'Posadas',
            'Neuquen': 'Neuquen',
            'Rio Negro': 'Viedma',
            'Salta': 'Salta',
            'San Juan': 'San Juan',
            'San Luis': 'San Luis',
            'Santa Cruz': 'Rio Gallegos',
            'Santa Fe': 'Santa Fe',
            'Santiago del Estero': 'Santiago del Estero',
            'Tierra del Fuego, Antartida e Islas del Atlantico Sur': 'Ushuaia',
            'Tucuman': 'San Miguel de Tucuman'}

# Writing the User interface

print('¿Cuantos examenes queres generar?')
exams_For_Pupil = input()
print(' ')

print('¿Cuantas preguntas por examen?')
answers_Quantity = input()
print(' ')

print('Creado Examen Aleatorio...')

# Program logic

for i in range (int(exams_For_Pupil)):

		# Creating the quiz and answer files
	quiz_Number = quiz_Number + 1
	quiz_File = open('Capitales_Examenes_' + str(quiz_Number) + '.txt' , 'w')
	answer_Key_File = open('Capitales_Examenes_Respuestas_' + str(quiz_Number) + '.txt', 'w')

		# Writing the header for the quizes
	quiz_File.write('''Nombre:\n\nFecha:\n\nPeriodo:\n\n''')
	quiz_File.write((' ' * 20) + 'Examen - Provincias y Capitales: ' + str(quiz_Number))
	quiz_File.write('\n\n')

		# Shuffle the order of the provinces
	provincias = list(capitales.keys())
	random.shuffle(provincias)

	for question_Number in range(int(answers_Quantity)): # Loop between the 23 provinces to make the number of answers
		# Get right and wrong answers
		correct_Answer = capitales[provincias[question_Number]]
		wrong_Answers = list(capitales.values())
		del wrong_Answers[wrong_Answers.index(correct_Answer)]
		wrong_Answers = random.sample(wrong_Answers, 3)
		answer_Options = wrong_Answers + [correct_Answer]
		random.shuffle(answer_Options)

		# Write the question and answers options of the exams
		quiz_File.write('%s. Cual es la capital de %s?\n' % (question_Number + 1, provincias[question_Number]))

		for i in range(4):
			quiz_File.write(' %s. %s\n' % ('ABCD'[i], answer_Options[i]))
		quiz_File.write('\n')

		# Write the answers keys to a file
		answer_Key_File.write('%s. %s\n' % (question_Number + 1, 'ABCD'[answer_Options.index(correct_Answer)]))

	quiz_File.close()
	answer_Key_File.close()

print('Examenes creados con exito')
print(' ')
print('Presiones una tecla para salir')
wait = input()