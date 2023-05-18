# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# ENUNCIADO=Pseudocódigo que nos permita calcular las soluciones de una ecuación de segundo grado, incluyendo los valores imaginarios
	# Definir 
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE A
	v_a = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE B
	v_b = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE C
	v_c = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION R
	v_r = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION I
	v_i = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION X1, PRIMER CORTE CON EL EJER X
	v_x1 = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION X2, SEGUNDO CORTE CON EL EJE X
	v_x2 = float()
	# VALOR INICIAL:
	v_a = 0.0
	v_b = 0.0
	v_c = 0.0
	v_r = 0.0
	v_i = 0.0
	v_x1 = 0.0
	v_x2 = 0.0
	# INTRODUCCION DE DATOS
	print("escribe el coeficiente a")
	v_a = float(input())
	print("escribe el coeficiente b")
	v_b = float(input())
	print("escribe el coeficiente c")
	v_c = float(input())
	# PROCESO Y SALIDA
	# SE DECIDE SI EL VALOR DE A ES DIFERENTE DE CERO
	if v_a!=0:
		# PARA OBTENER LA V_D ENTONCES: (EL VALOR B SE MULTIPLICA POR EL VALOR B) SE RESTA CON 4 Y SE MULTIPLICA POR EL VALOR A Y EL VALOR C
		v_d = (v_b*v_b)-4*v_a*v_c
		# SE DECIDE SI V_D ES DIFERENTE DE CERO
		if v_d!=0:
			# SE DECIDE SI V_D ES MAYOR A CERO
			if v_d>0:
				# PARA OBTENER EL PRIMER CORTE DE X : ((SE LE SACA RAIZ CUADRADA A V_D) SE LE SUMA EL VALOR DE B CON EL SIGNO CONTARIO) SE DIVIDE ENTRE (2 MULTIPLICADO POR EL VALOR DE A)
				v_x1 = (-v_b+sqrt(v_d))/(2*v_a)
				# PARA OBTENER EL SEGUNDO CORTE DE X : ((SE LE SACA RAIZ CUADRADA A V_D) SE LE RESTA EL VALOR DE B CON EL SIGNO CONTARIO) SE DIVIDE ENTRE (2 MULTIPLICADO POR EL VALOR DE A)
				v_x2 = (-v_b-sqrt(v_d))/(2*v_a)
				print("x1=",v_x1)
				print("x2=",v_x2)
				# SI EL VALOR DE V_D ES MENOR A CERO ENTONCES:
			else:
				# PARA OBTENER V_R: (EL VALOR DE B CON SIGNO CONTRARIO) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A)
				v_r = (-v_b)/(2*v_a)
				# PARA OBTENER V_I: (VALOR ABSOLUTO DEL VALOR B) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A) SE LE SACA RAIZ CUADRADA
				v_i = sqrt(abs(v_d))/(2*v_a)
				print(v_r,"+",v_i,"i")
				print(v_r,"-",v_i,"i")
			# SI EL VALOR DE V_D ES IGUAL A CERO ENTONCES:
		else:
			# PARA OBTENER EL PRIMER CORTE X: (VALOR DE B CON EL SIGNO CONTRARIO) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A)
			v_x1 = -v_b/(2*v_a)
			# EL SEGUNDO CORTE ES IGUAL AL PRIMER CORTE
			v_x2 = v_x1
			print("x1=",v_x1)
			print("x2=",v_x2)
	else:
		# SI EL VALOR DE A ES IGUAL A CERO ENTONCES SE COMUNICA QUE NO ES UNA ECUACION DE SEGUNDO GRADO
		print("no es una ecuacion de segundo grado")

