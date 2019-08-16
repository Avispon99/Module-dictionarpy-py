import re

def no_repeat(word,path_doc):
	repeat = False
	global open_file # Es un miesterio por que no es necesario usar 'Dict' en open_file... no se sabe si 'global' es la causa.. O tal vez no la reconoce como miembro de Dict pero no afecta.. 
	open_file = open(path_doc, 'r') # respecto al mieterio 'Dict' aqui por ejemplo contaria como una inicializacion de un open_file aparte
	read_fr = open_file.read()
	if re.search(word, read_fr):
		repeat = True         
	open_file = open(path_doc, 'r+')
	return repeat

def alfabet_file(path_doc, recv_abc= False):
	print('\nOrdenando Alfabeticamente\n')
	if recv_abc==True:
		print('entro')
		global open_file # Global No se puede usar por que por alguna razon al abrir documento desde la variable original en lugar de hacerlo desde una nueva provoca que no se pueda escribir.
		open_file = open(path_doc, 'r')
	else: 
		open_file = open(path_doc, 'r')
	f_read = open_file.read() # Guardando el contenido total del documento (back up)
	print('lect:',f_read)
	open_file = open(path_doc, 'w') # Reiniciando el documento de escritura en blanco usando formato write 'w'
	list_rows = f_read.splitlines() #  convertir renglones en elementos de lista
	print('\nROWS:',list_rows)
	for i in Dict.alfabet:
		for j in list_rows: 
			if re.findall('^'+i, j): # Usando regular expresion en lugar de startswith por variar
				print(':',j)
				open_file.write(j+'\n')
	open_file.close() # importante cerrar documento para que no se produzcan conflictos. Nota: Esta era la razon -_-

def write_file(path_doc, abc, n_rep): # Añadiendo el nuevo contenido del dicc
	if n_rep == False:
		open_file = open(path_doc, 'r+')
	for i in Dict.alfabet: # Como la variable de clase('alfabet') se llama en una funcion fuera de la clase entonces se llama "nombre de la clase.variable" y No "self.variable"
		list_keys = Dict.dicc.keys()
		for j in list_keys: # j nunca llega a asignarse por que list_keys esta vacio y no hay que asignar.. debido a funcion emptyVars >> borrar
			if j.startswith(i):
				open_file.read() # esto se requiere para que la nueva escritura se anexe al final podiendo usar formaro "r+"
				print('dicc:',Dict.dicc[j])
				open_file.write(Dict.dicc[j]+"\n") # Escribe el valor señalando la key del diccionario
	if abc==True: 
		alfabet_file(path_doc,recv_abc=abc) # Se debe entregar la escritura del contenido total del archivo ordenado alfabeticamente.	
	return Dict.dicc[j]

def emptyVars():
	Dict.dicc = {} 
	#test.count = 0  # count(self.count) le pertenece a la instancia y No a la clase por eso se llama con 'test.' . Aplica para todos los metodos, No solo para el metodo __init__
	return 0



class Dict:
	""" Variables de Clase """
	open_file = None
	dicc = {}	
	alfabet = ('A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k',
			'L','l','M','m','N','n','Ñ','ñ','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v', 
			'W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9	')
	"""
	def __new__(cls): # Verificacion de lectura y anexo o creacion del archivo.
		while True:
			try:	#PENDIENTE POR OPTIMIZAR
				cls.open_file = open(r'docu\base_eng.txt', 'r+') # Se usa formato 'r+' y no 'a' ya que 'a' permite anexar pero no leer.
				break
			except Exception as e:
				cls.open_file = open(r'docu\base_eng.txt', 'w') # En el metodo '__new__', 'self' se remplaza por 'cls' pero fuera de '__new__' se puede volver a usar 'self', tambien se puede remplazar con nombre de clase ('Dict')
				print('A file was created because the error was presented: ', e)
		return super().__new__(cls) """		

	"""inicializador"""
	def __init__(self,path_doc):
		self.path_doc = path_doc
		list_keys=[]
		self.count = 0
		f_read = None  # opcional
		while True:
			try:	#PENDIENTE POR OPTIMIZAR
				Dict.open_file = open(path_doc, 'r+') # Se usa formato 'r+' y no 'a' ya que 'a' permite anexar pero no leer.
				break
			except Exception as e:
				Dict.open_file = open(path_doc, 'w') # En el metodo '__new__', 'self' se remplaza por 'cls' pero fuera de '__new__' se puede volver a usar 'self', tambien se puede remplazar con nombre de clase ('Dict')
				#print('A file was created because the error was presented: ', e)		

	""" insetar palabras"""	
	def insert_1(self, w_d=None,t_n=None, sep= ' ', n_rep=False, abc=True): 
		"""Insertar strings, listas compuestas de strings o de otras listas o 
		   de tuplas pero que a su vez estas tambien esten compuestas de strings.
		   'sep' establece el separador"""
		inst = w_d 
		tran = t_n
		if type(inst) is  str:
			add_list = []
			add_list.append(inst) 
			inst = add_list #si es inst tipo string forzar a que sea tipo lista
		elif type(inst) is int:
			raise NameError('Type(Int) is useless.') # Forzar error en caso de que sea typo entero
		if type(tran) is  str:
			add_list = []
			add_list.append(tran) 
			tran = add_list #si es inst tipo string forzar a que sea tipo lista
		elif type(tran) is int:
			raise NameError('Type(Int) is useless.')  # Forzar error en caso de que sea typo entero
		for ii in inst:
			for jj in tran:
				if inst.index(ii) == tran.index(jj):
					"""Forzar la conversion a string"""
					if type(ii) is list or type(ii) is tuple:
						insert = ' '.join(ii)
					elif type(ii) is int:
						raise NameError('Type(Int) is useless in list.')
					else: insert = ii 	
					if type(jj) is list or type(jj) is tuple:
						translation = ' '.join(jj)
					elif type(jj) is int:
						raise NameError('Type(Int) is useless in list.')
					else: translation = jj
					"""comprobar que palabra no este repetida"""
					if n_rep == True:
						rep = no_repeat(insert,self.path_doc) 
						if rep == True: 
							print('\n-|| Esa expresion ya existe||-\n')
							break 
					for i in self.alfabet: # iterndo alfabeto
						if insert.startswith(i): # comparando si la palabra comienza por la misma letra del alfabeto iterado
							list_keys = self.dicc.keys() # extrayendo las actuales keys del diccionario / Nota: valores de diccionario se extraen con 'dicc.values()'
							for j in list_keys: # iterando las keys extraidas
								if j.startswith(i): # comparando si la key iterada comienza por la misma letra del alfabeto iterado
									self.count +=1 # iniciando la cuenta de las keys halladas que coinciden con la letra del alfabeto iterado     
							self.dicc[i+str(self.count)]= insert + sep + translation  # Utilizar count como indice de la letra iterada el alfabeto. 
							break
		return_w = write_file(self.path_doc, abc,n_rep)
		print ("\n",self.dicc,"\n")
		open_file.close()
		if n_rep == False:
			alfabet_file(self.path_doc) #>>
		self.count=emptyVars() # Se vacio count desde aca ya que al hacerlo afuera de la clase desde emptyVars abria que hacerlo con la instancia lo que afectaria su importación		
		return return_w

	"""Consultar palabras""" 	
	def query_2(self,consult):
		"""Retorna un diccionario con las lineas que contengan 
		   coincidencias halladas o retornara 'False' si no encuentra nada"""
		open_file = open(self.path_doc, 'r') # No hay que usar 'self' en open_file ya que al parecer lo toma como nueva variable inicializada (desvinculada)
		di_query={}
		c_qry=0
		read_f_2 = open_file.read()
		list_rows_2 = read_f_2.splitlines()
		query = consult
		for i in list_rows_2:
			if re.search(query, i):
				di_query[c_qry]=i
				c_qry+=1
		if di_query == {}: 
			return False # Retornara 'False' (int) en caso de no encontrar la busqueda
		else:
			return di_query		

	"""Corrector"""			
	def correction_3(self,consult=None, correct=None, select=False, key=None):
		"""consult establece la palabra a consultar, mientras que correct establece la palabra
		    a corregir. Si select=False corregira las coincidencias, si select=True retornara un diccionario
		    con las coincidencias halladas, para corregir una de las coincidencias del diccionario
		    se debera colocar select nuevamente en 'False' y el elemento del diccionario elegido ej: key=dict[str(key_element)]"""
		save=''
		#print(':::',key)
		di_corr={}    #Asignar variables en contexto general solo sirve para inicializarlos o para darle sun valor por defecto
		c_crr=0
		open_file = open(self.path_doc, 'r') 
		read_f_3 = open_file.read()
		list_rows_3 = read_f_3.splitlines()
		#if select == True: query_2 = consult
		#if select == False and key == None: query_2 =consult
		query_2=consult
		if select == False and key != None:
			d_line = key
			#query_2=consult
		for i in list_rows_3:
			#print(query_2, i) #query esta convirtiendo en 'None' al introducir la key
			if re.search(query_2, i):
				save=i
				if select == True:
					di_corr[str(c_crr)]=i
					c_crr+=1
				#print('\n< '+i+' >\n')
				elif select == False:
					if key != None:
						correct_line=re.sub(query_2, correct, d_line )
						read_f_3 = re.sub(d_line, correct_line, read_f_3)
					else:
						read_f_3 = re.sub(query_2, correct, read_f_3)
				#	open_file = open(r'docu\base_eng.txt', 'w')
				#	open_file.write(read_f_3)
				#	print('\n<La expresion fue corregida>\n') 
		#alfabet_file()
		if select == False:
			open_file = open(self.path_doc, 'w')
			open_file.write(read_f_3)
			print('\n<La expresion fue corregida>\n') 
			#print('uuuuuuuuu')
			return True
		if select == True:
			return di_corr

	""" Eliminar"""	
	def remove_4(self, search=None, select=False, key=None):
		""" Search sera la palabra a buscar, si 'select=False' el metodo retornara un 'True' final eliminando todas las
			coincidencias, si 'select=True' retornara un diccionario con la coincidencias halladas de las
			cuales podran ser eliminadas posteriormente usando select en 'False' y estableciendo en 'key' 
			el diccinario con la clave correspondiente al elemento del diccionario a eliminar ej: key=dict[str(key_element)] 
			Para cada caso de eliminacion exitora retornara 'True' mientras que para cada caso de no encontrar
			el elemento a eliminar, retornara 'False' """
		f = False
		di ={}
		c_di=0
		open_file = open(self.path_doc, 'r')
		read_f_4 = open_file.read()
		list_rows_4 = read_f_4.splitlines()
		try:
			if select == True:
				query_rm = search  # No hace falta declara query_rm fuera del if ya que basta con que if este dentro del contexto para que variable sea general
			if select == False:
				if key == None: query_rm = search
				else: query_rm = key
			open_file = open(self.path_doc, 'w')
			for i in list_rows_4:
				if select == True:
					if re.search(query_rm, i): # En caso de hallar la linea a remover cambiara la variable a 'True'
						#print('V:',i,re.search(query_rm, i))#>>
						f = True
						di[str(c_di)]=i
						c_di+=1
				if select == False:
					if re.search(query_rm,i): f = True # De esta forma siempre que encuentre la busqueda retornara 'True'		
					if not re.search(query_rm, i): # Rescribira todas las lineas que no contengan la palabra buscada
						open_file.write(i + '\n') 
			if select == True:
				for i in list_rows_4:
					open_file.write(i + '\n')
				return di
			elif select == False:
				if f is True: return True #ok
				else: return False 
		except Exception as e:
			print(e)
			for i in list_rows_4:
					open_file.write(i + '\n') 

	"""Imprimir"""	
	def print_5(self):
		read_f = self.open_file.read() # se podria usar nombre de clase('Dict') en lugar de 'self'. Nota: por alguna razon si lo lee previamente en __new__ o __init__ aca no lo leeria.
		#alfabet_file()
		return read_f

	def abc(self):
		alfabet_file(self.path_doc) 
		
	def error_opt(): print('\n Choose Correct Option..')


if __name__ == '__main__':

	while 1:

		test = Dict(r'docu\base_eng.txt') # instanciando objeto de clase Dict.

		val = input('Insertar - 1 >> Consulta - 2 >> Corregir - 3 >> Eliminar - 4 >> Imprimir 5>> ')
		if  val=='1':
			print('Enter <Continue> --- X <Exit>')
			while 1:
				option=input('..                        ')
				if option == 'x' or option == 'X':		
					break 
				var1=input('Palabra: ')
				var2= input('Traduccion: ')
				#var1=['cnn','perro','crush',"1",['Lista','es'],('Tupla','es','esta')]
				#var2=['canal','animal','puta',"2",['o','es','lista'],('9','oo')]
				print('desde instance:',test.insert_1(w_d=var1, t_n=var2, sep=' <--> ',n_rep=True)) #<<
				test.insert_1
		elif val=='2':
			buscar= input('Consultar Palabra>: ')
			print('Retorno query:',test.query_2(buscar))
		elif val=='3':
			optn=input('opt:' )
			if optn =='1':
				busqueda= input('Buscar>: ')
				corregir= input('Correccion>: ')
				elegir=test.correction_3(busqueda, corregir) # no es necesario poner 'select=False' por que ya esta por defecto	
			elif optn==	'2':
				busqueda= input('Buscar>: ')
				elegir=test.correction_3(busqueda, select=True)
				print(elegir,'\n')
				index=input('Index: ')
				corregir= input('Correccion>: ')
				print(test.correction_3(busqueda,corregir,key=elegir[index]))			

		elif val=='4':
			eliminar=input('PALABRA: ')
			elegir = test.remove_4(eliminar, select=True) # Nota python: Es posible insertar el parametro sin asignacion aunque tenga asignacion en la funcion/metodo
			if len(elegir) is not 0: 
				print('\nImpremir keys:',elegir,'\n')			 
				index = input('Index: ') # cambiar por selector de index
				print(test.remove_4(key=elegir[index]))

		elif val=='5':
			print(test.print_5())
			input('\n Press Enter to continue.. \n')

		elif val=='a':
			test.abc()