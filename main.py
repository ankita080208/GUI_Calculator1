# this is a GUI Calculator created using tkinter module and some functions defined to implement logic
import math as m
from tkinter import *
from tkinter.messagebox import *

# common font size.
font = ('Times New Roman',14, 'bold','italic')
font1 = ('Times New Roman',14, 'bold')

#this functions will clear input when backspace.
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END) #this will delete the existing expression
    textField.insert(0, ex) #this will insert new expression after deleting last digit input

#this function is created to clear of all inputs in one go.
def all_clear():
    textField.delete(0, END)

#click button function
def click_btn(event):
    global p
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == '*':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get() #this will fetch the expression from text field
            ans = eval(ex) #this will evaluate the expression and store it in ans
            textField.delete(0, END) #this will delete the existing expression
            textField.insert(0, ans) #after delete it was insert the new evaluate value of expression
        except Exception as e:
            print("Error..", e)
            showerror("Error", e) #this will show the error in message box to user
        return

    textField.insert(END, text)

# Class Tk is called for creating a window
window = Tk()
window.title('GUI Calculator') #title for calc

window.geometry('300x440') #customized size of calc
window.maxsize(400,500) #width,height
window.minsize(300,440)

window.iconbitmap(r'calculator.ico') #iconbitmap() is

iconFrame = Frame(window) #frame is a container with purpose of grouping to which, another widget can be added and organized.
iconFrame.pack(side=TOP, pady=3)

# pic variable storing the loaded image
pic = PhotoImage(file='calc.png') #this function will load the image
#here pic will be labelled and displayed on window
headingLabel = Label(iconFrame, image=pic)
headingLabel.grid(row=0,column=0)

#heading label, it will label the text and will display on window
heading = Label(iconFrame, text=' Solve your problem', font=font)
heading.grid(row=0,column=1)

#textfiled, entry() used to take the input from user
textField = Entry(window, font=font, justify=CENTER,relief='sunken',borderwidth= "2.5px")#it justify will in center it will take input
textField.pack(side=TOP, pady=10, fill=X, padx=10)

#buttons
buttonFrame = Frame(window) #frame is a container with purpose of grouping to which, another widget can be added and organized.
buttonFrame.pack(side=TOP, padx=10)

# adding 1-9 button using loop
num = 9
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(num), font=font, width=5,relief='ridge',borderwidth= "2.5px", activebackground='black',
                     activeforeground='orange',bg='orange')
        btn.grid(row=i, column=j)
        num = num - 1
        btn.bind('<Button-1>', click_btn)


#created all required buttons
equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge',borderwidth= "2.5px", bg='orange',activebackground='black',
                  activeforeground='orange')
equalBtn.grid(row=0, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge',borderwidth= "2.5px", bg='orange',activebackground='black',
                   activeforeground='orange')
divideBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='*',font=font1, width=5, relief='ridge',borderwidth= "2.5px", bg='orange',activebackground='black',
                 activeforeground='orange')
multBtn.grid(row=2, column=3)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge',borderwidth= "2.5px", bg='orange',activebackground='black',
                activeforeground='orange')
dotBtn.grid(row=3, column=0)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
zeroBtn.grid(row=3, column=1)

powBtn = Button(buttonFrame, text='^', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
powBtn.grid(row=3, column=2)

minusBtn = Button(buttonFrame, text='-', font=font, width=5,relief='ridge',borderwidth= "2.5px", bg='orange',activebackground='black',
                  activeforeground='orange')
minusBtn.grid(row=3, column=3)

sqrtBtn = Button(buttonFrame, text='√', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange',activebackground='black',
                 activeforeground='orange')
sqrtBtn.grid(row=4, column=0)

radBtn = Button(buttonFrame, text='toRad', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
radBtn.grid(row=4, column=1)

factBtn = Button(buttonFrame, text='x!', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                 activeforeground='orange')
factBtn.grid(row=4, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                 activeforeground='orange')
plusBtn.grid(row=4, column=3)

degBtn = Button(buttonFrame, text='toDeg', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
degBtn.grid(row=5, column=0)

sinBtn = Button(buttonFrame, text='sinθ', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
sinBtn.grid(row=5, column=1)

cosBtn = Button(buttonFrame, text='cosθ', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
cosBtn.grid(row=5, column=2)

tanBtn = Button(buttonFrame, text='tanθ', font=font, width=5, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                activeforeground='orange')
tanBtn.grid(row=5, column=3)

clearBtn = Button(buttonFrame, text='backspace', font=font, width=11, relief='ridge',borderwidth= "2.5px",bg='orange', activebackground='black',
                  activeforeground='orange', command=clear)
clearBtn.grid(row=6, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge',borderwidth= "2.5px",bg='orange',activebackground='black',
                     activeforeground='orange', command=all_clear)
allClearBtn.grid(row=6, column=2, columnspan=2)

# binding the buttons and <button1> is action of clicing on left button of mouse
plusBtn.bind('<Button-1>', click_btn)
minusBtn.bind('<Button-1>', click_btn)
multBtn.bind('<Button-1>', click_btn)
divideBtn.bind('<Button-1>', click_btn)
zeroBtn.bind('<Button-1>', click_btn)
dotBtn.bind('<Button-1>', click_btn)
equalBtn.bind('<Button-1>', click_btn)

#this function is created to calculate all the mathematical operations by calling the functions from the math library file.
def calculate(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    textField.delete(0, END)
    textField.insert(0, answer)

#binding the remaining buttons
sqrtBtn.bind("<Button-1>", calculate)
powBtn.bind("<Button-1>", calculate)
factBtn.bind("<Button-1>",calculate)
radBtn.bind("<Button-1>", calculate)
degBtn.bind("<Button-1>", calculate)
sinBtn.bind("<Button-1>", calculate)
cosBtn.bind("<Button-1>", calculate)
tanBtn.bind("<Button-1>", calculate)
window.mainloop()