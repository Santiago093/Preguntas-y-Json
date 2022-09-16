import random


class Cuestionador:
    
    def __init__(self):
        #atributos de tipo lista
        self.questions=[
            
            "¿Qué es el almocantarat?"    ,
            "Donde queda el zenit"  
        ]      
        self.answers=[
            
            "Circulo imaginario en la esfera celeste ",
            
            "90° respecto al horizonte ",
            
            "12" 
        ]
    def jugar(self):
        
        #generar un número aleatorio entre 0 y n-1 siendo n el tamaño de la lista de preguntas
        
        n=len(self.questions)
        number= random.randint(0, n)
        
        print(self.questions[number])
        
        #solicitar respuesta
        
        respuesta=input("Cual es su respuesta: ")
        
        #verificar si la respuesta es correcta
        
        if respuesta ==self.answers[number]:
        
