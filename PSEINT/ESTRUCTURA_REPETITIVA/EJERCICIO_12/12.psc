Algoritmo suma_
	//Enunciado: Encontrar el valor de la suma consecutiva de los numeros enteros positivos del 1 al 50
	//DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	//VERSION: 1.0
	//FECHA: 22/02/2023
	
	//DECLARAR:
	Definir v_n Como Entero //VARIABLE QUE ALAMCENA EL VALOR DE CADA NUMERO DEL 1 AL 50
	Definir v_suma como enteros //VARAIABLE QUE ALMACENA EL VALOR DE LA SUMA DE LOS NUMEROS DEL 1 AL 50
	
	//VALOR INICIAL:
	v_n=1 
	v_suma=0
	
	//procesos y salidas
	Escribir "Lista de numeros sumados"
	Para v_n<-1 Hasta 50 Con Paso 1 Hacer //PROCESO EN LE CUAL SE SELECCIONA CADA NUMERO DESDE EL 1 HASTA EL 50
		Escribir v_n
		v_suma=v_suma + v_n //SE SUMA CADA NUMERO DESDE EL 1 HASTA EL 50
	Fin Para
	Escribir "El resultado de la suma es ", v_suma
FinAlgoritmo
