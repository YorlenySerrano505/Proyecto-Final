#Equipo 17  Agenda   Fecha Entrega:13/08/21
#Flores Castillo Oscar David 318021584
#Serrano Mejia Yorleny Bianeth 318113551

#Importamos paqueterias 
import os
import csv
import itertools
import re
from datetime import date
from datetime import datetime

#Inicamos haciendo la primer clase que va englobar los datos del contacto
class Contacto:
    nuevoId=itertools.count()
    def __init__(self,nombre, telefono, fecha_nacimiento):
        self.codigo=next(self.nuevoId)
        self.nombre=nombre
        self.telefono=telefono
        self.fecha_nacimiento = fecha_nacimiento

#Hacemos una segunda clase para facilitar el acceso a la información 
class Agenda:
    def __init__(self):
        self.contactos=[]
        self.edades=[]
    def OrdenarNombre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)
    def Telefono(self):
        self.contactos.sort(key=lambda contacto: contacto.telefono)
    def NuevoContacto(self,nombre, telefono, fecha_nacimiento):
        contacto=Contacto(nombre, telefono, fecha_nacimiento)
        self.contactos.append(contacto)
    def MostrarTodos(self):
        self.submenuOrden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    def Buscar(self,textoBuscar):
        encontrado=0
        for contacto in self.contactos:
            if(re.findall(textoBuscar,contacto.nombre)) or (re.findall(textoBuscar,contacto.telefono)):
                self.imprimeContacto(contacto)
                encontrado=encontrado+1
                self.submenuBuscar(contacto.codigo)
        if encontrado==0:
            self.noEncontrado()
    def Eliminar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                print('---*---*---*---*---*---*---*---*')
                print('Quieres borrarlo? (s/n)')
                print('---*---*---*---*---*---*---*---*')
                opcion=str(input(""))
                if opcion=='s' or opcion=='S':
                    print('Borrando contacto!!!')
                    del self.contactos[codigo]
                elif opcion=='n' or opcion=='N':
                    break
    def Actualizacion_contacto(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                del self.contactos[codigo]
                nombre=str(input('Escribe el nombre: '))
                telefono=str(input('Escribe el telefono: '))
                dia=str(input('Escribe el dia de nacimiento: '))
                mes=str(input('Escribe el mes de nacimiento: '))
                año=str(input('Escribe el año de nacimiento: '))
                fecha_nacimiento= dia + " de " + mes + " de " + año
                contacto=Contacto(nombre.capitalize(),telefono.capitalize(),fecha_nacimiento.capitalize())
                self.contactos.append(contacto)
                break
    def submenuBuscar(self,codigo):
        print('---*---*---*---*---*---*---*---*')
        print('Quieres (m)odificarlo o (b)orrarlo? ')
        print('---*---*---*---*---*---*---*---*')
        opcion=str(input(""))
        if opcion=='m' or opcion=='M':
            self.Actualizacion_contacto(codigo)
        elif opcion=='b' or opcion=='B':
            self.Eliminar(codigo)
        else:
            print('Continuamos sin realizar modificacion alguna')
    def submenuOrden(self):
        print('---*---*---*---*---*---*---*---*')
        print('Quieres ordenar por (n)ombre o por (t)elefono?')
        print('---*---*---*---*---*---*---*---*')
        opcion=str(input(""))
        if opcion=='n' or opcion=='N':
            self.OrdenarNombre()
        elif opcion=='t' or opcion=='T':
            self.Telefono()

    def imprimeContacto(self,contacto):
        print('---*---*---*---*---*---*---*---*')
        print('Nombre: {}'.format(contacto.nombre))
        print('Telefono: {}'.format(contacto.telefono))
        print('Fecha de nacimiento: {}'.format(contacto.fecha_nacimiento))   
        print('---*---*---*---*---*---*---*---*')
       
    def noEncontrado(self):
        print('---*---*---*---*---*---*---*---*')
        print('Contacto no encontrado')
        print('---*---*---*---*---*---*---*---*')

    def edad_anios(self,anio,mes,dia):
        fecha_nacimiento=date(anio,mes,dia)
        fecha_actual = date.today()
        resultado = fecha_actual.year - fecha_nacimiento.year
        resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        self.edades.append(resultado)

    def PromedioEdad(self):
        SumaEdades=0
        CantidadEdades=0
        for edad in self.edades:
            SumaEdades += int(edad)
            CantidadEdades += 1
        if CantidadEdades == 0:
            print('No hay datos')
        else:
            Promedio= int(SumaEdades/CantidadEdades)
            print('El promedio de las edades es: ' +str(Promedio) + ' años')

    def edadMayor(self):
        edades=[]
        contador =0
        for contacto in self.edades:
            edades.append(int(contacto.edad))
            contador +=1
        if contador ==0:
            print('agenda sin datos')
        else:
            EdadMaxima = str(max(contacto))
            print('La Edad mayor de los contactos es:' +(EdadMaxima)+ 'años')
        

    def edadMenor (self):
        edades=[]
        contador=0
        for contacto in self.edades:
            edades.append(int(contacto.edad))
            contador +=1
        if contador==0:
            print('agenda sin datos')
        else: 
            EdadMinima = str(min(contacto))
            print('La Edad menor de los contactos es:' +(EdadMinima)+ 'años')
            

def ejecutar():
    agenda=Agenda()
    while True:
        menu=str(input("""Selecciona una opcion\n
        1 Mostrar lista de contactos
        2 Buscar contacto
        3 Añadir contacto
        4 Promedio de edades
        5 Edad de contacto mayor
        6 Edad de contacto menor
        0 Salir 
        Inserte la opcion a elegir: """))
        if menu=='1':
            agenda.MostrarTodos()
        elif menu=='2':
            texto=str(input('Escribe el texto a buscar en contactos: '))
            agenda.Buscar(texto.capitalize())
        elif menu=='3':
            nombre=str(input('Escribe el nombre: '))
            telefono=str(input('Escribe el telefono: '))
            dia=str(input('Escribe el dia de nacimiento: '))
            mes=str(input('Escribe el mes de nacimiento con numero: '))
            año=str(input('Escribe el año de nacimiento: '))
            fecha_nacimiento= dia + " de " + mes + " de " + año
            agenda.edad_anios(int(año),int(mes),int(dia))
            agenda.NuevoContacto(nombre.capitalize(),telefono.capitalize(),fecha_nacimiento.capitalize())
        elif menu == '4':
            agenda.PromedioEdad()
        elif menu =='5':
            agenda.edadMayor()
        elif menu =='6':
            agenda.edadMenor()
        elif menu=='0':
            print("Hasta pronto!!!")
            break
        else:
            print("Opción no válida")
if __name__=='__main__':
    ejecutar()
