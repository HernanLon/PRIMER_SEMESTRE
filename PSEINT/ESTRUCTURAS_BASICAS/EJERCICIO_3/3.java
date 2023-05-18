/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "ACELERACION_DISTANCIA.java."

import java.io.*;

public class aceleracion_distancia {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double vf_vi;
		double v_a;
		double v_d;
		int v_mt;
		int v_mvf;
		int v_mvi;
		double v_t;
		double v_t2;
		double v_vf;
		double v_vf2;
		double v_vi;
		double v_vi2;
		// VERSION=1.0
		// FECHA=22/02/2023
		// ENUNCIADO:Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
		// Suponiendo que su movimiento es uniformemente acelerado ¿Qué aceleración se le ha comunicado y qué espacio ha recorrido antes de alcanzar la velocidad regular?
		// HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
		// FECHA: 20/02/2023
		// VERSION: 1.0
		// DEFINICION:
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL
		// VARIABLE QUE ALMACENA EL VALOR DE TIEMPO
		// VARIABLE QUE ALAMCENA LA MEDICION DE VELOCIDAD INICIAL
		// VARIABLE QUE ALAMCENA LA MEDICION DE VELOCIDAD FINAL
		// VARIABLE QUE ALAMCENA LA MEDICION DE TIEMPO
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL EN M/S
		// VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL EN M/S
		// VARIABLE QUE ALMACENA TIEMPO EN SEGUNDOS.
		// VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE VF-VI
		// VARAIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE ACELERACION
		// VARAIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE DIATANCIA
		// VALOR INICA:
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
		v_d = 0.0;
		// INICIO
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad inicial");
		v_vi = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println(" si velocidad inicial esta en m/s escriba 1 o si esta en km/h escriba 2");
		v_mvi = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribe velocidad final");
		v_vf = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si velocidad final esta en m/s escriba 1 o si esta en km/h escriba 2");
		v_mvf = Integer.parseInt(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("escribe tiempo");
		v_t = Double.parseDouble(bufEntrada.readLine());
		// ENTRADA DE DATOS
		System.out.println("si tiempo esta en segundos escriba 1, si esta en minutos escriba 2, si esta en horas escriba 3");
		v_mt = Integer.parseInt(bufEntrada.readLine());
		System.out.println("-------------------------------------------------");
		// PROCESO
		// SE CONVIERTE LOS KM/H A M/S DE VELOCIDAD INICIAL
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
		// SE CONVIERTE LOS KM/H A M/S DE VELOCIDAD FINAL
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
		// SE CONVIERTE LAS HORAS Y MINUTOS A SEGUNDOS DEL TIEMPO
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
		System.out.println("tiempo en segundo es:"+v_t2+"seg");
		System.out.println("-------------------------------------------------");
		System.out.println("los resulatdos son:");
		// SALIDA
		// SE RESTA VELOCIDAD FINAL (EN SEGUNDOS) CON VELOCIDAD FINAL (EN SEGUNDOS) PARA OBTENER LA VARIABLE VF_VI
		vf_vi = v_vf2-v_vi2;
		// SE DIVIDE LA VARIABLE VF_VI ENTRE EL TMEPO (EN SEGUNDOS) PARA OBTENER ACELERACION
		v_a = vf_vi/v_t2;
		// SALIDA
		// PARA OBTENER TIEMPO AL CUADRADO, SE MULTIPLICA TIEMPO POR TIEMPO
		v_t2 = v_t2*v_t2;
		// PARA OBTENER DISTANCIA, SE DIVIDE ACELERACION ENTRE TIEMPO AL CUADRADO
		v_d = v_a*v_t2/2;
		// SALIDA
		System.out.println("la aceleracion es:"+v_a+"m/s2");
		System.out.println("la distancia es:"+v_d+"m");
		// FIN
	}


}

