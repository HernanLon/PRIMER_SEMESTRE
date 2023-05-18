# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Enunciado: Encontrar las coordenadas en el plano carteciano x,y para graficar una ecuacion cuadratica o de sgundo grado
	# Leer valores de a, b y c
	# Pedir cada valor por teclado
	# DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# VERSION: 1.0
	# FACHA: 22/02/2023
	# DECLARAR:
	# Variable de entrada que almacena el valor de a
	v_a = float()
	# Variable de entrada que almacena el valor de b
	v_b = float()
	# Variable de entrada que almacena el valor de c
	v_c = float()
	# Variable de proceso y salida que almacena el primer corte con x
	v_x1 = float()
	# Variable de proceso y salida que almacena el segundo corte con x
	v_x2 = float()
	# Variable de proceso y salida que almacena el corte con y
	v_y = float()
	# Variable de proceso y salida que almacena las coordenadas del vértice en y
	v_very = float()
	# Variable de proceso y salida que almacena las coordenadas del eje de simetría 
	v_ejes = float()
	# VALOR INICAIL:
	v_a = 0.0
	v_b = 0.0
	v_c = 0.0
	v_x1 = 0.0
	v_x2 = 0.0
	v_y = 0.0
	v_very = 0.0
	v_ejes = 0.0
	# ENTRADA DE DATOS:
	print("Ecuacion ax²+ bx + c")
	print("Por favor escribir el valor de a")
	v_a = float(input())
	print("Por favor escribir el valor de b")
	v_b = float(input())
	print("Por favor escribir el valor de c")
	v_c = float(input())
	# procesos y salidas
	# SE DECIDE SEGUN SI EL VALOR B ELEVADO A LA POTENCIA 2-4 MULTIPLICADO POR EL VALOR A Y MULTIPLICADO POR EL VALOR C GENERA UN RESULTADO MAYOR A CERO
	if v_b**2-4*v_a*v_c>0:
		# SI LA ANTERIOR ENCUACION ES MAYOR A CERO ENTONCES:
		print("el primer corte con x es")
		# PARA OBTENER EL PRIMER CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNO ANTES DE LA RAIZ ES POSITIVO
		v_x1 = -(-v_b+sqrt(v_b**2-4*v_a*v_c))/2*v_a
		print("(",v_x1,",0",")")
		print("Elsegundo corte con x es")
		# PARA OBTENER EL SEGUNDO CORTE X: SE REALIZA LA OPEACION EXPUESTA, SOLO QUE AQUI EL SIGNOANTES DE LA RAIZ ES NEGATIVO
		v_x2 = -(-v_b-sqrt(v_b**2-4*v_a*v_c))/2*v_a
		print("(",v_x2,",0",")")
	else:
		# SI LA CONDICION DE LA ECUACION NO ES MAYOR A CERO ENTONCES:
		print("Las raices son imaginarias")
		# SE REALIZA LA OPERACION EXPUESTA, YA QUE LAS RAICES SON IMAGINARIAS
		print(-v_b/(2*v_a),"+",(sqrt(abs(v_b**2-4*v_a*v_c)))/2*v_a,"i")
		# SE REALIZA LA OPERACION EXPUESTA YA QUE LAS RAICES SON IMAGINARIAS
		print(-v_b/(2*v_a),"-",(sqrt(abs(v_b**2-4*v_a*v_c)))/2*v_a,"i")
	# se emplea el condicional si para encontrar los cortes con el eje x pero si el resultado al que hay que sacar raiz cruadrada es negativo el resultado son numeros imaginarios
	print("el corte con y es")
	# PARA OBTENER EL CORTE Y: SE REALIZA LA OPERACION EXPUESTA
	v_y = v_a*(0)**2+v_b*(0)+v_c
	print("(","0,",v_y,")")
	# se halla el corte con y en cordendas x,y por eso 0,y
	print("El eje de simetría es")
	# PARA OBTENER LAS COORDENADAS DEL EJE DE SIMETRIA: SE DIVIDE EL VALOR B ENTRE 2 Y SE MULTIPLICA POR EL VALOR A
	v_ejes = -v_b/2*v_a
	print(v_ejes)
	print("El vertice en y es")
	# PARA OBTENER LAS COORDENADAS DEL VERTICE EN Y: SE REALIZA LA OPERACION EXPUESTA
	v_very = v_a*(v_ejes)**2+v_b*(v_ejes)+v_c
	print(v_very)
	print("Elvertice en coordenadas (x,y) es")
	print("(",v_ejes,",",v_very,")")
	# SE DECIDE SEGUN SI EL VALOR DE A ES MAYOR A CERO
	if v_a>0:
		# SI EL VALOR A ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ARRIVA
		print("La funcion es concava hacia arriba")
	else:
		# SI EL VALOR A NO ES MAYOR A CERO SE INDICA QUE LA FUNCION ES HACIA ABAJO
		print("la funcion es concava hacia abajo")
	# se emplea el condicional si poara saber hacia donde es concava la funcion y poder graficar 

