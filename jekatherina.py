import math
#==============================================TRIANGULO
def triangulo ():
#entrada base
    detener=True
    while detener:
        base= input("Introduzca el valor de la  base (>=0): ")
        try:
            base=float(base)
            if(base>=0 ):
                detener=False
            else:
                base=str(base)
                detener=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")
            
#entrada altura
    detener2=True
    while detener2:
        altura= input("Introduzca el valor de la  altura (>=0): ")
        try:
            altura=float(altura)
            if( altura>=0):
                detener2=False
                
            else:

                altura=str(altura)
                detener2=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")
    #calculo area            
    area = (base * altura)/2
    print("===========================================")
    print("El Área del triangulo es:  ",area)
    print("===========================================")
#==========================================TRAPECIO

def trapecio():
    #base superior
    detener=True
    while detener:
        base= input("Introduzca el valor de la  base superior (>=0): ")
        try:
            base=float(base)
            if(base>=0 ):
                detener=False
            else:
                base=str(base)
                detener=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")

     #base inferior
    detener=True
    while detener:
        base2= input("Introduzca el valor de la  base Inferior (>=0): ")
        try:
            base2=float(base2)
            if(base2>=0 ):
                detener=False
            else:
                base2=str(base2)
                detener=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")

#entrada altura
    detener2=True
    while detener2:
        altura= input("Introduzca el valor de la  altura (>=0): ")
        try:
            altura=float(altura)
            if( altura>=0):
                detener2=False
            else:
                altura=str(altura)
                detener2=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")
    #calculo area
    area = ((base +base2)*altura)/2
    print("===========================================")
    print("El Área del trapecio es:  ",area)
    print("===========================================")
#==============================================CIRCULO
  
def circulo():
    #radio input validado
    detener=True
    while detener:
        radio= input("Introduzca el valor de la  base superior (>=0): ")
        try:
            radio=float(radio)
            if(radio>=0 ):
                detener=False
            else:
                radio=str(radio)
                detener=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")

    #calculo area
    area = (( r**2)*(math.pi))
    print("===========================================")
    print("El Área del Circulo es:  ",area)
    print("===========================================")

#==============================================CUADRADO
  
def cuadrado():
    #radio input validado
    detener=True
    while detener:
        lado= input("Introduzca el valor de un lado  del cuadrado(>=0): ")
        try:
            lado=float(lado)
            if(lado>=0 ):
                detener=False
            else:
                lado=str(lado)
                detener=True
                print("Error: Recuerde que los valores ingresados debe ser un números >=0")
        except:
            print("Error: Recuerde que los valores ingresados debe ser un números >=0")

    #calculo area
    area = ( lado**2)
    print("===========================================")
    print("El Área del Cuadrado es:  ",area)
    print("===========================================")


            
    
