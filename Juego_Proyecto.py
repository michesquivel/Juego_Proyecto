#!/usr/bin/env python
# coding: utf-8

# # Proyecto 1

# # Juego del Ahorcado

# In[1]:


#Primero definiremos una lista de nombres de frutas posibles a adivinar
frutas = ["uva", "mango", "fresa", "sandia", "melon", "mamey", 
                         "tuna", "pera", "guayaba", "zarzamora", "platano"]


# In[8]:


#Importamos las librerias que nos van a ayudar a poder desarrollar el juego
import random
import string


# In[3]:


#Definimos la varible que nos ayudará a obtener el nombre de la fruta a adivinar

def obtener_nombre_valido(frutas):
    #Aqui utilizaremos random que nos ayudara a elegir una al azar
    fruta = random.choice(frutas)
    
    while '-' in fruta or ' ' in fruta:
        fruta = random.choice(frutas)
    
    return fruta.upper()


# In[4]:


#Vamos a definir ahora la varible del juego
def juegoahorcado ():
    
    print("************************************")
    print("             AHORCADO               ")
    print("************************************")
    

    fruta = obtener_nombre_valido(frutas)
    
    letras_por_adivinar = set(fruta)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    #Determinamos el numero de intentos que tiene el jugador
    intentos = 7
    
    while len(letras_por_adivinar) > 0 and intentos > 0:
        
        print(f"Adivina el nombre de la fruta :) Te quedan {intentos} intentos y has usado las siguientes letras:        {''.join(letras_adivinadas)}")
        
        #Aqui le vamos a enseñar al jugador cuantas letras ha adivinado de la palabra que le toco
        nombre_fruta_lista = [i if i in letras_adivinadas else '-' for i in fruta]
        #Aqui enseñamos el estado del juego, del "ahorcado".
        print(intentos_visual[intentos])
        #Mostramos las letras separadas por un espacio
        print(f"Fruta: {' '.join(nombre_fruta_lista)}")
        
        letra_jugador = input("Escribe una letra: ").upper()
        
        #Si la letra que escoge el jugador esta dentro de la palabra y no en el conjunto que se ha ingresado, se añade la letra a la palabra
        
        if letra_jugador in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_jugador)
            
            #Quitamos la letra de las letras a utilizar y si no le quitamos un intento al usuario
            
            if letra_jugador in letras_por_adivinar:
                letras_por_adivinar.remove(letra_jugador)
                print('')
            else:
                intentos = intentos - 1
                print(f"La letra {letra_jugador} no se encuentra en el nombre de la fruta")
                
            #Aqui si el usuario repite letras por desesperación, jaja
        elif letra_jugador in letras_adivinadas:
            print ("\nYa escribiste esa letra. Escoge una nuevamente")
        else: 
                print("La letra no es valida.")
         
        
    #El juego se gana cuando el jugador adivina la palabra o pierde cuando se le acaban los intentos
    
    if intentos == 0:
        print(intentos_visual)
        print(f"Fallaste. Has muerto. La fruta era {fruta}")
        
    else:
        print(f"Sobreviviste, adivinaste el nombre de la fruta {fruta}")
        
    


# In[5]:


intentos_visual = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }


# In[9]:


juegoahorcado()

