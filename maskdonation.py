from tkinter import *  # From the class tkinter all the functions are imported.
from tkinter import ttk  # From the class tkinter the function ttk is imported to create combobox.
from tkinter import messagebox  # From the class tkinter the function message box is imported to create Error messages.

s = "Select"
c = "Enter different qty.."
m1 = "Surgical mask"
m2 = "Face Filtering Piece (FFP) mask"
m3 = "N95 mask"
m4 = "Face shield"
s0 = "size"
s1 = "Child  (7.5x5)"
s2 = "Adult (9x6)"
font = "Times New Roman"
fontbgcolor = '#73C6B6'
frametext = """

Donate half price of the mask we will donate the other half



price will be adding soon


"""
class Maskdonation:

	def __init__(self,master):
		self.bg_photo = PhotoImage(file='covid.png')
		self.bg_label = Label(master,image=self.bg_photo)
		self.bg_label.place(relwidth=1.6,relheight=1.4)
		self.label()

		info_frame = Frame(master, bg=fontbgcolor, bd=5)
		info_frame.place(x=10, y=450, relwidth=0.50,relheight=0.40)
		self.info_label = Label(info_frame, text=frametext, fg='black', font=25)
		self.info_label.place(relwidth=1,relheight=1)

		edit_frame2 = Frame(master, bg='#000000', bd=2)
		edit_frame2.place(x=280, y=275, relwidth=0.30,relheight=0.054)
		self.edit_entry2 = Entry(edit_frame2)
		self.edit_entry2.place(relwidth=1, relheight=1)
		self.combomasktype(master)
		self.combomasksize(master)
		self.comboquantity(master)
		self.combodetails(master)
		self.fetchdata()
		self.allbuttons()


	def combomasktype(self,master):
		self.combotype = ttk.Combobox(master)
		self.combotype['values'] = (s, m1, m2, m3)
		self.combotype.current(0)
		self.combotype.place(x=25, y=180)


	def combomasksize(self,master):
		self.combosize = ttk.Combobox(master)
		self.combosize['values'] = (s, s1, s2)
		self.combosize.current(0)
		self.combosize.place(x=300, y=180)


	def comboquantity(self,master):
		self.comboqty = ttk.Combobox(master)
		self.comboqty['values'] = (c, )
		self.comboqty.current(0)
		self.comboqty.place(x=600, y=180)

	def combodetails(self,master):
		self.comboqty = ttk.Combobox(master)
		self.comboqty['values'] = (s, )
		self.comboqty.current(0)
		self.comboqty.place(x=289, y=350)

	def allbuttons(self):
		Button(self.bg_label, text="Show", activeforeground='#73C6B6', fg='black').place(x=500, y=350, relwidth=0.05,relheight=0.02)
		Button(self.bg_label, text="Donate", activeforeground='#73C6B6', fg='red', command=self.entername).place(x=750, y=275, relwidth=0.10,relheight=0.04),
		Button(self.bg_label, text="Check Amount", activeforeground='#73C6B6', fg='black', command=self.checkamount).place(x=820, y=180, relwidth=0.07,relheight=0.04),

	def label(self):
		Label(self.bg_label, text="Face Mask Donation Portal ", font=(font, 50),bg=fontbgcolor).place(x=400, y=45) #The heading label
		Label(self.bg_label, text="Facemask Type", font=(font, 25)).place(x=25, y=150) 
		Label(self.bg_label, text="Facemask size", font=(font, 25)).place(x=300, y=150)
		Label(self.bg_label, text="Quantity", font=(font, 25)).place(x=600, y=150)
		Label(self.bg_label, text="Name of the donator : ", font=(font, 25)).place(x=40, y=275)
		Label(self.bg_label, text="Check donator details : ", font=(font, 25)).place(x=40, y=345)


	def checkamount(self):
		defaultlist =self.comboqty.cget('values')
		newvalue = self.comboqty.get()
		try:
			newvalue == int(newvalue)
		except ValueError:
			messagebox.showerror('Error', 'Please input only numbers')
			return
		self.info_label.config(text="you have added " + newvalue +" no of mask")
		self.comboqty.config(values=defaultlist +(newvalue, ))


	def entername(self):
		maskname = self.combotype.get()
		qty = self.comboqty.get()
		donatorname = self.edit_entry2.get()
		
		messagebox.showinfo('Thank you', "Thank you " + donatorname +" for your donation")
		self.info_label.config (text=donatorname + " donated " + qty +" no of " + maskname )

	def fetchdata(self):
		maskname = self.combotype.get()
		qty = self.comboqty.get()
		donatorname = self.edit_entry2.get()




root = Tk()  # Passes the window Tk() to an object 'root'
root.geometry("2560x1600")  # Resolution of the window.
root.title("Covid-19 Mask Donation")  # Gives window title.
x = Maskdonation(root)  # Passes the class Maskdonation with parameter 'root' to an object 'x'
root.mainloop()  # Runs the main window on loop till the window is closed.



