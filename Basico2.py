# Se utiliza para comentarios

#Crear un string
#Se puede crear sting con comillas dobles o simples. El programa es sensible a
#el uso de mayusculas
"Hello Word"
'Hola Mundo' 
print("Hello Word")
print('Hola Mundo')

#Para saber que tipo de dato se utiliza el comando type
#Va a entregar como salida class string ya qie se trata de un codigo en string
print(type('Tipo de escritura'))

#Como lograr unir 2 string
#Se utiliza el comando + para producir la concatenacion pero lo va a pegar junto
print("Bye"+"World")


#Utilizacion de numeros

print(30)
#tipo de dato entero  int
print(type(30))

#Los decimales se les conoce como los floats
print(type(30.8))

#Variables de estado, logico Boolean
a = True
b = False
#El resultado del tipo de variable es bool
print(type(a))
print(type(b))



#Datos de tipo de listas de datos List

#El separador de coma es para que entienda los datos como independientes
#dentro de la lista, se definien entre parentesis
c = [10, 20, 30, 55]

#En la lista se puede incluir cualquier tipo de variables
d = ["Hola", 20, True, 30.5]

#El resultado por tupo de lista es un list
print(type(d))


#Agrupacion de datos en tuplas, datos que no cambian  Tuples

#Las tuplas no pueden cambiarse asi se definieron para siempre
#Se utilizan como variables parentesis en vez de corchetes de la lista
e = (10, 20, 30, 55)
#El tipo de variable de las tuplas es tuple
print(type(e))


#Variables de tipo diccionario. Agrupar datos de la misma identidad

#Se utilizan en formato entre llaves, se separan las unidades de informacion
#por comas
f = {
     "Jose",
     "Izquierdo",
     "Jote"
    }
print(f)

#Para identificar que tipo de informacion se anade los 2 puntos
#Concepto de clave/key =nombre, valor/value=Jose
g = {
     "nombre": "Jose",
     "apellido": "Izquierdo",
     "apodo": "Jote"
    }
print(g)

#Ejemplo de diccionario mezclando tipos de variables
h = {
     "latitud": 123.45,
     "longitud": 35.78
    }
print(h)

#Tipo de variable diccionario dict
print(type(h))



#Definicion de variables

#Se pueden definir un grupo de variables en una sola linea de codigo si se
#separan entre comas

i, j = "Jose", 1979

#La impresion se puede dejar en una sola linea
print(i, j)
