/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo deber�a llamarse "SALARIO_EJERCICIO_05.java."

import java.io.*;

public class salario_ejercicio_05 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_bf;
		double v_fe;
		int v_htd;
		int v_htn;
		String v_nomemp;
		double v_rf;
		double v_salarioneto;
		double v_sp;
		double v_subsalario;
		double v_vh;
		double v_vh40;
		double v_vhn;
		double v_vthd;
		double v_vthn;
		// Enunciado: Calcular el salario con descuentos
		// Leer valores de v_VH, v_HTD, v_HTN
		// Pedir cada valor por teclado
		// y hallar el valor de x
		// desarrollado por: Hernan Alberto Londo�o Velez
		// version 1.0
		// fecha 20/02/23
		// DECLARACION DE VARIABLES
		// varaible que almacena el valor de la hora dia o comunes
		// variable que almacena el valor del 40% de las horas dia
		// variable que almacena el valor de la hora nocturna
		// variable que alamcena el valor total de las horas dia
		// variable que alamcena el valor total de las horas noche
		// variable que almacena el valor del subsalario
		// variable que alamcena el descuento de retencion en la fuente
		// variable que alamcena el descuento de fondos de empleados
		// variable que alamcena el descuento bienestar familiar
		// variable que alamcena el descuento de salir y pension
		// variable que alamcena el valor del salario neto
		// variable que almacena la cantidad de horas dia
		// variable que alamcena la cantidad de horas noche
		// variable que alamcena el nombre del empleado
		// inicializacion de variables
		v_vh = 0.0;
		v_vh40 = 0.0;
		v_vhn = 0.0;
		v_vthd = 0.0;
		v_vthn = 0.0;
		v_subsalario = 0.0;
		v_rf = 0.0;
		v_fe = 0.0;
		v_bf = 0.0;
		v_sp = 0.0;
		v_salarioneto = 0.0;
		v_htd = 0;
		v_htn = 0;
		v_nomemp = "";
		// ENTRADA DE DATOS//
		System.out.println("Por favor ingrese el nombre del empleado ");
		v_nomemp = bufEntrada.readLine();
		System.out.println("Por favor ingrese el valor de la hora");
		v_vh = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Por favor ingrese la cantidad de Horas Trabajadas D�a");
		v_htd = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Por favor ingrese la cantidad de Horas Trabajadas Noche");
		v_htn = Integer.parseInt(bufEntrada.readLine());
		// Procesos
		// PARA OBTENER EL VALOR DE TODAS LAS HORAS DIA, SE MULTIPLICA EL VALOR DE LA HORA POR HORAS DIA
		v_vthd = (v_vh)*(v_htd);
		// PARA OBTENER EL 40% DEL VALOR DE LA HORA COMUN, SE MULTIPLICA EL VALOE DE LA HORA POR 0.4
		v_vh40 = v_vh*0.4;
		// PARA OBTENER EL VALOR DE LA HORA NOCTURA, SE SUMA EL VALOR DE LA HORA CON 40% DE LA HORA COMUN
		v_vhn = (v_vh)+(v_vh40);
		// PARA OBTENER EL VALOR DE TODAS LAS HORAS NOCHE, SE MULTIPLICA EL VALOR DE LA HORA NOCHE POR LA CANTODAD DE HORAS NOCHE
		v_vthn = (v_vhn)*(v_htn);
		// PARA OBTENER EL SUBSALARIO, SE SUMA EL VALOR DE TODAS LAS HORAS DIA CON EL VALOR DE TODAS LAS HORAS NOCHE
		v_subsalario = (v_vthd)+(v_vthn);
		// PARA OBTENER EL VALOR DE RETENCION EN LA FUENTE, SE MULTIPLICA SUBSALARIO POR 0.1
		v_rf = (v_subsalario)*(0.1);
		// PAAR OBTENER EL VALOR DE FONDOS DE EMPLEADOS, SE MULTIPLICA SUBSALARIO POR 0.03
		v_fe = (v_subsalario)*(0.03);
		// PARA OBTENER EL VALOR DE BIENESTAR FAMILIAR, SE MULTIPLICA SUBSALARIO POR 0.02
		v_bf = (v_subsalario)*(0.02);
		// PARA OBTENER EL VALOR DE SALUD  Y PENSION, SE MULTIPLICA SUBSALARIO POR 0.04
		v_sp = (v_subsalario)*(0.04);
		// PARA OBTENER EL VALOR DEL SALARIO NETO, SE RESTA SUBSALARIO CON RETENCION EN LA FUENTE, FONDO DE EMPLEADOS, BIENESTAR FAMILIAR Y SALUD Y PENCION
		v_salarioneto = (v_subsalario)-(v_rf)-(v_fe)-(v_bf)-(v_sp);
		// Salida
		System.out.println("Valo Hora Nocturna: "+v_vhn);
		System.out.println("El Subsalario es: "+v_subsalario);
		System.out.println("Descuentos");
		System.out.println("Descuento por retencion de fuente");
		System.out.println("10%");
		System.out.println("Descuento de fondos de empleados");
		System.out.println("3%");
		System.out.println("Descuento de bienestar familiar");
		System.out.println("2%");
		System.out.println("Descuento de salud y pension");
		System.out.println("4%");
		System.out.println("Salario neto");
		System.out.println(v_salarioneto);
	}


}

