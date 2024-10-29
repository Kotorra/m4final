import csv
from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta


class ErrorNumero(Exception):
	pass

class ControlErrores():
	@staticmethod
	def PositivoNoCero(n):
		if n<=0:
			raise ErrorNumero("Error. El número debe ser positivo.")

listavehiculosparte1=[]

print("***PARTE 1***\n")
while True:
	try:

		nVehiculos=int(input("Cuantos Vehiculos desea insertar: "))
		if nVehiculos<0:
			print("Ingrese un número entero.")
		else:
			break

	except ValueError:
		print("Entrada no válida.")


for i in range(nVehiculos):
	while True:
		try:
			print(f"\nDatos del automovil {i+1}")
			marca=input(("Inserte la marca del automóvil: "))
			modelo=input("Inserte el modelo: ")
			ruedas=int(input("Inserte el número de ruedas: "))
			ControlErrores.PositivoNoCero(ruedas)
			velocidad=int(input("Inserte la velocidad en km/h: "))
			ControlErrores.PositivoNoCero(velocidad)
			cilindraje=int(input("Inserte el cilindraje en cc: "))
			ControlErrores.PositivoNoCero(cilindraje)
			auto=Automovil(marca,modelo,ruedas,velocidad,cilindraje)
			listavehiculosparte1.append(auto)
			break

		except(ValueError,ErrorNumero) as e:

		    if isinstance(e, ValueError):
		        print("Error de entrada. Ingrese números enteros positivos.")
		    else:
		        print(e)

if len(listavehiculosparte1)>0:
	print("\nImprimiendo por pantalla los Vehículos:\n")

	for i in range(nVehiculos):
		print(f"Datos del automovil {i+1}: {listavehiculosparte1[i]}")

print("***FIN PARTE 1***\n")

print("***PARTE 2***")

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

listavehiculos=[]
listavehiculos+=[particular,carga,bicicleta,motocicleta]
print("")

for i in listavehiculos:
	print(i)
print("**********\n")
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta,Particular)}") 
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta,Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta,Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta,Motocicleta)}")
print("\n***FIN PARTE 2***\n")

print("***PARTE 3***")
Vehiculo.guardar_datos_csv(listavehiculos)
vehi=Vehiculo.leer_datos_csv()
print("***FIN PARTE 3***\n")