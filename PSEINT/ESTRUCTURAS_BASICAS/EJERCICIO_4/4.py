# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO:Un cuerpo posee una velocidad inicial de 12 m/s y una aceleración de 2 m/s2 ¿Cuánto tiempo tardará en adquirir una velocidad de 144 Km/h?
	# CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# VERSION=1.0
	# FECHA=22/02/2023
	# DEFINIR:
	# VARAIABLE QUE ALAMACENA EL VALOR DE VELOCIDAD INICIAL
	v_vi = float()
	# VARAIBLE QUE ALAMACENA EL VALOR DE VELOCIDAD FINAL
	v_vf = float()
	# VARIABLE QUE ALAMCENA EL VALOR DE ACELERACION
	v_a = float()
	# VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD INICIAL
	v_mvi = int()
	# VARIABLE QUE ALMACENA LA MEDICION DE VELOCIDAD DE VELOCIDAD FINAL
	v_mvf = int()
	# VARIABLE QUE ALAMCENA LA MEDICION DE ACELERACION
	v_ma = int()
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL EN M/S
	v_vi2 = float()
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL EN M/S
	v_vf2 = float()
	# VARIABLE QUE ALMACENA EL VALOR DE ACELERACION EN M/S2
	v_a2 = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE VF-VI
	vf_vi = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA, DE TIEMPO
	v_t = float()
	# VALOR INICIAL:
	v_vi = 0.0
	v_vf = 0.0
	v_a = 0.0
	v_mvi = 0
	v_mvf = 0
	v_ma = 0
	v_vi2 = 0.0
	v_vf2 = 0.0
	v_a2 = 0.0
	vf_vi = 0.0
	v_t = 0.0
	# INICIO
	# ENTRADA DE DATOS
	print("escribe velocidad inicial")
	v_vi = float(input())
	# ENTRADA DE DATOS
	print(" si velocidad inicial esta en m/s escriba 1 ó si esta en km/h escriba 2")
	v_mvi = int(input())
	# ENTRADA DE DATOS
	print("escribe velocidad final")
	v_vf = float(input())
	# ENTRADA DE DATOS
	print("si velocidad final esta en m/s escriba 1 ó si esta en km/h escriba 2")
	v_mvf = int(input())
	# ENTRADA DE DATOS
	print("escribe aceleración")
	v_a = float(input())
	# ENTRADA DE DATOS
	print("si aceleracion esta en m/s2 escriba 1 ó si esta en km/h2 escriba 2")
	v_ma = int(input())
	print("-------------------------------------------------")
	# PROCESO
	# SE CONVIERTE KM/H A M/S DE VELOCIDAD INICIAL
	if v_mvi==1:
		v_vi2 = v_vi
	elif v_mvi==2:
		v_vi2 = v_vi/3.6
	# PROCESO
	print("velocidad inicial en m/s es:",v_vi2,"m/s")
	# PROCESO
	# SE CONVIERTE KM/H A M/S DE VELOCIDAD FINAL
	if v_mvf==1:
		v_vf2 = v_vf
	elif v_mvf==2:
		v_vf2 = v_vf/3.6
	# PROCESO
	print("velocidad final en m/s es:",v_vf2,"m/s")
	# PROCESO
	# SE CONVIERTE KM/H AL CUADRADO EN M/S AL CUADRADO  DE ACELERACION
	if v_ma==1:
		v_a2 = v_a
	elif v_ma==2:
		v_a2 = v_a/12960
	# PROCESO
	print("aceleració en m/s2 es:",v_a2,"m/s2")
	print("-------------------------------------------------")
	print("los resultados son:")
	# SALIDA
	# PARA OBTERNER LA VARIANLE VF_VI, SE RESTA VELOCIDAD FINAL CON VELOCIDAD INICIAL
	vf_vi = v_vf2-v_vi2
	# PARA OBTENER TIEMPO, SE DIVIDE VF_VI ENTRE ACELERACION
	v_t = vf_vi/v_a2
	# SALIDA
	print("el tiempo es:",v_t,"seg")
	# FIN

