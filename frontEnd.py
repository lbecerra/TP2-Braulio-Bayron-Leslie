#!/usr/local/bin/python
# -*- coding: latin-1 -*-

#funciones del archivo backEnd
from backEnd import *


#librerias Importadas
import Tkinter
from Tkinter import *  
import ttk
import tkMessageBox

#se define la ventana principal
ventana =Tk()
ventana.title("Le Poulet")

#pestañas de la ventana principal
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)

notebook.add(frame1, text='Ingresar Receta')
notebook.add(frame2, text='Consultar Recetas')
notebook.add(frame3, text='Borrar Recetas')
notebook.add(frame4, text='Modificar Recetas')
Listacampos=[]
ListaModificar=[]
def CapturaCampos():#funcion que captura los campos para la modificacion
        global ListaCampos
        ListaCampos = [m_nombre.get(),m_chef.get(),m_tipo.get(),m_ingrediente.get(),m_cantidad.get(),m_paso.get()]
        plano_5.config(state="normal")
        plano_4.config(state=DISABLED)
        print ListaCampos

def Modificar():#funcion que modifica con las listas ya almacenadas
        global ListaCampos
        global ListaModificar
        ListaModificar = [m_nombre.get(),m_chef.get(),m_tipo.get(),m_ingrediente.get(),m_cantidad.get(),m_paso.get()]
        bandera=modificar(ListaCampos,ListaModificar)
        print bandera
        if(bandera==1):
                AvisoM()
        else:
                ErrorM()
        plano_4.config(state="normal")
        plano_5.config(state=DISABLED)
                       
        print ListaCampos,"\n\t",ListaModificar
        
def Ingreso():#funcion para ingresar ingredientes
        i_nombre.config(state=DISABLED)
        i_chef.config(state=DISABLED)
        i_tipo.config(state=DISABLED)
        nombre=i_nombre.get()
        chef=i_chef.get()
        tipo=i_tipo.get()
        ingrediente=i_ingrediente.get()
        cantidad=i_cantidad.get()
        paso=i_paso.get()
        if (i_nombre.get()=="" or i_chef.get()=="" or i_tipo.get()=="" or i_ingrediente.get()=="" or i_cantidad.get()=="" or i_paso.get()==""):
                Error()
        else:
                insertar(nombre,chef,tipo,ingrediente,cantidad,paso)
                Aviso()

def Finalizar():#funcion para terminar de ingresar el ultimo ingrediente de una receta
        i_nombre.config(state="normal")
        i_chef.config(state="normal")
        i_tipo.config(state="normal")
       
def Consulta():#funcion de consulta para enviar y recibir una respuesta del backend
	nombre=c_nombre.get()
	chef=c_chef.get()
	tipo=c_tipo.get()
	ingrediente=c_ingrediente.get()
	cantidad=c_cantidad.get()
	paso=c_paso.get()
	
	if c_nombre.get()=="":
		nombre="vacio"
	if c_chef.get()=="":
		chef="vacio"
	if c_tipo.get()=="":
		tipo="vacio"
	if c_ingrediente.get()=="":
		ingrediente="vacio"
	if c_cantidad.get()=="":
		cantidad="vacio"
	if c_paso.get()=="":
		paso="vacio"
	#llama a la funcion consulta del backend	
	lista=consulta(nombre,chef,tipo,ingrediente,cantidad,paso)
	Ventana(lista)

def Borrar():
        eliminar(b_nombre.get())
#funcion de salida del programa
def Salida():
        ventana.destroy()
 
 #mensaje de error al intentar insertar datos vacios
def Error():
	tkMessageBox.showinfo(title="Error", \
    message="Tiene que llenar todos los atributos de la receta")

#mensaje de error al intentar modificar datos
def ErrorM():
	tkMessageBox.showinfo(title="Error", \
    message="La modificación fallo por \ncampos inconsistentes")

#funcion de aviso al insertar los datos
def Aviso():
	tkMessageBox.showinfo(title="Aviso", \
    message="Inserción Exitosa")

#funcion de aviso al modificar los datos
def AvisoM():
	tkMessageBox.showinfo(title="Aviso", \
    message="Modificación Exitosa")
    
#ventana emergente con los resultados de las consultas
def Ventana(lista):
        ##      ventana2 = Tk()
        ##      ventana2.title("Consulta:")
        ventana2 = Toplevel(ventana)
        ventana2.title("Consulta:")
        ventana2 = Canvas(ventana2,height=300,width=500,bg="gray")
        ventana2.pack()
        ventana2.create_text(200,40,text="Resultado de su consulta: ")
        #print "lista",lista[0][0]
        EjeX = 200
        EjeY = 70
        i=0

        if (lista != []):

                rect=str(lista[0][0])
                aut=str(lista[0][1])

        while (i != len(lista)):
                r=str(lista[i][0])
                c=str(lista[i][1])
                t=str(lista[i][2])
                ing=str(lista[i][3])
                k=str(lista[i][4])
                p=str(lista[i][5])

                if ((str(rect) == str(r) and str(aut) == str(c)) and i!=0):
                        print str(rect)+"    "+r+"      "+str(aut)+"    "+c
                        ventana2.create_text(EjeX,EjeY,text= ("\nIngrediente:"+str(ing).title().replace("_"," "),"\tCantidad:"+str(k).replace("_"," "),"\tPaso:"+str(p).title().replace("_"," ")))
                        EjeY += 20
                        rect=lista[i][0]
                        aut=lista[i][1]
                        i+=1
                else:
                        EjeY += 20
                        print "eeeeeeee"+str(rect)+"    "+r+"      "+str(aut)+"    "+c
                        ventana2.create_text(EjeX,EjeY,text= ("\nReceta: "+str(r).title().replace("_"," ") ))
                        EjeY += 20
                        ventana2.create_text(EjeX,EjeY,text= ("\nChef: "+str(c).title().replace("_"," ")))
                        EjeY += 20
                        ventana2.create_text(EjeX,EjeY,text= ("\nTipo:"+str(t).title().replace("_"," ")))
                        EjeY += 20
                        ventana2.create_text(EjeX,EjeY,text= ("\nIngrediente:"+str(ing).title().replace("_"," "),"\tCantidad:"+str(k).replace("_"," "),"\tPaso:"+str(p).title().replace("_"," ")))
                        EjeY += 20
                        rect=lista[i][0]
                        aut=lista[i][1]
                        i+=1

        ventana2.config(scrollregion=(0,0,300, 1000))
        Vertical = Scrollbar(ventana2)
        ventana2.config(yscrollcommand=Vertical.set)
        Vertical.place(x=490,y=20,height=280)
        Vertical.config(command = ventana2.yview)

         
                

#----------------------------------------------------Ventana Principal-----------------------------------------------------------------------------------
#botones
        
plano_1_1 = Button(frame1, text = "Agregar Ingrediente", font = ("Helvetica", 10), command=Ingreso)
plano_1_1.place(x = 5, y = 220)

plano_1_2 = Button(frame1, text = "Terminar Receta", font = ("Helvetica", 10), command=Finalizar)
plano_1_2.place(x = 150, y = 220)

plano_2 = Button(frame2, text = "Hacer Consultas", font = ("Helvetica", 10), command=Consulta)
plano_2.place(x = 10, y = 220)

plano_3 = Button(frame3, text = "Borrar Receta", font = ("Helvetica", 10), command=Borrar)
plano_3.place(x = 10, y = 80)

plano_4 = Button(frame4, text = "Capturar Campos", font = ("Helvetica", 10), command=CapturaCampos)
plano_4.place(x = 10, y = 220)

plano_5 = Button(frame4, text = "Modificar Receta", font = ("Helvetica", 10), command=Modificar)
plano_5.place(x = 150, y = 220)
plano_5.config(state=DISABLED)

boton_s = Button(ventana, text = "Salir",font = ("Helvetica", 10), command = Salida)
boton_s.place(x = 385, y = 265)

boton_i = Button(ventana, text = "i",font = ("Helvetica", 10,"italic"), command = Salida)
boton_i.place(x = 350, y = 265)

#En este bloque se encuentran los labels de la parte de Ingreso

label_1 = Label(frame1,text="Ingrese la receta que desea crear", font = ("Helvetica", 16), fg = "black")
label_1.place(x = 10, y = 2)

label_2 = Label (frame1,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_2.place(x = 10, y = 40)

label_3 = Label (frame1,text="Chef: ", font = ("Helvetica", 12), fg = "black")
label_3.place(x = 10, y = 70)

label_4 = Label (frame1,text="Tipo: ", font = ("Helvetica", 12), fg = "black")
label_4.place(x = 10, y = 100)

label_5 = Label (frame1,text="Ingrediente: ", font = ("Helvetica", 12), fg = "black")
label_5.place(x = 10, y = 130)

label_6 = Label (frame1,text="Cantidad: ", font = ("Helvetica", 12), fg = "black")
label_6.place(x = 10, y = 160)

label_7 = Label (frame1,text="Paso: ", font = ("Helvetica", 12), fg = "black")
label_7.place(x = 10, y = 190)

nombre = StringVar()
i_nombre = Entry(frame1, textvariable = nombre)
i_nombre.place(x = 145, y = 40)

chef = StringVar()
i_chef = Entry(frame1, textvariable = chef)
i_chef.place(x = 145, y = 70)

tipo = StringVar()
i_tipo = Entry(frame1, textvariable = tipo)
i_tipo.place(x = 145, y = 100)

ingrediente = StringVar()
i_ingrediente = Entry(frame1, textvariable = ingrediente)
i_ingrediente.place(x = 145, y = 130)

cantidad = StringVar()
i_cantidad = Entry(frame1, textvariable = cantidad)
i_cantidad.place(x = 145, y = 160)

paso = StringVar()
i_paso = Entry(frame1, textvariable = paso)
i_paso.place(x = 145, y = 190)

#En este bloque se encuentran los labels de la parte de Consulta

label_8 = Label(frame2,text="Ingrese los datos de la receta: ", font = ("Helvetica", 16), fg = "black")
label_8.place(x = 10, y = 2)

label_9 = Label (frame2,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_9.place(x = 10, y = 40)

label_10 = Label (frame2,text="Autor: ", font = ("Helvetica", 12), fg = "black")
label_10.place(x = 10, y = 70)

label_11 = Label (frame2,text="Tipo: ", font = ("Helvetica", 12), fg = "black")
label_11.place(x = 10, y = 100)

label_12 = Label (frame2,text="Ingrediente: ", font = ("Helvetica", 12), fg = "black")
label_12.place(x = 10, y = 130)

label_13 = Label (frame2,text="Cantidad: ", font = ("Helvetica", 12), fg = "black")
label_13.place(x = 10, y = 160)

label_14 = Label (frame2,text="Paso: ", font = ("Helvetica", 12), fg = "black")
label_14.place(x = 10, y = 190)

nombre = StringVar()
c_nombre = Entry(frame2, textvariable = nombre)
c_nombre.place(x = 145, y = 40)

chef = StringVar()
c_chef = Entry(frame2, textvariable = chef)
c_chef.place(x = 145, y = 70)

tipo = StringVar()
c_tipo = Entry(frame2, textvariable = tipo)
c_tipo.place(x = 145, y = 100)

ingrediente = StringVar()
c_ingrediente = Entry(frame2, textvariable = ingrediente)
c_ingrediente.place(x = 145, y = 130)

cantidad = StringVar()
c_cantidad = Entry(frame2, textvariable = cantidad)
c_cantidad.place(x = 145, y = 160)

paso = StringVar()
c_paso = Entry(frame2, textvariable = paso)
c_paso.place(x = 145, y = 190)

#En este bloque se encuentran los labels de la parte de Borrado

label_8 = Label(frame3,text="Ingrese los datos de la receta a borrar: ", font = ("Helvetica", 16), fg = "black")
label_8.place(x = 10, y = 2)

label_9 = Label (frame3,text="Receta: ", font = ("Helvetica", 12), fg = "black")
label_9.place(x = 10, y = 40)

nombre = StringVar()
b_nombre = Entry(frame3, textvariable = nombre)
b_nombre.place(x = 145, y = 40)



#En este bloque se encuentran los labels de la parte de Modificacion

label_8 = Label(frame4,text="Ingrese los datos de la receta a modificar: ", font = ("Helvetica", 16), fg = "black")
label_8.place(x = 10, y = 2)

label_9 = Label (frame4,text="Nombre: ", font = ("Helvetica", 12), fg = "black")
label_9.place(x = 10, y = 40)

label_10 = Label (frame4,text="Autor: ", font = ("Helvetica", 12), fg = "black")
label_10.place(x = 10, y = 70)

label_11 = Label (frame4,text="Tipo: ", font = ("Helvetica", 12), fg = "black")
label_11.place(x = 10, y = 100)

label_12 = Label (frame4,text="Ingrediente: ", font = ("Helvetica", 12), fg = "black")
label_12.place(x = 10, y = 130)

label_13 = Label (frame4,text="Cantidad: ", font = ("Helvetica", 12), fg = "black")
label_13.place(x = 10, y = 160)

label_14 = Label (frame4,text="Paso: ", font = ("Helvetica", 12), fg = "black")
label_14.place(x = 10, y = 190)

nombre = StringVar()
m_nombre = Entry(frame4, textvariable = nombre)
m_nombre.place(x = 145, y = 40)

chef = StringVar()
m_chef = Entry(frame4, textvariable = chef)
m_chef.place(x = 145, y = 70)

tipo = StringVar()
m_tipo = Entry(frame4, textvariable = tipo)
m_tipo.place(x = 145, y = 100)

ingrediente = StringVar()
m_ingrediente = Entry(frame4, textvariable = ingrediente)
m_ingrediente.place(x = 145, y = 130)

cantidad = StringVar()
m_cantidad = Entry(frame4, textvariable = cantidad)
m_cantidad.place(x = 145, y = 160)

paso = StringVar()
m_paso = Entry(frame4, textvariable = paso)
m_paso.place(x = 145, y = 190)

ventana.geometry('445x300')
ventana.mainloop()
