from tkinter import *
from tkinter import messagebox

def ac(output=None):
    output.delete(1.0,END)

def del_(output=None):
    # Find the index of the start of the last line
    last_line_start_index = output.index("end-1c linestart")
    # Find the index of the end of the last line, which includes the newline character
    last_line_end_index = output.index("end-1c lineend +1c")
    # Delete from the start of the last line to the end of the last line, including the newline
    output.delete(last_line_start_index, last_line_end_index)

def move_cursor_up(event=None, output=None):
    output.mark_set("insert", "insert-1l")

def move_cursor_down(event=None, output=None):
    output.mark_set("insert", "insert+1l")

def normie(output=None, ans=None):
    
    expression = output.get(1.0,END).strip()
    try:
        ans = eval(expression, {"__builtins__": None}, {})
    except ZeroDivisionError as e:
        ans = e
        output.insert(END, "Arithmetic Error")
        messagebox.showerror(title="Arithmetic Error", message="Cannot Divide by Zero")
    except Exception as e:
        ans = e
        print(e); output.insert(END, "Syntax Error")
        messagebox.showerror(title="Syntax Error", message="Try deleting the previous answer. Press DEL")
    else:
        if expression == "399":
            output.insert(END, "https://youtu.be/xvFZjo5PgG0?si=3u4hOB0F0fCENz9o")
        else:
            output.insert(END, str(ans))
    ans = 0
