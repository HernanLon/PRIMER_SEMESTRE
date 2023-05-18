/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "ACELERACION1.java."

import java.io.*;

public class aceleracion1 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double vf_vi;
		double v_a;
		int v_mt;
		int v_mvf;
		int v_mvi;
		double v_t;
		double v_t2;
		double v_vf;
		double v_vf2;
		double v_vi;
		double v_vi2;
		// enunciado=Un camión circula por una carretea a 20m/s . En 5 s , su velocidad pasa a ser de 25 m/s ¿ cuál ha sido su aceleración ?
		// CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA:20/02/2023
		// VERSION: 1.0
		// DEFINICION:
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL
		// VARIABLE QUE ALMACENA EL VALOR DE TIEMPO
		// VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD INICIAL
		// VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD FINAL
		// VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE TIEMPO
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL EN M/S
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL EN M/S
		// VARIABLE QUE ALMACENA TIEMPO EN SEGUNDOS
		// VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE VF-VI
		// VARAIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE ACELERACION
		// VALOR INICIAL
		v_vi = 0.0;
		v_vf = 0.0;
		v_t = 0.0;
		v_mvi = 0;
		v_mvf = 0;
		v_mt = 0;
		v_vi2 = 0.0;
		v_vf2 = 0.0;
		v_t2 = 0.0;
		vf_vi = 0.0;
		v_a = 0.0;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad inicial");
		v_vi = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si velocidad inicial esta en m/s escriba 1, si esta en km/h escriba 2");
		v_mvi = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad final");
		v_vf = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si velocidad final esta en m/s escriba 1, si esta en km/h escriba 2");
		v_mvf = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribir tiempo");
		v_t = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si tiempo esta en segundos escriba 1, si esta en minutos escriba 2, si esta en horas escriba 3");
		v_mt = Integer.parseInt(bufEntrada.readLine());
		System.out.println("-------------------------------------------------");
		// PROCESO
		// SE CONVIERTE LOS KM/H A M/S DE LA VELOCIDAD INICIAL
		switch (v_mvi) {
		case 1:
			v_vi2 = v_vi;
			break;
		case 2:
			v_vf2 = v_vi*1000/3600;
			break;
		}
		// PROCESO
		System.out.println("velocidad inicial en m/s es:"+v_vi2);
		// PROCESO
		// SE CONVIERTE LOS KM/H A M/S DE LA VELOCIDAD FINAL
		switch (v_mvf) {
		case 1:
			v_vf2 = v_vf;
			break;
		case 2:
			v_vf2 = v_vf*1000/3600;
			break;
		}
		// PROCESO
		System.out.println("velocidad final en m/s es:"+v_vf2);
		// PROCESO
		// SE CONVIERTEN LAS HORAS Y MINUTOS A SEGUNDOS DEL TIEMPO
		switch (v_mt) {
		case 1:
			v_t2 = v_t;
			break;
		case 2:
			v_t2 = v_t*60;
			break;
		case 3:
			v_t2 = v_t*3600;
			break;
		}
		// PROCESO
		System.out.println("tiempo en segundos es:"+v_t2);
		System.out.println("----------------------------------------------------");
		// SALIDA
		System.out.println("las soluciones son:");
		// SALIDA
		// SE RESTA VELOCIDAD FINAL (EN M/S) CON VELOCIDAD INICIAL (EN M/S)
		vf_vi = v_vf2-v_vi2;
		// SE DIVIDE EL RESULTADO DE LA RESTA ANTERIOR ENTRE TIEMPO (EN SEGUNDOS) PARA OBTENER LA ACELERACION
		v_a = vf_vi/v_t2;
		// SALIDA
		System.out.println("la aceleracion es:"+v_a+"m/s2");
		// FIN
	}


}

