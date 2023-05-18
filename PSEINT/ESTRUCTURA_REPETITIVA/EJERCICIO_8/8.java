/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SECUENCIA.java."

import java.io.*;

public class secuencia {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_c;
		double v_dato;
		double v_media;
		double v_s;
		// ENUNCIADO=Calcular la media de una serie de números positivos, suponiendo que los datos se leen desde un terminal. 
		// Un valor de cero ?como entrada? indicará que se ha alcanzado el final de la serie de números positivos.
		// CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA: 26/02/2023
		// VERSION= 1.1
		// definir=
		// VARIABLE DE ENTRADA QUE CUENTA LOS NUMEROS
		// VARIABLE DE ENTRADA QUE SUMA LOS NUMEROS
		// VARIABLE DE PROCESO QUE ALMACENA EL NUMERO ESCRITO
		// VARIABLE DE SALIDA QUE ALMACENA LA MEDIA
		// VALOR INICIAL:
		v_c = 0;
		v_s = 0.0;
		v_dato = 0.0;
		v_media = 0.0;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("Datos nuemricos, para finalizar se introduce 0");
		// PROCESO
		// SE REPITE EL PROCESO DE CONTAR CUANTOS NUMEROS SE INGRESAN, DE SUMAR TODOS LOS NUMERO INGRESADOS Y SE DIVIDE LA SUMA DE LOS NUMEROS ENTRE LA CANTIDAD DE NUMEROS INGRESADOS, HASTA QUE SE INGRESE UN VALOR IGUAL A CERO
		do {
			v_dato = Double.parseDouble(bufEntrada.readLine());
			if (v_dato!=0) {
				// SE CUENTAN CUANTOS NUMEROS SE INGRESAN
				v_c = v_c+1;
				// SE SUMAN TODOS LOS NUMEROS INGRESADOS
				v_s = v_s+v_dato;
			} else {
				// PARA OBTENER LA MEDIA: SE DIVIDE LA SUMA DE LOS NUMEROS INGRESADOS ENTRE LA CANTIDAD DE NUMEROS INGRESADOS
				v_media = v_s/v_c;
				System.out.println(v_media);
			}
			// EL PROCESO DE REPETIR SE TERMINA CUANDO SE INGRESA UN VALOR IGUAL A CERO
		} while (v_dato!=0);
		// SALIDA
		System.out.println("-------------------------------------");
		System.out.println("la media es="+v_media);
	}


}

