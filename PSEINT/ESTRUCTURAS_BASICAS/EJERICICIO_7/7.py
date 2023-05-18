# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto.
	# HECHO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA:26/02/2023
	# VERSION: 1.0
	# DEFINICION=
	# VARAIBLE QUE ALMACENA EL NOMBRE DEL EMPLEADO
	v_ne = str()
	# VARIABLE QUE ALMACENA LAS HORAS TRABAJADAS
	v_tht = int()
	# VARIABLE QUE ALMACENA EL VALOR DE LA HORA
	v_vh = int()
	# VARIABLE QUE ALMACENA EL VALOR DEL SALARIO BRUTO
	v_bruto = int()
	# VARIABLE QUE ALMACENA EL VALOR DE LOS IMPUESTOS O TASAS
	v_tasas = float()
	# VARIABLE QUE ALAMCENA EL VALOR DEL SALARIO NETO
	v_neto = float()
	# VALOR INICIAL:
	v_ne = ""
	v_tht = 0
	v_vh = 0
	v_bruto = 0
	v_tasas = 0.0
	v_neto = 0.0
	# INICIO=
	# INGRESO DE DATOS
	print("escribe el nombre del empleado")
	v_ne = input()
	print("escribe el total de horas trabajadas")
	v_ht = float(input())
	print("escribe el precio de las horas")
	v_vh = int(input())
	print("-----------------------------------------")
	# PROCESO
	# PARA OBTENER EL VALOR DEL SALARIO BRUTO: SE MULTIPLICA LAS HORAS TRABAJASDAS POR EL VALOR DE LAS HORAS
	v_bruto = v_ht*v_vh
	# PARA OBTENER EL VALOR DE LAS TASAS O IMPUESTOS: SE MULTIPLICA EL SALRIO BRUTO POR 0.25 (25% = 0.25)
	v_tasas = v_bruto*0.25
	# PARA OBTENER EL VALOR DEL SALARIO NETO: SE RESTA EL SALARIO BRUTO CON LAS TASAS
	v_neto = v_bruto-v_tasas
	# SALIDA
	print("-----------------------------------------")
	print("el nomnbre del empleado es=",v_ne)
	print("el salario bruto es=","$",v_bruto)
	print("los impuestos o tasas a pagar son=","$",v_tasas)
	print("el salario neto es=","$",v_neto)
	print("--------------------------------------------")
	# FIN

