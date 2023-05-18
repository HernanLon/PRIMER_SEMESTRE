Algoritmo Ejercicio_2_Primer_Parcial
	//Enunciado: Encontrar la cantidad de días, horas y minutos a las que equivalen los segundos 
	//Leer Segundos
	//Pedir valor por teclado
	// y hallar los días, horas y minutos
	//desarrollado por Jonathan López y Hernan Londoño
	//version 1.0
	//fecha 13/03/23
	//declaracion de variables
	Definir v_dias, v_horas, v_minutos Como Real;
	Definir v_s Como Entero;
	//inicializacion de variables
	v_s=0;
	v_dias=0.0;
	v_horas=0.0
	v_minutos=0.0
	//Entrada de datos
	Escribir "Por favor ingrese los segundos"
	Leer v_s
	v_dias=v_s/86400
	Escribir "dias: ", v_dias;
	v_horas=v_s/3600
	Escribir "Horas: ", v_horas;
	v_minutos=v_s/60
	Escribir "Minutos: ", v_minutos;
FinAlgoritmo
