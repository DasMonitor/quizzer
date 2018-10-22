#!/usr/bin/python3

#This is the dbwriter function ripped from the original script to be called as a function versus
# additional code in the original script.
#TODO: FIXME: read config from file instead of having it all up in this script.

from datetime import date, datetime, timedelta
import mysql.connector

config = {
        'user': 'quizzer',
        'password': 'Quizdb$3@1',
        'host': 'butane',
        'database': 'questions',
        'port': '3306',
        }


def write_questions_2db(cnx=None):

    today = datetime.now().date()

    #Let's build our lists containing questions and answers.
    with open("docs/questions.txt", "r") as fo:
        questions = []
        for line in fo.read().split('\n'): # just for line in file if you're reading from a file
            if line:
                questions.append(line)
            else: # Empty line: stop looking, next line
                next

    with open("docs/choices.txt", "r") as fo:
        choices = []
        for line in fo.read().split('\n'): # just for line in file if you're reading from a file
            if line:
                choices.append(line)
            else: # Empty line: stop looking, next line
                next

    with open("docs/answers.txt", "r") as fo:
        answers = []
        for line in fo.read().split('\n'): # just for line in file if you're reading from a file
            if line:
                answers.append(line)
            else: # Empty line: stop looking, next line
                next
    count = 0
    for query in questions:
        qdata = {
                'question': str(questions[count]),
                'choices': str(choices[count]),
                'answers': str(answers[count]),
                'num_right': 0,
                'num_wrong': 0,
                }
        add_data_2db = ("INSERT INTO biochem "
                        "(question, choices, answers, num_right, num_wrong) "
                        "VALUES (%(question)s, %(choices)s, %(answers)s, %(num_right)s, %(num_wrong)s)"
                        )
        if cnx == None:
            cnx = mysql.connector.connect(**config) #kwargs for config above
        cursor = cnx.cursor()
        cursor.execute(add_data_2db, qdata)
        count = count + 1

    cnx.commit()
    cursor.close()
    cnx.close()


def category_initializer():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        init_db = ("TRUNCATE TABLE `walmart_categories`;")
        cursor.execute(init_db)
        cnx.commit()
    except:
        print("Something went wrong truncating category table.")
    cursor.close()
    cnx.close()



if __name__ == '__main__':
    write_questions_2db()
