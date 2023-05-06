import numpy as np
import csv
class Alumno:
    __dni: str
    __apellido: str
    __nombre: str
    __carrera: str
    __año_cursa: int
    __nota: int
    __materias_aprobadas:list
    def __init__(self,dni,apellido,nombre,carrera,año_cursa):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año_cursa = año_cursa

        self.__materias_aprobadas = []
    def __str__(self):
        return f'{self.__apellido}, {self.__nombre}, {self.__dni}, cursando {self.__carrera} | año {self.__año_cursa} '
    def calcular_promedio(self):
        calificacion = [self.__nota]
        for self.__nota in self.__materias_aprobadas:
            promedio = np.mean(calificacion)
        return promedio
    def promedio_sin_aplaso(self):
        calificacion = [self.__nota]
        for self.__nota in self.__materias_aprobadas:
            if Alumno.__nota >=4:
                promedio = np.mean(calificacion)
            else:
                promedio = 0
        return promedio
    def __it__(self,otro:int):
        if self.__año_cursa == otro.__año_cursa:
            resultado = self.__apellido < otro.__apellido
        else:
            resultado = self.__año_cursa < otro.__año_cursa
        return resultado
class Materiasaprobadas:
    __dni:str
    __nombreMateria:str
    __fecha:int
    __nota:int
    __aprobacion:chr
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    def __str__(self):
        return f'{self.__dni}, Materia {self.__nombreMateria}, Fecha {self.__fecha}, Nota {self.__nota}, Aprobacion {self.__aprobacion}'
class GestorAlumnos:
    gestor :list
    alumno: Alumno
    materia: Materiasaprobadas
    def __init__(self):
        self.gestor = []
        self.alumno = Alumno
        self.materia = Materiasaprobadas
    def cargar_alumno(self,alumno):
        self.gestor.append(alumno)
    def buscar_alumno(self,dni):
        while self.alumno:
            if self.alumno == dni:
                return self.alumno
    def ordenar_alumnos(self):
        i:int
        j:int
        i = 1
        valor: int
        while i in (self.gestor):
            valor = self.gestor[i]
            j = i-1
            while((j > 0) and ( valor < self.gestor[j])):
                self.gestor[j+1] = self.gestor[j]
                j=j+1
            self.gestor[j+1] = valor
        return self.gestor
    def mostrar_listado(self):
        return self.gestor


class GestorMateriasAprobadas:
    gestor_mateias: list
    materia: Materiasaprobadas
    alumno: Alumno

    def __init__(self):
        self.gestor_mateias = []
        materia = Materiasaprobadas
        alumno = Alumno

    
    def cargar_materiaa(self,materia):
        self.gestor_mateias.append(materia)
    
    def buscar_alumno(self,aux_materia):
        lista_aprobrados = []
        while self.materia:
            if self.materia == aux_materia and self.materia.__nota >= 7 and self.materia.__aprobacion == 'P':
                self.alumno = GestorAlumnos.buscar_alumno(self.materia.__dni)
                if self.alumno:
                    lista_aprobrados.append((self.alumno, self.materia.__fecha, self.materia.__nota))
        return lista_aprobrados

gestor_alumnos = GestorAlumnos()
gestor_mateias = GestorMateriasAprobadas()
#Programa principal
if __name__ == '__main__':

    with open('alumnos.csv', 'r',encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter=";")
        for linea in lector:
            datos_alum = linea.strip().split(';')
            dni = datos_alum[0]
            apellido = datos_alum[1]
            nombre = datos_alum[2]
            carrera = datos_alum[3]

