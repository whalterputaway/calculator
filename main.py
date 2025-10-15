from tkinter import *
main = Tk()
main.title("Калькулятор")
main.geometry("400x350+800+400")
def show_help(event="None"):
    help_window = Toplevel(main)
    help_window.title("Справочная информация")
    help_window.geometry("650x150+600+350")
    help_window.transient(main)
    help_window.grab_set()
    about = Label(help_window, text="Описание: Супер-калькулятор\nВозможности: Сложение/Вычитание/Умножение/Деление\nВозведение в квадрат/Поиск квадратного корня/Вычисление процента\nСлова благодарности: Хотел бы выразить огромное спасибо Цвырко Олегу Леонидовичу, за полученные знания!\n © Нгуен Чыонг 2025.",anchor="center")
    about.place(x=5,y=5)
def digit_click(digit):
    if label_workpad['text'] == "Делить на ноль нельзя!" or label_workpad['text'] == "Неверный ввод!" or label_workpad['text']=="0": 
        label_workpad['text'] = str(digit)
    else: 
        label_workpad['text'] = label_workpad['text'] + str(digit)
def add_to_memory(opera):
    memory.append(label_workpad["text"])
def negate_click():
    if label_workpad["text"][0][0] != '-':
        label_workpad["text"] = "-" + label_workpad["text"]
    else:
        label_workpad['text'] = label_workpad['text'].replace("-","",1)
def sqrt_click():
    current = float(label_workpad["text"])
    if current < 0:
        label_workpad["text"] = "Неверный ввод!"
    else:
        label_workpad["text"] = str(current**0.5)
def square_click():
    current = float(label_workpad["text"])
    label_workpad["text"] = str(current ** 2)
def click_1divx():
    current = float(label_workpad["text"])
    label_workpad["text"] = str(1 / current)
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
buttons_config = [
    {"text": "+", "x": 300, "y": 250, "command": lambda: operation_click("+")},{"text": "-", "x": 300, "y": 200, "command": lambda: operation_click("-")},{"text": "×", "x": 300, "y": 150, "command": lambda: operation_click("*")},{"text": "÷", "x": 300, "y": 100, "command": lambda: operation_click("/")},{"text": "=", "x": 300, "y": 300, "command": lambda: equal_click(what_to_do)},{"text": "1", "x": 0, "y": 150, "command": lambda: digit_click(1)},{"text": "2", "x": 100, "y": 150, "command": lambda: digit_click(2)},{"text": "3", "x": 200, "y": 150, "command": lambda: digit_click(3)},{"text": "4", "x": 0, "y": 200, "command": lambda: digit_click(4)},{"text": "5", "x": 100, "y": 200, "command": lambda: digit_click(5)},{"text": "6", "x": 200, "y": 200, "command": lambda: digit_click(6)},{"text": "7", "x": 0, "y": 250, "command": lambda: digit_click(7)},{"text": "8", "x": 100, "y": 250, "command": lambda: digit_click(8)},{"text": "9", "x": 200, "y": 250, "command": lambda: digit_click(9)},{"text": "0", "x": 100, "y": 300, "command": lambda: digit_click(0)},{"text": ".", "x": 0, "y": 300, "command": lambda: digit_click(".")},{"text": "+/-", "x": 200, "y": 300, "command": negate_click},{"text": "√x", "x": 200, "y": 100, "command": sqrt_click},{"text": "x²", "x": 100, "y": 100, "command": square_click},{"text": "1/x", "x": 0, "y": 100, "command": click_1divx},{"text": "%", "x": 0, "y": 50, "command": button_procent_click},{"text": "CE", "x": 100, "y": 50, "command": button_CE_click},{"text": "C", "x": 200, "y": 50, "command": button_C_click},{"text": "⌫", "x": 300, "y": 50, "command": button_delete_click}
]
buttons = []
for config in buttons_config:
    button = Button(text=config["text"], width=10, height=2, command=config["command"])
    button.place(x=config["x"], y=config["y"])
    buttons.append(button)
main.bind('<F1>', show_help)
label_workpad = Label(text="0",width=40,height=2,anchor="e",font=(100))
label_workpad.place(x=5, y = 4)
memory = []
main.mainloop()