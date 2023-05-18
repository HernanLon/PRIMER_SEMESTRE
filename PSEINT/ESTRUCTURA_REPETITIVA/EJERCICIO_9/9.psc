Algoritmo PARES
	//Enunciado: Encontrar el valor de la suma de los numeros enteros psositivos pares del 2 al 100
	//desarrollado por: HERNAN ALBERTO LONDOÑO VELEZ
	//version 1.0
	//fecha 22/02/2023
	
	//DEFINIR:
	Definir v_n Como Entero //VARIABLE QUE ALMACENA CADA NUMERO PAR DESDE EL 2 HASTA EL 100.
	Definir v_suma Como Entero //VARIABLE QUE ALMACENA UNA RESPUESTA DE UNA ECUACION ARITMETICA, SUMA DE LOS NUMEROS.
	
	//VALOR INICIAL:
	v_n=2
	v_suma=0
	
	//PROCESO Y SALIDA
	Escribir "Lista de numeros sumados"
	Para V_n<-2 Hasta 100 Con Paso 2 Hacer //PRECESO EN EL CUAL SOLO SE SELECCIONA LOS NUMERO DE DOS EN DOS DESDE EL 2 HASTA EL 100, (NUMERO PARES)
		Escribir v_n
		v_suma=v_suma + v_n //SE SUMAN SOLO LOS NUMEROS PARES DESDE EL 2 HASTA EL 100
	Fin Para;
	Escribir "El resultado de la suma es ", v_suma
	
FinAlgoritmo