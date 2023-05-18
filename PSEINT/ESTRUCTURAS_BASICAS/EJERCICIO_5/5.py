# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Enunciado: Calcular el salario con descuentos
	# Leer valores de v_VH, v_HTD, v_HTN
	# Pedir cada valor por teclado
	# y hallar el valor de x
	# desarrollado por: Hernan Alberto Londoño Velez
	# version 1.0
	# fecha 20/02/23
	# DECLARACION DE VARIABLES
	# varaible que almacena el valor de la hora dia o comunes
	v_vh = float()
	# variable que almacena el valor del 40% de las horas dia
	v_vh40 = float()
	# variable que almacena el valor de la hora nocturna
	v_vhn = float()
	# variable que alamcena el valor total de las horas dia
	v_vthd = float()
	# variable que alamcena el valor total de las horas noche
	v_vthn = float()
	# variable que almacena el valor del subsalario
	v_subsalario = float()
	# variable que alamcena el descuento de retencion en la fuente
	v_rf = float()
	# variable que alamcena el descuento de fondos de empleados
	v_fe = float()
	# variable que alamcena el descuento bienestar familiar
	v_bf = float()
	# variable que alamcena el descuento de salir y pension
	v_sp = float()
	# variable que alamcena el valor del salario neto
	v_salarioneto = float()
	# variable que almacena la cantidad de horas dia
	v_htd = int()
	# variable que alamcena la cantidad de horas noche
	v_htn = int()
	# variable que alamcena el nombre del empleado
	v_nomemp = str()
	# inicializacion de variables
	v_vh = 0.0
	v_vh40 = 0.0
	v_vhn = 0.0
	v_vthd = 0.0
	v_vthn = 0.0
	v_subsalario = 0.0
	v_rf = 0.0
	v_fe = 0.0
	v_bf = 0.0
	v_sp = 0.0
	v_salarioneto = 0.0
	v_htd = 0
	v_htn = 0
	v_nomemp = ""
	# ENTRADA DE DATOS//
	print("Por favor ingrese el nombre del empleado ")
	v_nomemp = input()
	print("Por favor ingrese el valor de la hora")
	v_vh = float(input())
	print("Por favor ingrese la cantidad de Horas Trabajadas Día")
	v_htd = int(input())
	print("Por favor ingrese la cantidad de Horas Trabajadas Noche")
	v_htn = int(input())
	# Procesos
	# PARA OBTENER EL VALOR DE TODAS LAS HORAS DIA, SE MULTIPLICA EL VALOR DE LA HORA POR HORAS DIA
	v_vthd = (v_vh)*(v_htd)
	# PARA OBTENER EL 40% DEL VALOR DE LA HORA COMUN, SE MULTIPLICA EL VALOE DE LA HORA POR 0.4
	v_vh40 = v_vh*0.4
	# PARA OBTENER EL VALOR DE LA HORA NOCTURA, SE SUMA EL VALOR DE LA HORA CON 40% DE LA HORA COMUN
	v_vhn = (v_vh)+(v_vh40)
	# PARA OBTENER EL VALOR DE TODAS LAS HORAS NOCHE, SE MULTIPLICA EL VALOR DE LA HORA NOCHE POR LA CANTODAD DE HORAS NOCHE
	v_vthn = (v_vhn)*(v_htn)
	# PARA OBTENER EL SUBSALARIO, SE SUMA EL VALOR DE TODAS LAS HORAS DIA CON EL VALOR DE TODAS LAS HORAS NOCHE
	v_subsalario = (v_vthd)+(v_vthn)
	# PARA OBTENER EL VALOR DE RETENCION EN LA FUENTE, SE MULTIPLICA SUBSALARIO POR 0.1
	v_rf = (v_subsalario)*(0.1)
	# PAAR OBTENER EL VALOR DE FONDOS DE EMPLEADOS, SE MULTIPLICA SUBSALARIO POR 0.03
	v_fe = (v_subsalario)*(0.03)
	# PARA OBTENER EL VALOR DE BIENESTAR FAMILIAR, SE MULTIPLICA SUBSALARIO POR 0.02
	v_bf = (v_subsalario)*(0.02)
	# PARA OBTENER EL VALOR DE SALUD  Y PENSION, SE MULTIPLICA SUBSALARIO POR 0.04
	v_sp = (v_subsalario)*(0.04)
	# PARA OBTENER EL VALOR DEL SALARIO NETO, SE RESTA SUBSALARIO CON RETENCION EN LA FUENTE, FONDO DE EMPLEADOS, BIENESTAR FAMILIAR Y SALUD Y PENCION
	v_salarioneto = (v_subsalario)-(v_rf)-(v_fe)-(v_bf)-(v_sp)
	# Salida
	print("Valo Hora Nocturna: ",v_vhn)
	print("El Subsalario es: ",v_subsalario)
	print("Descuentos")
	print("Descuento por retencion de fuente")
	print("10%")
	print("Descuento de fondos de empleados")
	print("3%")
	print("Descuento de bienestar familiar")
	print("2%")
	print("Descuento de salud y pension")
	print("4%")
	print("Salario neto")
	print(v_salarioneto)

