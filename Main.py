from basic import *
from psudorandom import *

def main():
    global result
    result = 0

    screen = Tk()

    screen.geometry("800x800")
    screen.title("Calculator")
    screen.configure(bg="beige")

    # Calculator framework
    cal_frame = Frame(screen, 
                      bg="silver", 
                      width=700, 
                      height=750)
    cal_frame.place(x=50, y=25)

    # Screen of calculator
    display_box = Text(cal_frame, 
                       bg="white",
                       fg="black",
                       highlightcolor="black",
                       font=("Arial", 24),
                       borderwidth=10,
                       relief=SUNKEN,
                       wrap=NONE)
    display_box.place(x=10, y=10, width=680, height=300)

    # Draws Clear Button
    clear = Button(cal_frame,
                   text="AC",
                   activebackground="black", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="lightgray",
                   cursor="hand",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   justify=CENTER,
                   overrelief=RIDGE,
                   command=lambda:ac(display_box))
    clear.place(x=300, y=400, width=70, height=30)

    # Draws Delete button
    delete = Button(cal_frame,
                    text="DEC",
                    activebackground="black", 
                    activeforeground="white",
                    anchor="center",
                    bd=2,
                    bg="lightgray",
                    cursor="hand",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    justify=CENTER,
                    overrelief=RIDGE,
                    command=lambda:del_(display_box))
    delete.place(x=380, y=400, width=70, height=30)

    # Draws Random# Button
    ran = Button(cal_frame,
                 text="Ran#",
                 activebackground="black",
                 activeforeground="white",
                 anchor="center",
                 bd=2,
                 bg="lightgray",
                 cursor="hand",
                 fg="black",
                 font=("Arial", 12),
                 height=2,
                 justify=CENTER,
                 overrelief=RIDGE,
                 command=lambda:display_box.insert(END, random.uniform(0, 1)))
    ran.place(x=220, y=400, width=70, height=30)

    # Draws RandInt Button
    rand_int_button = Button(cal_frame,
                             text="RandInt",
                             activebackground="black",
                             activeforeground="white",
                             anchor="center",
                             bd=2,
                             bg="lightgray",
                             cursor="hand",
                             fg="black",
                             font=("Arial", 12),
                             height=2,
                             justify=CENTER,
                             overrelief=RIDGE,
                             command=lambda:randomint(display_box))
    rand_int_button.place(x=140, y=400, width=70, height=30)

    # Bind Enter key to the calculation function
    def basic_cal(event=None):
        normie(display_box)
    screen.bind("<Return>", basic_cal)

    # Bind arrow keys to cursor navigation functions
    screen.bind("<Up>", lambda event: move_cursor_up(event, display_box))
    screen.bind("<Down>", lambda event: move_cursor_down(event, display_box))

    screen.mainloop()

main()
