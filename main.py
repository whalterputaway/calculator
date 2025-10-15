from tkinter import *
main = Tk()
main.title("Калькулятор")
main.geometry("400x350+800+400")
def show_help(event="None"):
    help_window = Toplevel(main)
    help_window.title("Справочная информация")
    help_window.geometry("695x150+600+350")
    help_window.transient(main)
    help_window.grab_set()
    about = Label(help_window, text="Описание: Супер-калькулятор\nВозможности: Сложение/Вычитание/Умножение/Деление\nВозведение в квадрат/Поиск квадратного корня/Вычисление процента\nСлова благодарности: Хотел бы выразить огромное спасибо Папе и Маме, за все что они для меня сделали и не сделали!\n © Нгуен Чыонг 2025.",anchor="center")
    about.place(x=5,y=5)
def digit_click(digit):
        label_workpad['text'] = str(digit) if (label_workpad['text'] == "Делить на ноль нельзя!" or label_workpad['text'] == "Неверный ввод!" or label_workpad['text']=="0") else label_workpad['text'] + str(digit)
def add_to_memory(opera):
    memory.append(label_workpad["text"])
def negate_click():
        label_workpad["text"] = "-" + label_workpad["text"] if label_workpad["text"][0][0] != '-' else label_workpad['text'].replace("-","",1)
def isdex():
        return float(label_workpad["text"]) if "." in label_workpad["text"] else int(label_workpad["text"])
def sqrt_click():
    label_workpad["text"] = str(isdex()**0.5)
    if label_workpad["text"].endswith('.0'):
        label_workpad["text"] =  label_workpad["text"][:-2]
def square_click():
    label_workpad["text"] = str(isdex() ** 2)
def click_1divx():
    label_workpad["text"] = str(1 / isdex())
def operation_click(opera):
    memory.append(float(label_workpad["text"]))
    global what_to_do
    what_to_do = opera
    label_workpad["text"]="0"
def equal_click(operation):
    memory.append(float(label_workpad["text"]))
    operations = {"+": lambda: memory[0] + memory[1], "-": lambda: memory[0] - memory[1],"*": lambda: memory[0] * memory[1],"/": lambda: "Делить на ноль нельзя!" if memory[1] == 0 else memory[0] / memory[1]}
    result = operations[operation]()
    if isinstance(result, str): 
        label_workpad["text"] = result
    else:
        if result == int(result):
            label_workpad["text"] = str(int(result))
        else: 
            label_workpad["text"] = str(result)
    memory.clear()
def button_delete_click():
    if label_workpad["text"]=="" or label_workpad["text"]=="Делить на ноль нельзя!" or label_workpad['text'] == "Неверный ввод!": 
        label_workpad["text"]="0"
    if label_workpad["text"]=="0":
        return
    label_workpad["text"] = label_workpad["text"][0:-1]
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
def comma_click():
    if "." not in label_workpad['text']:
        label_workpad["text"]+="." 
    else:
        pass
button_sum = Button(text="+", width=10, height=2,font=(5),command=lambda: operation_click("+")).place(x=300,y = 250)
button_sub = Button(text="-", width=10, height=2,font=(5),command=lambda: operation_click("-")).place(x=300,y=200)
button_mul = Button(text="×", width=10, height=2,font=(5),command=lambda: operation_click("*")).place(x=300,y=150)
button_div = Button(text="÷", width=10, height=2,font=(5),command=lambda: operation_click("/")).place(x=300,y =100)
button_equal = Button(text="=",width=10,height=2,font=(5),command=lambda: equal_click(what_to_do)).place(x=300, y=300)
button1 = Button(text="1", width=10, height=2,font=(5), command=lambda: digit_click(1)).place(x = 0, y = 250)
button2 = Button(text="2", width=10, height=2,font=(5), command=lambda: digit_click(2)).place(x = 100, y = 250)
button3 = Button(text="3", width=10, height=2,font=(5), command=lambda: digit_click(3)).place(x = 200, y = 250)
button4 = Button(text="4", width=10, height=2,font=(5), command=lambda: digit_click(4)).place(x = 0, y = 200)
button5 = Button(text="5", width=10, height=2, font=(5),command=lambda: digit_click(5)).place(x = 100, y = 200)
button6 = Button(text="6", width=10, height=2, font=(5),command=lambda: digit_click(6)).place(x = 200, y = 200)
button7 = Button(text="7", width=10, height=2,font=(5), command=lambda: digit_click(7)).place(x = 0, y = 150)
button8 = Button(text="8", width=10, height=2,font=(5), command=lambda: digit_click(8)).place(x = 100, y = 150)
button9 = Button(text="9", width=10, height=2, font=(5),command=lambda: digit_click(9)).place(x = 200, y = 150)
button0 = Button(text="0", width=10, height=2,font=(5), command=lambda: digit_click(0)).place(x = 100, y = 300)
button_comma = Button(text=".", width=10, height=2,font=(5),command=comma_click).place(x=200, y=300)
button_negate = Button(text="+/-", width=10, height=2,font=(5),command=negate_click).place(x=0, y=300)
button_sqrt = Button(text="√x", width=10, height=2,font=(5), command=sqrt_click).place(x=200, y=100)
button_square = Button(text="x²", width=10, height=2,font=(5),command=square_click).place(x=100, y=100)
button_1divx = Button(text="1/x", width=10, height=2, font=(5),command=click_1divx).place(x=0, y=100)
button_procent = Button(text="%", width=10, height=2,font=(5), command=button_procent_click).place(x=0, y=50)
button_CE = Button(text="CE", width=10, height=2,font=(5),command=button_CE_click).place(x=100, y=50)
button_C = Button(text="C", width=10, height=2,font=(5),command=button_C_click).place(x=200, y=50)
button_delete = Button(text="⌫", width=10, height=2,font=(5), command=button_delete_click).place(x=300, y=50)
main.bind('<F1>', show_help)
label_workpad = Label(text="0",width=40,height=2,anchor="e",font=(100))
label_workpad.place(x=5, y = 4)
memory = []
main.mainloop()