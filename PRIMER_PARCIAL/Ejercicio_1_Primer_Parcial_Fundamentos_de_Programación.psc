Algoritmo Ejercicio_1_Primer_Parcial_Fundamentos_de_Programación
	//Enunciado:resolver la ecuacio que el usuario necesite
	//Declarar los valores de Vf, Vi y t
	//pedir los valores por tecladp
	//Desarrollado por Hernan Londoño y Jonathan López
	//Version 1.0
	//Fecha: 13/03/23
	//Definir variables
	Definir v_ECU Como Caracter;
	Definir v_Vi Como Real;
	Definir v_Vf Como Real;
	Definir v_t Como Real;
	Definir v_a Como Real;
	Definir v_vm Como Real;
	Definir v_mvi Como Entero;
	Definir v_mvf Como Entero;
	Definir v_t2 como Real;
	Definir v_t22 como Real;
	Definir v_vf2 como Real;
	Definir v_vi2 como Real;
	Definir v_a2 Como Real;
	Definir v_d1 Como Real;
	Definir v_d2 Como Real;
	Definir v_ma Como Entero;
	Definir v_mt Como Entero;
	Definir v_dt Como Real
	Definir v_dt2 Como real
	//Inicializacion de variables
	v_ECU ="";
	v_Vi=0.0;
	v_Vf=0.0;
	v_t=0.0;
	v_a=0.0;
	v_Vm=0;
	v_mvi=0;
	v_mvf=0;
	v_t2=0.0;
	v_t22=0.0;
	v_vf2=0.0;
	v_vi2=0.0;
	v_a2=0.0;
	v_d1=0.0;
	v_d2=0.0;
	v_ma=0.0;
	v_mt=0.0;
	v_dt=0.0
	v_dt2=0.0
	//Entrada de datos
	Escribir "Por favor elija la ecuacion a realizar: aceleracion (a),velocidad media (vm), velocidad final (vf), distancia sin aceleracion (d1), distancia con aceleracion (d2)"
	Leer v_ECU;
	
	//Proceos y salidas
	Segun v_ECU Hacer //condicional que se utiliza para elegir que tipo de ejercicio resolver
		"a":
			//Entrada de datos
			Escribir "Por favor ingrese la velocidad inicial"
			Leer v_Vi
			Escribir "elija medicion de velocidad inicial: m/s (1) ó km/h (2)"
			Leer v_mvi
			Escribir "Por favor ingrese la velocidad final"
			Leer v_Vf
			Escribir "elija medicion de velocidad final: m/s (1) ó km/h (2)"
			Leer v_mvf
			Escribir "Por favor ingrese el tiempo en segundos"
			Leer v_t
			Escribir "elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)"
			Leer v_mt
			//Proceso
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
			//Salida
					Escribir "la velocidad inicial en m/s es: ", v_vi2;
			Fin Segun
			//Proceso
			Segun v_mvf Hacer//para pasar km/h a m/s
				1:
					v_vf2=v_vf
				2:
					v_vf2=v_vf/3.6
					Escribir "la velocidad final en m/s es: ", v_vf2;//Salida
			Fin Segun
			//Proceso
			Segun v_mt Hacer//para pasar de horas y minutos a segundos.
				1:
					v_t2=v_t
				2:
					v_t2=v_t*60
					Escribir "el tiempo en segundos es: ",v_t2 //Salida
				3:
					v_t2=v_t*3600
					Escribir "el tiempo en segundos es: ",v_t2 //Salida
			Fin Segun
			
			
			//Proceso
			v_a=(v_Vf2-v_Vi2)/v_t2;//es la escuación que se utiliza para hallar la aceleración
			Escribir "La aceleración es ",v_a;//Salida
			//-------------------------------------------------------------------------------------------
		"vm":
			//Entrada de datos
			Escribir "Por favor ingrese la velocidad inicial"
			Leer v_Vi
			Escribir "Por favor ingrese la velocidad final"
			Leer v_Vf
			//Proceso
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
					
					Escribir "la velocidad inicial en m/s es: ", v_vi2;//Salida
			Fin Segun
			//Proceso
			Segun v_mvf Hacer//para pasar km/h a m/s
				1:
					v_vf2=v_vf
				2:
					v_vf2=v_vf/3.6
					Escribir "la velocidad final en m/s es: ", v_vf2;//Salida
			Fin Segun
			
			//Proceso 
			v_Vm=(v_Vf2-v_Vi2)/2;//es la ecuación que se utiliza para  hallar la Velocidad media
			Escribir "La velocidad media es ",v_Vm;//Salida
			//----------------------------------------------------------------------------------------------
		"vf":
			//Entrada de datos
			Escribir "escriba la velocidad inicial"
			Leer v_vi
			Escribir "escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)"
			leer v_mvi
			
	     
			Escribir "escriba la aceleracion"
			Leer v_a
			Escribir "escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)"
			Leer v_ma
			
			Escribir "escriba el tiempo"
			Leer v_t
			Escribir "elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)"
			leer v_mt
			//Procesos
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
					Escribir "la velocidad inicial en m/s es: ", v_vi2;//Salida
			Fin Segun
			//Procesos
			Segun v_ma Hacer
				1:
					v_a2=v_a
				2:
					v_a2=v_a/12960
					Escribir "la aceleracion en m/s2 es: ",v_a2//Salida
			Fin Segun
			//Proceso
			Segun v_mt Hacer//para pasar de horas y minutos a segundos.
				1:
					v_t2=v_t
				2:
					v_t2=v_t*60
					Escribir "el tiempo en segundos es: ",v_t2//Salida
				3:
					v_t2=v_t*3600
					Escribir "el tiempo en segundos es: ",v_t2//Salida
			Fin Segun
			//Proceso
			v_vf=v_vi2+(v_a2*v_t2)
			Escribir "La velocidad final es: ",v_vf//Salida
			//-------------------------------------------------------------------------------
		"vf2":
			//Entrada de Datos 
			Escribir "escriba la velocidad inicial"
			Leer v_vi
			Escribir "escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)"
			leer v_mvi
			
			
			Escribir "escriba la aceleracion"
			Leer v_a
			Escribir "escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)"
			Leer v_ma
			
			Escribir "escriba la distancia"
			Leer v_d
			Escribir "elija medicion de distancia: mts(1) km(2)"
			leer v_md
			//Procesos
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
			        v_vi2=v_vi2*v_vi2
					Escribir "la velocidad inicial en m/s es: ", v_vi2;//Salida
			Fin Segun
			//Procesos
			Segun v_ma Hacer
				1:
					v_a2=v_a
				2:
					v_a2=v_a/12960
					Escribir "la aceleracion en m/s2 es: ",v_a2//Salida
			Fin Segun
			//Procesos
			Segun v_mdt Hacer//paar pasar de horas y minutos a segundos.
				1:
					v_dt2=v_dt
				2:
					v_dt2=v_dt*1000
					Escribir "la distancia en mts es: ",v_dt2//Salida

			Fin Segun
			//Proceso
			v_vf=v_vi2+(2*(v_a2*v_t2))
			Escribir "La velocidad final es: ",v_vf//Salida
			//-----------------------------------------------------------------------------
			
		"d1":
			//Entrada de datos
			Escribir "escriba la velocidad inicial"
			Leer v_vi
			Escribir "escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)"
			leer v_mvi
			
			Escribir "Por favor ingrese la velocidad final"
			Leer v_Vf
			Escribir "elija medicion de velocidad final: m/s (1) ó km/h (2)"
			Leer v_mvf
//			
			Escribir "escriba el tiempo"
			Leer v_t
			Escribir "elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)"
			leer v_mt
			//Procesos
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
					Escribir "la velocidad inicial en m/s es: ", v_vi2;//Salida
			Fin Segun
			//Procesos
			Segun v_mvf Hacer//para pasar km/h a m/s
				1:
					v_vf2=v_vf
				2:
					v_vf2=v_vf/3.6
					Escribir "la velocidad final en m/s es: ", v_vf2;//Salida
			Fin Segun
			//Procesos
			Segun v_mt Hacer//paar pasar de horas y minutos a segundos.
				1:
					v_t2=v_t
				2:
					v_t2=v_t*60
					Escribir "el tiempo en segundos es: ",v_t2//Salida
				3:
					v_t2=v_t*3600
					Escribir "el tiempo en segundos es: ",v_t2//Salida
			Fin Segun
			//Proceso
			v_d1=((v_vf2+v_vi2)/2)*v_t2
			Escribir "La distancia sin aceleracion es: ",v_d1, "m"//Salida
			//-------------------------------------------------------------------------
		"d2":
			//Entrada de datos
			Escribir "escriba la velocidad inicial"
			Leer v_vi
			Escribir "escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)"
			leer v_mvi
			
			Escribir "escriba el tiempo"
			Leer v_t
			Escribir "elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)"
			leer v_mt
			
			Escribir "escriba la aceleracion"
			Leer v_a
			Escribir "escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)"
			Leer v_ma
			
			//Procesos
			Segun v_mvi Hacer//para pasar km/h a m/s
				1:
					v_vi2=v_vi
				2:
					v_vi2=v_vi/3.6
					Escribir "la velocidad inicial en m/s es: ", v_vi2;//Salida
			Fin Segun
			//Procesos
			Segun v_mt Hacer//paar pasar de horas y minutos a segundos.
				1:
					v_t2=v_t
				2:
					v_t2=v_t*60
					Escribir "el tiempo en segundos es: ",v_t2//Salida
				3:
					v_t2=v_t*3600
					Escribir "el tiempo en segundos es: ",v_t2//Salida
					
			Fin Segun
			//Procesos
			v_t22=v_t2*v_t2
			Segun v_ma Hacer
				1:
					v_a2=v_a
				2:
					v_a2=v_a/12960
					Escribir "la aceleracion en m/s2 es: ",v_a2//Salida
			Fin Segun
			//Proceso
			v_d2=((v_vi2*v_t2)+(1/2))*(v_a2*v_t22)
			Escribir "La distancia con aceleracion es:" v_d2//Salida
			
	Fin Segun
	
	
	
	
FinAlgoritmo
