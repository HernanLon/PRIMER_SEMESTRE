# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos
	# HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA: 26/02/2023
	# VERSION=1.1
	# DEFINICION
	# VARIABLE QUE ALMACENA EL PRIMER NUMERO
	v_a = float()
	# VARIABLE QUE ALMACENA EL SEGUNDO NUMERO
	v_b = float()
	# VARIABLE QUE ALMACENA EL TERCER NUMERO
	v_c = float()
	# VALOR INICIAL:
	v_a = 0.0
	v_b = 0.0
	v_c = 0.0
	# INICIO
	# ENTRADA DE DATOS
	print("escriba numero 1")
	v_a = float(input())
	print("escriba numero 2")
	v_b = float(input())
	print("escriba numero 3")
	v_c = float(input())
	# PROCESO
	# SALIDA
	# SE DECIDE SEGUN SI EL PRIMER NUMERO ES MENOR AL SEGUNDO NUMERO PARA DECIDIR CUAL ES EL MAOR
	if v_a<v_b:
		# SE DECIDE SEGUN SI EL SEGUNDO NUMERO ES MENOR AL TRECER NUMERO PARA DECIDIR CUAL ES EL MAOR
		if v_b<v_c:
			# EL TERCER NUMERO ES EL MAYOR
			print("C=",v_c)
		else:
			# EL SEGUNDO NUMERO ES EL MAYOR
			print("B=",v_b)
	else:
		# SE DECIDE SEGUN SI EL PRIMER NUMERO ES MENOR AL TERCER NUMERO PARA DECIDIR CUAL ES EL MAOR
		if v_a<v_c:
			# EL TERCER NUMERO ES EL MAYOR
			print("C=",v_c)
		else:
			# EL PRIMER NUMERO ES EL MAYOR
			print("A=",v_a)
	# FIN

