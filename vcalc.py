import tkinter as tk

value = '0'
expr = ''

def add_digit(s):
    global value
    if value == '0':
        value = s
    else:
        value += s
    show_res()


def add_sign(s):
    global expr, value
    signs = {'+', '-', '*', '/'}
    if len(expr) == 0:
        expr = value+s
    elif expr[-1] in signs or len(expr) == 0:
        expr = expr[:-1]
        expr = expr + s
    else:
        expr = expr + value + s
    label_expr['text'] = expr


def show_res():
    global value
    label_res['text'] = value


calc = tk.Tk()
calc.title('Калкулатор')
calc.geometry('240x360+200+100')
calc.resizable(False, False)

calc.grid_columnconfigure(0, minsize=60)
calc.grid_columnconfigure(1, minsize=60)
calc.grid_columnconfigure(2, minsize=60)
calc.grid_columnconfigure(3, minsize=60)

calc.grid_rowconfigure(0, minsize=60)
calc.grid_rowconfigure(1, minsize=60)
calc.grid_rowconfigure(2, minsize=60)
calc.grid_rowconfigure(3, minsize=60)
calc.grid_rowconfigure(4, minsize=60)
calc.grid_rowconfigure(5, minsize=60)

label_res = tk.Label(calc, text='0')
label_res.configure(anchor='e',
                 bd=2,
                 padx=10,
                 font=('Arial', 30, 'bold'))
label_res.grid(row=0, column=0, columnspan=4, sticky='ew',)

label_expr = tk.Label(calc, text='')
label_expr.configure(anchor='e',
                 bd=2,
                 padx=10)
label_expr.grid(row=1, column=0, columnspan=4, sticky='ew',)

btn_1 = tk.Button(calc, text='1', command=lambda: add_digit('1')).grid(row=2, column=0, sticky='ewns')
btn_2 = tk.Button(calc, text='2', command=lambda: add_digit('2')).grid(row=2, column=1, sticky='ewns')
btn_3 = tk.Button(calc, text='3', command=lambda: add_digit('3')).grid(row=2, column=2, sticky='ewns')
btn_4 = tk.Button(calc, text='4', command=lambda: add_digit('4')).grid(row=3, column=0, sticky='ewns')
btn_5 = tk.Button(calc, text='5', command=lambda: add_digit('5')).grid(row=3, column=1, sticky='ewns')
btn_6 = tk.Button(calc, text='6', command=lambda: add_digit('6')).grid(row=3, column=2, sticky='ewns')
btn_7 = tk.Button(calc, text='7').grid(row=4, column=0, sticky='ewns')
btn_8 = tk.Button(calc, text='8').grid(row=4, column=1, sticky='ewns')
btn_9 = tk.Button(calc, text='9').grid(row=4, column=2, sticky='ewns')
btn_0 = tk.Button(calc, text='0',).grid(row=5, column=0, sticky='ewns', columnspan=2)
btn_add = tk.Button(calc, text='+', command=lambda: add_sign('+')).grid(row=5, column=3, sticky='ewns')
btn_sub = tk.Button(calc, text='-', command=lambda: add_sign('-')).grid(row=4, column=3, sticky='ewns')
btn_mult = tk.Button(calc, text='*', command=lambda: add_sign('*')).grid(row=3, column=3, sticky='ewns')
btn_div = tk.Button(calc, text='/', command=lambda: add_sign('/')).grid(row=2, column=3, sticky='ewns')
btn_ok = tk.Button(calc, text='=').grid(row=5, column=2, sticky='ewns')


calc.mainloop()
