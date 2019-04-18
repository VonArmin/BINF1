# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 24-01-2019
# opdracht: Thematoets Informatica Blok 2
# klas    : BIN-1B
import re
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from PIL import ImageTk, Image


def main():
    file_name = 'ploop.fa'
    file = open_file(file_name)
    if file:
        try:
            name_list, seq_list = list_creator(file)
            homo_match_pat = pattern_finder(name_list, seq_list)
            matchdict, organism_matchlist = pattern_matcher(homo_match_pat, seq_list, name_list)
            MyGui(matchdict, organism_matchlist)
        except TypeError:
            print('type error, type may be None')
        except IOError:
            print('general IO error')


def open_file(file):
    """opens the file and reads from line 6 till the end
    :param file: name of the file
    :return: file
    """
    try:
        file = open(file).readlines()[6:]
        return file
    except FileNotFoundError:
        print('file not found')
        return False


def list_creator(file):
    """iterates over the file and creates lists of the names and sequences in the file.
    iterates over file to strip unnecessary characters
    :param file: opened file from def open_file
    :return: list of names, list of sequences
    """
    file_length = 0
    seq_list = []
    name_list = []
    line_temp = ''
    name_filter1 = r'\[.*\]'
    name_filter2 = '[A-Z]{1}[a-z]* [a-z]*'
    for line in file:
        file_length += 1
        line = line.strip('\n')
        if not line.startswith('>'):
            name_match1 = re.search(name_filter1, line)
            if name_match1:
                name_list.append(name_match1.group())
            if line.isupper():
                line_temp += line
        if line.startswith('>'):
            seq_list.append(line_temp)
            line_temp = ''
        if file_length == len(file):
            seq_list.append(line_temp)
    for line in range(len(name_list)):
        name_match2 = re.search(name_filter2, name_list[line])
        if name_match2:
            name_list[line] = name_match2.group()
    return name_list, seq_list
# file_length = length of the file so when it reaches the end it appends the last sequence.
# seq_list = list of each sequence.
# name_list = list of each name.
# line_temp = each sequence will be saved in this param before appending, where-after is gets emptied.
# name_filter1 = re filter used to find the general name of the organism.
# name_filter2 = re filter used to strip the name of unnecessary characters.


def pattern_finder(name_list, seq_list):
    """iterates over name list to find Homo sapiens in their name, appends its index# when True.
    iterates over Homo sapiens index list to find the p-loop pattern and appends them in a new list.
    :param name_list: list of all organism names
    :param seq_list: list of all sequences
    :return: homo_match_pat, list of p-loop patterns found in Homo sapiens
    """
    p_loop = '[AG].{4}GK[ST]'
    re_homo = 'Homo sapiens'
    name_list_entry = -1
    homo_match_nr = []
    homo_match_pat = []
    for name in name_list:
        name_list_entry += 1
        homo_match_re = re.search(re_homo, name)
        if homo_match_re:
            homo_match_nr.append(name_list_entry)
    for hmatch in homo_match_nr:
        seq_match = re.findall(p_loop, seq_list[hmatch])
        for smatch in seq_match:
            if smatch not in homo_match_pat:
                homo_match_pat.append(smatch)
    return homo_match_pat
# p-loop =  re filter to find p-loop pattern.
# re_homo = re filter to find homo sapiens in name_list.
# name_list_entry = used to find the index number of homo sapiens in name_list.
# homo_match_nr = used to store the index numbers of homo sapiens in name_list.
# homo_match_pat = used to store unique p-loop patterns found in seq_list.


def pattern_matcher(match_pat, seq_list, name_list):
    """iterates over all p-loop matches to find them in sequences in seq_list, adds them to a dictionary and match list.
    :param match_pat: list of unique p-loop patterns found in Homo sapiens
    :param seq_list: list of all sequences
    :param name_list: list of all organism names
    :return: dictionary with key=organism, value=amount of p-loops
    """
    matches = {}
    organism_matches = []
    for pattern in match_pat:
        seq_nr = -1
        for seq in seq_list:
            seq_nr += 1
            match = re.search(pattern, seq)
            if match:
                if name_list[seq_nr] not in organism_matches:
                    organism_matches.append(name_list[seq_nr])
                try:
                    matches[name_list[seq_nr]] += 1
                except KeyError:
                    matches[name_list[seq_nr]] = 1
    return matches, organism_matches
# matches = dictionary of names and number of matches, key = organism name, value = matches.
# organism_matches = list of organisms containing p-loop patterns.


class MyGui:
    def __init__(self, matchdict, organisms):
        """init function to set up general GUI, both lists are made class-wide
        :param matchdict: dictionary of organisms, matches
        :param organisms: list of organisms
        """
        self.matchdict = matchdict
        self.organisms = organisms
        self.mpl_info = []

        self.main_window = Tk()
        self.main_window.title('SACPF')

        self.top_frame = Frame(self.main_window)
        self.top_frame.pack(side='top')
        self.checkbox_frame = Frame(self.main_window)
        self.checkbox_frame.pack()
        self.image_frame = Frame(self.main_window)
        self.button_frame = Frame(self.main_window)
        self.button_frame.pack()

        self.label = Label(self.top_frame, text='Select organisms to compare')
        self.label.pack(side='top')

        self.confirm_button = Button(self.button_frame, text='Confirm', command=self.matplotlib_info)
        self.confirm_button.pack(side='left')

        self.exit_button = Button(self.button_frame, text='Exit', command=self.main_window.destroy)
        self.exit_button.pack(side='right')

        self.checkboxes()
        mainloop()
    # main window consists of 4 frames, top_frame, checkboxes, buttons and image
    # image frame gets destroyed in matplotlib_show and created again to display only 1 matplotlib graph

    def checkboxes(self):
        """iterates over organism list, creates list of each organism with IntVar boolean. places them in a grid
        using .grid(). mpl=matplotlib
        :return: mpl_info, a list of checked boxes in IntVar booleans
        """
        row = 0
        column = 0
        for x in range(len(self.organisms)):
            self.mpl_info.append('')
            self.mpl_info[x] = IntVar()
            self.mpl_info[x].set(0)
            Checkbutton(self.checkbox_frame, text=self.organisms[x], variable=self.mpl_info[x]).grid(row=row,
                                                                                                     column=column,
                                                                                                     sticky='w')
            if column == 4:
                column = 0
                row += 1
            else:
                column += 1
    # mpl_info is used to store checked boxes, this data is accessed in matplotlib_info to make a clean list of
    # the checked organisms and their values

    def matplotlib_info(self):
        """called from confirm button.
        iterates over match dictionary and appends the organism to a new list(mpl_list_names)
        when True (returned from IntVar)
        iterates over match dictionary keys, compares it mpl_list names to to find their values and adds them to a list.
        generates a list of data used in matplotlib generation. uses mpl_info.get() to find wether
        True or False(checked or unchecked)
        :return: list of checked organisms and list of their values
        """
        mpl_list_names = []
        mpl_list_values = []
        for x in range(len(self.matchdict)):
            if self.mpl_info[x].get():
                mpl_list_names.append(self.organisms[x])
        for key in self.matchdict.keys():
            if key in mpl_list_names:
                mpl_list_values.append(self.matchdict.get(key))
        self.matplotlib_generate(mpl_list_names, mpl_list_values)
    # mpl_list_names = list with checked organism names
    # mpl_list_values = list with ckecked organism values
    # it is not necessary to create new lists, the dictionary can be used right away but for me its more clear what
    # happens at each step this way

    def matplotlib_generate(self, mpl_list_names, mpl_list_values):
        """generates matplotlib image using lists generated in matplotlib_info.
        iterates over values to put them at the end of each bar and make the values more clear
        :param mpl_list_names: list of checked names
        :param mpl_list_values: list of values of checked names
        :return: saves generated matplotlib file
        """
        y_pos = np.arange(len(mpl_list_names))
        plt.figure(figsize=(7.65, 5))
        plt.subplots_adjust(left=0.28)
        plt.barh(y_pos, mpl_list_values, align='center', alpha=1, color='blue')
        plt.yticks(y_pos, mpl_list_names, fontsize='small')
        for x in range(len(mpl_list_values)):
            plt.text(mpl_list_values[x]+0.01, x-0.08, mpl_list_values[x], fontsize='small')
        plt.xlabel('Amount Found')
        plt.ylabel('Organism')
        plt.title('P-loop patterns found')
        plt.savefig('organism diagram')
        self.matplotlib_show()

    def matplotlib_show(self):
        """opens matplotlib file using PIL's ImageTK and Image packages
        to make sure only 1 graph gets displayed each time this function is called it destroys, remakes and packs
        the image frame. this is also done with the image itself by pack_forget() and pack()
        :return: puts out image to GUI
        """
        filename = 'organism diagram.png'
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        self.image_frame.destroy()
        self.image_frame = Frame(self.main_window)
        image = Label(self.image_frame, image=img)
        self.image_frame.pack(side='bottom')
        image.pack_forget()
        image.pack(side='bottom', fill='both', expand='yes')
        image.image = img


main()
