#!/usr/bin/python

from Tkinter import *
from ttk import Frame, Label, Scale, Style


class Window(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()
	
	
	def initUI(self):
		self.parent.title("WORLD")
		
		self.style = Style()
		self.style.theme_use("default")
		
		self.pack(fill=BOTH,expand=1) #pack = a geometry manager
		
		
		#button
		b = Button(self,text=" GO ",command=self.callback)
		b.pack(side=TOP,padx=15,pady=20)
		
		#text
		t = Text(self,height = 3, width = 40)
		t.pack(side=TOP,padx=15)
		t.insert(END, "Welcome.\nPlease select the number of years\nyou would like to run the Simulation.\n")
		
		#slider
		slider = Scale(self,from_=0,to=400,command=self.onScale) #values of slider!
		slider.pack(side=TOP,padx=15)
		
		self.var = IntVar()
		self.label = Label(self,text=0,textvariable=self.var)
		self.label.pack(side=TOP,padx=15)
		
	def onScale(self,val):
		v = int(float(val))
		self.var.set(v)
		
	def callback(self):
		print("CLICK!")
		
		

def main():
	top = Tk()
	top.geometry("1000x700+300+300") #width x height + x + y
	app = Window(top)
	top.mainloop()
	

if __name__ == '__main__':
	main()