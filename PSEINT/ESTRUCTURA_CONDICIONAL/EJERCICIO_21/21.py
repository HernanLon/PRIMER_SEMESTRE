# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=6.  Pag 146.  EJEMPLO 4.15 Diseñar un programa que lea tres números A, B, C y visualice en pantalla el valor del más grande. 
	# Se supone que los tres valores son diferentes.
	# HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA:03/03/2023
	# VERSION: 1.0
	# Definir 
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE A
	v_a = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE B
	v_b = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE C
	v_c = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION
	v_mayor = float()
	# VALOR INICIAL:
	v_a = 0.0
	v_b = 0.0
	v_c = 0.0
	v_mayor = 0.0
	# INTRODUCCION DE INFORMACION
	print("escribir el primer numero")
	v_a = float(input())
	print("escribe el segundo numero")
	v_b = float(input())
	print("escribe el tercer numero")
	v_c = float(input())
	# PROCESO Y SALIDA
	# SE DECIDE SI EL VALOR DE A ES MAYOR QUE EL VALOR DE B PARA OBTENER EL NUMERO MAYOR
	if v_a>v_b:
		# SE DECIDE SI EL VALOR DE A ES MAYOR QUE EL VALOR DE C PARA OBTENER EL NUMERO MAYOR
		if v_a>v_c:
			# EL NUMERO MAYOR ES EL VALOR DE A
			v_mayor = v_a
		else:
			# EL NUMERO MAYOR ES EL VALOR DE C
			v_mayor = v_c
	else:
		# SE DECIDE SI EL VALOR DE B ES MAYOR QUE LE VALOR DE C PARA OBTENER EL NUMERO MAYOR
		if v_b>v_c:
			# EL NUMERO MAYOR ES EL VALOR DE B
			v_mayor = v_b
		else:
			# EL NUMERO MAYOR ES EL VALOR DE C
			v_mayor = v_c
	print("el numero mayor es=",v_mayor)

