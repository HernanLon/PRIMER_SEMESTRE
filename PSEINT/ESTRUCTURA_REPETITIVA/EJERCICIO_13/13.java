/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "NATURALES.java."

import java.io.*;

public class naturales {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_n;
		int v_p;
		// Enunciado=Escribir un algoritmo que calcule el producto de los n primeros números naturales.
		// CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA: 26/02/2023
		// VERSION=1.1
		// DEFINIR:
		// VARIABLE QUE ALMACENA EL NUMERO NATURAL.
		// VARIABLE QUE ALMACENA EL PRODUCTO O FACTORIAL.
		// VALOR INICIAL:
		v_n = 0;
		v_p = 1;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("Escriba un numero natura");
		v_n = Integer.parseInt(bufEntrada.readLine());
		// PROCESO
		// SE DECIDE SEGUN SI EL NUMERO INTRODUCIDO ES IGUAL A CERO
		if (v_n==0) {
			// SI EL NUMERO ES IGUAL A CERO SE GENERA UN AVISO QUE COMUNICA QUE EL FACTORIAL CERO ES IGUAL A 1
			System.out.println("Factorial de 0 igual a 1");
			// SI EL NUMERO ES DIFERENTE DE CERO ENTONCES:
		} else {
			// SI EL NUMERO ES MAYOR A CERO: EL VALOR DEL FACTORIAL SIGUE SIENDO UNO
			if (v_n>0) {
				v_p = 1;
				// SI EL NUMERO NO ES IGUAL O MAYOR A CERO, QUIERE DECIR QUE ES NEGATIVO ENTONCES: SE GENERA UN AVISO QUE COMUNICA QUE EL NUMERO ES NEGATIVO
			} else {
				System.out.println("Numero negativo");
			}
		}
		// PROCESO EN EL CUAL PARA OBTENER EL PRODUCTO SE MULTIPLICA EL PROMEDIO ANTERIOR POR EL NUMERO Y SE LE RESTA 1 AL NUMERO INTRODUCIDO Y SE FINALISA ELPROCESO CUANDO EL NUMERO QUEDE IGUAL A 1
		do {
			// PARA OBTENER EL PRODUCTO SE MULTIPLICA EL PRODUCTO ANTERIOR POR EL NUMERO 
			v_p = v_p*v_n;
			// SE LE RESTA 1 AL NUMERO 
			v_n = v_n-1;
			// SE FINALISA ELPROCESO CUANDO EL NUMERO QUEDE IGUAL A 1
		} while (v_n!=1);
		// SALIDA
		System.out.println("Factorial="+v_p);
		// FIN
	}


}

