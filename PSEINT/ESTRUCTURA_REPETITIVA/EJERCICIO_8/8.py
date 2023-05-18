# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=Calcular la media de una serie de números positivos, suponiendo que los datos se leen desde un terminal. 
	# Un valor de cero ?como entrada? indicará que se ha alcanzado el final de la serie de números positivos.
	# CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA: 26/02/2023
	# VERSION= 1.1
	# definir=
	# VARIABLE DE ENTRADA QUE CUENTA LOS NUMEROS
	v_c = int()
	# VARIABLE DE ENTRADA QUE SUMA LOS NUMEROS
	v_s = float()
	# VARIABLE DE PROCESO QUE ALMACENA EL NUMERO ESCRITO
	v_dato = float()
	# VARIABLE DE SALIDA QUE ALMACENA LA MEDIA
	v_media = float()
	# VALOR INICIAL:
	v_c = 0
	v_s = 0.0
	v_dato = 0.0
	v_media = 0.0
	# INICIO
	# ENTRADA DE DATOS
	print("Datos nuemricos, para finalizar se introduce 0")
	# PROCESO
	# SE REPITE EL PROCESO DE CONTAR CUANTOS NUMEROS SE INGRESAN, DE SUMAR TODOS LOS NUMERO INGRESADOS Y SE DIVIDE LA SUMA DE LOS NUMEROS ENTRE LA CANTIDAD DE NUMEROS INGRESADOS, HASTA QUE SE INGRESE UN VALOR IGUAL A CERO
	while True:# no hay 'repetir' en python
		v_dato = float(input())
		if v_dato!=0:
			# SE CUENTAN CUANTOS NUMEROS SE INGRESAN
			v_c = v_c+1
			# SE SUMAN TODOS LOS NUMEROS INGRESADOS
			v_s = v_s+v_dato
		else:
			# PARA OBTENER LA MEDIA: SE DIVIDE LA SUMA DE LOS NUMEROS INGRESADOS ENTRE LA CANTIDAD DE NUMEROS INGRESADOS
			v_media = v_s/v_c
			print(v_media)
		# EL PROCESO DE REPETIR SE TERMINA CUANDO SE INGRESA UN VALOR IGUAL A CERO
		if v_dato==0: break
	# SALIDA
	print("-------------------------------------")
	print("la media es=",v_media)

