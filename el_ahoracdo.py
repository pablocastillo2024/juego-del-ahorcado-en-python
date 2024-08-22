import random


def palabra_en_el_ahorcado() -> str:
    palabras= ['medicina','contaduria', 'ingenieria','marketing', 'negocios', 'arquitectura']
    
    return random.choice(palabras)


def mostrar_progreso (palabra_secreta ,letras_adivinadas):
    letra_a_adivinar = " "
    
    for letra in palabra_secreta :
        if letra in letras_adivinadas:
            letra_a_adivinar += letra
        
        else:
            letra_a_adivinar += "_"
            
    return letra_a_adivinar

def  juegoDelAhorcado ():
    palabra_secreta = palabra_en_el_ahorcado()
    letras_adivinadas = []
    intentos= 10
    juego_terminado = False
    
    print('Bienvenido al juego del ahorcado')
    print(f'tienes {intentos} intentos  para  completar la palabra')
    print(mostrar_progreso (palabra_secreta , letras_adivinadas), "la cantidad de letras de la palabra es ", len(palabra_secreta))
    
    while not juego_terminado and intentos > 0 :
        letra_a_adivinar = input('introduce  una letra ' ).lower()
        
        if len(letra_a_adivinar)!= 1 or not letra_a_adivinar. isalpha():
            print('por favor  introduzca  una letra , no se admite numeros ni simbolos')
            
        elif letra_a_adivinar in letras_adivinadas:
            print( 'ya utilisaste  esta letra , intentalo con otra')
        else:
            letras_adivinadas.append (letra_a_adivinar)
            
            if letra_a_adivinar in palabra_secreta:
                print(f'muy bien  la letra {letra_a_adivinar} esta en la palabra')
                
            else:
                intentos -=1
                print(f'lo siento la letra {letra_a_adivinar} no esta en la palabra')
                print( f'te quedan {intentos} intentos')
                
        progreso_actual = mostrar_progreso (palabra_secreta , letras_adivinadas)
        print(progreso_actual)
        
        if "_"  not in  progreso_actual:
            juego_terminado=  True   
            print(f'felicitaciones  ganaste  la palabra secreta es {palabra_secreta}')  
             
                
    if intentos == 0:
        print(f'lo sentimos  terminaste  todos los intentos , la palabra secreta  es {palabra_secreta}') 
        
        
juegoDelAhorcado()  
            
        
  

