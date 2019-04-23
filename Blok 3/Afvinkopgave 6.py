# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 21-03-2019
# opdracht: afvinkopgave 6
# klas    : BIN-1A
# functie : interface voor de piep database, waarmee pieps gepost, gezien en gefilterd kunnen worden
from tkinter import *
import mysql.connector


class PiepGui:
    def __init__(self):

        # sql connection
        self.connection = mysql.connector.connect(host='hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com',
                                                  user='ounhs@hannl-hlo-bioinformatica-mysqlsrv',
                                                  db='ounhs',
                                                  password='LM6lx70EFxVb')

        # main window
        self.main_window = Tk()
        self.main_window.title('PiepApp')

        # frames
        self.top_frame = Frame(self.main_window)
        self.top_frame.pack(side='top')
        self.middle_frame = Frame(self.main_window)
        self.middle_frame.pack()
        self.bottom_frame = Frame(self.main_window)
        self.bottom_frame.pack(side='bottom')

        # labels
        self.label_piep = Label(self.top_frame, text='bericht')
        self.label_piep.pack(side='left')
        self.label_filter = Label(self.middle_frame, text='filter')
        self.label_filter.pack(side='left')

        # input fields
        self.piep_input = Entry(self.top_frame, width='60')
        self.piep_input.pack(side='left')
        self.filter_input = Entry(self.middle_frame, width='60')
        self.filter_input.pack(side='left')

        # buttons
        self.post_button = Button(self.top_frame, text='Post piep', command=self.post_piep)
        self.post_button.pack(side='right')
        self.filter_button = Button(self.middle_frame, text='Vind', command=self.filter_pieps)
        self.filter_button.pack(side='left')
        self.refresh_button = Button(self.bottom_frame, text='Ververs', command=self.get_pieps)
        self.refresh_button.pack(side='bottom')

        # output field
        self.scrollbar = Scrollbar(self.bottom_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.piep_output_field = Text(self.bottom_frame, height=40, width=70,
                                      bg="white",
                                      yscrollcommand=self.scrollbar.set)
        self.piep_output_field.pack()
        self.scrollbar.config(command=self.piep_output_field.yview)

        self.get_pieps()
        mainloop()

    def post_piep(self):
        cursor = self.connection.cursor()
        if self.piep_input.get():
            cursor.execute(
                "insert into piep (bericht, datum, tijd, student_nr)"
                "values ('{}', curdate(), curtime(), 618604) ;".format(self.piep_input.get())
            )
        cursor.close()
        self.connection.commit()
        self.get_pieps()

    def get_pieps(self):
        self.piep_output_field.delete(1.0, END)
        cursor = self.connection.cursor()
        cursor.execute(
            "select p.bericht, s.voornaam, p.datum, p.tijd "
            "from piep p natural join student s order by datum desc, tijd desc"
        )
        rows = cursor.fetchall()
        for line in rows:
            self.insert_lines(line)
        cursor.close()

    def filter_pieps(self):
        self.piep_output_field.delete(1.0, END)
        cursor = self.connection.cursor()
        if self.filter_input.get():
            cursor.execute(
                "select p.bericht, s.voornaam, p.datum, p.tijd from piep p natural join student s"
                " where bericht regexp '{}'".format(self.filter_input.get())
            )
            rows = cursor.fetchall()
            for line in rows:
                self.insert_lines(line)
            cursor.close()
        else:
            self.piep_output_field.insert(END, 'Je moet wel iets invoeren!')
        self.connection.commit()

    def insert_lines(self, line):
        self.piep_output_field.insert(END, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                                           '\nbericht : {}'
                                           '\ngeplaatst door : {}, op : {}, om : {}\n'
                                           .format(line[0], line[1], line[2], line[3]))


piep_app = PiepGui()
