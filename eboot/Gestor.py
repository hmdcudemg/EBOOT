from Tkinter import *
from tkMessageBox import *
import cPickle
import os

form1=Tk()
form1.title('Base de Datos EBOOT')
form1.iconbitmap(default="ico1.ico")
form1.resizable(width=FALSE, height=FALSE)
form1.geometry('543x427+100+100')

def gplant():
	form2=Tk()
	form2.title('Administrador de Plantillas')
	form2.resizable(width=FALSE, height=FALSE)
	form2.geometry('646x403+100+100')
	form2.iconbitmap("ico1.ico")

	plantillas =cPickle.load(open("plantillas.dat","rb")) #BASE DE DATOS 
	datos = cPickle.load(open("datos.dat","rb")) #BASE DE DATOS

	def guardarp():
		cPickle.dump(plantillas,open("plantillas.dat","wb"))
		print "plantillas guardadas"
	def guardard():
		cPickle.dump(datos,open("datos.dat","wb"))
		print "datos guardados"
	label2=Label(form2,text='Plantilla:')
	label2.place(relx=0.02, rely=0.06, relwidth=0.38, relheight=0.05)
	plan=Entry(form2,font = '{MS Sans Serif} 10')
	plan.place(relx=0.02, rely=0.12, relwidth=0.49, relheight=0.04)

	label4=Label(form2,text='Datos:')
	label4.place(relx=0.00, rely=0.23, relwidth=0.12, relheight=0.04)
	lista=Listbox(form2)
	lista.place(relx=0.02, rely=0.32, relwidth=0.12, relheight=0.60)
	def cargarr():
		lista.delete(0,END)
		for i in plantillas:
			a =  i
			lista.insert(0,a)
	cargarr()
	label2=Label(form2,text='Dato:')
	label2.place(relx=0.52, rely=0.05, relwidth=0.15, relheight=0.05)
	dat=Entry(form2,font = '{MS Sans Serif} 10')
	dat.place(relx=0.52, rely=0.12, relwidth=0.15, relheight=0.04)

	label3=Label(form2,text='Valor de dato:')
	label3.place(relx=0.69, rely=0.06, relwidth=0.15, relheight=0.04)
	var=Entry(form2,font = '{MS Sans Serif} 10')
	var.place(relx=0.69, rely=0.12, relwidth=0.13, relheight=0.04)


	def cargar1():
		g = []
		n = ""
		h = plan.get().split(";")
		plantillas[dat.get()] = h
		datos[dat.get()] = [var.get()]
		plan.delete(0,END)
		dat.delete(0,END)
		var.delete(0,END)
		guardarp()
		guardard()
		cargarr()
	button1=Button(form2,text='Cargar',command=cargar1)
	button1.place(relx=0.84, rely=0.12, relwidth=0.14, relheight=0.04)








	label4=Label(form2,text='Plantillas:')
	label4.place(relx=0.16, rely=0.23, relwidth=0.12, relheight=0.04)
	planta=Listbox(form2)
	planta.place(relx=0.15, rely=0.32, relwidth=0.80, relheight=0.60)

	ins=Entry(form2,font = '{MS Sans Serif} 10')
	ins.place(relx=0.30, rely=0.95, relwidth=0.50, relheight=0.04)
	b = []

	def lel():
		planta.insert(END,ins.get())
		h =plantillas[b[0]]
		h.append(ins.get())
		guardarp()
	button1=Button(form2,text='Agregar',command=lel)
	button1.place(relx=0.84, rely=0.95, relwidth=0.14, relheight=0.04)


	def insertar(donde,que,pos):
		donde.delete(0,END)
		for i in que:
			donde.insert(END,i)



	def cargar(object):																	#Borrar palabra de  clave
				click0 = lista.curselection()[0]
				clave3 = lista.get(click0)
				if b==[]:
					pass
				else:
					b.pop(0)
				b.append(clave3)
				index = int(click0)
				insertar(planta,plantillas[clave3],0)

	def sup(object):
				click0 = lista.curselection()[0]
				clave3 = lista.get(click0)
				print clave3
				j = askokcancel(title="Confirmacion",message="Desea eliminar esta clave?")
				if j== True:
					del plantillas[clave3]
					del datos[clave3]
					g = int(click0)
					lista.delete(g)
					guardard()
					guardarp()
				else:
					pass
	def eliminar(dic,clave,pos):#dic/clave/posicion de la clave/valor de la lista de pos
		a  = dic[clave]
		del a[pos]
		print "=========================================="
		print dic

	def elim(object):
		h =  planta.curselection()[0]
		h1 = planta.get(h)
		index = int(h)
		print index
		eliminar(plantillas,b[0],index)
		planta.delete(index)
		guardarp()

	lista.bind("<Button-1>",cargar)

	lista.bind("<Delete>",sup)
	planta.bind("<Delete>",elim)
	form2.mainloop()

def crear():
	if os.path.exists("db.dat"):
		pass
	else:
		memoria = {}
		db = cPickle.dump(memoria,open("db.dat","wb"))
crear()
def actualizar():
	cPickle.dump(memoria,open("db.dat","wb"))
	print "actualizado"
memoria = cPickle.load(open("db.dat","rb")) #BASE DE DATOS
def eliminar(dic,clave,pos1,pos):#dic/clave/posicion de la clave/valor de la lista de pos
	b = []
	for i in dic:
		b.append(i)
	m = dic.values()[b.index(clave)]
	s =  m[pos1]
	del s[pos]

j =  PhotoImage(file="logo.gif")
Label(form1,image=j).pack()

###########LABELS
cantidad = StringVar()
lel = "Terminos:" , int(len(memoria))
cantidad.set(lel)
cant = Label(textvar=cantidad)
cant.place(relx=0.78, rely=0.0001, relwidth=0.21, relheight=0.05)
jub = StringVar()

def ac():
	global lel1
	lel1 = "Conocidas:" , int(len(memoria))
	cantidad.set(lel1)
label1=Label(text='Termino')
label1.place(relx=0.32, rely=0.25, relwidth=0.11, relheight=0.03)
label4=Label(text='Malo')
label4.place(relx=0.57, rely=0.42, relwidth=0.21, relheight=0.06)
label3=Label(text='Bueno')
label3.place(relx=0.34, rely=0.42, relwidth=0.21, relheight=0.06)
label2=Label(text='Normal')
label2.place(relx=0.12, rely=0.42, relwidth=0.21, relheight=0.06)
############ENTRADAS
palabra=Entry(font = '{MS Sans Serif} 10')
palabra.place(relx=0.34, rely=0.30, relwidth=0.21, relheight=0.04)
clase=Entry(font = '{MS Sans Serif} 10')
clase.place(relx=0.34, rely=0.36, relwidth=0.21, relheight=0.04)
malo=Entry(font = '{MS Sans Serif} 10')
malo.place(relx=0.57, rely=0.49, relwidth=0.21, relheight=0.04)
bueno=Entry(font = '{MS Sans Serif} 10')
bueno.place(relx=0.34, rely=0.49, relwidth=0.21, relheight=0.04)
normal=Entry(font = '{MS Sans Serif} 10')
normal.place(relx=0.12, rely=0.49, relwidth=0.21, relheight=0.04)
######LISTAS
mal=Listbox()#MALO
mal.place(relx=0.57, rely=0.57, relwidth=0.21, relheight=0.33)
buen=Listbox() #BUENO
buen.place(relx=0.34, rely=0.57, relwidth=0.21, relheight=0.33)
norma=Listbox() #NORMAL
norma.place(relx=0.12, rely=0.57, relwidth=0.21, relheight=0.33)
def load():
	try:
		insertar(clase,memoria,0)
		insertar(norma,memoria,1)
		insertar(buen,memoria,2)
		insertar(mal,memoria,3)
	except:
		showerror(title="Error",message="No existe este termino en la base de datos")
def obtener(x):
	buf = []
	y =  x.split(";")
	for i in y:
		buf.append(i)
	print buf
	return buf
def low(x):
		b = []
		for i in x:
			b.append(i.lower())
		return b
def cargar():
	if palabra.get() not in memoria:
		una  = obtener(normal.get())
		dos  = obtener(bueno.get())
		tres = obtener(malo.get())
		ne = palabra.get()
		na = ne.split(";")
		for i in na:
			memoria[i.lower()] = [[clase.get()],una,dos,tres] 
	else:
		if palabra.get() in memoria:
			unas  = obtener(normal.get())
			dos  = obtener(bueno.get())
			tres = obtener(malo.get())
			def agregar(dic,donde,valor,pos):
				h = dic[donde]
				j = h
				if valor == [""]:
					pass
				else:
					for i in valor:
						j[pos].append(i)
			agregar(memoria,palabra.get(),unas,1)
			agregar(memoria,palabra.get(),dos,2)
			agregar(memoria,palabra.get(),tres,3)
			####fin
	malo.delete(0,END)
	bueno.delete(0,END)
	normal.delete(0,END)
	actualizar()
	load()
	ac()
def insertar(donde,que,pos):
	donde.delete(0,END)
	h =  palabra.get()
	nn = h.split(";")
	a = que[nn[0].lower()]
	j = a[pos]
	for i in j:
			donde.insert(END,i)

def pos(dic,clave):
	b = []
	for i in dic:
		b.append(i)
	return b.index(clave)
def male(object):																	#Borrar palabra de  clave
			click0 = mal.curselection()[0]
			clave3 = mal.get(click0)
			index = int(click0)
			eliminar(memoria,palabra.get(),3,index)
			actualizar()
			mal.delete(index)
def buene(object):																	#Borrar palabra de  clave
			click0 = buen.curselection()[0]
			clave3 = buen.get(click0)
			index = int(click0)
			eliminar(memoria,palabra.get(),2,index)
			actualizar()
			buen.delete(index)
def norme(object):																	#Borrar palabra de  clave
			click0 = norma.curselection()[0]
			clave3 = norma.get(click0)
			index = int(click0)
			eliminar(memoria,palabra.get(),1,index)
			actualizar()
			norma.delete(index)
mal.bind("<Delete>",male)
buen.bind("<Delete>",buene)
norma.bind("<Delete>",norme)

def borrar():
	mensaje = askokcancel(title="Confirmacion",message="Desea eliminar la palabra del diccionario para siempre?")
	if mensaje == True:
		del memoria[palabra.get()]
		palabra.delete(0,END)
		actualizar()
	else:
		pass
def opene():
	os.startfile("memori.txt")
can = 0
memoria = cPickle.load(open("db.dat","rb"))
def compilar():
	def car():
			global can
			archivo = file("memori.txt","rb")
			o = []
			for i in archivo:
				i.strip()
				o.append(i)
				
			op = []
			def add(x):
				cache = []
				for i in o[x:]:
						if i=="\n":
							break
						cache.append(i)
				op.append(cache)

			v = 0 
			k = 0
			while k == 0:
				add(v)
				v+=6
				if [] in op:
					k+=1
				else:
					can +=1
			def sa(pos):
				def nav():
					ope = []
					for t in op[pos]:
						j = t.split(";")
						ope.append(j)
					return ope
				return nav()

			bf = {}
			def agre(x):
				for i in sa(x)[0]:
					memoria[i.replace("\n","")] = [sa(x)[1],sa(x)[2],sa(x)[3],sa(x)[4]]
			for i in range(0,can):
				agre(i)
			return bf
	car()
	def actualizar():
			cPickle.dump(memoria,open("db.dat","wb"))
	actualizar()
	showinfo(title="Compilado",message="Base de datos recompilada con exito!")
def ver_datos():
	def ver(usuario):
		t = Tk()
		t.geometry("600x400")
		t.title(usuario)
		c = "Datos de:" +usuario
		Label(t,text=c).pack(side=TOP)
		Label(t,text="Datos interactivos de usuario").pack()
		l = Listbox(t,width=600,height=400)
		l.pack()
		datos = cPickle.load(open("datos.dat","rb"))
		dat = datos[entrada.get()]
		for i in dat:
			e = dat[i]
			inf = i.replace("%","")+":------------------>"+str(e)
			l.insert(END,inf)
		t.mainloop()
	g = Tk()
	g.title("User")
	Label(g,text="Introduzca el usuario del cual desea obtener los datos").pack()
	entrada = Entry(g)
	entrada.pack()
	def ide(object):
		ver(entrada.get())
		g.destroy()
	entrada.bind("<Return>",ide)
	g.mainloop()
button4=Button(text='Guardar',command=cargar)
gh = Button(text='Borrar Palabra',command=borrar)
gh.place(relx=0.78, rely=0.94, relwidth=0.21, relheight=0.05)
gh = Button(text='Abrir DB',command=opene)
gh.place(relx=0.78, rely=0.80, relwidth=0.21, relheight=0.05)
gh4 = Button(text='Compilar',command=compilar)
gh4.place(relx=0.78, rely=0.89, relwidth=0.21, relheight=0.05)
gh8 = Button(text='Ver Datos',command=ver_datos)
gh8.place(relx=0.78, rely=0.089, relwidth=0.21, relheight=0.05)
def lista():
		db = memoria
		indice = {}
		def clasificar(db,indice):		 #organiza las clases de la db en el indice			
			def obtener_clave2(clase,db):
				cach = []
				for i in db:			
					a = db[i]
					g = a[0]
					if g[0]	== clase:
						cach.append(i)
				return cach
			def obtener_clave(clase,db):
					for i in db:
						a = db[i]
						b = a[0]
						indice[b[0]] = []
			for i in db:
				obtener_clave(i,db)
			for x in indice:
				indice[x] = obtener_clave2(x,db)
		v = Tk()
		v.title("Eboot-  Administracion por Clases")
		v.geometry("500x300")
		lista1 = Listbox(v,height=50,width=40)
		lista1.pack(side=LEFT)
		lista2 = Listbox(v,height=50,width=40)
		lista2.pack(side=RIGHT)
		entr =Entry(v)
		clasificar(db,indice)
		a = indice.keys()[1]
		for i in indice:
			lista1.insert(END,i)
		def cargar0(object):
			global p
			ind = lista1.curselection()[0]
			p = indice.keys()[int(ind)]
			lista2.delete(0,END)
			for m in indice[p]:
				lista2.insert(0,m)
		def eliminar(object):
			l = askokcancel(title="Confirmacion",message="Desea eliminar realmente este termino?")
			if l == True:
				ind = lista2.curselection()[0]
				v =  lista2.get(ind)
				del db[v]
				j = indice[p]
				print j
				del j[j.index(v)]	
				print j
				lista2.delete(ind)
				actualizar()
			else:
				pass
		def car(object):
			click0 = lista2.curselection()[0]
			print click0
			clave3 = lista2.get(click0)
			index = int(click0)
			palabra.delete(0,END)
			palabra.insert(END,clave3)
			cargar()
		lista1.bind("<Double-Button-1>",cargar0)
		lista2.bind("<Double-Button-1>",car)
		lista2.bind("<Delete>",eliminar)

		v.mainloop()
me = Button(text='Lista',command=lista)
me.place(relx=0.78, rely=0.34, relwidth=0.21, relheight=0.05)
me1 = Button(text='Plantillas',command=gplant)
me1.place(relx=0.78, rely=0.30, relwidth=0.21, relheight=0.05)
fi = Button(text='Cargar Palabra',command=load)
fi.place(relx=0.01, rely=0.94, relwidth=0.21, relheight=0.05)
button4.place(relx=0.34, rely=0.94, relwidth=0.21, relheight=0.05)



form1.mainloop()
