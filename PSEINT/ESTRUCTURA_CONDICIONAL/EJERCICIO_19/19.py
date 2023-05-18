# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO= 4.  Pag. 142. EJEMPLO 4.12  Leída una fecha, decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes.
	# CREADO POR: Hernan Alberto Londoño Velez
	# FECHA: 03/03/2023
	# VERSION: 1.0
	# Definir 
	# VARIABLE QUE ALAMACENA EL VALOR DE DIA.
	v_dia = int()
	# VALOR INICIAL:
	v_dia = 0
	# INTRODUCCION DE DATOS
	print("escribe el numero del dia")
	v_dia = int(input())
	# PROCESO
	# SE DECIDE SI DIA ES MAYOR A 7
	if v_dia>7:
		# SI DIA ES MAYOR A 7 ENTONCES:SE REALIZA EL SIGUIENTE PROCESO
		while True:# no hay 'repetir' en python
			# PARA OBTENER EL NUEVO VALOR DE DIA: SE RESTA DIA CON 7
			v_dia = v_dia-7
			# SE TERMINA EL PROCESO CUANDO DIA SEA MENOR O IGUAL A 7
			if v_dia<=7: break
	# SALIDA
	# SE DECIDE SEGUN SI DIA ES IAGUAL A UN NUMERO DEL 1 AL 7
	if v_dia==1:
		# SI DIA ES IGUAL A 1 ENTONCES: ES LUNES
		print("Ese dia fue un lunes")
	elif v_dia==2:
		# SI DIA ES IGUAL A 2 ENTONCES: ES MARTES
		print("Ese dia fue un martes")
	elif v_dia==3:
		# SI DIA ES IGUAL A 3 ENTONCES: ES MIERCOLES
		print("Ese dia fue un miercoles")
	elif v_dia==4:
		# SI DIA ES IGUAL A 4 ENTONCES: ES JUEVES
		print("Ese dia fue un jueves")
	elif v_dia==5:
		# SI DIA ES IGUAL A 5 ENTONCES: ES VIERNES
		print("Ese dia fue un viernes")
	elif v_dia==6:
		# SI DIA ES IGIAL A 6 ENTONCES: ES SABADO
		print("Ese dia fue un sabado")
	elif v_dia==7:
		# SI DIA ES IGUAL A 7 ENTONCES: ES DOMINGO
		print("Ese dia fue un domingo")

