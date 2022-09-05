import turtle
import random

tela = turtle.Screen() #Variável para controle da tela
tela.bgcolor("dark slate grey") #Comando para alterar a cor de fundo

#Tortuguita 1
t1 = turtle.Turtle()
t1.shape("turtle")#Altera o formato do cursor
t1.color("dodger blue")#Altera a cor do cursor e traçado
t1.pensize(5)#Define a espessura do traço
#Tortuguita 2
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.pensize(5)
#Tortuguita 3
t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("slate blue")
t3.pensize(5)
#Tortuguita 4
t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("dark orange")
t4.pensize(5)

#Juiz (Mestre Splinter)
splinter = turtle.Turtle()
splinter.shape("triangle")#Altera o formato do cursor
splinter.fillcolor("grey")#Altera a cor do cursor
splinter.penup()#"Levanta" a caneta para não marcar o traçado
splinter.setpos(300, 80)#Define a posição do cursor no plano cartesiano
splinter.right(90)#Define a direção do cursor
splinter.pendown()#"Abaixa" a caneta para marcar o traçado novamente
splinter.pensize(5)#Define a espessura do traçado
splinter.forward(200)
splinter.right(180)

#Distancia da corrida
distancia = 300 #Contador para distância
vencedor=0 #Contador para definir o vencedor
t1_passos=0 #Contador de passos de cada Tortuguita
t2_passos=0
t3_passos=0
t4_passos=0

#Posição de cada Tortuguita (usando como base a posição da t2 como centro)
t1.penup()
t1.setpos(0, 50)
t1.pendown()
t3.penup()
t3.setpos(0, -50)
t3.pendown()
t4.penup()
t4.setpos(0, -100)
t4.pendown()

#Laço de repetição que dá início a corrida
for i in range(600):
    k = random.randrange(4)
    t1.forward(k)
    t1_passos += k
    if t1_passos >= distancia:
        pen = turtle.Turtle()
        pen.shape("blank")
        pen.color("dodger blue")
        pen.goto(0,100)
        pen.write("Leo venceu a corrida!",font=("Impact",20,"bold"))
        vencedor += 1
    k = random.randrange(4)
    t2.forward(k)
    t2_passos += k
    if t2_passos >= distancia:
        pen = turtle.Turtle()
        pen.shape("blank")
        pen.color("red")
        pen.goto(0,100)
        pen.write("Rapha venceu a corrida!",font=("Impact",20,"bold"))
        vencedor += 1
    k = random.randrange(4)
    t3.forward(k)
    t3_passos += k
    if t3_passos >= distancia:
        pen = turtle.Turtle()
        pen.shape("blank")
        pen.color("slate blue")
        pen.goto(0,100)
        pen.write("Don venceu a corrida!",font=("Impact",20,"bold"))
        vencedor += 1
    k = random.randrange(4)
    t4.forward(k)
    t4_passos += k
    if t4_passos >= distancia:
        pen = turtle.Turtle()
        pen.shape("blank")
        pen.color("dark orange")
        pen.goto(0,100)
        pen.write("Miche venceu a corrida!",font=("Impact",20,"bold"))
        vencedor += 1
    if (vencedor > 0):
        break
if (vencedor == 1):
    pen = turtle.Turtle()
    pen.shape("blank")
    pen.color("lime green")
    pen.goto(0,50)
    pen.write("Cowabungaaa!!!", font=("Impact",20,"bold"))
else:
    pen = turtle.Turtle()
    pen.shape("blank")
    pen.color("goldenrod")
    pen.goto(0,50)
    pen.write("Corrida empatada!!!", font=("Impact",20,"bold"))
    
