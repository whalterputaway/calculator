from tkinter import *
main = Tk()
main.title("Калькулятор")
main.geometry("400x400+800+400")
main.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
main.maxsize(400,350)   # максимальные размеры: ширина - 400, высота - 300
main.iconbitmap(default="C:\\Users\\modes\\BSBO-21-24\\source\\calculator.ico")

def digit_click(digit):
    current = label_workpad['text']
    if current == "Делить на ноль нельзя!" or current == "Неверный ввод!":
        current = "0"
    if current == "0":
        label_workpad['text'] = str(digit)
    else:
        label_workpad['text'] = current + str(digit)

def add_to_memory(opera):
    current = label_workpad["text"]
    memory.append(current)

def negate_click():
    if int(label_workpad["text"]) >= 0:
        label_workpad["text"] = "-"+label_workpad["text"]
    elif label_workpad["text"][0]=="-":
        label_workpad["text"] = label_workpad["text"][1:]

def sqrt_click():
    current = float(label_workpad["text"])
    if current < 0:
        label_workpad["text"] = "Неверный ввод!"
    else:
        label_workpad["text"] = (current**0.5)

def square_click():
    current = float(label_workpad["text"])
    label_workpad["text"] = current ** 2

def click_1divx():
    current = float(label_workpad["text"])
    label_workpad["text"] = 1 / current

def operation_click(opera):
    memory.append(float(label_workpad["text"]))
    global what_to_do
    what_to_do = opera
    label_workpad["text"]="0"


def equal_click(operation):
    memory.append(float(label_workpad["text"]))
    if operation=="+":
        label_workpad["text"]=memory[0]+memory[1]
    elif operation=="-":
        label_workpad["text"]=memory[0]-memory[1]
    elif operation=="*":
        label_workpad["text"]=memory[0]*memory[1]
    elif operation=="/":
        if memory[1]==0:
            label_workpad["text"]="Делить на ноль нельзя!"
        else:
            label_workpad["text"]=memory[0]/memory[1]
    memory.clear()

def button_delete_click():
    label_workpad["text"] = label_workpad["text"][0:-1]
    if label_workpad["text"]=="" or label_workpad["text"]=="0":
        label_workpad["text"]="0"

def button_procent_click():
    memory.append(float(label_workpad["text"]))
    if what_to_do=="*":
        label_workpad["text"] =(memory[0]*memory[1])*0.01
    memory.clear()

def button_CE_click():
    label_workpad["text"] = "0"

def button_C_click():
    label_workpad["text"] = "0"
    memory.clear()


button_sum = Button(text="+", width=5, height=2,command=lambda: operation_click("+")).place(x=200+50,y = 200+50)
button_sub = Button(text="-", width=5, height=2,command=lambda: operation_click("-")).place(x=200+50,y=150+50)
button_mul = Button(text="*", width=5, height=2,command=lambda: operation_click("*")).place(x=200+50,y=100+50)
button_div = Button(text="÷", width=5, height=2,command=lambda: operation_click("/")).place(x=200+50,y = 50+50)
button_equal = Button(text="=",width=5,height=2,command=lambda: equal_click(what_to_do)).place(x=200+50, y=250+50)


button1 = Button(text="1", width=5, height=2, command=lambda: digit_click(1)).place(x = 50+50, y = 100+50)
button2 = Button(text="2", width=5, height=2, command=lambda: digit_click(2)).place(x = 100+50, y = 100+50)
button3 = Button(text="3", width=5, height=2, command=lambda: digit_click(3)).place(x = 150+50, y = 100+50)
button4 = Button(text="4", width=5, height=2, command=lambda: digit_click(4)).place(x = 50+50, y = 150+50)
button5 = Button(text="5", width=5, height=2, command=lambda: digit_click(5)).place(x = 100+50, y = 150+50)
button6 = Button(text="6", width=5, height=2, command=lambda: digit_click(6)).place(x = 150+50, y = 150+50)
button7 = Button(text="7", width=5, height=2, command=lambda: digit_click(7)).place(x = 50+50, y = 200+50)
button8 = Button(text="8", width=5, height=2, command=lambda: digit_click(8)).place(x = 100+50, y = 200+50)
button9 = Button(text="9", width=5, height=2, command=lambda: digit_click(9)).place(x = 150+50, y = 200+50)
button0 = Button(text="0", width=5, height=2, command=lambda: digit_click(0)).place(x = 100+50, y = 250+50)


button_comma = Button(text=".", width=5, height=2,command=lambda:digit_click(".")).place(x=50+50, y=250+50 )
button_negate = Button(text="+/-", width=5, height=2,command=negate_click).place(x=150+50, y=250+50 )
button_sqrt = Button(text="√x", width=5, height=2, command=sqrt_click).place(x=150+50, y=50+50 )
button_square = Button(text="x²", width=5, height=2,command=square_click).place(x=100+50, y=50 +50)
button_1divx = Button(text="1/x", width=5, height=2, command=click_1divx).place(x=50+50, y=50 +50)
button_procent = Button(text="%", width=5, height=2, command=button_procent_click).place(x=50+50, y=50)
button_CE = Button(text="CE", width=5, height=2,command=button_CE_click).place(x=100+50, y=50)
button_C = Button(text="C", width=5, height=2,command=button_C_click).place(x=150+50, y=50)
button_delete = Button(text="⌫", width=5, height=2, command=button_delete_click).place(x=200+50, y=50)


label_workpad = Label(text="0",width=27,height=2,bg='white',anchor="e")
label_workpad.place(x=100, y = 10)
memory = []
what_to_do = "+"
print(memory)
main.mainloop()