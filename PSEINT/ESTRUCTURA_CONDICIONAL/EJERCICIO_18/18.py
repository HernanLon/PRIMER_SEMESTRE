# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# ENUNCIADO=Pag. 137. EJEMPLOS 4.8 Programa que nos calcule el área de un triángulo conociendo sus lados. La estructura selectiva se utiliza para el
	# control de la entrada de datos en el programa.
	# DESARROLLADO POR: Hernan Alberto Londoño Velez
	# FECHA: 03/03/2023
	# DEFINICION
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE A.
	v_a = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE B.
	v_b = float()
	# VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE C.
	v_c = float()
	# VARIABLE QUE ALMACENA UN RESULTADO DE UNA OPERACIÓN ARITMETICA.
	v_p = float()
	# VARIABLE QUE ALMACENA UN RESULTADO DE UNA OPERACION ARITMETICA.
	v_area = float()
	# VALOR INICIAL:
	v_a = 0.0
	v_b = 0.0
	v_c = 0.0
	v_p = 0.0
	v_area = 0.0
	# ENTRADA DE DATOS
	print("escribe el lado ,a, del triangulo")
	v_a = float(input())
	print("escribe el lado ,b, del triangulo")
	v_b = float(input())
	print("escribe el lado ,c, del triangulo")
	v_c = float(input())
	# PROCEOS
	# SALIDA
	# PARA OBTENER LA V_P: SE SUMAN LOS TRES VALORES INTRODUCIDOS Y SE DIVIDEN ENTRE 2
	v_p = (v_a+v_b+v_c)/2
	# SE DECIDE SI V_P ES MAYOR A LOS TRES VALORES INTRODUCIDOS
	if (v_p>v_a) and (v_p>v_b) and (v_p>v_c):
		# SI V_P ES MAYOR ENTONCES: AREA SE OBTIENE: (SE RESTA V_P CON VALOR A) SE MULTIPLICA CON (RESTA DE V_P CON VALOR B) SE MULTIPLICA CON (RESTA DE V_P CON VALOR C)  EL RESULTADO DE LO ANTEROR SE MULTIPLICA POR V_P Y SE LE SACA RAIZ CUADRADA
		v_area = sqrt(v_p*(v_p-v_a)*(v_p-v_b)*(v_p-v_c))
		print("el area del triangulo es=",v_area)
	else:
		# SI V_P NO ES MAYOR ENTONCES: SE COMINICA QUE NO ES UN TRIANGULO
		print("no es un triangulo")

