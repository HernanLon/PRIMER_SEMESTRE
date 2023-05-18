# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Resolución de una ecuación de primer grado.
	# FECHA:03/03/2023
	# VERSION= 1.0
	# CREADO POR: Hernan Alberto Londoño Velez
	# DEFINIR VARIABLES=
	# VARIABLE QUE ALMACENA EL VALOR DE A
	v_a = float()
	# VARIABLE QUE ALMACENA EL VALOR DE B
	v_b = float()
	# VARIABLE QUE ALMACENA UN RESULTADO DE UNA OPERACION 
	v_x = float()
	# VALOR INICIAL
	v_a = 0
	v_b = 0
	v_x = 0
	# INICIO=
	print("escriba (a) de la ecuacion ax+b=0")
	v_a = float(input())
	print("escriba (b) de la ecuacion ax+b=0")
	v_b = float(input())
	# PROCESO
	# SALIDA
	# SE DECIDE SI EL VALOR DE A ES DIFERENTE DE CERO
	if v_a!=0:
		# SI EL VALOR A ES DIFERENTE DE CERO: EL VALOR B SE DIVIDE ENTRE EL VALOR A
		v_x = -v_b/v_a
		print("X es=",v_x)
	else:
		# SE DECIDE SI EL VALOR B ES DIFERENTE DE CERO
		if b!=0:
			# SI EL VALOR B ES DIFERENTE DE CERO ENTONCES LA SOLUCION ES IMPOSIBLE
			print("Solucion imposible")
		else:
			# SI EL VALOR DE B ES IGUAL A CERO ENTONCES LA SOLUCION ES INDETERMINADA
			print("Solucion indeterminada")
	# FIN

