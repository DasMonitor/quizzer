import mysql.connector
import configparser
import random

config = configparser.ConfigParser()
config.read('/home/analog/quizzer.config')


class Question:
    '''
    Question class is an object that contains data for each question
    '''
    def __init__(self,query,choices,answer):
        self.query = query
        self.choices = choices
        self.answer = answer

    def __str__(self):
        #In the future, let's return a printout of the question

        return(
            print(f"Question:\t{self.query}"),
            #{for choice in choices print(f"{choices.index(choice)}: {choice}")},
            print(f"Answer:\t{self.answer}"),
        )
        #return f"Question:\t{self.query}\nChoices:\t{self.choices}\nAnswer:\t{self.answer}"


class Bank(Question):
    '''
    Bank class is an object that inherits the Question class to hold each
    deck of questions
    The Bank can be initialized with bank = Bank()
    '''
    cnx = mysql.connector.connect(
            host=config['mysqlDB']['host'],
            user=config['mysqlDB']['user'],
            password=config['mysqlDB']['pass'],
            database=config['mysqlDB']['db'],
            port=config['mysqlDB']['port'],
            )
    cursor = cnx.cursor()

    dbquery = ("select question, choices, answers from biochem")
    cursor.execute(dbquery)

    questionDict = {}
    random.shuffle(questionDict)
    count = int(0)
    for (question, choices, answers) in cursor:
        questionDict[count] = {
            'question': question,
            'choices': choices,
            'answers': answers,
        }
        count = count + 1


    #print(questionDict)
    #print(len(questionDict))



    def __init__(self):
        #pass
        self.query = []
        #Create Question objects for each of our questions in db
        for index in range(len(self.questionDict)):
            self.query.append(Question(
                                self.questionDict[index]['question'],
                                self.questionDict[index]['choices'],
                                self.questionDict[index]['answers']
                                )
                            )
        random.shuffle(self.query)

    def __str__(self):
        #For any number of Questions in the list of self.query; print all Questions leveraging the Question class
        #for questions in self.query:
        #    print(questions)
        pass
        #return f"{self.question[0]}"



#### Test question building
    #question will be read in from database perhaps in a for loop or select a certain number
    # question='''    A 24-year-old is brought in by ambulance.
    # She is unresponsive with a respiratory rate of 4/minute, pulse 90/minute.
    # An empty bottle of morphine is found lying nearby by the EMT.
    # Given the data below, what diagnosis is most appropriate for this patient?
    # (PaO2 = 68 mm Hg; CO2 = 60 mm Hg; pH = 7.24; HCO3 = 25 mM)
    # To rule out additional problems in the patient, you also calculate
    # her A-a gradient to be 7. This means:'''
    # choices=(
    #     "She has a secondary respiratory problem.",
    #     "She has a chronic problem.",
    #     "She has anemia.",
    #     "She has a delta gap.",
    #     "She has no underlying gas exchange problem in her lungs.",
    #     )
    # answer=("She has no underlying gas exchange problem in her lungs.")
