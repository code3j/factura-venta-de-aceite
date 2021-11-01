import jekatherina 
print("===============Bienvenido  a la calculador de Área =================")
print("Instrucciones basicas")
print("A) Debe ingresar solo valores númericos positivos")
print("B) Utilice los números del 1 al 5 para indicar que operación desea realizar en el siguiente menu")
print("")
print("")
repet_menu=True
while(repet_menu):
    print(" ")
    print("========================Menú de Opciones========================")
    print("\t1_Calcular el área de un TRIANGULO")
    print("\t2_Calcular el área de un TRAPECIO")
    print("\t3_Calcular el área de un CIRCULO")
    print("\t4_Calcular el área de un CUADRADO")
    print("\t5_Salir del programa")

    #validación menu
    detener=True
    while detener:
        menu=input("\tPor favor ingrese su respuesta: ")
        try:
            menu=int(menu)
            if(menu>0 and menu<=5 ):
                detener=False
            else:
                menu=str(menu)
                menu=True
                print("Error: Debe ingresar un número del 1 al 5")
        except:
            print("Error: Debe ingresar un número del 1 al 5")

    #condiciones del menu
    print("")
    print("")
    if(menu==1):
        jekatherina.triangulo()
        print("Realizado por: JEKATHERINA JIMENEZ")
    if(menu==2):
        jekatherina.trapecio()
        print("Realizado por: JEKATHERINA JIMENEZ")
    if(menu==3):
        jekatherina.circulo()
        print("Realizado por: JEKATHERINA JIMENEZ")
    if(menu==4):
        jekatherina.cuadrado()
        print("Realizado por: JEKATHERINA JIMENEZ")
    if(menu==5):
        print("============================================")
        print("Fin del programa: BY JEKATHERINA JIMENEZ")
        print("============================================")
        repet_menu=False


    
