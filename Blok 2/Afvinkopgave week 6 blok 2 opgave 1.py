# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 20-01-2019
# opdracht: afvinkopdracht 6 blok 2 opgave 1
# klas    : BIN-1B

import tkinter

class MyGUI:

    def __init__(self):
        """opent een venster en laat geen data zien tot je op show info drukt
        """
        self.main_window = tkinter.Tk()
        self.main_window.geometry('200x100')
        self.main_window.title('exercise 1')

        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame(self.main_window)
        self.button1 = tkinter.Button(self.bottom_frame, text='Show Info', command=self.showstuff)
        self.button1.pack(side='left')
        self.button2 = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.bottom_frame.pack(side='bottom')
        self.button2.pack(side='right')
        tkinter.mainloop()

    def showstuff(self):
        self.label = tkinter.Label(self.top_frame, text='Armin van Eldik\nKalkestraat 34\n6669 CP, Dodewaard')
        self.label.pack()
        self.top_frame.pack(side='top')

my_gui = MyGUI()