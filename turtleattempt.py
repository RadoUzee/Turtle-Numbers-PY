import turtle


x = int(input("Which number: "))
scale = int(input("What size: "))

digit = 0


t= turtle.Pen()


def one():
    t.down()
    t.left(90)
    t.forward(2*scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.right(90)
    t.down()
 
def two():
    t.down()
    t.left(180)
    t.forward(scale)
    t.right(90)
    t.forward(scale)
    t.right(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.right(180)
    t.down()
 
def three():
    t.down()
    t.left(180)
    t.forward(scale)
    t.right(180)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.right(180)
    t.forward(scale)
    t.down()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.right(180)
    t.down()
 
def four():
    t.down()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.right(90)
    t.forward(scale)
    t.up()
    t.right(90)
    t.forward(scale)
    t.down()
    t.right(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.left(90)
    t.down()
 
def five():
    t.down()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.right(90)
    t.forward(scale)
    t.right(90)
    t.forward(scale)
    t.right(90)
    t.up()
    t.forward(2*scale)
    t.down()
    t.right(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.right(180)
    t.down()
 
def six():
    t.down()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.left(90)
    t.forward(2*scale)
    t.down()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.left(90)
    t.down()
 
def seven():
    t.down()
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250 ,0)
    t.right(180)
    t.down()
 
def eight():
    t.down()
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.down()
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250,0)
    t.right(180)
    t.down()

def nine():
    t.down()
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.forward(scale)
    t.down()
    t.left(90)
    t.forward(scale)
    t.up()
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.down()
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250,0)
    t.right(180)
    t.down()

def zero():
    t.down()
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.forward(2*scale)
    t.left(90)
    t.forward(scale)
    t.up()
    t.goto(index*scale*1.5-250,0)
    t.down()
    

 
 
def numbers_to_turtle(argument):

        if(argument==0): zero(),
        if(argument==1): one(),
        if(argument==2): two(),
        if(argument==3): three(),
        if(argument==4): four(),
        if(argument==5): five(),
        if(argument==6): six(),
        if(argument==7): seven(),
        if(argument==8): eight(),
        if(argument==9): nine(),

k=x

while k>=1 :
    k=k//10
    digit = digit + 1

print(digit)
index = 1
t.up()
t.goto(-250,0)
t.down()
numbers_to_turtle(x//(pow(10,digit-1)))
print (x//(pow(10,digit-1)))


while digit-2>=0:
    index = index + 1
    numbers_to_turtle((x//(pow(10,digit-2)))%10)
    print((x//(pow(10,digit-2)))%10)
    digit = digit - 1


