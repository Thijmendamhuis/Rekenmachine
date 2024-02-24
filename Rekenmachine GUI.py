import tkinter as tk
import math

#Expression zorgt dat ervoor dat de input een lange variable wordt#
expression = "" 

#Dit zorgt ervoor dat de input van de knoppen een variablen worden#
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

#Equalpress zorgt er voor dat de som die ingevuld in door het te typen of via de knoppen wordt uitgerekend als je op  de = drukt#
def equalpress(event=None):

    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except: 
        equation.set(" Error ")
        expression = "" 

#clear zorgt er voor dat als er variablen op het scherm zijn ingevuld dat die weer weg gaat en het vakje weer leeg wordt# 
def clear():
    global expression
    expression = ""
    equation.set("")

#Functie om Pi te gebruiken#
def pi():
    global expression
    expression = expression + str(math.pi)
    equation.set(expression)

#Functie om sin te gebruiken#
def sin():
    global expression
    try:
        result = math.sin(math.radians(eval(expression)))
        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" Error ")
        expression = ""

#Functie om tan te gebruiken#
def tan():
    global expression
    try:
        result = math.sin(math.radians(eval(expression)))
        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" Error ")
        expression = ""

#Functie om cos te gebruiken#
def cos(): 
    global expression
    try:
        result = math.cos(math.radians(eval(expression)))
        expression = str(result)
        equation.set(expression)
    except:
        expression.set(" Error ")
        expression = ""

#Functie om het kwadraat van een getal uit te rekenen#
def power():
    global expression
    try:
        result = eval(expression) ** 2
        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" Error ")
        expression = ""

#Functie om een wortel van een getal uit te rekenen#
def square_root(): 
    global expression
    try:
        result = math.sqrt(eval(expression))
        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" Error ")
        expression = ""
    
#Key_press zorgt ervoor dat de input van een toetsbord een werkt inplaats van in indrukken van de knoppen#    
def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":  
        press(key)
    elif key == "\r" or key == "\n":  
        equalpress()

#Het maken van de interfance/menutje van de rekenmachine met de knoppen#
if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="black")
    gui.title("Calculator")
    gui.geometry("432x285")

    equation = tk.StringVar()
    expression_field = tk.Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=6, ipadx=100, ipady=10)
    expression_field.bind("<Key>", key_press)  
    expression_field.bind_all("<Key>", key_press)

#Alle knoppen die nodig zijn voor de rekenmachine staat hier onder#
button1 = tk.Button(gui, text=' 1 ', bg='gray', fg='white', height=2, width= 14,
                 command=lambda: press(1))
button1.grid(row=3, column=0) 

button2 = tk.Button(gui, text='2', bg ='gray', fg='white', height= 2, width= 14, 
                 command=lambda: press(2))
button2.grid(row=3, column=1) 

button3 = tk.Button(gui, text='3', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(3))
button3.grid(row=3, column=2) 

button4 = tk.Button(gui, text='4', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(4))
button4.grid(row=4, column=0) 

button5 = tk.Button(gui, text='5', bg='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(5))
button5.grid(row=4, column=1) 

button6 = tk.Button(gui, text='6', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(6))
button6.grid(row=4, column=2) 

button7 = tk.Button(gui, text='7', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(7))
button7.grid(row=5, column=0) 

button8 = tk.Button(gui, text='8', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(8))
button8.grid(row=5, column=1) 

button9 = tk.Button(gui, text='9', bg ='gray', fg='white', height= 2, width= 14,
                 command=lambda: press(9))
button9.grid(row=5, column=2) 

button10 = tk.Button(gui, text='0', bg ='gray', fg='white', height= 2, width= 14,
                  command=lambda: press(0))
button10.grid(row=6, column=0, columnspan= 2, ipadx= 54 ) 

equal = tk.Button(gui, text='=', bg ='gray', fg='white', height= 2, width= 14, 
               command=equalpress)
equal.grid(row=6, column=3) 

comma = tk.Button(gui, text=',', bg ='gray', fg='white', height= 2, width= 14,
               command=lambda: press(","))
comma.grid(row=6, column=2)

plus = tk.Button(gui, text='+', bg ='gray', fg='white', height= 2, width= 14, 
              command=lambda: press('+'))
plus.grid(row=5, column= 3)

minus = tk.Button(gui, text='-', bg ='gray', fg='white', height= 2, width= 14, 
              command=lambda: press('-'))
minus.grid(row=4, column= 3)

clear = tk.Button(gui, text='CE', bg ='gray', fg='white', height= 2, width= 14, 
              command=clear)
clear.grid(row=1, column=0)

divide = tk.Button(gui, text='/', bg= 'gray', fg='white', height= 2, width= 14, 
                command=lambda: press('/'))
divide.grid(row=2, column=3)

multiple= tk.Button(gui, text='x', bg= 'gray', fg= 'white', height= 2, width= 14,
                 command=lambda: press("*"))
multiple.grid(row=3, column= 3)

pi_button = tk.Button(gui, text='π', bg='gray', fg='white', height=2, width=14,
                    command=pi)
pi_button.grid(row=1, column=3)

sqrt_button = tk.Button(gui, text='√', bg='gray', fg='white', height=2, width=14,
                    command=square_root)
sqrt_button.grid(row=1, column=1)

sin_button = tk.Button(gui, text='sin', bg ='gray', fg='white', height=2, width=14,
                    command=sin)
sin_button.grid(row=2, column=0)

tan_button = tk.Button(gui, text='tan',bg ='gray', fg='white', height=2, width=14,
                    command=tan)
tan_button.grid(row=2, column= 1)

cos_button = tk.Button(gui, text='cos',bg ='gray', fg='white', height=2, width=14,
                    command=cos)
cos_button.grid(row=2 , column= 2)

squared_button = tk.Button(gui, text='x^2',bg ='gray', fg='white', height=2, width=14,
                    command=power )
squared_button.grid(row=1, column=2)

#Het starten van het menutje/interface van de rekenmachine#
gui.mainloop() 
