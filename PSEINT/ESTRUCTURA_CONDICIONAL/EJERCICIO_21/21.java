/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "MAYOR_.java."

import java.io.*;

public class mayor_ {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_a;
		double v_b;
		double v_c;
		double v_mayor;
		// ENUNCIADO=6.  Pag 146.  EJEMPLO 4.15 Diseñar un programa que lea tres números A, B, C y visualice en pantalla el valor del más grande. 
		// Se supone que los tres valores son diferentes.
		// HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA:03/03/2023
		// VERSION: 1.0
		// Definir 
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE A
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE B
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE C
		// VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION
		// VALOR INICIAL:
		v_a = 0.0;
		v_b = 0.0;
		v_c = 0.0;
		v_mayor = 0.0;
		// INTRODUCCION DE INFORMACION
		System.out.println("escribir el primer numero");
		v_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escribe el segundo numero");
		v_b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escribe el tercer numero");
		v_c = Double.parseDouble(bufEntrada.readLine());
		// PROCESO Y SALIDA
		// SE DECIDE SI EL VALOR DE A ES MAYOR QUE EL VALOR DE B PARA OBTENER EL NUMERO MAYOR
		if (v_a>v_b) {
			// SE DECIDE SI EL VALOR DE A ES MAYOR QUE EL VALOR DE C PARA OBTENER EL NUMERO MAYOR
			if (v_a>v_c) {
				// EL NUMERO MAYOR ES EL VALOR DE A
				v_mayor = v_a;
			} else {
				// EL NUMERO MAYOR ES EL VALOR DE C
				v_mayor = v_c;
			}
		} else {
			// SE DECIDE SI EL VALOR DE B ES MAYOR QUE LE VALOR DE C PARA OBTENER EL NUMERO MAYOR
			if (v_b>v_c) {
				// EL NUMERO MAYOR ES EL VALOR DE B
				v_mayor = v_b;
			} else {
				// EL NUMERO MAYOR ES EL VALOR DE C
				v_mayor = v_c;
			}
		}
		System.out.println("el numero mayor es="+v_mayor);
	}


}

