f1 = open("File2.txt","r")
f2 = open("ResultadosFile2.txt","a")

lugares = []

def insideFile(dato,distancias,cuadras,existZ):
	i = 0

	for x in range(0,cuadras):
		print(x)
		if dato[x] == "D":	
			for y in range(x+1,cuadras):
				if dato[x] != "R":
					i += 1
				else:
					break

			distancias.append(i)
			print(distancias)
			i = 0
		elif dato[x] == "R":
			for y in range(x+1,cuadras):
				if dato[x] != "D":
					i += 1
				else:
					break
			distancias.append(i)
			print(distancias)	
			i = 0	
		elif dato[x] == "Z":
			f2.write("(0) Hay una farmacia en la misma cuadra del restaurante\n")
			existZ = True
	
	lugares.clear()

	if existZ == False:
		distancias.sort()
		print(distancias)
		Lminima = str(distancias[0])
		msj = "("+Lminima+")"+"Hay una farmacia a "+Lminima+" cuadra ????? del restaurante"
		f2.write(msj+"\n")
		distancias.clear()

	
def getter():#Itera cada linea del archivo
	existZ = False 
	cont = -1
	distancias = [] #Lista que contiene cada distancia entre R y D
	cuadras = 0

	for dato in f1:
		dato = dato.strip()
		print("GETTER")
		cont +=1
		if cont % 2 == 0:
			cuadras = int(dato)
			continue

		print("100")
		insideFile(dato,distancias,cuadras,existZ)#Los datos de cada linea se pasan a la funcion
		existZ = False
		
		if dato == 0:
			break

getter()

f1.close()
f2.close()