# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO= 5.  Pag. 143.  EJEMPLO 4.13 Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy.
	# DESARROLLADO POR: Hernan Alberto Londoño Velez
	# FECHA: 03/03/2023
	# VERSION: 1.0
	# Definir 
	# VARIABLE QUE ALMACENA LA LETRA INICIAL DE LA SEMANA DEL PRIMER DIA DEL MES.
	v_dia1 = str()
	# VARIABLE QUE ALMACENA EL VALOR DEL PRIMER DIA DEL MES.
	v_d1 = int()
	# VARIABLE QUE ALMACENA EL DIA DEL MES.
	v_dia = int()
	# VARIABLE QUE ALMACENA UN RESULADO DE UNA ECUACION ARITMETICA.
	v_diasem = int()
	# VALOR INICIAL:
	v_dia1 = ""
	v_d1 = 0
	v_dia = 0
	v_diasem = 0
	# ENTRADA DE DATOS
	print("el dia 1 fue (L,M,X,J,V,S,D) por favor escriba la letra en mayuscula")
	v_dia1 = input()
	# PROCESO Y SALIDA
	# SE DECIDE SEGUN CUAL ES EL PRIMER DIA DEL MES 
	if v_dia1=="L":
		# SI EL PRIMER DIA DEL MES ES LUNES ENTONCES ES 0
		v_d1 = 0
	elif v_dia1=="M":
		# SI EL PRIMER DIA DEL MES ES MARTES ENTONCES ES 1
		v_d1 = 1
	elif v_dia1=="X":
		# SI EL PRIMER DIA DEL MES ES MIERCOLES ENTONCES ES 2
		v_d1 = 2
	elif v_dia1=="J":
		# SI EL PRIMER DIA DEL MES ES JUEVES ENTONCES ES 3
		d1 = 3
	elif v_dia1=="V":
		# SI EL PRIMER DIA DEL MES ES VIERNES ENTONCES ES 4
		v_d1 = 4
	elif v_dia1=="S":
		# SI EL PRIMER DIA DEL MES ES SABADO ENTONCES ES 5
		v_d1 = 5
	elif v_dia1=="D":
		# SI EL PRIMER DIA DEL MES ES DOMINGO ENTONCES ES 6
		v_d1 = 6
	else:
		# SI ES OTRA OPCION ENTONCES NO SERIA UNA RESPUESTA CORRESTA
		v_d1 = -40
	print("escriba el numero del dia")
	v_dia = int(input())
	# PARA OBTENER EL DIA DE LA SEMANA ENTONCES: SUMO EL DIA DEL MES CON EL NUMERO DE LA SEMANA DEL PRIMER DIA DEL MES
	v_diasem = v_dia+v_d1
	# SE DECIDE SI DIA ES MAYOR A 7
	if v_diasem>7:
		# SI V_DIASEM ES MAYOR A 7 ENTONCES:SE REALIZA EL SIGUIENTE PROCESO
		while True:# no hay 'repetir' en python
			# PARA OBTENER EL NUEVO VALOR DE V_DIASEM: SE RESTA DIA CON 7
			v_diasem = v_diasem-7
			# SE TERMINA EL PROCESO CUANDO V_DIASEM SEA MENOR O IGUAL A 7
			if v_diasem<=7: break
	# SALIDA
	# SE DECIDE SEGUN SI V_DIASEM ES IAGUAL A UN NUMERO DEL 1 AL 7
	if v_diasem==1:
		# SI V_DIASEM ES IGUAL A 1 ENTONCES: ES LUNES
		print("Ese dia es un lunes")
	elif v_diasem==2:
		# SI V_DIASEM ES IGUAL A 2 ENTONCES: ES MARTES
		print("Ese dia es un martes")
	elif v_diasem==3:
		# SI V_DIASEM ES IGUAL A 3 ENTONCES: ES MIERCOLES
		print("Ese dia es un miercoles")
	elif v_diasem==4:
		# SI V_DIASEM ES IGUAL A 4 ENTONCES: ES JUEVES
		print("Ese dia es un jueves")
	elif v_diasem==5:
		# SI V_DIASEM ES IGUAL A 5 ENTONCES: ES VIERNES
		print("Ese dia es un viernes")
	elif v_diasem==6:
		# SI V_DIASEM ES IGIAL A 6 ENTONCES: ES SABADO
		print("Ese dia es un sabado")
	elif v_diasem==7:
		# SI V_DIASEM ES IGUAL A 7 ENTONCES: ES DOMINGO
		print("Ese dia es un domingo")

