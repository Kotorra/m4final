import csv
class Vehiculo():
	Vehiculos=[]
	def __init__(self,marca,modelo,nro_ruedas):
		self.marca=marca
		self.modelo=modelo
		self.nro_ruedas=nro_ruedas


	def get_marca(self):
		return self.marca

	def set_marca(self,nuevo):
		self.marca=nuevo
		print("Marca modificada.")

	@property
	def Modelo(self):
		return self.modelo

	@Modelo.setter
	def SetModelo(self,modelonuevo):
		self.modelo=modelonuevo
		print("Modelo modificado.")

	@staticmethod
	def guardar_datos_csv(listavehiculos):
		with open("vehiculos.csv", "w", encoding="utf-8", newline='') as Archivo:
			Archivo= csv.writer(Archivo)
			for i in listavehiculos:
				Archivo.writerows([(i.__class__, i.__dict__)])

	@classmethod
	def leer_datos_csv(cls):
		ParticularesL=[]
		CargoL=[]
		BicicletaL=[]
		MotocicletaL=[]
		with open("vehiculos.csv", "r", encoding="utf-8") as Archivo:
			Archivo = csv.reader(Archivo)
			for vehiculo in Archivo:
					Vehiculo.Vehiculos.append(vehiculo)
		for i in range(len(cls.Vehiculos)):
			aux=cls.Vehiculos[i][0]
			if aux=="<class 'vehiculo.Particular'>":
				ParticularesL.append(cls.Vehiculos[i])
			elif aux=="<class 'vehiculo.Carga'>":
				CargoL.append(cls.Vehiculos[i])
			elif aux=="<class 'vehiculo.Bicicleta'>":
				BicicletaL.append(cls.Vehiculos[i])
			elif aux=="<class 'vehiculo.Motocicleta'>":
				MotocicletaL.append(cls.Vehiculos[i])

		print("\nLista de Vehículos Particular")
		for i in ParticularesL:
			print(i[1])

		print("\nLista de Vehículos Carga")
		for i in CargoL:
			print(i[1])
		print("\nLista de Vehículos Bicicleta")
		for i in BicicletaL:
			print(i[1])
		print("\nLista de Vehículos Motocicleta")
		for i in MotocicletaL:
			print(i[1])

class Automovil(Vehiculo):
	def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada):
		super().__init__(marca,modelo,nro_ruedas)
		self.velocidad=velocidad
		self.cilindrada=cilindrada

	def __str__(self):
		return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}Km/h, {self.cilindrada}cc.")

class Particular(Automovil):
	def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada,npuestos):
		super().__init__(marca,modelo,nro_ruedas,velocidad,cilindrada)
		self.npuestos=npuestos

	def __str__(self):
		return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}km/h, {self.cilindrada}cc., {self.npuestos} puestos.")

class Carga(Automovil):
	def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada,carga):
		super().__init__(marca,modelo,nro_ruedas,velocidad,cilindrada)
		self.carga=carga

	def __str__(self):
		return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}km/h, {self.cilindrada}cc., {self.carga}Kg.")

class Bicicleta(Vehiculo):
	def __init__(self,marca,modelo,nro_ruedas,tipo):
		super().__init__(marca,modelo,nro_ruedas)
		self.tipo=tipo
	def __str__(self):
		return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}.")
	
class Motocicleta(Bicicleta):
	def __init__(self,marca,modelo,nro_ruedas,tipo,motor,cuadro,nro_radios):
		super().__init__(marca,modelo,nro_ruedas,tipo)
		self.motor=motor
		self.cuadro=cuadro
		self.nro_radios=nro_radios
	def __str__(self):
		return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro:{self.cuadro}, Nro Radios:{self.nro_radios}.")
