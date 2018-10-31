class Ball:#定义类Ball
    def __init__(self,color,size,direction):#定义Ball的属性
        self.color=color
        self.size=size
        self.direction=direction
    def __str__(self):#定义打印格式
        msg="Hi,I'm a "+self.size+" "+self.color+" ball!"
        return msg

    def bounce(self):#定义动作或者方法
        if self.direction=="down":
           self.direction="up"

#引用类Ball
myBall=Ball("red","small","down")
#myBall.direction="down"
#myBall.color="red"
#myBall.size="small"

print("I just created a ball.")
print("My ball is ",myBall.size)
print("My ball is ",myBall.color)
print("my ball's direction is",myBall.direction)
print("Now I'm going to bounce the ball")
print(myBall)
myBall.bounce()
print("Now the ball's direction is",myBall.direction)