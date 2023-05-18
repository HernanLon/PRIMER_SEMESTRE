# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# ENUNCIADO=Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta lo siguiente:
	# -toda llamada que dure menos de tres minutos (cinco pasos) tiene un coste de 10 céntimos,
	# -cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 5 céntimos.
	# CREADO POR: HERNAN ALBERTO LONDOÑO VELEZ
	# FECHA: 26/02/2023
	# VERSION: 1.0
	# DEFINIR=
	# VARIABLE DE INICIO Y SALIDA QUE ALMACENA EL NUMERO DE PASOS DESDE QUE COMIENZA LA LLAMADA.
	v_npasos = int()
	# VARIABLE DE PROCESO Y SALIDA QUE ALMACENA EL PRECIO DE LA LLAMADA
	v_fact = int()
	# VARIABLE DE PROCESO QUE ALMACENA EL NUMERO DE PASOS QUE ECXEDE A 5.
	v_n = int()
	# VALOR INICIAL:
	v_npasos = 0
	v_fact = 0
	v_n = 0
	# INICIO
	# ENTRADA DE DATOS
	print("Escribir numero de pasos")
	v_npasos = int(input())
	# PROCESO
	# CUANDO EMPIEZA LA LLAMADA Y LOS TOTAL PASOS SON MENORES O IGUALES A CERO: SE ESCRIBE ERROR
	if v_npasos<=0:
		print("ERROR")
	# CUANDO EMPIEZA LA LLAMADA Y LOS TOTAL PASOS SON MAYORES A CERO: LOS PRIMEROS TRES MINUTOS (CINCO PASOS) CUESTAN 10 CENTIMOS
	v_fact = 10
	# PARA CONTAR SOLO LOS PASOS EXHEDENTES A LOS PRIMEROS CINCO: SE LE RESTA 5 AL TOTAL DE PASOS
	v_n = v_npasos-5
	# SE DECIDE SEGUN SI EL NUMERO EXHEDENTE SON MAYORES A CERO
	if v_n>0:
		# SI LOS PASOS EXHEDENTES SON MAYORES A CERO: SE MULTIPLICA LOS PASOS EXHEDENTES POR CINCO Y SE LE SUMA EL VALOR DE LOS PRIMERO 3 MINUTOS O CINCO PASOS (LOS PRIMEROS 3 MINUTOS O CINCO PASOS VALES 10 CENTIMOS) 
		v_fact = v_fact+(v_n*5)
	print("-----------------------------------")
	# SALIDA
	print("PASOS=",v_npasos)
	print("VALOR DE LA LLAMADA=",v_fact,"CENTIMOS")
	# FIN

