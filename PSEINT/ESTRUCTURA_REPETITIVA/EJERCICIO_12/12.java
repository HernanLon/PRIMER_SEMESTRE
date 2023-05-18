/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SUMA_.java."

import java.io.*;

public class suma_ {

	public static void main(String args[]) {
		int v_n;
		int v_suma;
		// Enunciado: Encontrar el valor de la suma consecutiva de los numeros enteros positivos del 1 al 50
		// DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// VERSION: 1.0
		// FECHA: 22/02/2023
		// DECLARAR:
		// VARIABLE QUE ALAMCENA EL VALOR DE CADA NUMERO DEL 1 AL 50
		// VARAIABLE QUE ALMACENA EL VALOR DE LA SUMA DE LOS NUMEROS DEL 1 AL 50
		// VALOR INICIAL:
		v_n = 1;
		v_suma = 0;
		// procesos y salidas
		System.out.println("Lista de numeros sumados");
		// PROCESO EN LE CUAL SE SELECCIONA CADA NUMERO DESDE EL 1 HASTA EL 50
		for (v_n=1;v_n<=50;v_n++) {
			System.out.println(v_n);
			// SE SUMA CADA NUMERO DESDE EL 1 HASTA EL 50
			v_suma = v_suma+v_n;
		}
		System.out.println("El resultado de la suma es "+v_suma);
	}


}

