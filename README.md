# Estrella
Mi dirección de este repositorio es: [GitHub](https://github.com/pelahumi/Estrella)
https://github.com/pelahumi/Estrella

El diagrama de flujo de esta tarea es el siguiente:

![Diagrama de flujo](https://github.com/pelahumi/Estrella/blob/main/Captura%20de%20pantalla%202021-12-20%20a%20las%2016.46.06.png)

El código de esta tarea es el siguiente:

'''import turtle #Importamos la biblioteca que nos va a ayudar a dibujar nuestra estrella

#Le decimos al programa de que color queremos nuestra estrella y que empiece a printar
turtle.color("blue", "red")
turtle.begin_fill()

#Creamos un bucle para que la tortuga se mueva y pinte nuestra estrella de 5 puntas
n = 0
while n <= 5:
    turtle.forward(100)
    turtle.left(144)
    n = n + 1
    

#Le decimos al programa que pare de pintar
turtle.end_fill()
turtle.donedone()
