import mysql.connector
from tabulate import tabulate
import os

class tienda_libros:
    def __init__(self):
        self.conex = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '',
            db = 'tienda-libros'
            )
        self.cur = self.conex.cursor()
    
    def volverfinalizar(self):
        self.conex.close()
        self.cur.close()
        try:
            print("------ ¿Desea continuar? ------")
            defi = int(input("1- Volver al menú principal \n2- Finalizar programa \nSeleccione una opción: "))   
            while defi <= 0 or defi >= 3:
                print("////// Ingrese un valor valido \\\\\\\\\\\\")
                defi = int(input("1- Volver al menú principal \n2- Finalizar programa \nSeleccione una opción: "))
            redi = 0
        except:
            print("////// Ingrese un valor valido \\\\\\\\\\\\")
            redi = 1    
        
        if redi == 1:
            tiend.volverfinalizar()
        else:
            if defi == 1:
                self.conex = mysql.connector.connect(
                host = 'localhost',
                port = '3306',
                user = 'root',
                password = '',
                db = 'tienda-libros'
                )
                self.cur = self.conex.cursor()
                tiend.menu()
            elif defi == 2:
                exit()   

    def lis(self):
        self.cur.execute("SELECT * FROM libros ORDER BY id")
        num = self.cur.fetchall()
        print("------ Lista de Libros ------")
        librs = []
        for i in num:
            librs.append([str(i[0]),str(i[1]),str(i[2])])
        print(tabulate(librs, headers=['Id', 'Nombre', 'Precio']))

    def listar(self):
        lisql = "SELECT * FROM libros ORDER BY id ;"
        self.cur.execute(lisql)    
        num = self.cur.fetchall()
        librs = []
        for i in num:
            librs.append([str(i[0]),str(i[1]),str(i[2])])
        print("------ Lista de Libros ------")
        print(tabulate(librs, headers=['Id', 'Nombre', 'Precio']))
        os.system('pause')
        tiend.volverfinalizar()
                    
    def insertar(self):
        print("Para agregar un libro debe de llenar los siguientes datos")
        try:
            nombre = input("Ingrese el nombre del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            while precio <= 0:
                print("////// Ingrese valores validos \\\\\\\\\\\\")
                nombre = input("Ingrese el nombre del libro: ")
                precio = float(input("Ingrese el precio del libro: "))
            hey = 2
        except:
            print("////// Ingrese un valor valido \\\\\\\\\\\\")
            os.system('pause')
            hey = 1

        if hey == 1:
            tiend.insertar()

        elif hey == 2:
            sql1 = "INSERT INTO libros(id,nombre,precio) values('','" + nombre + "', '" + str(precio) + "');"
            sql2= "SET @autoid :=0; update libros set id= @autoid := (@autoid+1); alter table libros AUTO_increment = 1 ;"
            self.cur.execute(sql1)
            self.cur.execute(sql2)
            print("****** Registro Insertado ******")
            os.system('pause')
            tiend.volverfinalizar()

    def modificar(self):
        tiend.lis()
        jul = 0
        say = 0
        try:
            idd = int(input("Seleccione el id del libro que desea modificar: "))
            while idd <= 0:
                print("////// Ingrese un valor valido \\\\\\\\\\\\")
                idd = int(input("Seleccione el id del libro que desea modificar: "))
        except:
            jul = 1    
        if jul == 1:
            print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
            print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
            os.system('pause')
            tiend.volverfinalizar()
        else:    
            self.cur.execute("SELECT * FROM libros WHERE id = " + str(idd) + ";")        
            obj = self.cur.fetchall()
            if not obj:
                print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
                print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                os.system('pause')
                tiend.volverfinalizar()
            else:
                print("------ Usted ha seleccionado ------")
                print(tabulate(obj, headers=['Id','Nombre','Precio']))
                print("------ Opciones a Modificar ------")
                print("1. Nombre \n2. Precio\n3. Nombre y Precio")
                try:
                    modify = int(input("Seleccione la opción a modificar que requiera: "))
                    while modify <= 0 or modify >= 4:
                        print("////// Ingrese un valor valido \\\\\\\\\\\\")
                        modify = int(input("Seleccione la opción a modificar que requiera: "))
                except:
                    print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
                    print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                    os.system('pause')
                    modify = 4

                if modify == 1:
                    try:
                        nombre = input("Ingrese el nuevo nombre: ")
                        while nombre == '':
                            print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                            os.system('pause')
                            nombre = input("Ingrese el nuevo nombre: ")
                        self.cur.execute("UPDATE libros SET nombre = '" + nombre + "' WHERE id = " + str(idd) + ";")
                    except:
                        print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                        print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                        os.system('pause')
                        say = 1
                elif modify == 2:
                    try:
                        precio = float(input("Ingrese el nuevo precio: "))
                        while precio <= 0:
                            print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                            os.system('pause')
                            precio = float(input("Ingrese el nuevo precio: "))
                        self.cur.execute("UPDATE libros SET precio = '" + str(precio) + "' WHERE id = " + str(idd) +";")
                    except:
                        print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                        print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                        os.system('pause')
                        say = 1
                elif modify == 3:
                    try:
                        nombre = input("Ingrese el nuevo nombre: ")
                        precio = float(input("Ingrese el nuevo precio: "))
                        while precio <= 0 or nombre == '':
                            print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                            os.system('pause')
                            nombre = input("Ingrese el nuevo nombre: ")
                            precio = float(input("Ingrese el nuevo precio: "))
                        self.cur.execute("UPDATE libros SET nombre = '" + nombre + "' WHERE id = " + str(idd) + ";")
                        self.cur.execute("UPDATE libros SET precio = '" + str(precio) + "' WHERE id = " + str(idd) + ";")
                    except:
                        print("////// Ingreso un valor no valido \\\\\\\\\\\\")
                        print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                        os.system('pause')
                        say = 1
                elif modify == 4:
                    tiend.volverfinalizar()
                if say == 1:
                    tiend.volverfinalizar()
                else:
                    self.conex.commit()
                    print("****** Registro Modificado ******")
                    os.system('pause')
                    tiend.volverfinalizar()

    def eliminar(self):
        tiend.lis()
        try:
            idd = input("Seleccione el id del libro que desea eliminar: ")
            while idd == '':
                idd = input("Seleccione el id del libro que desea eliminar: ")    
            self.cur.execute("SELECT * FROM libros WHERE id = " + str(idd) + ";")        
            obj = self.cur.fetchall()
            pul = 2
        except:
            print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
            print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
            os.system('pause')
            pul = 1
            
        if pul == 1:
            tiend.eliminar()
        else:     
            if not obj:
                print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
                print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                os.system('pause')
                tiend.eliminar()
            else:
                print("------ Usted ha seleccionado ------")
                print(tabulate(obj, headers=['Id','Nombre','Precio']))
                try:
                    confi = int(input("¿Seguro que desea eliminarlo?\n1- Si \n2- No\nIngrese el número correspondiente a su respuesta: "))
                    while confi <= 0 or confi >= 3:
                        print("////// Ingrese un valor valido \\\\\\\\\\\\")
                        confi = int(input("¿Seguro que desea eliminarlo?\n1- Si \n2- No\nIngrese el número correspondiente a su respuesta: "))
                    
                except:
                    print("////// Ingreso un valor no encontrado \\\\\\\\\\\\")
                    print("////// La base de datos denego la solicitud \\\\\\\\\\\\")
                    os.system('pause')
                    confi = 3
                if confi == 1:
                    self.cur.execute("DELETE FROM libros WHERE id = " + str(idd) + " ; SET @autoid :=0; update libros set id= @autoid := (@autoid+1); alter table libros AUTO_increment = 1 ;")
                    print("****** Registro eliminado ******")
                    os.system('pause')
                    tiend.volverfinalizar()
                elif confi == 2:
                    tiend.volverfinalizar()    
                elif confi == 3:
                    tiend.volverfinalizar()

    def finalizar(self):
        print("------ Gracias por visitarnos ------")
        exit()
    
    def menu(self):
        print("------ Bienvenido a nuestra tienda de libros ------\n1. Añadir un Registro\n2. Listar los registros\n3. Modificar un registro\n4. Borrar un registro \n5. Finalizar")
        try:
            opci = int(input("Seleccione una opción: "))
            while opci > 5 or opci <= 0:
                print("////// Ingrese un valor valido \\\\\\\\\\\\")
                opci = int(input("Seleccione una opción: "))
        except:
            print("////// Ingrese un valor valido \\\\\\\\\\\\")
            os.system('pause')
            opci = 6
        if opci >= 1 and opci <= 6:
            if opci == 1:
                tiend.insertar()
            elif opci == 2:
                tiend.listar()
            elif opci == 3:
                tiend.modificar()
            elif opci == 4:
                tiend.eliminar()
            elif opci == 5:
                tiend.finalizar()
            elif opci == 6:
                tiend.menu()
tiend = tienda_libros()
tiend.menu()
    
    
