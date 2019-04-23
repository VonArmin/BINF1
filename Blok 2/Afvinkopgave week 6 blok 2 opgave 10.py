# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 20-01-2019
# opdracht: afvinkopdracht 6 blok 2 opgave 10
# klas    : BIN-1B

import tkinter

class MyGUI:

    def __init__(self):
        """opent een venster en tekent een ster met een naam er in
         """
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x500')
        self.main_window.title('exercise 10')

        self.canvas = tkinter.Canvas(self.main_window, width=600, height=600)

        self.canvas.create_line(250, 0, 310, 200, 500, 200, 350, 310, 400, 500, 250, 380, 100, 500, 150, 310, 0, 200,
                                190, 200, 250, 0)

        self.canvas.create_text(250, 250, font='Helvetica', text='Armin van Eldik')

        self.canvas.pack()

        tkinter.mainloop()

my_gui = MyGUI()