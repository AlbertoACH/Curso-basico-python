# Declaramos variable
calificacion = input ("Introduce tu calficacion de la AZ-900:  ")

calificacion = int(calificacion)

# Preguntamos se la calificacion es menor a 700
if calificacion < 700 : 
        print("Veees, por no estudiar!")
elif calificacion > 1000 :
    print("Mientes!!! No puedes sacar mas de mil")
else : #Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecutasi ninguno de los if se cumple

# Verificardor de mayoria de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido, pasa a votar")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes entrar, aun no eres mayor")