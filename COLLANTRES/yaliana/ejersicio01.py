from turtle import done


notas = ()
def agregar():
    nota = float(input ("nota (0-20)"))
    notas.append(nota) if 0 <=nota 
    def mostrar ( filtrar = done ):
        if not notas : return print (" no hay notas . ")
        res = [ n for n in notas if filtrar (n)]if filtrar else notas 
        print ( " notas : " , res )
        while True : 
            print ("n1. agregar 2. mostrar  3 . promedio 4 . mayor 5. menor 6 . aprobados 7 . desaprobado 8 . salir ")
            op = input ("opcion:")
            if op == "1":agregar()
            elif op =="2": mostrar()
            elif op =="3":print(f" promedio : {sum (notas)/ len (notas ):.2f}") if notas else print ("no hay notas.")
            elif op =="4":print ("mayor :" , max (notas ))if notas else print ( "No hay notas .")
            elif op == "5":print ("menor :", min (notas )) if notas else print ( "noy hay notas." )
            elif op =="6":mostrar (lambda n : n >= 11)
            elif op =="7":mostrar (lambda n : n >= 11)
            elif op =="8":break 
            else:  print ("Opcion invalida.")