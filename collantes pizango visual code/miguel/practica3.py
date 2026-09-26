def saludar_aleatorio():
    import random
    saludos = [
     "¡Hola!",
     "¡Bienvenido!" ,
     "¡Que gusto verte!",
     "¡Hola amig@!",
     "¡Buenos dias!"
    ]
    saludo_elegido = random.choice(saludos)
    print(saludo_elegido) 
    
saludar_aleatorio();  
    