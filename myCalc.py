from tkinter import *

interim_results= []
exp_count = 0


root = Tk()


def numButton(number: str, row: int, col: int):
    """Creates a number button, places it to the right place and adds a callback upon pressing the button"""
    Button(root,
                  text=number,
                  width=10,
                  height=5,
                  command= lambda: fireNumber(number)).grid(row=row, column=col, rowspan=2, columnspan=2)


def fireNumber(number):
    """Callback for adding numbers to a StringVar which feeds the EntryWidget at the bottom"""
    global exp_count
    temp = v.get()
    v.set(temp + number)
    exp_count += 1


def calc(operator: str):
    """Callback which is used by the math operators to feed interim_results list,
    clear the EntryWidged at the bottom and add to the Text Widget to the right"""
    global exp_count
    interim_results.append(v.get()+operator)
    v.set("")
    history.configure(state=NORMAL)
    history.insert(float(len(interim_results)), interim_results[-1])
    history.configure(state=DISABLED)
    exp_count += 1


def evaluate():
    """Callback to calculate the current equation and write the result into the Text Widget"""
    global exp_count
    if exp_count >= 1:
        expression = ""
        for i in interim_results:
            expression = expression + i
        expression = expression + v.get()
        #print(f"InterimRes: {interim_results}")
        #print(f"Exp: {expression} - ExpCount: {exp_count}")
        result = eval(expression[-exp_count:])
        history.configure(state=NORMAL)
        history.insert(str(len(interim_results))+".end", v.get())
        history.insert(str(len(interim_results)) + ".end", f"={result}\n")
        history.configure(state=DISABLED)
        interim_results.append(v.get()+"="+str(result) + ";")
    v.set("")
    exp_count = 0


# Generate Widgets
numButton("1", 0, 0)
numButton("2", 0, 2)
numButton("3", 0, 4)
numButton("4", 2, 0)
numButton("5", 2, 2)
numButton("6", 2, 4)
numButton("7", 4, 0)
numButton("8", 4, 2)
numButton("9", 4, 4)
numButton("0", 6, 0)

Button(root, text="+", command=lambda: calc("+"), width=4, height=2).grid(row=6, column=2)
Button(root, text="-", command=lambda: calc("-"), width=4, height=2).grid(row=6, column=3)
Button(root, text="*", command=lambda: calc("*"), width=4, height=2).grid(row=7, column=2)
Button(root, text="/", command=lambda: calc("/"), width=4, height=2).grid(row=7, column=3)
Button(root, text="=", command=evaluate, width=10, height=5).grid(row=6, column=4, columnspan=2, rowspan=2)


v = StringVar()
entry = Entry(root, width=34, textvariable=v, state="readonly", fg="black").grid(row=8, column=0, columnspan=6)


history = Text(root, width=30, height=15, state=DISABLED)
history.grid(row=0, column=7, rowspan=6)


root.mainloop()