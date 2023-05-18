/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "COMPARACIONES.java."

import java.io.*;

public class comparaciones {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_a;
		double v_b;
		double v_c;
		// ENUNCIADO=Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos
		// HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA: 26/02/2023
		// VERSION=1.1
		// DEFINICION
		// VARIABLE QUE ALMACENA EL PRIMER NUMERO
		// VARIABLE QUE ALMACENA EL SEGUNDO NUMERO
		// VARIABLE QUE ALMACENA EL TERCER NUMERO
		// VALOR INICIAL:
		v_a = 0.0;
		v_b = 0.0;
		v_c = 0.0;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("escriba numero 1");
		v_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escriba numero 2");
		v_b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escriba numero 3");
		v_c = Double.parseDouble(bufEntrada.readLine());
		// PROCESO
		// SALIDA
		// SE DECIDE SEGUN SI EL PRIMER NUMERO ES MENOR AL SEGUNDO NUMERO PARA DECIDIR CUAL ES EL MAOR
		if (v_a<v_b) {
			// SE DECIDE SEGUN SI EL SEGUNDO NUMERO ES MENOR AL TRECER NUMERO PARA DECIDIR CUAL ES EL MAOR
			if (v_b<v_c) {
				// EL TERCER NUMERO ES EL MAYOR
				System.out.println("C="+v_c);
			} else {
				// EL SEGUNDO NUMERO ES EL MAYOR
				System.out.println("B="+v_b);
			}
		} else {
			// SE DECIDE SEGUN SI EL PRIMER NUMERO ES MENOR AL TERCER NUMERO PARA DECIDIR CUAL ES EL MAOR
			if (v_a<v_c) {
				// EL TERCER NUMERO ES EL MAYOR
				System.out.println("C="+v_c);
			} else {
				// EL PRIMER NUMERO ES EL MAYOR
				System.out.println("A="+v_a);
			}
		}
		// FIN
	}


}

