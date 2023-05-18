/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SALARIOS.java."

import java.io.*;

public class salarios {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_bruto;
		double v_ht;
		String v_ne;
		double v_neto;
		double v_tasas;
		int v_tht;
		int v_vh;
		// ENUNCIADO=Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto.
		// HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA:26/02/2023
		// VERSION: 1.0
		// DEFINICION=
		// VARAIBLE QUE ALMACENA EL NOMBRE DEL EMPLEADO
		// VARIABLE QUE ALMACENA LAS HORAS TRABAJADAS
		// VARIABLE QUE ALMACENA EL VALOR DE LA HORA
		// VARIABLE QUE ALMACENA EL VALOR DEL SALARIO BRUTO
		// VARIABLE QUE ALMACENA EL VALOR DE LOS IMPUESTOS O TASAS
		// VARIABLE QUE ALAMCENA EL VALOR DEL SALARIO NETO
		// VALOR INICIAL:
		v_ne = "";
		v_tht = 0;
		v_vh = 0;
		v_bruto = 0;
		v_tasas = 0.0;
		v_neto = 0.0;
		// INICIO=
		// INGRESO DE DATOS
		System.out.println("escribe el nombre del empleado");
		v_ne = bufEntrada.readLine();
		System.out.println("escribe el total de horas trabajadas");
		v_ht = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escribe el precio de las horas");
		v_vh = Integer.parseInt(bufEntrada.readLine());
		System.out.println("-----------------------------------------");
		// PROCESO
		// PARA OBTENER EL VALOR DEL SALARIO BRUTO: SE MULTIPLICA LAS HORAS TRABAJASDAS POR EL VALOR DE LAS HORAS
		v_bruto = v_ht*v_vh;
		// PARA OBTENER EL VALOR DE LAS TASAS O IMPUESTOS: SE MULTIPLICA EL SALRIO BRUTO POR 0.25 (25% = 0.25)
		v_tasas = v_bruto*0.25;
		// PARA OBTENER EL VALOR DEL SALARIO NETO: SE RESTA EL SALARIO BRUTO CON LAS TASAS
		v_neto = v_bruto-v_tasas;
		// SALIDA
		System.out.println("-----------------------------------------");
		System.out.println("el nomnbre del empleado es="+v_ne);
		System.out.println("el salario bruto es="+"$"+v_bruto);
		System.out.println("los impuestos o tasas a pagar son="+"$"+v_tasas);
		System.out.println("el salario neto es="+"$"+v_neto);
		System.out.println("--------------------------------------------");
		// FIN
	}


}

