/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "DIA_SEMANA_MODIFICADO.java."

import java.io.*;

public class dia_semana_modificado {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double d1;
		int v_d1;
		int v_dia;
		String v_dia1;
		int v_diasem;
		// ENUNCIADO= 5.  Pag. 143.  EJEMPLO 4.13 Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy.
		// DESARROLLADO POR: Hernan Alberto Londoño Velez
		// FECHA: 03/03/2023
		// VERSION: 1.0
		// Definir 
		// VARIABLE QUE ALMACENA LA LETRA INICIAL DE LA SEMANA DEL PRIMER DIA DEL MES.
		// VARIABLE QUE ALMACENA EL VALOR DEL PRIMER DIA DEL MES.
		// VARIABLE QUE ALMACENA EL DIA DEL MES.
		// VARIABLE QUE ALMACENA UN RESULADO DE UNA ECUACION ARITMETICA.
		// VALOR INICIAL:
		v_dia1 = "";
		v_d1 = 0;
		v_dia = 0;
		v_diasem = 0;
		// ENTRADA DE DATOS
		System.out.println("el dia 1 fue (L,M,X,J,V,S,D) por favor escriba la letra en mayuscula");
		v_dia1 = bufEntrada.readLine();
		// PROCESO Y SALIDA
		// SE DECIDE SEGUN CUAL ES EL PRIMER DIA DEL MES 
		switch (v_dia1) {
		case "L":
			// SI EL PRIMER DIA DEL MES ES LUNES ENTONCES ES 0
			v_d1 = 0;
			break;
		case "M":
			// SI EL PRIMER DIA DEL MES ES MARTES ENTONCES ES 1
			v_d1 = 1;
			break;
		case "X":
			// SI EL PRIMER DIA DEL MES ES MIERCOLES ENTONCES ES 2
			v_d1 = 2;
			break;
		case "J":
			// SI EL PRIMER DIA DEL MES ES JUEVES ENTONCES ES 3
			d1 = 3;
			break;
		case "V":
			// SI EL PRIMER DIA DEL MES ES VIERNES ENTONCES ES 4
			v_d1 = 4;
			break;
		case "S":
			// SI EL PRIMER DIA DEL MES ES SABADO ENTONCES ES 5
			v_d1 = 5;
			break;
		case "D":
			// SI EL PRIMER DIA DEL MES ES DOMINGO ENTONCES ES 6
			v_d1 = 6;
			break;
		default:
			// SI ES OTRA OPCION ENTONCES NO SERIA UNA RESPUESTA CORRESTA
			v_d1 = -40;
		}
		System.out.println("escriba el numero del dia");
		v_dia = Integer.parseInt(bufEntrada.readLine());
		// PARA OBTENER EL DIA DE LA SEMANA ENTONCES: SUMO EL DIA DEL MES CON EL NUMERO DE LA SEMANA DEL PRIMER DIA DEL MES
		v_diasem = v_dia+v_d1;
		// SE DECIDE SI DIA ES MAYOR A 7
		if (v_diasem>7) {
			// SI V_DIASEM ES MAYOR A 7 ENTONCES:SE REALIZA EL SIGUIENTE PROCESO
			do {
				// PARA OBTENER EL NUEVO VALOR DE V_DIASEM: SE RESTA DIA CON 7
				v_diasem = v_diasem-7;
				// SE TERMINA EL PROCESO CUANDO V_DIASEM SEA MENOR O IGUAL A 7
			} while (v_diasem>7);
		}
		// SALIDA
		// SE DECIDE SEGUN SI V_DIASEM ES IAGUAL A UN NUMERO DEL 1 AL 7
		switch (v_diasem) {
		case 1:
			// SI V_DIASEM ES IGUAL A 1 ENTONCES: ES LUNES
			System.out.println("Ese dia es un lunes");
			break;
		case 2:
			// SI V_DIASEM ES IGUAL A 2 ENTONCES: ES MARTES
			System.out.println("Ese dia es un martes");
			break;
		case 3:
			// SI V_DIASEM ES IGUAL A 3 ENTONCES: ES MIERCOLES
			System.out.println("Ese dia es un miercoles");
			break;
		case 4:
			// SI V_DIASEM ES IGUAL A 4 ENTONCES: ES JUEVES
			System.out.println("Ese dia es un jueves");
			break;
		case 5:
			// SI V_DIASEM ES IGUAL A 5 ENTONCES: ES VIERNES
			System.out.println("Ese dia es un viernes");
			break;
		case 6:
			// SI V_DIASEM ES IGIAL A 6 ENTONCES: ES SABADO
			System.out.println("Ese dia es un sabado");
			break;
		case 7:
			// SI V_DIASEM ES IGUAL A 7 ENTONCES: ES DOMINGO
			System.out.println("Ese dia es un domingo");
			break;
		}
	}


}

