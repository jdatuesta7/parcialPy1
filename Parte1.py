from datetime import datetime
hoy = str(datetime.now())
#resultados[inicial_NombreApellidoCompleto]01-YYYYMMDD-HHmmSS.txt
#Removiendo Puntos y dos puntos de la fecha
nombre = "resultados[J_Atuesta]01-" 
cad1 = (hoy[0:13]+"-")
cad2 = (hoy[14:16]+"-")
cad3 = (hoy[17:19])
hoy = cad1 + cad2 + cad3
fecha = nombre + hoy + ".txt"

print(fecha)

f1 = open("[J_Atuesta]01.txt", "r")
f2 = open(fecha,"a")

def tNumerador(dato,f1num,f1den,f2num,f2den):
	#Total numerador
	if dato[7] == "+":
		tnum = (f1num*f2den)+(f1den*f2num)
	elif dato[7] == "-":
		tnum = (f1num*f2den)-(f1den*f2num)
	elif dato[7] == "*" or dato[7] == "x":
		tnum = (f1num*f2num)
	elif dato[7] == "/":
		tnum = (f1num*f2den)
	return tnum

def tDenominador(dato,f1den,f2den,f2num):
	#Total denominador
	if dato[7] == "/":
		tden = f1den * f2num
	elif dato[7] == "+" or dato[7] == "-" or dato[7] == "*" or dato[7] == "+":
		tden = f1den * f2den
	return tden

def fImpropias(dato): #Si ambas fracciones son impropias
	f1Ent = int(dato[0])
	f1num = int(dato[2])
	f1den = int(dato[4])
	f2Ent = int(dato[9])
	f2num = int(dato[11])
	f2den = int(dato[13])

	#Convirtiendo fracion impropia a propia
	coc1 = int(f1num/f1den)
	newNumerador1 = int(f1num%f1den) #nuevo numerador
	f1Ent += coc1 #Nuevo numero Entero
	
	#Convirtiendo fracion impropia a propia
	coc2 = int(f2num/f2den)
	newNumerador2 = int(f2num%f2den) #nuevo numerador
	f2Ent += coc2 #Nuevo numero Entero

	f1num = int(f1Ent*f1den+newNumerador1)
	f2num = int(f2Ent*f2den+newNumerador2)

	tnum = tNumerador(dato,f1num,f1den,f2num,f2den)
	tden = tDenominador(dato,f1den,f2den,f2num)

	coc = int(tnum/tden)
	res = int(tnum%tden)

	fraccion = str(" = "+str(coc)+"("+str(res)+"/"+str(tden)+")")
	f2.write(dato[:15]+fraccion+"\n")


def fImpropia2(dato): #si la segunda fracion no es propia
	f2Ent = int(dato[9])
	f2num = int(dato[11])
	f2den = int(dato[13])
	#Convirtiendo fracion propia a impropia
	coc1 = int(f2num/f2den)
	newNumerador = int(f2num%f2den) #nuevo numerador
	f2Ent += coc1 #Nuevo numero Entero
	
	f2num = int(f2Ent*f2den+newNumerador)
	f1num = int(int(dato[0])*int(dato[4])+int(dato[2]))
	f1den = int(dato[4])

	tnum = tNumerador(dato,f1num,f1den,f2num,f2den)
	tden = tDenominador(dato,f1den,f2den,f2num)

	coc = int(tnum/tden)
	res = int(tnum%tden)
	
	fraccion = str(" = "+str(coc)+"("+str(res)+"/"+str(tden)+")")
	f2.write(dato[:15]+fraccion+"\n")	

def fImpropia1(dato): #si la primera fracion no es propia
	f1Ent = int(dato[0])
	f1num = int(dato[2])
	f1den = int(dato[4])

	#Convirtiendo fracion impropia a propia
	coc1 = int(f1num/f1den)
	newNumerador = int(f1num%f1den) #nuevo numerador
	f1Ent += coc1 #Nuevo numero Entero
	f1num = int(f1Ent*f1den+newNumerador)

	f2num = int(int(dato[9])*int(dato[13])+int(dato[11]))
	f2den = int(dato[13])

	tnum = tNumerador(dato,f1num,f1den,f2num,f2den)
	tden = tDenominador(dato,f1den,f2den,f2num)

	coc = int(tnum/tden)
	res = int(tnum%tden)
	
	fraccion = str(" = "+str(coc)+"("+str(res)+"/"+str(tden)+")")
	f2.write(dato[:15]+fraccion+"\n")


def fPropias(dato):#Si todas son fraciones propias
	if dato[2]<dato[4] and dato[11]<dato[13]:
		f1num = int(int(dato[0])*int(dato[4])+int(dato[2]))
		f1den = int(dato[4])
		f2num = int(int(dato[9])*int(dato[13])+int(dato[11]))
		f2den = int(dato[13])

		tnum = tNumerador(dato,f1num,f1den,f2num,f2den)
		tden = tDenominador(dato,f1den,f2den,f2num)

		coc = int(tnum/tden)
		res = int(tnum%tden)

		fraccion = str(" = "+str(coc)+"("+str(res)+"/"+str(tden)+")")
		f2.write(dato[:15]+fraccion+"\n")
	elif dato[2]>=dato[4] and dato[11]<dato[13]:
		fImpropia1(dato) #si la primera fraccion no es propia
	elif dato[2]<dato[4] and dato[11]>=dato[13]:
	 	fImpropia2(dato) #si la segunda fraccion no es propia
	elif dato[2]>=dato[4] and dato[11]>=dato[13]:
	 	fImpropias(dato) #Si ambas fracciones no son propias

def getter():#Itera cada linea del archivo
	for dato in f1:
		dato = dato.strip()+"\n"
		fPropias(dato)#Los datos de cada linea se pasan a la funcion fpropias

getter()

f1.close()
f2.close()