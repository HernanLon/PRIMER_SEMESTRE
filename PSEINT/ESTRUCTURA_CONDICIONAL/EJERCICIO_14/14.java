/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "ECUACION_CUADRATICA_EJERCICIO_3_17.java."

import java.io.*;
import java.math.*;

public class ecuacion_cuadratica_ejercicio_3_17 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_a;
		double v_b;
		double v_c;
		double v_ejes;
		double v_very;
		double v_x1;
		double v_x2;
		double v_y;
		// Enunciado: Encontrar las coordenadas en el plano carteciano x,y para graficar una ecuacion cuadratica o de sgundo grado
		// Leer valores de a, b y c
		// Pedir cada valor por teclado
		// DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// VERSION: 1.0
		// FACHA: 22/02/2023
		// DECLARAR:
		// Variable de entrada que almacena el valor de a
		// Variable de entrada que almacena el valor de b
		// Variable de entrada que almacena el valor de c
		// Variable de proceso y salida que almacena el primer corte con x
		// Variable de proceso y salida que almacena el segundo corte con x
		// Variable de proceso y salida que almacena el corte con y
		// Variable de proceso y salida que almacena las coordenadas del vértice en y
		// Variable de proceso y salida que almacena las coordenadas del eje de simetría 
		// VALOR INICAIL:
		v_a = 0.0;
		v_b = 0.0;
		v_c = 0.0;
		v_x1 = 0.0;
		v_x2 = 0.0;
		v_y = 0.0;
		v_very = 0.0;
		v_ejes = 0.0;
		// ENTRADA DE DATOS:
		System.out.println("Ecuacion ax²+ bx + c");
		System.out.println("Por favor escribir el valor de a");
		v_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Por favor escribir el valor de b");
		v_b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Por favor escribir el valor de c");
		v_c = Double.parseDouble(bufEntrada.readLine());
		// procesos y salidas
		// SE DECIDE SEGUN SI EL VALOR B ELEVADO A LA POTENCIA 2-4 MULTIPLICADO POR EL VALOR A Y MULTIPLICADO POR EL VALOR C GENERA UN RESULTADO MAYOR A CERO
		if (Math.pow(v_b,2)-4*v_a*v_c>0) {
			// SI LA ANTERIOR ENCUACION ES MAYOR A CERO ENTONCES:
			System.out.println("el primer corte con x es");
			// PARA OBTENER EL PRIMER CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNO ANTES DE LA RAIZ ES POSITIVO
			v_x1 = -(-v_b+Math.sqrt(Math.pow(v_b,2)-4*v_a*v_c))/2*v_a;
			System.out.println("("+v_x1+",0"+")");
			System.out.println("Elsegundo corte con x es");
			// PARA OBTENER EL SEGUNDO CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNOANTES DE LA RAIZ ES NEGATIVO
			v_x2 = -(-v_b-Math.sqrt(Math.pow(v_b,2)-4*v_a*v_c))/2*v_a;
			System.out.println("("+v_x2+",0"+")");
		} else {
			// SI LA CONDICION DE LA ECUACION NO ES MAYOR A CERO ENTONCES:
			System.out.println("Las raices son imaginarias");
			// SE REALIZA LA OPERACION EXPUESTA, YA QUE LAS RAICES SON IMAGINARIAS
			System.out.println(-v_b/(2*v_a)+"+"+(Math.sqrt(Math.abs(Math.pow(v_b,2)-4*v_a*v_c)))/2*v_a+"i");
			// SE REALIZA LA OPERACION EXPUESTA YA QUE LAS RAICES SON IMAGINARIAS
			System.out.println(-v_b/(2*v_a)+"-"+(Math.sqrt(Math.abs(Math.pow(v_b,2)-4*v_a*v_c)))/2*v_a+"i");
		}
		// se emplea el condicional si para encontrar los cortes con el eje x pero si el resultado al que hay que sacar raiz cruadrada es negativo el resultado son numeros imaginarios
		System.out.println("el corte con y es");
		// PARA OBTENER EL CORTE Y: SE REALIZA LA OPERACION EXPUESTA
		v_y = v_a*Math.pow((0),2)+v_b*(0)+v_c;
		System.out.println("("+"0,"+v_y+")");
		// se halla el corte con y en cordendas x,y por eso 0,y
		System.out.println("El eje de simetría es");
		// PARA OBTENER LAS COORDENADAS DEL EJE DE SIMETRIA: SE DIVIDE EL VALOR B ENTRE 2 Y SE MULTIPLICA POR EL VALOR A
		v_ejes = -v_b/2*v_a;
		System.out.println(v_ejes);
		System.out.println("El vertice en y es");
		// PARA OBTENER LAS COORDENADAS DEL VERTICE EN Y: SE REALIZA LA OPERACION EXPUESTA
		v_very = v_a*Math.pow((v_ejes),2)+v_b*(v_ejes)+v_c;
		System.out.println(v_very);
		System.out.println("Elvertice en coordenadas (x,y) es");
		System.out.println("("+v_ejes+","+v_very+")");
		// SE DECIDE SEGUN SI EL VALOR DE A ES MAYOR A CERO
		if (v_a>0) {
			// SI EL VALOR A ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ARRIVA
			System.out.println("La funcion es concava hacia arriba");
		} else {
			// SI EL VALOR A NO ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ABAJO
			System.out.println("la funcion es concava hacia abajo");
		}
		// se emplea el condicional si poara saber hacia donde es concava la funcion y poder graficar 
	}


}

