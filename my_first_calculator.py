from tkinter import *

FONT = ('xenara',15,'normal')
FONT_FOR_NUMBERS = ('Noto Sans Math',25,'bold')
operation_dict = {'+':'+','-':'-','X':'*','÷':'/'}
history = []

result = None
numbers = []
last_operation  = None
last_number = None

def validate_digit(input):
    if input.isdigit() or input == "" or '.' in input or '-' in input :
        return True
    else:
        return False

def clear():
    global result, last_operation, numbers
    numbers.clear()
    result = None
    last_operation = None
    history.clear()
    number_entry.delete(0, END)

def calc(oprn):
    global result, last_operation,history
    if result is None:
        result = f'{number_entry.get()}'
    else:
        result = eval(f'{result} {last_operation} {number_entry.get()}')
    last_operation = f'{operation_dict[oprn]}'
    history.append(number_entry.get())
    number_entry.delete(0, END)
    numbers.clear()

def show_result():
    global result, last_operation, history, last_number, number

    if result is not None:
        last_number = number_entry.get()
        numbers.append(number_entry.get())
        result = eval(f'{result} {last_operation} {last_number}')
        number_entry.delete(0, END)
        number_entry.insert(0,result)
        numbers.append(result)
        history.append(f'{last_operation}{last_number}')
        result = None
    else:
        result = eval(f'{numbers[-1]} {last_operation} {numbers[0]}')
        numbers.append(result)
        number_entry.delete(0, END)
        number_entry.insert(0, result)
        history.append(f'{last_operation}{numbers[0]}')
        result = None

def input_negative(sign):
    number_entry.insert(END,sign)

def insert_number(num):
    number_entry.insert(END, num)

def show_history():
    global history
    for i in history:
        print(i)

def backspace():
    current_text = number_entry.get()
    number_entry.delete(0, END)
    number_entry.insert(0, current_text[:-1])

window = Tk()
window.title('Calculator')
window.config(background='black',padx=20,pady=20)

title_label = Label(text = 'MY FIRST CALCULATOR',fg='white',font=FONT,background='black')
title_label.grid(row=0,column = 0,columnspan=5)

validate_cmd = window.register(validate_digit)

number_entry = Entry(width=15,background='#2F4F4F',fg='black',font=FONT_FOR_NUMBERS,validatecommand=(validate_cmd,'%P'),validate='key',borderwidth=5)
number_entry.grid(row = 1,column = 0,columnspan = 5,pady=20,sticky='N')

plus_button = Button(text='+',background='black',font=('xenera',20,'bold'),fg='white',width=2,height=1,highlightcolor='white',command = lambda: calc('+') if number_entry.get() else None,borderwidth=5)
plus_button.grid(row=2,column=0,pady=2)

minus_button = Button(text='-',background='black',font=('xenera',20,'bold'),fg='white',width=2,height=1,highlightcolor='white',command = lambda : calc('-') if number_entry.get() else input_negative('-'),borderwidth=5)
minus_button.grid(row=2,column=1)

into_button = Button(text='X',background='black',font=('xenera',20,'bold'),fg='white',width=2,height=1,highlightcolor='white',command = lambda: calc('X') if number_entry.get() else None,borderwidth=5)
into_button.grid(row=2,column=2)

divide_button = Button(text='÷',background='black',font=('xenera',20,'bold'),fg='white',width=2,height=1,highlightcolor='white',command = lambda: calc('÷') if number_entry.get() else None,borderwidth=5)
divide_button.grid(row=2,column=3)

equal_to_button = Button(text='=',background='black',font=('xenera',20,'bold'),fg='white',width=3,height=1,highlightcolor='white',command = lambda : show_result(),borderwidth=5)
equal_to_button.grid(row=2,column=4,sticky='E')

clear_button = Button(text='C', background='black', font=('xenera', 20, 'bold'),
                      fg='white', width=2, height=1, command=clear,borderwidth=5)
clear_button.grid(row=4, column=4,sticky = 'E',pady = 4)

for i in range(1, 10):
    Button(window, text=str(i), background='black', font=('xenera', 20, 'bold'),
           fg='white', width=2, height=1, command=lambda x=i : insert_number(x),borderwidth=5).grid(row=(i-1)//3 + 3, column=(i-1) % 3,pady=3)

Button(window, text='0', background='black', font=('xenera', 20, 'bold'),
       fg='white', width=2, height=1, command=lambda: insert_number(0),borderwidth=5).grid(row=3, column=3,sticky='W')

history_button = Button(text='H', background='black', font=('xenera', 20, 'bold'),
                      fg='white', width=2, height=1,command = show_history,borderwidth=5)
history_button.grid(row=5, column=4,sticky = 'E')

backspace_button = Button(text = '⌫',background='black', font=('xenera', 20, 'bold'),
                      fg='white', width=2, height=1,command = backspace,borderwidth=5)
backspace_button.grid(row = 3,column = 4,sticky='E')

window.mainloop()