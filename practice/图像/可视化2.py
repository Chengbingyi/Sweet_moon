import tkinter as tk

class MyGUI:

    def __init__(self):
        # create the main window widget
        self.main_window = tk.Tk()
        self.my_button = tk.Button(self.main_window,
                                       text='Click Me!',
                                       command=self.do_something)
        self.label1 = tk.Label(self.main_window,
                                  text='Hello World!')
        self.label2 = tk.Label(self.main_window,
                                   text='This is my GUI program.')
        self.my_button.pack()

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        tk.mainloop()

    def do_something(self):
        tk.Messagebox.showinfo('Response',
                               'Thanks for clicking the button.')



my_gui = MyGUI()

