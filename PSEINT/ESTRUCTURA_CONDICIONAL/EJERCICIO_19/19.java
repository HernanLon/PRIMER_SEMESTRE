/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "DIA_SEMANA.java."

import java.io.*;

public class dia_semana {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_dia;
		// ENUNCIADO= 4.  Pag. 142. EJEMPLO 4.12  Leída una fecha, decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes.
		// CREADO POR: Hernan Alberto Londoño Velez
		// FECHA: 03/03/2023
		// VERSION: 1.0
		// Definir 
		// VARIABLE QUE ALAMACENA EL VALOR DE DIA.
		// VALOR INICIAL:
		v_dia = 0;
		// INTRODUCCION DE DATOS
		System.out.println("escribe el numero del dia");
		v_dia = Integer.parseInt(bufEntrada.readLine());
		// PROCESO
		// SE DECIDE SI DIA ES MAYOR A 7
		if (v_dia>7) {
			// SI DIA ES MAYOR A 7 ENTONCES:SE REALIZA EL SIGUIENTE PROCESO
			do {
				// PARA OBTENER EL NUEVO VALOR DE DIA: SE RESTA DIA CON 7
				v_dia = v_dia-7;
				// SE TERMINA EL PROCESO CUANDO DIA SEA MENOR O IGUAL A 7
			} while (v_dia>7);
		}
		// SALIDA
		// SE DECIDE SEGUN SI DIA ES IAGUAL A UN NUMERO DEL 1 AL 7
		switch (v_dia) {
		case 1:
			// SI DIA ES IGUAL A 1 ENTONCES: ES LUNES
			System.out.println("Ese dia fue un lunes");
			break;
		case 2:
			// SI DIA ES IGUAL A 2 ENTONCES: ES MARTES
			System.out.println("Ese dia fue un martes");
			break;
		case 3:
			// SI DIA ES IGUAL A 3 ENTONCES: ES MIERCOLES
			System.out.println("Ese dia fue un miercoles");
			break;
		case 4:
			// SI DIA ES IGUAL A 4 ENTONCES: ES JUEVES
			System.out.println("Ese dia fue un jueves");
			break;
		case 5:
			// SI DIA ES IGUAL A 5 ENTONCES: ES VIERNES
			System.out.println("Ese dia fue un viernes");
			break;
		case 6:
			// SI DIA ES IGIAL A 6 ENTONCES: ES SABADO
			System.out.println("Ese dia fue un sabado");
			break;
		case 7:
			// SI DIA ES IGUAL A 7 ENTONCES: ES DOMINGO
			System.out.println("Ese dia fue un domingo");
			break;
		}
	}


}

