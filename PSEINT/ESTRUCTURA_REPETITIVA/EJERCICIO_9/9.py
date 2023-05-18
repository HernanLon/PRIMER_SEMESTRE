# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Enunciado: Encontrar el valor de la suma de los numeros enteros psositivos pares del 2 al 100
	# desarrollado por: HERNAN ALBERTO LONDOÑO VELEZ
	# version 1.0
	# fecha 22/02/2023
	# DEFINIR:
	# VARIABLE QUE ALMACENA CADA NUMERO PAR DESDE EL 2 HASTA EL 100.
	v_n = int()
	# VARIABLE QUE ALMACENA UNA RESPUESTA DE UNA ECUACION ARITMETICA, SUMA DE LOS NUMEROS.
	v_suma = int()
	# VALOR INICIAL:
	v_n = 2
	v_suma = 0
	# PROCESO Y SALIDA
	print("Lista de numeros sumados")
	# PRECESO EN EL CUAL SOLO SE SELECCIONA LOS NUMERO DE DOS EN DOS DESDE EL 2 HASTA EL 100, (NUMERO PARES)
	for v_n in range(2,101,2):
		print(v_n)
		# SE SUMAN SOLO LOS NUMEROS PARES DESDE EL 2 HASTA EL 100
		v_suma = v_suma+v_n
	print("El resultado de la suma es ",v_suma)

