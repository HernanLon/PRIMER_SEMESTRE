/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "PARES.java."

import java.io.*;

public class pares {

	public static void main(String args[]) {
		int v_n;
		int v_suma;
		// Enunciado: Encontrar el valor de la suma de los numeros enteros psositivos pares del 2 al 100
		// desarrollado por: HERNAN ALBERTO LONDOÑO VELEZ
		// version 1.0
		// fecha 22/02/2023
		// DEFINIR:
		// VARIABLE QUE ALMACENA CADA NUMERO PAR DESDE EL 2 HASTA EL 100.
		// VARIABLE QUE ALMACENA UNA RESPUESTA DE UNA ECUACION ARITMETICA, SUMA DE LOS NUMEROS.
		// VALOR INICIAL:
		v_n = 2;
		v_suma = 0;
		// PROCESO Y SALIDA
		System.out.println("Lista de numeros sumados");
		// PRECESO EN EL CUAL SOLO SE SELECCIONA LOS NUMERO DE DOS EN DOS DESDE EL 2 HASTA EL 100, (NUMERO PARES)
		for (v_n=2;v_n<=100;v_n+=2) {
			System.out.println(v_n);
			// SE SUMAN SOLO LOS NUMEROS PARES DESDE EL 2 HASTA EL 100
			v_suma = v_suma+v_n;
		}
		System.out.println("El resultado de la suma es "+v_suma);
	}


}

