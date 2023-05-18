/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SOLUCION_ECUACION.java."

import java.io.*;
import java.math.*;

public class solucion_ecuacion {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_a;
		double v_b;
		double v_c;
		double v_d;
		double v_i;
		double v_r;
		double v_x1;
		double v_x2;
		// ENUNCIADO=Pseudocódigo que nos permita calcular las soluciones de una ecuación de segundo grado, incluyendo los valores imaginarios
		// Definir 
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE A
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE B
		// VARIABLE QUE ALMACENA EL VALOR INTRODUCIDO DE C
		// VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION R
		// VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION I
		// VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION X1, PRIMER CORTE CON EL EJER X
		// VARIABLE QUE ALMACENA EL RESULTADO DE LA OPERACION X2, SEGUNDO CORTE CON EL EJE X
		// VALOR INICIAL:
		v_a = 0.0;
		v_b = 0.0;
		v_c = 0.0;
		v_r = 0.0;
		v_i = 0.0;
		v_x1 = 0.0;
		v_x2 = 0.0;
		// INTRODUCCION DE DATOS
		System.out.println("escribe el coeficiente a");
		v_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escribe el coeficiente b");
		v_b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("escribe el coeficiente c");
		v_c = Double.parseDouble(bufEntrada.readLine());
		// PROCESO Y SALIDA
		// SE DECIDE SI EL VALOR DE A ES DIFERENTE DE CERO
		if (v_a!=0) {
			// PARA OBTENER LA V_D ENTONCES: (EL VALOR B SE MULTIPLICA POR EL VALOR B) SE RESTA CON 4 Y SE MULTIPLICA POR EL VALOR A Y EL VALOR C
			v_d = (v_b*v_b)-4*v_a*v_c;
			// SE DECIDE SI V_D ES DIFERENTE DE CERO
			if (v_d!=0) {
				// SE DECIDE SI V_D ES MAYOR A CERO
				if (v_d>0) {
					// PARA OBTENER EL PRIMER CORTE DE X : ((SE LE SACA RAIZ CUADRADA A V_D) SE LE SUMA EL VALOR DE B CON EL SIGNO CONTARIO) SE DIVIDE ENTRE (2 MULTIPLICADO POR EL VALOR DE A)
					v_x1 = (-v_b+Math.sqrt(v_d))/(2*v_a);
					// PARA OBTENER EL SEGUNDO CORTE DE X : ((SE LE SACA RAIZ CUADRADA A V_D) SE LE RESTA EL VALOR DE B CON EL SIGNO CONTARIO) SE DIVIDE ENTRE (2 MULTIPLICADO POR EL VALOR DE A)
					v_x2 = (-v_b-Math.sqrt(v_d))/(2*v_a);
					System.out.println("x1="+v_x1);
					System.out.println("x2="+v_x2);
					// SI EL VALOR DE V_D ES MENOR A CERO ENTONCES:
				} else {
					// PARA OBTENER V_R: (EL VALOR DE B CON SIGNO CONTRARIO) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A)
					v_r = (-v_b)/(2*v_a);
					// PARA OBTENER V_I: (VALOR ABSOLUTO DEL VALOR B) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A) SE LE SACA RAIZ CUADRADA
					v_i = Math.sqrt(Math.abs(v_d))/(2*v_a);
					System.out.println(v_r+"+"+v_i+"i");
					System.out.println(v_r+"-"+v_i+"i");
				}
				// SI EL VALOR DE V_D ES IGUAL A CERO ENTONCES:
			} else {
				// PARA OBTENER EL PRIMER CORTE X: (VALOR DE B CON EL SIGNO CONTRARIO) DIVIDIDO ENTRE (2 MULTIPLICADO POR VALOR DE A)
				v_x1 = -v_b/(2*v_a);
				// EL SEGUNDO CORTE ES IGUAL AL PRIMER CORTE
				v_x2 = v_x1;
				System.out.println("x1="+v_x1);
				System.out.println("x2="+v_x2);
			}
		} else {
			// SI EL VALOR DE A ES IGUAL A CERO ENTONCES SE COMUNICA QUE NO ES UNA ECUACION DE SEGUNDO GRADO
			System.out.println("no es una ecuacion de segundo grado");
		}
	}


}

