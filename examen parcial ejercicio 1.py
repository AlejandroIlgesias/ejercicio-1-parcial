from random import randint
elec_turno=randint(1,6)
puntuacion1=0
puntuacion2=0
v=0
finaliza=0
while True:
    print("comienza el juego")
    cadena_de_caracteres="abcdefghijklmn"
    print("vuestra cadena de caracteres:",cadena_de_caracteres)
    print("hora de determinar el orden de los turnos")
    
    while True:
        numero1=int(input("que un jugador elija un numero entre 1 y 6:"))
        numero2=int(input("que el jugador restante elija un numer entre 1 y 6"))
        if numero1==elec_turno:
            jugador1=0
            print("comienza el jugador 1")
            break
        else:
            if numero2==elec_turno:
                jugador2=1
                print("comienza el jugador 2")
                break
    if numero1==elec_turno:
        print("comienza jugador 1")
        letras=int(input("indique el numero de letras que va a usar:"))
        convertir=list(cadena_de_caracteres)
        print(convertir)
        escoger=[]
        i=0#variable de control
        while True:
            letra=int(input("indique la posicion de la letra que va a escoger"))
            posicion=convertir[letra]
            print("letra escogida",posicion)#comprobacion
            escoger.append(posicion)
            
            i=i+1
            if i==letras:
                print("ya ha escogido las letras")
                break
        print("lista de letras escogidas",escoger)#comprobar
        #trabajamos con escoger,lista con letras.
        c=0#variable de control
        print("empiece a formar la palabra")
        formar=[]
        j=0
        while True:
            print("escoger",escoger)
            letra1=int(input("pon la letra:"))
            q=escoger[letra1]
            formar=formar+[q]
            print("letra puesta:",formar)
            print("esta seguro de poner la letra ahi?")
            respuesta=input("si/no:")
            if respuesta=="no":
                del formar[j]
                if j!=0:
                    j=j-1
                continue
            j=j+1
            c=c+1
            if c==len(escoger):
                print("letras escogidas",formar)
                break
        r=0#variable de control
        while True:
            palabraform=""
            for i in range(len(formar)):
                palabraform=palabraform+formar[r]
            r=r+1
            if r==len(formar):
                print("palabra formada:",palabraform)
                puntuacion1=puntuacion1+1
                break
        v=v+1
        if v==1:
            print("comienza el siguiente jugador")
            letras=int(input("indique el numero de letras que va a usar:"))
            convertir=list(cadena_de_caracteres)
            print(convertir)
            i=0#variable de control
            while True:
                letra=int(input("indique la posicion de la letra que va a escoger"))
                posicion=convertir[letra]
                print("letra escogida",posicion)#comprobacion
                escoger.append(posicion)
            
                i=i+1
                if i==letras:
                    print("ya ha escogido las letras")
                    break
            print("lista de letras escogidas",escoger)#comprobar
            #trabajamos con escoger,lista con letras.
            c=0#variable de control
            print("empiece a formar la palabra")
            formar=[]
            j=0
            while True:
                print("escoger",escoger)
                letra1=int(input("pon la letra:"))
                q=escoger[letra1]
                formar=formar+[q]
                print("letra puesta:",formar)
                print("esta seguro de poner la letra ahi?")
                respuesta=input("si/no:")
                if respuesta=="no":
                    del formar[j]
                    if j!=0:
                        j=j-1
                        continue
                j=j+1
                c=c+1
                if c==len(escoger):
                    print("letras escogidas",formar)
                    break
            r=0#variable de control
            while True:
                palabraform=""
                for i in range(len(formar)):
                    palabraform=palabraform+formar[r]
                r=r+1
                if r==len(formar):
                    print("palabra formada:",palabraform)
                    puntuacion2=puntuacion2+1
                    break
            v=0
    if numero2==elec_turno:
        print("comienza jugador 2")
        letras=int(input("indique el numero de letras que va a usar:"))
        convertir=list(cadena_de_caracteres)
        print(convertir)
        escoger=[]
        i=0#variable de control
        while True:
            letra=int(input("indique la posicion de la letra que va a escoger"))
            posicion=convertir[letra]
            print("letra escogida",posicion)#comprobacion
            escoger.append(posicion)
            
            i=i+1
            if i==letras:
                print("ya ha escogido las letras")
                break
        print("lista de letras escogidas",escoger)#comprobar
        #trabajamos con escoger,lista con letras.
        c=0#variable de control
        print("empiece a formar la palabra")
        formar=[]
        j=0
        while True:
            print("escoger",escoger)
            letra1=int(input("pon la letra:"))
            q=escoger[letra1]
            formar=formar+[q]
            print("letra puesta:",formar)
            print("esta seguro de poner la letra ahi?")
            respuesta=input("si/no:")
            if respuesta=="no":
                del formar[j]
                if j!=0:
                    j=j-1
                continue
            j=j+1
            c=c+1
            if c==len(escoger):
                print("letras escogidas",formar)
                break
        r=0#variable de control
        while True:
            palabraform=""
            for i in range(len(formar)):
                palabraform=palabraform+formar[r]
            r=r+1
            if r==len(formar):
                print("palabra formada:",palabraform)
                puntuacion2=puntuacion2+1
                break
        v=v+1
        if v==1:
            print("comienza el siguiente jugador")
            letras=int(input("indique el numero de letras que va a usar:"))
            convertir=list(cadena_de_caracteres)
            print(convertir)
            i=0#variable de control
            while True:
                letra=int(input("indique la posicion de la letra que va a escoger"))
                posicion=convertir[letra]
                print("letra escogida",posicion)#comprobacion
                escoger.append(posicion)
            
                i=i+1
                if i==letras:
                    print("ya ha escogido las letras")
                    break
            print("lista de letras escogidas",escoger)#comprobar
            #trabajamos con escoger,lista con letras.
            c=0#variable de control
            print("empiece a formar la palabra")
            formar=[]
            j=0
            while True:
                print("escoger",escoger)
                letra1=int(input("pon la letra:"))
                q=escoger[letra1]
                formar=formar+[q]
                print("letra puesta:",formar)
                print("esta seguro de poner la letra ahi?")
                respuesta=input("si/no:")
                if respuesta=="no":
                    del formar[j]
                    if j!=0:
                        j=j-1
                        continue
                j=j+1
                c=c+1
                if c==len(escoger):
                    print("letras escogidas",formar)
                    break
            r=0#variable de control
            while True:
                palabraform=""
                for i in range(len(formar)):
                    palabraform=palabraform+formar[r]
                r=r+1
                if r==len(formar):
                    print("palabra formada:",palabraform)
                    puntuacion1=puntuacion1+1
                    break
            v=0
    finaliza=finaliza+1
    if finaliza==5:
        if puntuacion1>puntuacion2:
            print("gana el jugador 1")
            break
        else:
            if puntuacion2>puntuacion1:
                print("gana el jugador 2")
                break
            

        
                    
            
            
        
            
            
            
            
            
    
            

