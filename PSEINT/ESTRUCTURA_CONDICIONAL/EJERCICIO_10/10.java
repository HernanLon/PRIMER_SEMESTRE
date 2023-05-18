/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SALARIO.java."

import java.io.*;

public class salario {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_hes1;
		int v_hes2;
		int v_hes3;
		int v_hes4;
		int v_hs1;
		int v_hs2;
		int v_hs3;
		int v_hs4;
		String v_nom;
		double v_phe1;
		double v_phe2;
		double v_phe3;
		double v_phe4;
		double v_phn1;
		double v_phn2;
		double v_phn3;
		double v_phn4;
		double v_ps1;
		double v_ps2;
		double v_ps3;
		double v_ps4;
		double v_sm;
		double v_vh;
		// Enunciado: Encontrar el salario a pagar
		// Leer valores de la hora, la cantidad de horas normales de la semana 1, 2, 3 y 4
		// Pedir cada valor por teclado
		// y calcular el salario a pagar
		// dDESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELES
		// vVERSION: 1.0
		// FECHA: 22/02/2023
		// DECLARAR:
		// nombre del empleado
		// valor hora
		// cantidad horas primera semana
		// cantidad horas segunda semana
		// cantidad horas tercera semana
		// cantidad horas cuarta semana
		// pago por horas normales de la primera semana
		// pago por horas normales de la segunda semana
		// pago por horas normales de la tercera semana
		// pago por horas normales de la cuarta semana
		// cantidad horas extraordinarias primera semana
		// cantidad horas extraordinarias segunda semana
		// cantidad horas extraordinarias tercera semana
		// cantidad horas extraordinarias cuarta semana
		// pago por horas extraordinarias de la primera semana
		// pago por horas extraordinarias de la segunda semana
		// pago por horas extraordinarias de la tercera semana
		// pago por horas extraordinarias de la cuarta semana
		// pago primera semana
		// pago segunda semana
		// pago tercera semana
		// pago cuarta semana
		// salario mensual
		// VALOR INICIAL
		v_nom = "";
		v_vh = 0.0;
		v_phn1 = 0.0;
		v_phn2 = 0.0;
		v_phn3 = 0.0;
		v_phn4 = 0.0;
		v_phe1 = 0.0;
		v_phe2 = 0.0;
		v_phe3 = 0.0;
		v_phe4 = 0.0;
		v_ps1 = 0.0;
		v_ps2 = 0.0;
		v_ps3 = 0.0;
		v_ps4 = 0.0;
		v_sm = 0.0;
		v_hs1 = 0;
		v_hs2 = 0;
		v_hs3 = 0;
		v_hs4 = 0;
		v_hes1 = 0;
		v_hes2 = 0;
		v_hes3 = 0;
		v_hes4 = 0;
		// Entrada de datos
		System.out.println("Por favor escribir el nombre del empleado");
		v_nom = bufEntrada.readLine();
		System.out.println(v_nom);
		System.out.println("Por favor introdusca el valor de la hora");
		v_vh = Double.parseDouble(bufEntrada.readLine());
		System.out.println("El valor de la hora es");
		System.out.println(v_vh);
		System.out.println("Por favor introduzca la cantidad de horas trabajadas de la primera semana");
		v_hs1 = Integer.parseInt(bufEntrada.readLine());
		// Procesos y salidas
		// pago primera semana//
		// SE DECIDE SEGUN SI HORAS DE LA PRIMERA SEMANA SON MAYORES A 40
		if (v_hs1>40) {
			System.out.println("La cantidad de horas trabajadas normales es");
			System.out.println("40");
			// SI LAS HORAS DE LA PRIMERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
			v_hes1 = v_hs1-40;
			System.out.println("La cantidad de horas trabajadas extraordinarias es");
			System.out.println(v_hes1);
		} else {
			System.out.println("La cantidad de horas trabajadas normales es");
			// SI LAS HORAS DE LA PRIMERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
			System.out.println(v_hs1);
			System.out.println("La cantidad de horas trabajadas extraordinarias es");
			System.out.println(v_hes1);
		}
		// SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		if (v_hes1!=0) {
			System.out.println("El pago por horas normales en la primera semana es");
			// SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
			v_phn1 = v_vh*40;
			System.out.println(v_phn1);
		} else {
			System.out.println("El pago por horas normales en la primera semana es");
			// SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA PRIMERA SEMANA
			v_phn1 = v_vh*v_hs1;
			System.out.println(v_phn1);
		}
		// PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA PRIMERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
		v_phe1 = v_hes1*v_vh*(1.5);
		System.out.println("El pago por horas extraordinarias en la primera semana es");
		System.out.println(v_phe1);
		System.out.println("El pago de la primera semana es");
		// PARA OBTENER EL PAGO TOTAL DE LA PRIMERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
		v_ps1 = v_phe1+v_phn1;
		System.out.println(v_ps1);
		// pago segunda semana//
		System.out.println("Por favor introduzca la cantidad de horas trabajadas de la segunda semana");
		v_hs2 = Integer.parseInt(bufEntrada.readLine());
		// SE DECIDE SEGUN SI HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40
		if (v_hs2>40) {
			System.out.println("La cantidad de horas trabajadas normales en la segunda semana  es");
			System.out.println("40");
			// SI LAS HORAS DE LA SEGUNDA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
			v_hes2 = v_hs2-40;
			System.out.println("La cantidad de horas trabajadas extraordinarias en la segunda semana es");
			System.out.println(v_hes2);
		} else {
			System.out.println("La cantidad de horas trabajadas normales en la segunda semana es");
			// SI LAS HORAS DE LA SEGUNDA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
			System.out.println(v_hs2);
			System.out.println("La cantidad de horas trabajadas extraordinarias en la segunda semana es");
			System.out.println(v_hes2);
		}
		// SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		if (v_hes2!=0) {
			System.out.println("El pago por horas normales en la segunda semana es");
			// SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
			v_phn2 = v_vh*40;
			System.out.println(v_phn2);
		} else {
			System.out.println("El pago por horas normales en la segunda semana es");
			// SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA SEGUNDA SEMANA
			v_phn2 = v_vh*v_hs2;
			System.out.println(v_phn2);
		}
		// PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA SEGUNDA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
		v_phe2 = v_hes2*v_vh*(1.5);
		System.out.println("El pago por horas extraordinarias en la segunda semana es");
		System.out.println(v_phe2);
		System.out.println("El pago de la segunda semana es");
		// PARA OBTENER EL PAGO TOTAL DE LA SEGUNDA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
		v_ps2 = v_phe2+v_phn2;
		System.out.println(v_ps2);
		// pago tercera semana//
		System.out.println("Por favor introduzca la cantidad de horas trabajadas de la tercera semana");
		v_hs3 = Integer.parseInt(bufEntrada.readLine());
		// SE DECIDE SEGUN SI HORAS DE LA TERCERA SEMANA SON MAYORES A 40
		if (v_hs3>40) {
			System.out.println("La cantidad de horas trabajadas normales en la tercera semana  es");
			System.out.println("40");
			// SI LAS HORAS DE LA TERCERA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
			v_hes3 = v_hs3-40;
			System.out.println("La cantidad de horas trabajadas extraordinarias en la tercera semana es");
			System.out.println(v_hes3);
		} else {
			System.out.println("La cantidad de horas trabajadas normales en la tercera semana es");
			// SI LAS HORAS DE LA TERCERA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
			System.out.println(v_hs3);
			System.out.println("La cantidad de horas trabajadas extraordinarias en la tercera semana es");
			System.out.println(v_hes3);
		}
		// SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		if (v_hes3!=0) {
			System.out.println("El pago por horas normales en la tercera semana es");
			// SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
			v_phn3 = v_vh*40;
			System.out.println(v_phn3);
		} else {
			System.out.println("El pago por horas normales en la tercera semana es");
			// SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA TERCERA SEMANA
			v_phn3 = v_vh*v_hs3;
			System.out.println(v_phn3);
		}
		// PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA TERCERA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
		v_phe3 = v_hes3*v_vh*(1.5);
		System.out.println("El pago por horas extraordinarias en la tercera semana es");
		System.out.println(v_phe3);
		System.out.println("El pago de la tercera semana es");
		// PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
		v_ps3 = v_phe3+v_phn3;
		System.out.println(v_ps3);
		// pago cuarta semana//
		System.out.println("Por favor introduzca la cantidad de horas trabajadas de la cuarta semana");
		v_hs4 = Integer.parseInt(bufEntrada.readLine());
		// SE DECIDE SEGUN SI HORAS DE LA CUARTA SEMANA SON MAYORES A 40
		if (v_hs4>40) {
			System.out.println("La cantidad de horas trabajadas normales en la cuarta semana  es");
			System.out.println("40");
			// SI LAS HORAS DE LA CUARTA SEMANA SON MAYORES A 40: ENTONCES SE LE RESTA 40, PARA DARNOS LAS HORAS EXTRAS
			v_hes4 = v_hs4-40;
			System.out.println("La cantidad de horas trabajadas extraordinarias en la cuarta semana es");
			System.out.println(v_hes4);
		} else {
			System.out.println("La cantidad de horas trabajadas normales en la cuarta semana es");
			// SI LAS HORAS DE LA CUARTA SEMANA SON MENORES A 40: ENTONCES NO HAY HORAS EXTRAS
			System.out.println(v_hs4);
			System.out.println("La cantidad de horas trabajadas extraordinarias en la cuarta semana es");
			System.out.println(v_hes4);
		}
		// SE DECIDE SEGUN SI HAY O NO HORAS EXTRAS
		if (v_hes4!=0) {
			System.out.println("El pago por horas normales en la cuarta semana es");
			// SI HAY HORAS EXTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTOCES SE MULTIPLICA EL VALOR DE HORA POR 40
			v_phn4 = v_vh*40;
			System.out.println(v_phn4);
		} else {
			System.out.println("El pago por horas normales en la cuarta semana es");
			// SI NO HAY HORAS EXGTRAS, PARA OBTENER EL PAGO POR LAS HORAS COMUNES: ENTONCES SE MULTIPLICA EL VALOR HORA POR LAS HORAS DE LA CUARTA SEMANA
			v_phn4 = v_vh*v_hs4;
			System.out.println(v_phn4);
		}
		// PARA OBTENER EL PAGO DE LAS HORAS EXTRAS: SE MULTIPLICA LAS HORAS EXTRAS DE LA CUARTA SEMEMANA POR EL VALOR HORA POR 1.5 (150% = 1.5)
		v_phe4 = v_hes4*v_vh*(1.5);
		System.out.println("El pago por horas extraordinarias en la cuarta semana es");
		System.out.println(v_phe4);
		System.out.println("El pago de la tercera semana es");
		// PARA OBTENER EL PAGO TOTAL DE LA TERCERA SEMANA SE SUMA EL PAGO DE LAS HORAS EXTRAS CON EL PAGO DE LAS HORAS COMUNES
		v_ps4 = v_phe4+v_phn4;
		System.out.println(v_ps4);
		// pago total del mes
		System.out.println("El salario mensual es");
		// PARA OBTENER EL PAGO TOTAL DEL MES: SE SUMAN LOS PAGOS TOTALES DE LAS CUATRO SEMANAS
		v_sm = v_ps1+v_ps2+v_ps3+v_ps4;
		System.out.println(v_sm);
	}


}

