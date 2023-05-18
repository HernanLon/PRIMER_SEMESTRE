# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# VERSION=1.0
	# FECHA=22/02/2023
	# ENUNCIADO:Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
	# Suponiendo que su movimiento es uniformemente acelerado ¿Qué aceleración se le ha comunicado y qué espacio ha recorrido antes de alcanzar la velocidad regular?
	# HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA: 20/02/2023
	# VERSION: 1.0
	# DEFINICION:
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL
	v_vi = float()
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL
	v_vf = float()
	# VARIABLE QUE ALMACENA EL VALOR DE TIEMPO
	v_t = float()
	# VARIABLE QUE ALAMCENA LA MEDICION DE VELOCIDAD INICIAL
	v_mvi = int()
	# VARIABLE QUE ALAMCENA LA MEDICION DE VELOCIDAD FINAL
	v_mvf = int()
	# VARIABLE QUE ALAMCENA LA MEDICION DE TIEMPO
	v_mt = int()
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD INICIAL EN M/S
	v_vi2 = float()
	# VARIABLE QUE ALMACENA EL VALOR DE VELOCIDAD FINAL EN M/S
	v_vf2 = float()
	# VARIABLE QUE ALMACENA TIEMPO EN SEGUNDOS.
	v_t2 = float()
	# VARIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE VF-VI
	vf_vi = float()
	# VARAIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE ACELERACION
	v_a = float()
	# VARAIABLE QUE ALMACENA EL RESULTADO DE UNA OPERACION ARITMETICA DE DIATANCIA
	v_d = float()
	# VALOR INICA:
	v_vi = 0.0
	v_vf = 0.0
	v_t = 0.0
	v_mvi = 0
	v_mvf = 0
	v_mt = 0
	v_vi2 = 0.0
	v_vf2 = 0.0
	v_t2 = 0.0
	vf_vi = 0.0
	v_a = 0.0
	v_d = 0.0
	# INICIO
	# ENTRADA DE DATOS
	print("escribe velocidad inicial")
	v_vi = float(input())
	# ENTRADA DE DATOS
	print(" si velocidad inicial esta en m/s escriba 1 o si esta en km/h escriba 2")
	v_mvi = int(input())
	# ENTRADA DE DATOS
	print("escribe velocidad final")
	v_vf = float(input())
	# ENTRADA DE DATOS
	print("si velocidad final esta en m/s escriba 1 o si esta en km/h escriba 2")
	v_mvf = int(input())
	# ENTRADA DE DATOS
	print("escribe tiempo")
	v_t = float(input())
	# ENTRADA DE DATOS
	print("si tiempo esta en segundos escriba 1, si esta en minutos escriba 2, si esta en horas escriba 3")
	v_mt = int(input())
	print("-------------------------------------------------")
	# PROCESO
	# SE CONVIERTE LOS KM/H A M/S DE VELOCIDAD INICIAL
	if v_mvi==1:
		v_vi2 = v_vi
	elif v_mvi==2:
		v_vi2 = v_vi/3.6
	# PROCESO
	print("velocidad inicial en m/s es:",v_vi2,"m/s")
	# PROCESO
	# SE CONVIERTE LOS KM/H A M/S DE VELOCIDAD FINAL
	if v_mvf==1:
		v_vf2 = v_vf
	elif v_mvf==2:
		v_vf2 = v_vf/3.6
	# PROCESO
	print("velocidad final en m/s es:",v_vf2,"m/s")
	# PROCESO
	# SE CONVIERTE LAS HORAS Y MINUTOS A SEGUNDOS DEL TIEMPO
	if v_mt==1:
		v_t2 = v_t
	elif v_mt==2:
		v_t2 = v_t*60
	elif v_mt==3:
		v_t2 = v_t*3600
	# PROCESO
	print("tiempo en segundo es:",v_t2,"seg")
	print("-------------------------------------------------")
	print("los resulatdos son:")
	# SALIDA
	# SE RESTA VELOCIDAD FINAL (EN SEGUNDOS) CON VELOCIDAD FINAL (EN SEGUNDOS) PARA OBTENER LA VARIABLE VF_VI
	vf_vi = v_vf2-v_vi2
	# SE DIVIDE LA VARIABLE VF_VI ENTRE EL TMEPO (EN SEGUNDOS) PARA OBTENER ACELERACION
	v_a = vf_vi/v_t2
	# SALIDA
	# PARA OBTENER TIEMPO AL CUADRADO, SE MULTIPLICA TIEMPO POR TIEMPO
	v_t2 = v_t2*v_t2
	# PARA OBTENER DISTANCIA, SE DIVIDE ACELERACION ENTRE TIEMPO AL CUADRADO
	v_d = v_a*v_t2/2
	# SALIDA
	print("la aceleracion es:",v_a,"m/s2")
	print("la distancia es:",v_d,"m")
	# FIN

