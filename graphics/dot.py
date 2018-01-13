from java.awt import *
from java.awt.event import *
from java.lang import *

class dot(Frame):
	def __init__(self):
		pass

	def paint(self,g):
		g.setColor(Color.white)
		while True:
			#x = Integer(String(Math.random() * 800))
			#y = Integer(String(Math.random() * 600))
			#g.drawLine(x.toValue(),y.toValue(),x.toValue(),y.toValue())
			x = int(round(float(Math.random()*800),0))
			y = int(round(float(Math.random()*600),0))
			g.drawLine(x,y,x,y)
			
			Thread.sleep(100)


d = dot()
d.setBackground(Color.black)
d.setSize(500,400)
d.setVisible(True)
d.setTitle("Random dots")
