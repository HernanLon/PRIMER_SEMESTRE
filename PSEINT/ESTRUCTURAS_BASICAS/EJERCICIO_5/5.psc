Algoritmo Salario_Ejercicio_05
	//Enunciado: Calcular el salario con descuentos
	//Leer valores de v_VH, v_HTD, v_HTN
	//Pedir cada valor por teclado
	// y hallar el valor de x
	//desarrollado por: Hernan Alberto Londoño Velez
	//version 1.0
	//fecha 20/02/23
	
	//DECLARACION DE VARIABLES
	Definir v_VH Como Real //varaible que almacena el valor de la hora dia o comunes
	Definir v_VH40 Como Real //variable que almacena el valor del 40% de las horas dia
	Definir v_VHN Como Real //variable que almacena el valor de la hora nocturna
	Definir v_VTHD Como Real //variable que alamcena el valor total de las horas dia
	Definir v_VTHN Como Real //variable que alamcena el valor total de las horas noche
	Definir v_SubSalario Como Real //variable que almacena el valor del subsalario
	Definir v_RF Como Real //variable que alamcena el descuento de retencion en la fuente
	Definir v_FE Como Real //variable que alamcena el descuento de fondos de empleados
	Definir v_BF Como Real //variable que alamcena el descuento bienestar familiar
	Definir v_SP Como Real //variable que alamcena el descuento de salir y pension
	Definir v_SalarioNeto Como Real; //variable que alamcena el valor del salario neto
	Definir v_HTD Como Entero //variable que almacena la cantidad de horas dia
	Definir v_HTN Como Entero; //variable que alamcena la cantidad de horas noche
	Definir v_NomEmp como caracter; //variable que alamcena el nombre del empleado
	
	//inicializacion de variables
	v_VH =0.0;
	v_VH40=0.0;
	v_VHN=0.0;
	v_VTHD=0.0;
	v_VTHN=0.0;
	v_SubSalario=0.0;
	v_RF=0.0;
	v_FE=0.0;
	v_BF=0.0;
	v_SP=0.0;
	v_SalarioNeto=0.0;
	v_HTD=0;
	v_HTN=0;
	v_NomEmp=""
	
	// ENTRADA DE DATOS//
	Escribir "Por favor ingrese el nombre del empleado "
	Leer v_NomEmp
	Escribir "Por favor ingrese el valor de la hora";
	Leer v_VH;
	Escribir 'Por favor ingrese la cantidad de Horas Trabajadas Día';
	Leer v_HTD;
	Escribir 'Por favor ingrese la cantidad de Horas Trabajadas Noche';
	Leer v_HTN;
	//Procesos
	v_VTHD <- (v_VH)*(v_HTD); //PARA OBTENER EL VALOR DE TODAS LAS HORAS DIA, SE MULTIPLICA EL VALOR DE LA HORA POR HORAS DIA
	v_VH40 <- v_VH*0.4; //PARA OBTENER EL 40% DEL VALOR DE LA HORA COMUN, SE MULTIPLICA EL VALOE DE LA HORA POR 0.4
	v_VHN <- (v_VH)+(v_VH40); //PARA OBTENER EL VALOR DE LA HORA NOCTURA, SE SUMA EL VALOR DE LA HORA CON 40% DE LA HORA COMUN
	v_VTHN <- (v_VHN)*(v_HTN); //PARA OBTENER EL VALOR DE TODAS LAS HORAS NOCHE, SE MULTIPLICA EL VALOR DE LA HORA NOCHE POR LA CANTODAD DE HORAS NOCHE
	v_SubSalario <- (v_VTHD)+(v_VTHN); //PARA OBTENER EL SUBSALARIO, SE SUMA EL VALOR DE TODAS LAS HORAS DIA CON EL VALOR DE TODAS LAS HORAS NOCHE
	v_RF <- (v_SubSalario)*(0.1); //PARA OBTENER EL VALOR DE RETENCION EN LA FUENTE, SE MULTIPLICA SUBSALARIO POR 0.1
	v_FE <- (v_SubSalario)*(0.03); //PAAR OBTENER EL VALOR DE FONDOS DE EMPLEADOS, SE MULTIPLICA SUBSALARIO POR 0.03
	v_BF <- (v_SubSalario)*(0.02); //PARA OBTENER EL VALOR DE BIENESTAR FAMILIAR, SE MULTIPLICA SUBSALARIO POR 0.02
	v_SP <- (v_SubSalario)*(0.04); //PARA OBTENER EL VALOR DE SALUD  Y PENSION, SE MULTIPLICA SUBSALARIO POR 0.04
	v_SalarioNeto <- (v_SubSalario)-(v_RF)-(v_FE)-(v_BF)-(v_SP); //PARA OBTENER EL VALOR DEL SALARIO NETO, SE RESTA SUBSALARIO CON RETENCION EN LA FUENTE, FONDO DE EMPLEADOS, BIENESTAR FAMILIAR Y SALUD Y PENCION
	
	//Salida
	Escribir 'Valo Hora Nocturna: ', v_VHN;
	Escribir 'El Subsalario es: ',v_SubSalario;
	Escribir 'Descuentos';
	Escribir 'Descuento por retencion de fuente';
	Escribir '10%';
	Escribir 'Descuento de fondos de empleados';
	Escribir '3%';
	Escribir 'Descuento de bienestar familiar';
	Escribir '2%';
	Escribir 'Descuento de salud y pension';
	Escribir '4%';
	Escribir 'Salario neto';
	Escribir v_SalarioNeto;
FinAlgoritmo
