import turtle

file = open("turtle")
data = file.readlines()
file.close()

my_turtle = turtle.Turtle()
turtle.pensize(3)
#turtle.delay(1000)
turtle.speed(100)
for line in data:
    if line.rfind("Avance") >= 0:
        n = [int(tmp)for tmp in line.split() if tmp.isdigit()]
        #print(n[0])
        my_turtle.forward(n[0])
    elif line.rfind("Recule") >= 0:
        n = [int(tmp)for tmp in line.split() if tmp.isdigit()]
        my_turtle.backward(n[0])
        print("back")
    elif line.find("droite") > 0:
        n = [int(tmp)for tmp in line.split() if tmp.isdigit()]
        my_turtle.right(n[0])
        print("droite")
    elif line.find("gauche") > 0:
        n = [int(tmp)for tmp in line.split() if tmp.isdigit()]
        my_turtle.left(n[0])
        print("gauche")
turtle.delay(1000) 
