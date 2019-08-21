#!usr/bind/python
#-*- coding: utf-8 -*-

"""This module allows to create, consult, modify and visualize simple databases in text documents."""

__autor__ = "Jhonatan Leonardo Zuluaga Torres "
__copyright__ = "Copyright 2018, Jhonatan Zu"
__credits__ = "Jhonatan Zu"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jhonatan Zu"
__email__ = "jhonatan.zero@gmail.com"
__status__ = "Developer"


import re

def no_repeat(word,path_doc):
	repeat = False
	global open_file  
	open_file = open(path_doc, 'r') 
	read_fr = open_file.read()
	if re.search(word, read_fr):
		repeat = True         
	open_file = open(path_doc, 'r+')
	return repeat

def alfabet_file(path_doc, recv_abc= False):
	print('\nOrdenando Alfabeticamente\n')
	if recv_abc==True:
		print('entro')
		global open_file 
		open_file = open(path_doc, 'r')
	else: 
		open_file = open(path_doc, 'r')
	f_read = open_file.read() 
	print('lect:',f_read)
	open_file = open(path_doc, 'w') 
	list_rows = f_read.splitlines() 
	print('\nROWS:',list_rows)
	for i in Dict.alfabet:
		for j in list_rows: 
			if re.findall('^'+i, j): 
				print(':',j)
				open_file.write(j+'\n')
	open_file.close() 

def write_file(path_doc, abc, n_rep): 
	if n_rep == False:
		open_file = open(path_doc, 'r+')
	for i in Dict.alfabet: 
		list_keys = Dict.dicc.keys()
		for j in list_keys: 
			if j.startswith(i):
				open_file.read() 
				print('dicc:',Dict.dicc[j])
				open_file.write(Dict.dicc[j]+"\n") 
	if abc==True: 
		alfabet_file(path_doc,recv_abc=abc) 	
	return Dict.dicc[j]

def emptyVars():
	Dict.dicc = {} 
	#test.count = 0  
	return 0



class Dict:
	""" set path"""
	open_file = None
	dicc = {}	
	alfabet = ('A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k',
			'L','l','M','m','N','n','Ñ','ñ','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v', 
			'W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9	')
	"""
	def __new__(cls): 
		while True:
			try:	#PENDIENTE POR OPTIMIZAR
				cls.open_file = open(r'docu\base_eng.txt', 'r+') 
				break
			except Exception as e:
				cls.open_file = open(r'docu\base_eng.txt', 'w') 
				print('A file was created because the error was presented: ', e)
		return super().__new__(cls) """		

	"""inicializador"""
	def __init__(self,path_doc):
		self.path_doc = path_doc
		list_keys=[]
		self.count = 0
		f_read = None  # opcional
		while True:
			try:	
				Dict.open_file = open(path_doc, 'r+') 
				break
			except Exception as e:
				Dict.open_file = open(path_doc, 'w') 
				#print('A file was created because the error was presented: ', e)		

	""" insetar palabras"""	
	def insert_1(self, w_d=None,t_n=None, sep= ' ', n_rep=False, abc=True): 
		"""Insert strings, lists composed of strings or other lists or
			of tuples but which in turn are also composed of strings.
			(sep) set the separator"""
		inst = w_d 
		tran = t_n
		if type(inst) is  str:
			add_list = []
			add_list.append(inst) 
			inst = add_list 
		elif type(inst) is int:
			raise NameError('Type(Int) is useless.') 
		if type(tran) is  str:
			add_list = []
			add_list.append(tran) 
			tran = add_list 
		elif type(tran) is int:
			raise NameError('Type(Int) is useless.')  
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
					for i in self.alfabet: 
						if insert.startswith(i): 
							list_keys = self.dicc.keys() 
							for j in list_keys: 
								if j.startswith(i): 
									self.count +=1      
							self.dicc[i+str(self.count)]= insert + sep + translation   
							break
		return_w = write_file(self.path_doc, abc,n_rep)
		print ("\n",self.dicc,"\n")
		open_file.close()
		if n_rep == False:
			alfabet_file(self.path_doc) #>>
		self.count=emptyVars() 		
		return return_w

	"""Consultar palabras""" 	
	def query_2(self,consult):
		"""Returns a dictionary with the lines containing
			matches found or (False) will return if nothing is found"""
		open_file = open(self.path_doc, 'r') 
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
			return False 
		else:
			return di_query		

	"""Corrector"""			
	def correction_3(self,consult=None, correct=None, select=False, key=None):
		""" consult sets the word to consult, while correct sets the word
			to correct. If (select = False) will correct the matches, if select = True will return a dictionary
			with the matches found, to correct one of the dictionary matches
            select select again in 'False' and the chosen dictionary element example: key = dict [str(key_element)]"""
		save=''
		#print(':::',key)
		di_corr={}    
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
			#print(query_2, i) 
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
		""" Search will be the word to search, if (select = False) the method will return a final (True) eliminating all
			matches, if (select = True) will return a dictionary with the matches found from the
			which can be removed later using select in (False) and setting to (key)
			the dictionary with the key corresponding to the dictionary element to be deleted example: key = dict [str (key_element)]
			For each case of successful elimination, (True) will return while for each case of not finding
			the item to be deleted will return (False) """
		f = False
		di ={}
		c_di=0
		open_file = open(self.path_doc, 'r')
		read_f_4 = open_file.read()
		list_rows_4 = read_f_4.splitlines()
		try:
			if select == True:
				query_rm = search  
			if select == False:
				if key == None: query_rm = search
				else: query_rm = key
			open_file = open(self.path_doc, 'w')
			for i in list_rows_4:
				if select == True:
					if re.search(query_rm, i): 
						#print('V:',i,re.search(query_rm, i))#>>
						f = True
						di[str(c_di)]=i
						c_di+=1
				if select == False:
					if re.search(query_rm,i): f = True 		
					if not re.search(query_rm, i): 
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
		"""Print document"""
		read_f = self.open_file.read() 
		#alfabet_file()
		return read_f

	def abc(self):
		alfabet_file(self.path_doc) 
		
	def error_opt(): print('\n Choose Correct Option..')







if __name__ == '__main__':

	while 1:

		test = Dict(r'docu\base_eng.txt') 

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

		test = Dict