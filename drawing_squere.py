import turtle

def draw_square( some_turtle):
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.left(60)
   
        

def draw_art():    
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()#create object turtle
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    #code for flower design
    for i in range(1,37):  
        brad.left(35)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(145)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(10)
    brad.seth(270)
    brad.forward(200)

   # angie = turtle.Turtle() #Create object turtle
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick() #wylaczenie 
  
draw_art()
