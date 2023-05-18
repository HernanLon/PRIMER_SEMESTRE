Proceso Ecuacion_cuadratica_Ejercicio_3_17
	//Enunciado: Encontrar las coordenadas en el plano carteciano x,y para graficar una ecuacion cuadratica o de sgundo grado
	//Leer valores de a, b y c
	//Pedir cada valor por teclado
	//DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	//VERSION: 1.0
	//FACHA: 22/02/2023
	
	//DECLARAR:
	Definir v_a Como Real //Variable de entrada que almacena el valor de a
	Definir v_b Como Real //Variable de entrada que almacena el valor de b
	Definir v_c Como Real //Variable de entrada que almacena el valor de c
	Definir v_x1 Como Real //Variable de proceso y salida que almacena el primer corte con x
	Definir v_x2 Como Real //Variable de proceso y salida que almacena el segundo corte con x
	Definir v_y Como Real //Variable de proceso y salida que almacena el corte con y
	Definir v_very Como Real //Variable de proceso y salida que almacena las coordenadas del vértice en y
	Definir v_ejes  Como Real //Variable de proceso y salida que almacena las coordenadas del eje de simetría 
	
	//VALOR INICAIL:
	v_a=0.0
	v_b=0.0
	v_c=0.0
	v_x1=0.0
	v_x2=0.0
	v_y=0.0
	v_very=0.0
	v_ejes=0.0
	
	//ENTRADA DE DATOS:
	Escribir"Ecuacion ax²+ bx + c"
	Escribir "Por favor escribir el valor de a"
	Leer v_a
	Escribir "Por favor escribir el valor de b"
	Leer v_b
	Escribir "Por favor escribir el valor de c"
	Leer v_c
	
	//procesos y salidas
	si v_b^2-4*v_a*v_c>0 Entonces //SE DECIDE SEGUN SI EL VALOR B ELEVADO A LA POTENCIA 2-4 MULTIPLICADO POR EL VALOR A Y MULTIPLICADO POR EL VALOR C GENERA UN RESULTADO MAYOR A CERO
		Escribir"el primer corte con x es" //SI LA ANTERIOR ENCUACION ES MAYOR A CERO ENTONCES:
		v_x1=-(-v_b+RC(v_b^2-4*v_a*v_c))/2*v_a //PARA OBTENER EL PRIMER CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNO ANTES DE LA RAIZ ES POSITIVO
		Escribir "(", v_x1, ",0", ")"
		Escribir"Elsegundo corte con x es"
		v_x2=-(-v_b-RC(v_b^2-4*v_a*v_c))/2*v_a //PARA OBTENER EL SEGUNDO CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNOANTES DE LA RAIZ ES NEGATIVO
		Escribir "(", v_x2, ",0", ")"
	SiNo  
		Escribir "Las raices son imaginarias" //SI LA CONDICION DE LA ECUACION NO ES MAYOR A CERO ENTONCES:
		Escribir -v_b/(2*v_a), "+",(RC(abs(v_b^2-4*v_a*v_c)))/2*v_a, "i" //SE REALIZA LA OPERACION EXPUESTA, YA QUE LAS RAICES SON IMAGINARIAS
		Escribir -v_b/(2*v_a), "-",(RC(abs(v_b^2-4*v_a*v_c)))/2*v_a, "i" //SE REALIZA LA OPERACION EXPUESTA YA QUE LAS RAICES SON IMAGINARIAS
	FinSi
	
	// se emplea el condicional si para encontrar los cortes con el eje x pero si el resultado al que hay que sacar raiz cruadrada es negativo el resultado son numeros imaginarios
	Escribir "el corte con y es"
	v_y=v_a*(0)^2+v_b*(0)+v_c //PARA OBTENER EL CORTE Y: SE REALIZA LA OPERACION EXPUESTA
	Escribir "(", "0,", v_y, ")"
	
	//se halla el corte con y en cordendas x,y por eso 0,y
	Escribir "El eje de simetría es"
	v_ejes=-v_b/2*v_a //PARA OBTENER LAS COORDENADAS DEL EJE DE SIMETRIA: SE DIVIDE EL VALOR B ENTRE 2 Y SE MULTIPLICA POR EL VALOR A
	Escribir v_ejes
	Escribir "El vertice en y es"
	v_very= v_a*(v_ejes)^2+v_b*(v_ejes)+v_c //PARA OBTENER LAS COORDENADAS DEL VERTICE EN Y: SE REALIZA LA OPERACION EXPUESTA
	Escribir v_very
	Escribir "Elvertice en coordenadas (x,y) es"
	Escribir "(", v_ejes, ",", v_very, ")"
	Si v_a>0 Entonces //SE DECIDE SEGUN SI EL VALOR DE A ES MAYOR A CERO
		Escribir "La funcion es concava hacia arriba" //SI EL VALOR A ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ARRIVA
	SiNo
		Escribir"la funcion es concava hacia abajo" //SI EL VALOR A NO ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ABAJO
	Fin Si
	//se emplea el condicional si poara saber hacia donde es concava la funcion y poder graficar 
FinProceso
