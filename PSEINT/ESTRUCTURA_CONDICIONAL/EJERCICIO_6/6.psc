Algoritmo Ejercicio_06
	// Enunciado: Encontrar el valor de x en una ecuacion lineal tip ax + b
	// Leer valores de a y b
	// Pedir cada valor por teclado
	// y hallar el valor de x
	// desarrollado por: Hernan Alberto Londoño Velez
	// version 1.0
	// fecha 20/02/23
	// Declaracion de variables
	Definir v_n1 Como Real // VARIABLE QUE ALAMACENA EL VALOR DEL PRIMER PARCIAL
	Definir v_n2 Como Real // VARIABLE QUE ALAMACENA EL VALOR DEL SEGUNDO PARCIAL
	Definir v_n3 Como Real // VARIABLE QUE ALAMACENA EL VALOR DEL TERCER PARCIAL
	Definir v_p1 Como Real // VARAIBLE QUE ALMACENA EL PORCENTAJE QUE REPRESENTA EL PRIMER PARCIAL
	Definir v_p2 Como Real // VARAIBLE QUE ALMACENA EL PORCENTAJE QUE REPRESENTA EL SEGUNDO PARCIAL
	Definir v_p3 Como Real // VARAIBLE QUE ALMACENA EL PORCENTAJE QUE REPRESENTA EL TERCER PARCIAL
	Definir v_np Como Real // VARAIBLE QUE ALAMCENA LA NOTA DEL PRIMER PARCIAL
	Definir v_ns Como Real // VARAIBLE QUE ALAMCENA LA NOTA DEL SEGUNDO PARCIAL
	Definir v_nt Como Real // VARAIBLE QUE ALAMCENA LA NOTA DEL TERCER PARCIAL
	Definir v_N Como Real // VARIABLE QUE ALAMCENA LA SUMA DE LOS TRES PARCIALES
	Definir v_ND Como Real // VARIABLE QUE ALAMCENA LA NOTA DEFINITIVA
	Definir v_si Como Entero // VARIABLE QUE ALAMCENA LAS DECISIONES DE INASISTENCIAS DEL ESTUDIANTE
	Definir v_ina Como Entero // VARIABLE QUE ALAMCENA EL NUMERO DE INASISTENCIAS
	Definir v_NomEst Como Caracter // VARIABLE QUE ALMACENA EL NOMBRE DEL ESTUDIANTE
	Definir v_NomAsi Como Caracter // VARIABLE QUE ALAMCENA EL NOMBRE DE LA ASIGNATURA
	// Inicializacion de variables
	v_n1 <- 0.0
	v_n2 <- 0.0
	v_n3 <- 0.0
	v_p1 <- 0.0
	v_p2 <- 0.0
	v_p3 <- 0.0
	v_np <- 0.0
	v_ns <- 0.0
	v_nt <- 0.0
	v_N <- 0.0
	v_ND <- 0.0
	v_si <- 0
	v_ina <- 0
	v_NomEst <- ''
	v_NomAsi <- ''
	// Entrada de datos
	Escribir 'Por favor ingrese el nombre del estudiante'
	Leer v_NomEst
	Escribir 'Por favor ingrese el nombre e la asignatura'
	Leer v_NomAsi
	Escribir 'Por favor ingrese nota del primer parcial'
	Leer v_n1
	Escribir 'Por favor ingrese nota del segundo parcial'
	Leer v_n2
	Escribir 'Por favor ingrese nota del tercer parcial'
	Leer v_n3
	Escribir 'Por favor ingrese el primer porsentaje recuerde que debe ser en decimal así 10%= 0.1'
	Leer v_p1
	Escribir 'Por favor ingrese el segundo porsentaje'
	Leer v_p2
	Escribir 'Por favor ingrese el tercer porsentaje '
	Leer v_p3
	Escribir 'Por favor Ingrese la cantidad de inacistencias'
	Leer v_ina
	// Procesos y salidas 
	Escribir 'la nota del primaer parcial es '
	v_np <- v_n1*v_p1 // PARA OBTENER LA NOTA DEL PRIMER PARCIAL: SE MULTIPLICA VALOR PRIMER PARCIAL POR PORCENTAJE DEL PRIMER PARCIAL
	Escribir v_np
	Escribir 'la nota del segundo parcial es '
	v_ns <- v_n2*v_p2 // PARA OBTENER LA NOTA DEL SEGUNDO PARCIAL: SE MULTIPLICA VALOR SEGUNDO PARCIAL POR PORCENTAJE DEL SEGUNDO PARCIAL
	Escribir v_ns
	Escribir 'la nota del tercer parcial es '
	v_nt <- v_n3*v_p3 // PARA OBTENER LA NOTA DEL TERCER PARCIAL: SE MULTIPLICA VALOR TERCER PARCIAL POR PORCENTAJE DEL TERCER PARCIAL
	Escribir v_nt
	Escribir 'La nota es '
	v_N <- v_np+v_ns+v_nt // PARA OBTENER V_N, SE SUMAN LAS NOTAS DE LOS 3 PARCIALES
	Escribir v_N
	Escribir 'si el numero de inacistencias es menor a 12 y nota  es mayor a 3.5 opcion 1, si el numero de inacistencias es menor a 12 pero la nota es menor a 3.5 opcion 2, si el numero de inacistencias es mayor o igual a 12 opcion 3 '
	Leer v_si
	Segun v_si  Hacer // DONDE SE SELECCIONA UNA DE LAS SUTUACIONES QUE SE PUEDE PRESENTAR TENIENDO EN CUANTA LA SUMA DE LAS NOTAS Y TAMBIEN LA ACNTIDAD DE INASISTANCIAS
		1:
			Escribir 'aprueba academicamente'
			Escribir 'la Nota definitiva es igual a'
			v_ND <- v_N // NOTA FINAL
			Escribir v_ND
		2:
			Escribir 'reprueba academicamente'
			Escribir 'la Notade definitiva es igual a'
			v_ND <- v_N // NOTA FINAL
			Escribir v_ND
		3:
			Escribir 'reprueba por inacistencias'
			Escribir 'la Notade definitiva es igual a'
			v_ND <- v_N/2 // SI LAS INASISTENCIAS SON IGUALES O MAYORES A 12 SE DIVIDE LA SUMA DE LAS 3 NOTAS ENTRE 2 PARA DAR LA NOTA FINAL
			Escribir v_ND
	FinSegun
FinAlgoritmo
