Algoritmo Salario
	//Enunciado: Encontrar el salario a pagar
	//Leer valores de la hora, la cantidad de horas normales de la semana 1, 2, 3 y 4
	//Pedir cada valor por teclado
	// y calcular el salario a pagar
	//dDESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELES
	//vVERSION: 1.0
	//FECHA: 22/02/2023
	
	//DECLARAR:
	Definir v_nom Como Caracter //nombre del empleado
	Definir v_vh Como Real //valor hora
	Definir v_hs1 Como Entero //cantidad horas primera semana
	Definir v_hs2 Como Entero //cantidad horas segunda semana
	Definir v_hs3 Como Entero //cantidad horas tercera semana
	Definir v_hs4 Como Entero //cantidad horas cuarta semana
	Definir v_phn1 Como Real //pago por horas normales de la primera semana
	Definir v_phn2 Como Real //pago por horas normales de la segunda semana
	Definir v_phn3 Como Real //pago por horas normales de la tercera semana
	Definir v_phn4 Como Real //pago por horas normales de la cuarta semana
	Definir v_hes1 Como Entero //cantidad horas extraordinarias primera semana
	Definir v_hes2 Como Entero //cantidad horas extraordinarias segunda semana
	Definir v_hes3 Como Entero //cantidad horas extraordinarias tercera semana
	Definir v_hes4 Como Entero //cantidad horas extraordinarias cuarta semana
	Definir v_phe1 Como Real //pago por horas extraordinarias de la primera semana
	Definir v_phe2 Como Real //pago por horas extraordinarias de la segunda semana
	Definir v_phe3 Como Real //pago por horas extraordinarias de la tercera semana
	Definir v_phe4 Como Real //pago por horas extraordinarias de la cuarta semana
	Definir v_ps1 Como Real //pago primera semana
	Definir v_ps2 Como Real //pago segunda semana
	Definir v_ps3 Como Real //pago tercera semana
	Definir v_ps4 Como Real //pago cuarta semana
	Definir v_sm Como Real //salario mensual
	
	
	//VALOR INICIAL
	v_nom=""
	v_vh=0.0
	v_phn1=0.0
	v_phn2=0.0
	v_phn3=0.0
	v_phn4=0.0
	v_phe1=0.0
	v_phe2=0.0
	v_phe3=0.0
	v_phe4=0.0
	v_ps1=0.0
	v_ps2=0.0
	v_ps3=0.0
	v_ps4=0.0
	v_sm=0.0
	v_hs1=0
	v_hs2=0
	v_hs3=0
	v_hs4=0
	v_hes1=0
	v_hes2=0
	v_hes3=0
	v_hes4=0
	
	//Entrada de datos
	Escribir "Por favor escribir el nombre del empleado"
	leer v_nom
	Escribir v_nom
	Escribir "Por favor introdusca el valor de la hora"
	Leer v_vh
	Escribir "El valor de la hora es"
	Escribir v_vh
	Escribir "Por favor introduzca la cantidad de horas trabajadas de la primera semana"
	Leer v_hs1
	
	//Procesos y salidas
	//pago primera semana//
	Si v_hs1 > 40 Entonces //SE DECIDE SEGUN SI HORAS DE LA PRIMERA SEMANA SON MAYORES A 40
		Escribir "La cantidad de horas trabajadas normales es"
		Escribir "40"
		v_hes1= v_hs1 - 40 //SI LAS HORAS DE LA PRIMERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias es"
		Escribir v_hes1
	SiNo
		Escribir "La cantidad de horas trabajadas normales es"
		Escribir v_hs1 //SI LAS HORAS DE LA PRIMERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias es"
		Escribir v_hes1
	Fin Si
	
	Si v_hes1 <> 0 Entonces; //SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		Escribir "El pago por horas normales en la primera semana es"
		v_phn1 = v_vh * 40 //SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		Escribir v_phn1
	SiNo
		Escribir "El pago por horas normales en la primera semana es"
		v_phn1 = v_vh * v_hs1 //SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA PRIMERA SEMANA
		Escribir v_phn1
	Fin Si;
	
	v_phe1 = v_hes1 * v_vh * (1.5) //PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA PRIMERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	Escribir "El pago por horas extraordinarias en la primera semana es"
	Escribir v_phe1
	Escribir "El pago de la primera semana es"
	v_ps1= v_phe1 + v_phn1 //PARA OBTENER EL PAGO TOTAL DE LA PRIMERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	Escribir v_ps1
	
	//pago segunda semana//
	Escribir "Por favor introduzca la cantidad de horas trabajadas de la segunda semana"
	Leer v_hs2
	Si v_hs2 > 40 Entonces //SE DECIDE SEGUN SI HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40
		Escribir "La cantidad de horas trabajadas normales en la segunda semana  es"
		Escribir "40"
		v_hes2= v_hs2 - 40 //SI LAS HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la segunda semana es"
		Escribir v_hes2
	SiNo
		Escribir "La cantidad de horas trabajadas normales en la segunda semana es"
		Escribir v_hs2 //SI LAS HORAS DE LA SEGUNDA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la segunda semana es"
		Escribir v_hes2
	Fin Si;
	Si v_hes2 <> 0 Entonces //SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		Escribir "El pago por horas normales en la segunda semana es"
		v_phn2 = v_vh * 40 //SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		Escribir v_phn2
	SiNo
		Escribir "El pago por horas normales en la segunda semana es"
		v_phn2 = v_vh * v_hs2 //SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA SEGUNDA SEMANA
		Escribir v_phn2
	Fin Si
	v_phe2 = v_hes2 * v_vh * (1.5) //PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA SEGUNDA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	Escribir "El pago por horas extraordinarias en la segunda semana es"
	Escribir v_phe2
	Escribir "El pago de la segunda semana es"
	v_ps2= v_phe2 + v_phn2 //PARA OBTENER EL PAGO TOTAL DE LA SEGUNDA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	Escribir v_ps2
	
	//pago tercera semana//
	Escribir "Por favor introduzca la cantidad de horas trabajadas de la tercera semana"
	Leer v_hs3
	Si v_hs3 > 40 Entonces //SE DECIDE SEGUN SI HORAS DE LA TERCERA SEMANA SON MAYORES A 40
		Escribir "La cantidad de horas trabajadas normales en la tercera semana  es"
		Escribir "40"
		v_hes3= v_hs3 - 40 //SI LAS HORAS DE LA TERCERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la tercera semana es"
		Escribir v_hes3
	SiNo
		Escribir "La cantidad de horas trabajadas normales en la tercera semana es"
		Escribir v_hs3 //SI LAS HORAS DE LA TERCERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la tercera semana es"
		Escribir v_hes3
	Fin Si
	Si v_hes3 <> 0 Entonces //SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		Escribir "El pago por horas normales en la tercera semana es"
		v_phn3 = v_vh * 40 //SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		Escribir v_phn3
	SiNo
		Escribir "El pago por horas normales en la tercera semana es"
		v_phn3 = v_vh * v_hs3 //SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA TERCERA SEMANA
		Escribir v_phn3
	Fin Si
	v_phe3 = v_hes3 * v_vh * (1.5) //PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA TERCERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	Escribir "El pago por horas extraordinarias en la tercera semana es"
	Escribir v_phe3
	Escribir "El pago de la tercera semana es"
	v_ps3= v_phe3 + v_phn3 //PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	Escribir v_ps3
	
	//pago cuarta semana//
	Escribir "Por favor introduzca la cantidad de horas trabajadas de la cuarta semana"
	Leer v_hs4
	Si v_hs4 > 40 Entonces //SE DECIDE SEGUN SI HORAS DE LA CUARTA SEMANA SON MAYORES A 40
		Escribir "La cantidad de horas trabajadas normales en la cuarta semana  es"
		Escribir "40"
		v_hes4= v_hs4 - 40 //SI LAS HORAS DE LA CUARTA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la cuarta semana es"
		Escribir v_hes4
	SiNo
		Escribir "La cantidad de horas trabajadas normales en la cuarta semana es"
		Escribir v_hs4 //SI LAS HORAS DE LA CUARTA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
		Escribir "La cantidad de horas trabajadas extraordinarias en la cuarta semana es"
		Escribir v_hes4
	Fin Si
	Si v_hes4 <> 0 Entonces //SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		Escribir "El pago por horas normales en la cuarta semana es"
		v_phn4 = v_vh * 40 //SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
		Escribir v_phn4
	SiNo
		Escribir "El pago por horas normales en la cuarta semana es"
		v_phn4 = v_vh * v_hs4 //SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA CUARTA SEMANA
		Escribir v_phn4
	Fin Si
	v_phe4 = v_hes4 * v_vh * (1.5) //PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA CUARTA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
	Escribir "El pago por horas extraordinarias en la cuarta semana es"
	Escribir v_phe4
	Escribir "El pago de la tercera semana es"
	v_ps4= v_phe4 + v_phn4 //PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
	Escribir v_ps4
	
	//pago total del mes
	Escribir "El salario mensual es"
	v_sm=v_ps1 + v_ps2 + v_ps3 +v_ps4 //PARA OBTENER EL PAGO TOTAL DEL MES: SE SUMAN LOS PAGOS TOTALES DE LAS CUATRO SEMANAS
	Escribir v_sm
FinAlgoritmo

