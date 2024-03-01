#
# Simple tkinter example
#
import tkinter

def create_window() -> None:
    window = tkinter.Tk()
    window.title("ICS32 Example GUI")
    message = tkinter.Label(master=window, text="This is an example label.")
    button = tkinter.Button(master=window, text="Press me",
                            command=run_method)
    
    message.pack()
    button.pack()
    window.mainloop()
    

def run_method() -> None:
    print("This method was executed after you clicked on the button!")
    
if __name__ == '__main__':
    create_window()