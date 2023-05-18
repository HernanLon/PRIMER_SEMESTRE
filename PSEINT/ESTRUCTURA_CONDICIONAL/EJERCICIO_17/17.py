# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=
	# Se desea obtener la nómina semanal ?salario neto? de los empleados de una empresa cuyo trabajo se paga por 
	# horas y del modo siguiente:
	# las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa determinada que se debe introducir 
	# por teclado al igual que el número de horas y el nombre del trabajador,
	# las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas normales,
	# los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
	# sueldo <= 2.000, libre de impuestos,
	# las siguientes 220 euros al 20 por 100,
	# el resto, al 30 por 100.
	# CREADO POR= Hernan Alberto Londoño Velez
	# FECHA: 03/03/2023
	# VERSION: 1.0
	# DEFINICION=
	# VARIABLE QUE ALMACENA EL NOMBRE DEL TRABAJADOR
	v_nombre = str()
	# VARIABLE QUE ALMACENA EL NUMERO DE HORAS
	v_horas = int()
	# VARIABLE QUE ALMACENA EL VALOR DE LOS IMPUESTOS
	v_impuestos = float()
	# VARIABLE QUE ALMACENA EL VALOS DE SALARIO BRUTO
	v_sbruto = float()
	# VARIABLE QUE ALMACENA EL VALOS DE SALARIO NETO
	v_sneto = float()
	# VARIABLE QUE ALMACENA EL VALOR DE LA HORA DE TRABAJO
	v_tarifa = int()
	# VALOR INICIAL:
	v_nombre = ""
	v_horas = 0
	v_impuestos = 0.0
	v_sbruto = 0.0
	v_sneto = 0.0
	v_tarifa = 0
	# INICIO
	print("escriba el nombre del empleado")
	v_nombre = input()
	print("escriba la cantidad de horas trabajadas")
	v_horas = int(input())
	print("escribor el valor de la hora de trabajo")
	v_tarifa = int(input())
	# PROCESO
	# SE DECIDE SI EL NUMERO DE HORAS ES MENOR O IGUAL A 35
	if v_horas<=35:
		# SI ES MENOR O IGUAL A 35: LA CANTIDAD DE HORAS SE MULTIPLICA POR EL VALOR DE LA TARIFA PARA OBTENER EL SALARIO BRUTO
		v_sbruto = v_horas*v_tarifa
	else:
		# SI ES MAYOR A 35: ((SE RESTA LA CANTIDAD DE HORAS CON 35) SE MULTIPLICA POR 1.5 Y POR EL VALOR DE LA TARIFA) Y SE SUMA COMO (35 MULTIPLICADO POR EL VALOR DE LA TARIFA)
		v_sbruto = 35*v_tarifa+((v_horas-35)*1.5*v_tarifa)
	# SE DECIDE SI EL SALARIO BRUTO ES MENOR O IGUAL A 2000
	if v_sbruto<=2000:
		# SI SALARIO BRUTO ES MENOR O IGUAL A 2000: NO HAY IMPUESTOS
		v_impuestos = 0
		# SI SALARIO BRUTO ES MAYOR A 2000 ENTONCES:
	else:
		# SE DECIDE SI SALARIO BRUTO ES MAYOR A 2000 Y MENOR O IGUAL A 2220
		if (v_sbruto>2000) and (v_sbruto<=2220):
			# SI LA CONDICION SE CUMPLE ENTONCES: PARA OBTENER EL VALOR LOS IMPUESTOS SE (RESTA EL SALARIO BRUTO CON 2000) Y SE MULTIPLICA POR 0.2 (20% = 0.2)
			v_impuestos = (v_sbruto-2000)*0.2
			# SI LA CONDICION NO SE CUMPLE ENTONCES:
		else:
			# PARA OBTENER EL VALOR DE LOS IMPUESTOS: ((SE RESTA EL SALARIO BRUTO CON 2220)SE MULTIPLICA POR 0.3) Y SE SUMA CON EL RESULADO DE (220 MULTIPLICADO POR 0.2)
			v_impuestos = (220*0.2)+((v_sbruto-2220)*0.3)
	# PARA OBTENER EL VALOR DEL SALARIO NETO: SE RESTA EL SALARIO BRUTO CON LOS IMPUESTOS
	v_sneto = v_sbruto-v_impuestos
	# SALIDA
	print("Nombre reabajador=")
	print(v_nombre)
	print("El salario bruto es=")
	print(v_sbruto)
	print("El valor de los impuestos es=")
	print(v_impuestos)
	print("El salario neto es=")
	print(v_sneto)
	# FIN

