from turtle import * #Importamos la biblioteca que nos va a ayudar a dibujar nuestra estrella

#Le decimos al programa de que color queremos nuestra estrella y que empiece a printar
color("blue", "red")
begin_fill()

#Creamos un bucle para que la tortuga se mueva y pinte nuestra estrella de 5 puntas
while True:
    forward(100)
    left(144)
    if abs(pos()) < 1:
        break



