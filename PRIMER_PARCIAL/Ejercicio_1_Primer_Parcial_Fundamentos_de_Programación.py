# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Enunciado:resolver la ecuacio que el usuario necesite
	# Declarar los valores de Vf, Vi y t
	# pedir los valores por tecladp
	# Desarrollado por Hernan Londoño y Jonathan López
	# Version 1.0
	# Fecha: 13/03/23
	# Definir variables
	v_ecu = str()
	v_vi = float()
	v_vf = float()
	v_t = float()
	v_a = float()
	v_vm = float()
	v_mvi = int()
	v_mvf = int()
	v_t2 = float()
	v_t22 = float()
	v_vf2 = float()
	v_vi2 = float()
	v_a2 = float()
	v_d1 = float()
	v_d2 = float()
	v_ma = int()
	v_mt = int()
	v_dt = float()
	v_dt2 = float()
	# Inicializacion de variables
	v_ecu = ""
	v_vi = 0.0
	v_vf = 0.0
	v_t = 0.0
	v_a = 0.0
	v_vm = 0
	v_mvi = 0
	v_mvf = 0
	v_t2 = 0.0
	v_t22 = 0.0
	v_vf2 = 0.0
	v_vi2 = 0.0
	v_a2 = 0.0
	v_d1 = 0.0
	v_d2 = 0.0
	v_ma = 0.0
	v_mt = 0.0
	v_dt = 0.0
	v_dt2 = 0.0
	# Entrada de datos
	print("Por favor elija la ecuacion a realizar: aceleracion (a),velocidad media (vm), velocidad final (vf), distancia sin aceleracion (d1), distancia con aceleracion (d2)")
	v_ecu = input()
	# Proceos y salidas
	# condicional que se utiliza para elegir que tipo de ejercicio resolver
	if v_ecu=="a":
		# Entrada de datos
		print("Por favor ingrese la velocidad inicial")
		v_vi = float(input())
		print("elija medicion de velocidad inicial: m/s (1) ó km/h (2)")
		v_mvi = int(input())
		print("Por favor ingrese la velocidad final")
		v_vf = float(input())
		print("elija medicion de velocidad final: m/s (1) ó km/h (2)")
		v_mvf = int(input())
		print("Por favor ingrese el tiempo en segundos")
		v_t = float(input())
		print("elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)")
		v_mt = int(input())
		# Proceso
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Proceso
		# para pasar km/h a m/s
		if v_mvf==1:
			v_vf2 = v_vf
		elif v_mvf==2:
			v_vf2 = v_vf/3.6
			# Salida
			print("la velocidad final en m/s es: ",v_vf2)
		# Proceso
		# para pasar de horas y minutos a segundos.
		if v_mt==1:
			v_t2 = v_t
		elif v_mt==2:
			v_t2 = v_t*60
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		elif v_mt==3:
			v_t2 = v_t*3600
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		# Proceso
		# es la escuación que se utiliza para hallar la aceleración
		v_a = (v_vf2-v_vi2)/v_t2
		# Salida
		print("La aceleración es ",v_a)
		# -------------------------------------------------------------------------------------------
	elif v_ecu=="vm":
		# Entrada de datos
		print("Por favor ingrese la velocidad inicial")
		v_vi = float(input())
		print("Por favor ingrese la velocidad final")
		v_vf = float(input())
		# Proceso
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Proceso
		# para pasar km/h a m/s
		if v_mvf==1:
			v_vf2 = v_vf
		elif v_mvf==2:
			v_vf2 = v_vf/3.6
			# Salida
			print("la velocidad final en m/s es: ",v_vf2)
		# Proceso 
		# es la ecuación que se utiliza para  hallar la Velocidad media
		v_vm = (v_vf2-v_vi2)/2
		# Salida
		print("La velocidad media es ",v_vm)
		# ----------------------------------------------------------------------------------------------
	elif v_ecu=="vf":
		# Entrada de datos
		print("escriba la velocidad inicial")
		v_vi = float(input())
		print("escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)")
		v_mvi = int(input())
		print("escriba la aceleracion")
		v_a = float(input())
		print("escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)")
		v_ma = int(input())
		print("escriba el tiempo")
		v_t = float(input())
		print("elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)")
		v_mt = int(input())
		# Procesos
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Procesos
		if v_ma==1:
			v_a2 = v_a
		elif v_ma==2:
			v_a2 = v_a/12960
			# Salida
			print("la aceleracion en m/s2 es: ",v_a2)
		# Proceso
		# para pasar de horas y minutos a segundos.
		if v_mt==1:
			v_t2 = v_t
		elif v_mt==2:
			v_t2 = v_t*60
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		elif v_mt==3:
			v_t2 = v_t*3600
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		# Proceso
		v_vf = v_vi2+(v_a2*v_t2)
		# Salida
		print("La velocidad final es: ",v_vf)
		# -------------------------------------------------------------------------------
	elif v_ecu=="vf2":
		# Entrada de Datos 
		print("escriba la velocidad inicial")
		v_vi = float(input())
		print("escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)")
		v_mvi = int(input())
		print("escriba la aceleracion")
		v_a = float(input())
		print("escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)")
		v_ma = int(input())
		print("escriba la distancia")
		v_d = input()
		print("elija medicion de distancia: mts(1) km(2)")
		v_md = input()
		# Procesos
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			v_vi2 = v_vi2*v_vi2
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Procesos
		if v_ma==1:
			v_a2 = v_a
		elif v_ma==2:
			v_a2 = v_a/12960
			# Salida
			print("la aceleracion en m/s2 es: ",v_a2)
		# Procesos
		# paar pasar de horas y minutos a segundos.
		if v_mdt==1:
			v_dt2 = v_dt
		elif v_mdt==2:
			v_dt2 = v_dt*1000
			# Salida
			print("la distancia en mts es: ",v_dt2)
		# Proceso
		v_vf = v_vi2+(2*(v_a2*v_t2))
		# Salida
		print("La velocidad final es: ",v_vf)
		# -----------------------------------------------------------------------------
	elif v_ecu=="d1":
		# Entrada de datos
		print("escriba la velocidad inicial")
		v_vi = float(input())
		print("escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)")
		v_mvi = int(input())
		print("Por favor ingrese la velocidad final")
		v_vf = float(input())
		print("elija medicion de velocidad final: m/s (1) ó km/h (2)")
		v_mvf = int(input())
		print("escriba el tiempo")
		v_t = float(input())
		print("elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)")
		v_mt = int(input())
		# Procesos
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Procesos
		# para pasar km/h a m/s
		if v_mvf==1:
			v_vf2 = v_vf
		elif v_mvf==2:
			v_vf2 = v_vf/3.6
			# Salida
			print("la velocidad final en m/s es: ",v_vf2)
		# Procesos
		# paar pasar de horas y minutos a segundos.
		if v_mt==1:
			v_t2 = v_t
		elif v_mt==2:
			v_t2 = v_t*60
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		elif v_mt==3:
			v_t2 = v_t*3600
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		# Proceso
		v_d1 = ((v_vf2+v_vi2)/2)*v_t2
		# Salida
		print("La distancia sin aceleracion es: ",v_d1,"m")
		# -------------------------------------------------------------------------
	elif v_ecu=="d2":
		# Entrada de datos
		print("escriba la velocidad inicial")
		v_vi = float(input())
		print("escriba la medicion de velocidad inicial: m/s (1) ó km/h (2)")
		v_mvi = int(input())
		print("escriba el tiempo")
		v_t = float(input())
		print("elija medicion de tiempo: segundos (1), minutos (2) ó horas (3)")
		v_mt = int(input())
		print("escriba la aceleracion")
		v_a = float(input())
		print("escriba la medicion de aceleracion: m/s2 (1) ó km/h2 (2)")
		v_ma = int(input())
		# Procesos
		# para pasar km/h a m/s
		if v_mvi==1:
			v_vi2 = v_vi
		elif v_mvi==2:
			v_vi2 = v_vi/3.6
			# Salida
			print("la velocidad inicial en m/s es: ",v_vi2)
		# Procesos
		# paar pasar de horas y minutos a segundos.
		if v_mt==1:
			v_t2 = v_t
		elif v_mt==2:
			v_t2 = v_t*60
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		elif v_mt==3:
			v_t2 = v_t*3600
			# Salida
			print("el tiempo en segundos es: ",v_t2)
		# Procesos
		v_t22 = v_t2*v_t2
		if v_ma==1:
			v_a2 = v_a
		elif v_ma==2:
			v_a2 = v_a/12960
			# Salida
			print("la aceleracion en m/s2 es: ",v_a2)
		# Proceso
		v_d2 = ((v_vi2*v_t2)+(1/2))*(v_a2*v_t22)
		# Salida
		print("La distancia con aceleracion es:",v_d2)

