
from tkinter import Tk, Label, Button
import tkinter.font
#import pyserial 
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("JUMPLIGHTS")

        self.label = Label(master, text="DIMMING")
        self.label.pack()

        self.All_Lights_Button = Button (master, text= "ALL LED BARS",bg="Red", command = self.All_Lights, height = 10, width = 20)
        self.All_Lights_Button.pack()
        self.All_Lights_Button.place(x = 10, y=20)    
        self.Fixed_button = Button(master, text="FIXED LED BARS",bg="Red", command=self.Fixed_Final, height = 10, width = 20 )
        self.Fixed_button.pack()
        self.Fixed_button.place (x =195, y=20)
        #if self.greet_button == 1:
        self.Supplemental_button = Button (master, text="SUPPLEMENTAL LED BARS",bg="Red", command=self.Supplemental, height = 10, width = 20)
        self.Supplemental_button.pack()
        self.Supplemental_button.place (x=545, y=20)
        self.Individual_button = Button(master, text = "INDIVIDUAL LED BAR",bg="Red", command=self.Individual_Bars, height=10, width=20)
        self.Individual_button.pack()
        self.Individual_button.place (x=360, y=20)
        
        self.close_button = Button(master, text="Close", command=self.quit)
        self.close_button.pack()
        self.close_button.place(x = 460, y = 200)

    def Fixed(self):
        if self.Fixed_button:
            #then send [02 hex]
            #holding variable string
            print("Fixed button pressed send 02x")
    def Fixed_Final(self):
        Fixed()
        Dimming_Level()

    def Supplemental(self):
        if self.Supplemental_button:
            #then send [01 hex]
            #holding variable string
            print("You've Selected Supplemental LED Bars")
            
    def Individual(self):
        if self.Individual_button:
            #then send [03 hex]
            #holding variable string
            #NEEDS THIRD WINDOW
            print("You've Selected Individual Bar")

    def All_Lights(self):
         if self.All_Lights_Button:
             #then send [00 hex]
             #holding variable string
             print("All lights")
             
         
    def quit(self):
        root.destroy()

    def Dimming_Level(self):
        
        newwindow = Tk()
        newwindow.geometry('750x480')
        self.Level_0 = Button(newwindow, text="OFF",bg="Red", command=self.Off_command, height = 10, width = 20 )
        self.Level_0.pack()
        self.Level_0.place (x=10,y=20)

        self.Level_1 = Button(newwindow, text="10%",bg="Red", command=self.Ten_Percent, height = 10, width = 20 )
        self.Level_1.pack()
        self.Level_1.place (x=185,y=20)


        self.Level_2 = Button(newwindow, text="20%",bg="Red", command=self.twenty_Percent, height = 10, width = 20 )
        self.Level_2.pack()
        self.Level_2.place (x=360,y=20)


        self.Level_3 = Button(newwindow, text="30%",bg="Red", command=self.thirty_Percent, height = 10, width = 20 )
        self.Level_3.pack()
        self.Level_3.place (x=535,y=20)


        self.Level_4 = Button(newwindow, text="40%",bg="Red", command=self.fourty_Percent, height = 10, width = 20 )
        self.Level_4.pack()
        self.Level_4.place (x=10,y=200)


        self.Level_5 = Button(newwindow, text="50%",bg="Red", command=self.fifty_Percent, height = 10, width = 20 )
        self.Level_5.pack()
        self.Level_5.place (x=185,y=200)

        self.Level_6 = Button(newwindow, text="60%",bg="Red", command=self.sixty_Percent, height = 10, width = 20 )
        self.Level_6.pack()
        self.Level_6.place (x=360,y=200)

        self.Level_7 = Button(newwindow, text="70%",bg="Red", command=self.seventy_Percent, height = 10, width = 20 )
        self.Level_7.pack()
        self.Level_7.place (x=535,y=200)

        self.Level_8 = Button(newwindow, text="80%",bg="Red", command=self.eighty_Percent, height = 10, width = 20 )
        self.Level_8.pack()
        self.Level_8.place (x=150,y=400)

        self.Level_9 = Button(newwindow, text="90%",bg="Red", command=self.ninety_Percent, height = 10, width = 20 )
        self.Level_9.pack()
        self.Level_9.place (x=400,y=400)
    def Off_command(self):
        #turn off lights
        #send [00 hex]
        print("lights are off")
    def Ten_Percent(self):
        print("Lights are 10%")
    def twenty_Percent(self):
        print("Lights are 20%")
    def thirty_Percent(self):
        print("Lights are 30%") 
    def fourty_Percent(self):
        print("Lights are 40%")
    def fifty_Percent(self):
        print("Lights are 50%")
    def sixty_Percent(self):
        print("Lights are 60%")
    def seventy_Percent(self):
        print("Lights are 70%")
    def eighty_Percent(self):
        print("Lights are 80%")
    def ninety_Percent(self):
        print("Lights are 90%")







    def Individual_Bars(self):
        newwindow2=Tk()
        newwindow2.geometry('750x480')


#    def Bar1:
 #       print("Bar 1 Selected")
        
  #  def Bar2:
   # def Bar3:
    #def Bar4:
    #def Bar5:
    #def Bar6:
    #def Bar7:
    #def Bar8:
    #def Bar9:
        
        
        
    #def program that takes in the stored variables from dimming and leds, write to tx pin)
        
   # user_
root = Tk()
root.geometry('750x750')
root.resizable(0,0) #non resizable
my_gui = MyFirstGUI(root)
root.mainloop()
