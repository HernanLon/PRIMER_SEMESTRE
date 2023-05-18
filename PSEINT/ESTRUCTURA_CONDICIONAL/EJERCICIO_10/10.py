# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Enunciado: Encontrar el salario a pagar
	# Leer valores de la hora, la cantidad de horas normales de la semana 1, 2, 3 y 4
	# Pedir cada valor por teclado
	# y calcular el salario a pagar
	# dDESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELES
	# vVERSION: 1.0
	# FECHA: 22/02/2023
	# DECLARAR:
	# nombre del empleado
	v_nom = str()
	# valor hora
	v_vh = float()
	# cantidad horas primera semana
	v_hs1 = int()
	# cantidad horas segunda semana
	v_hs2 = int()
	# cantidad horas tercera semana
	v_hs3 = int()
	# cantidad horas cuarta semana
	v_hs4 = int()
	# pago por horas normales de la primera semana
	v_phn1 = float()
	# pago por horas normales de la segunda semana
	v_phn2 = float()
	# pago por horas normales de la tercera semana
	v_phn3 = float()
	# pago por horas normales de la cuarta semana
	v_phn4 = float()
	# cantidad horas extraordinarias primera semana
	v_hes1 = int()
	# cantidad horas extraordinarias segunda semana
	v_hes2 = int()
	# cantidad horas extraordinarias tercera semana
	v_hes3 = int()
	# cantidad horas extraordinarias cuarta semana
	v_hes4 = int()
	# pago por horas extraordinarias de la primera semana
	v_phe1 = float()
	# pago por horas extraordinarias de la segunda semana
	v_phe2 = float()
	# pago por horas extraordinarias de la tercera semana
	v_phe3 = float()
	# pago por horas extraordinarias de la cuarta semana
	v_phe4 = float()
	# pago primera semana
	v_ps1 = float()
	# pago segunda semana
	v_ps2 = float()
	# pago tercera semana
	v_ps3 = float()
	# pago cuarta semana
	v_ps4 = float()
	# salario mensual
	v_sm = float()
	# VALOR INICIAL
	v_nom = ""
	v_vh = 0.0
	v_phn1 = 0.0
	v_phn2 = 0.0
	v_phn3 = 0.0
	v_phn4 = 0.0
	v_phe1 = 0.0
	v_phe2 = 0.0
	v_phe3 = 0.0
	v_phe4 = 0.0
	v_ps1 = 0.0
	v_ps2 = 0.0
	v_ps3 = 0.0
	v_ps4 = 0.0
	v_sm = 0.0
	v_hs1 = 0
	v_hs2 = 0
	v_hs3 = 0
	v_hs4 = 0
	v_hes1 = 0
	v_hes2 = 0
	v_hes3 = 0
	v_hes4 = 0
	# Entrada de datos
	print("Por favor escribir el nombre del empleado")
	v_nom = input()
	print(v_nom)
	print("Por favor introdusca el valor de la hora")
	v_vh = float(input())
	print("El valor de la hora es")
	print(v_vh)
	print("Por favor introduzca la cantidad de horas trabajadas de la primera semana")
	v_hs1 = int(input())
	# Procesos y salidas
	# pago primera semana//
	# SE DECIDE SEGUN SI HORAS DE LA PRIMERA SEMANA SON MAYORES A 40
	if v_hs1>40:
		print("La cantidad de horas trabajadas normales es")
		print("40")
		# SI LAS HORAS DE LA PRIMERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		v_hes1 = v_hs1-40
		print("La cantidad de horas trabajadas extraordinarias es")
		print(v_hes1)
	else:
		print("La cantidad de horas trabajadas normales es")
		# SI LAS HORAS DE LA PRIMERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		print(v_hs1)
		print("La cantidad de horas trabajadas extraordinarias es")
		print(v_hes1)
	# SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
	if v_hes1!=0:
		print("El pago por horas normales en la primera semana es")
		# SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		v_phn1 = v_vh*40
		print(v_phn1)
	else:
		print("El pago por horas normales en la primera semana es")
		# SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA PRIMERA SEMANA
		v_phn1 = v_vh*v_hs1
		print(v_phn1)
	# PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA PRIMERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	v_phe1 = v_hes1*v_vh*(1.5)
	print("El pago por horas extraordinarias en la primera semana es")
	print(v_phe1)
	print("El pago de la primera semana es")
	# PARA OBTENER EL PAGO TOTAL DE LA PRIMERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	v_ps1 = v_phe1+v_phn1
	print(v_ps1)
	# pago segunda semana//
	print("Por favor introduzca la cantidad de horas trabajadas de la segunda semana")
	v_hs2 = int(input())
	# SE DECIDE SEGUN SI HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40
	if v_hs2>40:
		print("La cantidad de horas trabajadas normales en la segunda semana  es")
		print("40")
		# SI LAS HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		v_hes2 = v_hs2-40
		print("La cantidad de horas trabajadas extraordinarias en la segunda semana es")
		print(v_hes2)
	else:
		print("La cantidad de horas trabajadas normales en la segunda semana es")
		# SI LAS HORAS DE LA SEGUNDA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		print(v_hs2)
		print("La cantidad de horas trabajadas extraordinarias en la segunda semana es")
		print(v_hes2)
	# SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
	if v_hes2!=0:
		print("El pago por horas normales en la segunda semana es")
		# SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		v_phn2 = v_vh*40
		print(v_phn2)
	else:
		print("El pago por horas normales en la segunda semana es")
		# SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA SEGUNDA SEMANA
		v_phn2 = v_vh*v_hs2
		print(v_phn2)
	# PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA SEGUNDA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	v_phe2 = v_hes2*v_vh*(1.5)
	print("El pago por horas extraordinarias en la segunda semana es")
	print(v_phe2)
	print("El pago de la segunda semana es")
	# PARA OBTENER EL PAGO TOTAL DE LA SEGUNDA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	v_ps2 = v_phe2+v_phn2
	print(v_ps2)
	# pago tercera semana//
	print("Por favor introduzca la cantidad de horas trabajadas de la tercera semana")
	v_hs3 = int(input())
	# SE DECIDE SEGUN SI HORAS DE LA TERCERA SEMANA SON MAYORES A 40
	if v_hs3>40:
		print("La cantidad de horas trabajadas normales en la tercera semana  es")
		print("40")
		# SI LAS HORAS DE LA TERCERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		v_hes3 = v_hs3-40
		print("La cantidad de horas trabajadas extraordinarias en la tercera semana es")
		print(v_hes3)
	else:
		print("La cantidad de horas trabajadas normales en la tercera semana es")
		# SI LAS HORAS DE LA TERCERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		print(v_hs3)
		print("La cantidad de horas trabajadas extraordinarias en la tercera semana es")
		print(v_hes3)
	# SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
	if v_hes3!=0:
		print("El pago por horas normales en la tercera semana es")
		# SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		v_phn3 = v_vh*40
		print(v_phn3)
	else:
		print("El pago por horas normales en la tercera semana es")
		# SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA TERCERA SEMANA
		v_phn3 = v_vh*v_hs3
		print(v_phn3)
	# PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA TERCERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	v_phe3 = v_hes3*v_vh*(1.5)
	print("El pago por horas extraordinarias en la tercera semana es")
	print(v_phe3)
	print("El pago de la tercera semana es")
	# PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	v_ps3 = v_phe3+v_phn3
	print(v_ps3)
	# pago cuarta semana//
	print("Por favor introduzca la cantidad de horas trabajadas de la cuarta semana")
	v_hs4 = int(input())
	# SE DECIDE SEGUN SI HORAS DE LA CUARTA SEMANA SON MAYORES A 40
	if v_hs4>40:
		print("La cantidad de horas trabajadas normales en la cuarta semana  es")
		print("40")
		# SI LAS HORAS DE LA CUARTA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		v_hes4 = v_hs4-40
		print("La cantidad de horas trabajadas extraordinarias en la cuarta semana es")
		print(v_hes4)
	else:
		print("La cantidad de horas trabajadas normales en la cuarta semana es")
		# SI LAS HORAS DE LA CUARTA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		print(v_hs4)
		print("La cantidad de horas trabajadas extraordinarias en la cuarta semana es")
		print(v_hes4)
	# SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
	if v_hes4!=0:
		print("El pago por horas normales en la cuarta semana es")
		# SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		v_phn4 = v_vh*40
		print(v_phn4)
	else:
		print("El pago por horas normales en la cuarta semana es")
		# SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA CUARTA SEMANA
		v_phn4 = v_vh*v_hs4
		print(v_phn4)
	# PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA CUARTA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	v_phe4 = v_hes4*v_vh*(1.5)
	print("El pago por horas extraordinarias en la cuarta semana es")
	print(v_phe4)
	print("El pago de la tercera semana es")
	# PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	v_ps4 = v_phe4+v_phn4
	print(v_ps4)
	# pago total del mes
	print("El salario mensual es")
	# PARA OBTENER EL PAGO TOTAL DEL MES: SE SUMAN LOS PAGOS TOTALES DE LAS CUATRO SEMANAS
	v_sm = v_ps1+v_ps2+v_ps3+v_ps4
	print(v_sm)

