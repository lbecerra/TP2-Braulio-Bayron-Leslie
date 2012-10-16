from pyswip import*

#Para definir las afirmaciones y su aridad



#Funcion para insertar los datos en la base de conocimiento
def Escritura(Archivo, Texto, Tipo):
        archivo = open(Archivo, Tipo)
        archivo.write(Texto)
        archivo.close()

def insertar(Nombre, Autor, Estilo, Ingrediente, Cantidad, Paso):
        Contenido = "receta("+Nombre.lower().replace(" ","_")+","+Autor.lower().replace(" ","_")+","+Estilo.lower().replace(" ","_")+","+Ingrediente.lower().replace(" ","_")+","+Cantidad+","+Paso.lower().replace(" ","_")+").\n"
        Escritura("Le_Poulet.pl",Contenido,"a")

def leer():
        archivo = open("Le_Poulet.pl","r")
        lineas = archivo.readlines()
        lista=[]
        for i in lineas:
                #print i[7:len(i)-3].split(",")
                lista+=[i[7:len(i)-3].split(",")]
        archivo.close()
        return lista

def eliminar(Nombre):
        lineas=leer()
        i=0
        
        while(i!=len(lineas)):
                if(lineas[i][0]==Nombre):
                        
                        lineas.pop(i)
                else:
                        i+=1
                
        archivo = open("Le_Poulet.pl", "w") #Se reescribe el archivo con la receta eliminada.
        print lineas
        for r in lineas:
            archivo.write("receta("+r[0]+","+r[1]+","+r[2]+","+r[3]+","+r[4]+","+r[5]+").\n")
            
        archivo.close()

def modificar(ListaA,ListaN):
        bandera=0
        lineas=leer()
        for i in lineas:
                if (ListaA[0]==i[0] and ListaA[1]=="" and ListaA[2]==""):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                
                        elif(ListaN[0]!=""):
                                i[0]=ListaN[0]
                elif (ListaA[0]=="" and ListaA[1]==i[1] and ListaA[2]==""):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                
                        elif(ListaN[1]!=""):
                                i[1]=ListaN[1]
                elif (ListaA[0]=="" and ListaA[1]=="" and ListaA[2]==i[2]):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                
                        elif(ListaN[2]!=""):
                                i[2]=ListaN[2]
                elif (ListaA[0]==i[0]and ListaA[1]==i[1] and ListaA[2]==""):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                print "cuarta a"
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                print "cuarta b"
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                print "cuarta c"
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                print "cuarta d"
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                print "cuarta e"
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                print "cuarta f"
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                print "cuarta g"
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                
                        elif(ListaN[0]!="" and ListaN[1]!=""):
                                i[0]=ListaN[0]
                                i[1]=ListaN[1]
                elif (ListaA[0]==i[0]and ListaA[1]=="" and ListaA[2]==i[2]):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                
                        elif(ListaN[0]!="" and ListaN[2]!=""):
                                i[0]=ListaN[0]
                                i[2]=ListaN[2]
                elif (ListaA[0]==""and ListaA[1]==i[1] and ListaA[2]==i[2]):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                break
                        elif(ListaN[1]!="" and ListaN[2]!=""):
                                i[2]=ListaN[2]
                                i[1]=ListaN[1]
                elif (ListaA[0]==i[0]and ListaA[1]==i[1] and ListaA[2]==i[2]):
                        bandera=1
                        if(ListaA[3]==i[3] and ListaA[4]=="" and ListaA[5]==""):
                                i[3]=ListaN[3]
                        elif (ListaA[3]=="" and ListaA[4]==i[1] and ListaA[5]==""):
                                i[4]=ListaN[4]
                        elif (ListaA[3]=="" and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==""):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]=="" and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[5]=ListaN[5]
                        elif (ListaA[3]==""and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[5]=ListaN[5]
                                i[4]=ListaN[4]
                        elif (ListaA[3]==i[3]and ListaA[4]==i[4] and ListaA[5]==i[5]):
                                i[3]=ListaN[3]
                                i[4]=ListaN[4]
                                i[5]=ListaN[5]
                                break
                        elif(ListaN[0]!="" and ListaN[1]!="" and ListaN[2]!=""):
                                i[0]=ListaN[0]
                                i[1]=ListaN[1]
                                i[2]=ListaN[2]
        archivo = open("Le_Poulet.pl", "w") #Se reescribe el archivo con la receta eliminada.
        print lineas
        for r in lineas:
            archivo.write("receta("+r[0]+","+r[1]+","+r[2]+","+r[3]+","+r[4]+","+r[5]+").\n")
        archivo.close()
        return bandera
                        
        
#esta funcion retorna una lista con los valores que se optuvieron de la consulta
def consulta(nombre,chef,tipo,ingrediente,cantidad,paso):
        #Se definen las variables Unbound y las variables en las que se guardaran los valores
        prolog=Prolog()
        prolog.consult("Le_Poulet.pl")
        receta = Functor("receta", 6)
        Nombre = Variable()
        Chef = Variable()
        Tipo = Variable()
        Ingrediente = Variable()
        Cantidad = Variable()
        Paso= Variable()
        a=Nombre;
        b=Chef;
        c=Tipo;
        d=Ingrediente;
        e=Cantidad;
        f=Paso;

        #Condiciones para encontar las variables que unificaran
        if nombre != "vacio":
                a=nombre;
        if chef != "vacio":
                b=chef;
        if tipo != "vacio":
                c=tipo;
        if ingrediente != "vacio":
                d=ingrediente;
        if cantidad != "vacio":
                e=cantidad;
        if paso != "vacio":
                f=paso;
        #esta lista almacena todas las consultas	
        lista=[]
        #apertura del query para iniciar consulta en prolog
        prolog.consult("Le_Poulet.pl")
        q=Query(receta(a,b,c,d,e,f))
        #Permite acceder a la soluciones de la consulta y almacenarlas en una lista
        while q.nextSolution():
                if nombre == "vacio":
                        a=Nombre.value;
                        
                if chef == "vacio":
                        b=Chef.value;
                if tipo == "vacio":
                        c=Tipo.value;
                if ingrediente == "vacio":
                        d=Ingrediente.value;
                if cantidad == "vacio":
                        e=Cantidad.value;
                if paso == "vacio":
                        f=Paso.value;
                lista2=[a,b,c,d,e,f]
                lista.insert(len(lista),lista2)
        #cierre del query
        q.closeQuery()
        return lista


