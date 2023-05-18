# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Enunciado: Encontrar el valor de la suma consecutiva de los numeros enteros positivos del 1 al 50
	# DESARROLLADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# VERSION: 1.0
	# FECHA: 22/02/2023
	# DECLARAR:
	# VARIABLE QUE ALAMCENA EL VALOR DE CADA NUMERO DEL 1 AL 50
	v_n = int()
	# VARAIABLE QUE ALMACENA EL VALOR DE LA SUMA DE LOS NUMEROS DEL 1 AL 50
	v_suma = int()
	# VALOR INICIAL:
	v_n = 1
	v_suma = 0
	# procesos y salidas
	print("Lista de numeros sumados")
	# PROCESO EN LE CUAL SE SELECCIONA CADA NUMERO DESDE EL 1 HASTA EL 50
	for v_n in range(1,51):
		print(v_n)
		# SE SUMA CADA NUMERO DESDE EL 1 HASTA EL 50
		v_suma = v_suma+v_n
	print("El resultado de la suma es ",v_suma)

