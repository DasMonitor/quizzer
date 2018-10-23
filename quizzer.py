from tkinter import *
#from multiprocessing import Process
import qbank
import ast
import random
#import pyttsx3

#TODO: FIXME: This is hacked together... fix it.

class QuizGUI:
    #Initialize a new bank
    bank = qbank.Bank()

    #Define class level variables
    nextquestion = None
    choices = []

    #Initialize text-to-speech engine
#    engine = pyttsx3.init()

    def __init__(self, master):
        self.master = master
        master.title("Quizzer")
        self.nextq()
        #self.readq()


    def update_form(self):
        self.clear()
        self.nextq()

    def response_status(self, bgvar):
        self.frame = Frame(
            self.master,
            padx=30,
            width=550,
            height=30,
            bg=bgvar,
        )
        # self.frame_message = Message(
        #     self.master,
        #     padx=30,
        #     anchor=N,
        #     text='Question: '
        # )
        self.frame.grid(columnspan=2, sticky=N)
        #self.frame_message.grid(row=self.frame.grid_info()['row'])

    #TODO: This needs to be refactored, this function does too much.
    def nextq(self):
        #FIXME: Temporarily build the status bar
        self.response_status('blue')

        print("Pulling next question...")


        #Pop off next question
        self.nextquestion = self.bank.query.pop()

        #Print question data
        print(f"Question: {self.nextquestion.query}\n",
            f"Answer: {self.nextquestion.answer}\n",
            f"Choices: {ast.literal_eval(self.nextquestion.choices)}\n")

        #Adding multiple frames in grid
        self.label_text = StringVar()
        self.label_text.set(self.nextquestion.query)
        self.label = Message(
            self.master,
            anchor=W,
            padx=30,
            width=550,
            textvariable=self.label_text
        )
        self.label.grid(columnspan=2, sticky=W)

        #Function to Generates choices
        self.gen_choices()

        self.next_button = Button(
            self.master,
            text="Next",
            command=self.update_form
        )
        self.next_button.grid()
        #self.next_button.bind('<Return>', self.nextq())

        self.close_button = Button(
            self.master,
            text="Close",
            command=self.master.quit
        )
        self.close_button.grid(
            row=self.next_button.grid_info()['row'],
            column=1
        )



    def gen_choices(self):
        #Setup the multiple choice answers and shuffle them.
        self.choices = ast.literal_eval(self.nextquestion.choices)
        random.shuffle(self.choices)

        #Iterate over the choices
        #global answerList
        #answerList = dict()

        #This is required to check which boxes are ticked
        global enabled
        enabled = dict()


        count = 0
        self.vars=[]
        for n in range(len(self.choices)):
            var = IntVar()
            #var = Variable()
            self.vars.append(var)

        for choice in self.choices:
            choicetext = str(count + 1) + ": " + choice
            #answerList[count] = choicetext
            enabled[count] = Variable()
            enabled[count] = choice
            self.label_index = count
            self.label_choice = StringVar()
            self.label_choice.set(choicetext)
            #self.checkbox[count] = Checkbutton(
            self.label = Checkbutton(
                self.master,
                padx=30,
                variable=self.vars[count],
                command=self.check_selection,
                textvariable=self.label_choice
                )
            #self.checkbox[count].grid(columnspan=2, sticky=W)
            self.label.grid(columnspan=2, sticky=W)
            #print(self.label.variable)
            count = count + 1



    #Destroy every object on our form before rebuilding new question
    def clear(self):
        list = root.grid_slaves()
        for l in list:
            l.destroy()

    def check_selection(self):
        #Create a list to contain the user's selected answers
        answer_selection = []

        correct_answers = []
        correct_answers = ast.literal_eval(self.nextquestion.answer)

        #global dictionary "enabled" for question choices
        for i in range(len(enabled)):
            #If the checkbox is selected, add to answer_selection list
            if self.vars[i].get() == 1:
                answer_selection.append(self.choices[i])

        #Sort the correct & user's answers so we can compare for correctness
        correct_answers.sort()
        answer_selection.sort()

        print(f"Correct Answers: {correct_answers}\nSelected Answers: {answer_selection}")
        if correct_answers == list(answer_selection):
            print("Correct!")
            self.frame['bg'] = 'green'

        else:
            print("Incorrect!")
            self.frame['bg'] = 'red'


#    def readq():
        #FIXME: This reads and prevents the windwo from rendering
        #Test reading the question
#        my_gui.engine.say(my_gui.nextquestion.query)
#        my_gui.engine.say("Is it?")
#        for choice in ast.literal_eval(my_gui.nextquestion.choices):
#            my_gui.engine.say(choice, "?")
#        my_gui.engine.setProperty('rate',100)  #100 words per minute
#        my_gui.engine.setProperty('volume',0.9)
#        #self.engine.setProperty('gender', 'female')
#        my_gui.engine.runAndWait()

root = Tk()
my_gui = QuizGUI(root)

root.mainloop()
