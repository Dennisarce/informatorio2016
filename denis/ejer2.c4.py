
importe_total=input("ingrese monto")
impuestos=input("ingrese monto de impuestos")
importe_neto=importe_total-impuestos
if (importe_neto<=0):
	print("error")
else:
	if importe_total >5000:	
		print "importe superado para consumidor final"
	else:
		print "el importe neto es",importe_neto 
	

