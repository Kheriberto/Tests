""" Program used to display the results for some personality tests.
It does not include the questions for the tests, in only requires the input
of the answersa and then it shows the results"""

# Variables

on = True
rList = []
test = ""
show = False

# print('not loop') # <------ Loop Test
# Funciones
def q_list(number):
	list = []
	for i in range(number):
		list.append("Pregunta " + str(i + 1))
	return list
def invert(x):
	invX = []
	chng = 0
	for i in x:
		if i == 5:
			chng += 1
		elif i == 4:
			chng += 2
		elif i == 2:
			chng += 4
		else:
			chng += i
	return chng

print(
	"""
			¡Bienvenido(a)! Gracias por usar 
			este programa.
	""")

while on == True:
	# print ('in loop') # <------ Loop Test

	if test != "x":

		launch = input(
			"""			
			¿Quiere registrar resultados de una prueba?: 
			(responde s- si / n- no)
			""")

	if launch == "n" and len(rList) > 0 and show == True:
		res_ = input("""
			¿Desea ver los resultados de las pruebas registradas?:
			(responde s- si / n- no)
			""")
		if res_ == 's' and len(rList) > 0:
			rList = list(dict.fromkeys(rList))
			for i in rList:

# MARCADOR --- Código de la prueba c (Control)
				if i == "c":
					a_c = 0
					b_c = 0
					lsA = ['Pregunta 2', 
					'Pregunta 3',
					'Pregunta 6',
					'Pregunta 7',
					'Pregunta 8',
					'Pregunta 10']
					lsB = ['Pregunta 1',
					'Pregunta 4',
					'Pregunta 5',
					'Pregunta 9']
					for keys in dic_c.keys():
						if keys in lsA and dic_c[keys].upper() == "A":
							a_c += 1
						elif keys in lsB and dic_c[keys].upper() == "B":
							b_c += 1
					ttl_c = a_c + b_c
					if ttl_c >= 8 and ttl_c <= 10:
						sent_c = "alto sitio interno"
					elif ttl_c >= 6 and ttl_c <= 7:
						sent_c = "moderado sitio interno"
					elif ttl_c == 5:
						sent_c = "sitio mixto"
					elif ttl_c >= 3 and ttl_c <= 4:
						sent_c = "moderado sitio externo"
					elif ttl_c >= 1 and ttl_c <= 2:
						sent_c = "alto sitio externo"
					print(
"""			--------------------------------------------
			TEST DE SITIO DE CONTROL
			El resultado de la prueba de control es: %i.
			El sujeto tiene un %s de control.
			El máximo puntaje posible es 10.
			""" % (ttl_c, sent_c))

# MARCADOR --- Código de la prueba m (Maquiavelismo)
				elif i == 'm':
					a_m = 0
					b_m = 0
					ls_mBR = []
					ls_mA = ['Pregunta 1', 
					'Pregunta 3',
					'Pregunta 4',
					'Pregunta 5',
					'Pregunta 9',
					'Pregunta 10']
					ls_mB = ['Pregunta 2',
					'Pregunta 6',
					'Pregunta 7',
					'Pregunta 8']
					for keys in dic_m.keys():
						if keys in ls_mA:
							a_m += dic_m[keys]
						elif keys in ls_mB:
							ls_mBR.append(dic_m[keys])
					b_m = invert(ls_mBR)
					ttl_m = a_m + b_m
					if ttl_m == 25:
						sent_m = "igual al"
					elif ttl_m < 25:
						sent_m = "por debajo del"
					elif ttl_m > 25:
						sent_m = "por arriba del"
					print(
"""			--------------------------------------------
			TEST DE MAQUIAVELISMO
			El resultado de la prueba de maquiavelismo es: %i.
			El sujeto presenta un maquiavelismo %s promedio.
			El máximo puntaje posible es 50.
			""" % (ttl_m, sent_m))
# MARCADOR --- Código de la prueba a (Autoestima)
				elif i == 'a':
					a_a = 0
					b_a = 0
					ls_aBR = []
					ls_aA = ['Pregunta 1', 
					'Pregunta 2',
					'Pregunta 6',
					'Pregunta 8',
					'Pregunta 9',
					'Pregunta 10',
					'Pregunta 15',
					'Pregunta 16',
					'Pregunta 17',
					'Pregunta 18']
					ls_aB = ['Pregunta 3',
					'Pregunta 4',
					'Pregunta 5',
					'Pregunta 7',
					'Pregunta 11',
					'Pregunta 12',
					'Pregunta 13',
					'Pregunta 14',
					'Pregunta 19',
					'Pregunta 20',]
					for keys in dic_a.keys():
						if keys in ls_aA:
							a_a += dic_a[keys]
						elif keys in ls_aB:
							ls_aBR.append(dic_a[keys])
					b_a = invert(ls_aBR)
					ttl_a = a_a + b_a
					print(
"""			--------------------------------------------
			TEST AUTOESTIMA
			El resultado de la prueba de autoestima es: %i.
			Mientras más alto el número, mayor autoestima. 
			El valor máximo es 100.
			""" % (ttl_a))

# MARCADOR --- Código de la prueba a (Autocontrol)
				elif i == 'au':
					a_au = 0
					b_au = 0
					ls_auBR = []
					ls_auA = ['Pregunta 1',
					'Pregunta 2',
					'Pregunta 3',
					'Pregunta 4',
					'Pregunta 5',
					'Pregunta 6',
					'Pregunta 7',
					'Pregunta 8',
					'Pregunta 10',
					'Pregunta 11',
					'Pregunta 13']
					ls_auB = ['Pregunta 9',
					'Pregunta 12']
					for keys in dic_au.keys():
						if keys in ls_auA:
							a_au += dic_au[keys]
						elif keys in ls_auB:
							ls_auBR.append(dic_au[keys])
					b_au = invert(ls_auBR)
					ttl_au = a_au + b_au
					print(
"""			--------------------------------------------
			TEST AUTOCONTROL
			El resultado de la prueba de autocontrol es: %i.
			Se considera que una persona tiene autocontrol 
			cuando su calificación es mayor o igual a 53.
			La calificación máxima es de 65.
			""" % (ttl_au))

# MARCADOR --- Código de la prueba r (Toma de Riesgos)
				elif i == 'r':
					a_r = 0
					for values in dic_r.values():
						if values != 0:
							a_r += values
						elif values == 0:
							a_r += 10
					ttl_r = a_r / 4
					print(
"""			--------------------------------------------
			TEST DE TOMA DE RIESGOS
			El resultado de la prueba de toma de riesgos es: %.2f.
			Mientras menor sea el resultado, el sujeto tiene una 
			tendencia a tomar más riesgos.
			El resultado máximo es 10.
			""" % (ttl_r))

# MARCADOR --- Código de la prueba ab (Peronalidad A/B)
				elif i == 'ab':
					a_ab = 0
					for values in dic_ab.values():
							a_ab += values
					ttl_ab = a_ab * 3
					if ttl_ab >= 120:
						sent_ab = "tipo A+"
					elif ttl_ab in range(106,120):
						sent_ab = "tipo A"
					elif ttl_ab in range(100,106):
						sent_ab = "tipo A-"
					elif ttl_ab in range(90,100):
						sent_ab = "tipo B+"
					elif ttl_ab < 90:
						sent_ab = "tipo B"
					print(
"""			--------------------------------------------
			TEST DE PERSONALIDAD A/B
			El resultado de la prueba de personalidad A/B es: %i.
			De acuerdo con los resultados, el sujeto tiene una
			personalidad %s.
			""" % (ttl_ab, sent_ab))

				elif i == 'x' and len(rList) == 0:
					print(
"""			No se registró respuestas de ninguna prueba.""")
					exit()

				test = ""
				show = False

		elif res_ == 'n':
			print("""
			¡Gracias por usar el programa!""")
			exit()

	elif launch	== 'n':
		if len(rList) == 0:
			print("""
			No se registró respuestas de ninguna prueba.""")
		elif show == False:
			print("""
			¡Gracias por usar el programa!""")
		exit()

	elif launch != "n" and launch != "s":
		print("""
			Has seleccionado una respuesta equivocada.
			Por favor elige una respuesta válida:
			""")

		continue

	elif launch == "s":
		test = input("""
			¿Qué prueba vas a realizar?
			Escribe: 
			(c) - Sitio de Control
			(m) - Maquiavelismo
			(a) - Autoestima
			(au) - Autocontrol
			(r) - Riesgo
			(ab) - Prueba de personalidad A/B

			(x) - Salir
		   
			(solo puedes registrar datos de
			 una prueba a la vez)
		   
			** Presiona ENTER

			Prueba: """)

		on1 = True

		while on1 == True:
			rList.append(test)
			if test == "c":
				print(
			"""			
			TEST DE SITIO DE CONTROL:
			Las respuestas deben ser la letra 'a' o 'b'.
			""")
				keys = q_list(10)
				dic_c = {}
				for i in keys:
					dic_c[i] = input(
			"""				Respuesta de la %s: """ % (i))
					# print(dic_c) # <----- Test
				on1 = False
				show = True
				break
			if test == "m":
				print(
			"""			
			TEST DE MAQUIAVELISMO:
			Las respuestas deben estar en un rango del 1 - 5.
			""")
				keys = q_list(10)
				dic_m = {}
				for i in keys:
					dic_m[i] = int(input(
			"""				Respuesta de la %s: """ % (i)))
				on1 = False
				show = True
				break
			if test == "a":
				print(
			"""			
			TEST DE AUTOESTIMA:
			Las respuestas deben estar en un rango del 1 - 5.
			""")
				keys = q_list(20)
				dic_a = {}
				for i in keys:
					dic_a[i] = int(input(
			"""				Respuesta de la %s: """ % (i)))
				on1 = False
				show = True
				break
			if test == "au":
				print(
			"""			
			TEST DE AUTOCONTROL:
			Las respuestas deben estar en un rango del 0 - 5.
			""")
				keys = q_list(13)
				dic_au = {}
				for i in keys:
					dic_au[i] = int(input(
			"""				Respuesta de la %s: """ % (i)))
				on1 = False
				show = True
				break
			if test == "r":
				print(
			"""			
			TEST DE TOMA DE RIESGOS:
			Las respuestas deben ser: 0, 1, 3, 5, 7 y 9.
			""")
				keys = [1,2,3,4]
				dic_r = {}
				for i in keys:
					dic_r[i] = int(input(
			"""				Respuesta del caso %s: """ % (i)))
				on1 = False
				show = True
				break
			if test == "ab":
				print(
			"""			
			TEST DE PERSONALIDAD A/B:
			Las respuestas deben estar en un rango del 1 - 8.
			""")
				keys = q_list(7)
				dic_ab = {}
				for i in keys:
					dic_ab[i] = int(input(
			"""				Respuesta de la %s: """ % (i)))
				on1 = False
				show = True
				break

			if test == "x":
				if len(rList) == 1:
					print(
	"""			No se registró respuestas de ninguna prueba.""")
					exit()
				else:
					launch = 'n'
				on1 = False
				show = False
				break
			continue