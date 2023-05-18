/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "RESOL1.java."

import java.io.*;

public class resol1 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double b;
		double v_a;
		double v_b;
		double v_x;
		// Resolución de una ecuación de primer grado.
		// FECHA:03/03/2023
		// VERSION= 1.0
		// CREADO POR: Hernan Alberto Londoño Velez
		// DEFINIR VARIABLES=
		// VARIABLE QUE ALMACENA EL VALOR DE A
		// VARIABLE QUE ALMACENA EL VALOR DE B
		// VARIABLE QUE ALMACENA UN RESULTADO DE UNA OPERACION 
		// VALOR INICIAL
		v_a = 0;
		v_b = 0;
		v_x = 0;
		// INICIO=
		System.out.println("escriba (a) de la ecuacion ax+b=0");
		v_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escriba (b) de la ecuacion ax+b=0");
		v_b = Double.parseDouble(bufEntrada.readLine());
		// PROCESO
		// SALIDA
		// SE DECIDE SI EL VALOR DE A ES DIFERENTE DE CERO
		if (v_a!=0) {
			// SI EL VALOR A ES DIFERENTE DE CERO: EL VALOR B SE DIVIDE ENTRE EL VALOR A
			v_x = -v_b/v_a;
			System.out.println("X es="+v_x);
		} else {
			// SE DECIDE SI EL VALOR B ES DIFERENTE DE CERO
			if (b!=0) {
				// SI EL VALOR B ES DIFERENTE DE CERO ENTONCES LA SOLUCION ES IMPOSIBLE
				System.out.println("Solucion imposible");
			} else {
				// SI EL VALOR DE B ES IGUAL A CERO ENTONCES LA SOLUCION ES INDETERMINADA
				System.out.println("Solucion indeterminada");
			}
		}
		// FIN
	}


}

