/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "TIEMPO.java."

import java.io.*;

public class tiempo {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double vf_vi;
		double v_a;
		double v_a2;
		int v_ma;
		int v_mvf;
		int v_mvi;
		double v_t;
		double v_vf;
		double v_vf2;
		double v_vi;
		double v_vi2;
		// ENUNCIADO:Un cuerpo posee una velocidad inicial de 12 m/s y una aceleración de 2 m/s2 ¿Cuánto tiempo tardará en adquirir una velocidad de 144 Km/h?
		// CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// VERSION=1.0
		// FECHA=22/02/2023
		// DEFINIR:
		// VARAIABLE QUE ALAMACENA EL VALOR DE VELOCIDAD INICIAL
		// VARAIBLE QUE ALAMACENA EL VALOR DE VELOCIDAD FINAL
		// VARIABLE QUE ALAMCENA EL VALOR DE ACELERACION
		// VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD INICIAL
		// VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD FINAL
		// VARIABLE QUE ALAMCENA LA MEDICION DE ACELERACION
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL EN M/S
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL EN M/S
		// VARIABLE QUE ALMACENA EL VALOR DE ACELERACION EN M/S2
		// VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE VF-VI
		// VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA, DE TIEMPO
		// VALOR INICIAL:
		v_vi = 0.0;
		v_vf = 0.0;
		v_a = 0.0;
		v_mvi = 0;
		v_mvf = 0;
		v_ma = 0;
		v_vi2 = 0.0;
		v_vf2 = 0.0;
		v_a2 = 0.0;
		vf_vi = 0.0;
		v_t = 0.0;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad inicial");
		v_vi = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println(" si velocidad inicial esta en m/s escriba 1 ó si esta en km/h escriba 2");
		v_mvi = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad final");
		v_vf = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si velocidad final esta en m/s escriba 1 ó si esta en km/h escriba 2");
		v_mvf = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribe aceleración");
		v_a = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si aceleracion esta en m/s2 escriba 1 ó si esta en km/h2 escriba 2");
		v_ma = Integer.parseInt(bufEntrada.readLine());
		System.out.println("-------------------------------------------------");
		// PROCESO
		// SE CONVIERTE KM/H A M/S DE VELOCIDAD INICIAL
		switch (v_mvi) {
		case 1:
			v_vi2 = v_vi;
			break;
		case 2:
			v_vi2 = v_vi/3.6;
			break;
		}
		// PROCESO
		System.out.println("velocidad inicial en m/s es:"+v_vi2+"m/s");
		// PROCESO
		// SE CONVIERTE KM/H A M/S DE VELOCIDAD FINAL
		switch (v_mvf) {
		case 1:
			v_vf2 = v_vf;
			break;
		case 2:
			v_vf2 = v_vf/3.6;
			break;
		}
		// PROCESO
		System.out.println("velocidad final en m/s es:"+v_vf2+"m/s");
		// PROCESO
		// SE CONVIERTE KM/H AL CUADRADO EN M/S AL CUADRADO  DE ACELERACION
		switch (v_ma) {
		case 1:
			v_a2 = v_a;
			break;
		case 2:
			v_a2 = v_a/12960;
			break;
		}
		// PROCESO
		System.out.println("aceleració en m/s2 es:"+v_a2+"m/s2");
		System.out.println("-------------------------------------------------");
		System.out.println("los resultados son:");
		// SALIDA
		// PARA OBTERNER LA VARIANLE VF_VI, SE RESTA VELOCIDAD FINAL CON VELOCIDAD INICIAL
		vf_vi = v_vf2-v_vi2;
		// PARA OBTENER TIEMPO, SE DIVIDE VF_VI ENTRE ACELERACION
		v_t = vf_vi/v_a2;
		// SALIDA
		System.out.println("el tiempo es:"+v_t+"seg");
		// FIN
	}


}

