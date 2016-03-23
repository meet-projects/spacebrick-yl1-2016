from turtle import *
import turtle
class Brick(Turtle):
	def __init__(self,x,radius,y,color="blue"):
		Turtle.__init__(self)
		#ast=turtle.clone()
		#ast.shape("astroid.gif")
		#ast.ht()
		self.penup()
		self.radius=radius
		self.goto(x,y)
		self.color("pink",color)
		self.shape("circle")
		#self.shape("planet")