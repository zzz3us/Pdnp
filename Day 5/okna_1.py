import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label_text = tkinter.Label(self.main_window, text='Hello, World!')

        self.label_text.pack(side='top')

        tkinter.mainloop()

my_gui = MyGui()