#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:27:19 2022

@author: vasigo
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:38:25 2022

@author: vasigo
"""

import random

class Quiz:
    def __init__(self, question, correct, wrong):
        self.question = question
        self.correct = correct
        self.wrong = wrong


questions_count_per_quiz = 5
quiz_questions = [Quiz("Capital of the state Maryland:", "Annapolis", ["Dover", "Richmond", "Washington"]),
                  Quiz("'After me, the flood' said king:", "Louis XV", ["Louis XVI", "Louis XIII", "Louis XVIII"]),
                  Quiz("What programme is used for automatic load testing of websites", "Apache",
                       ["Selenium", "Kindle", "Op Test"]),
                  Quiz("To which group of Sioux belonged glorious sorcerer and chief Sitting Bull?", "Hunkpapa",
                       ["Minniconjou", "Sihasapa", "Oglala"]),
                  Quiz("The biggest mammal is:", "Blue whale", ["African elephant", "Giraffe", "White mouse"]),
                  Quiz("Birth place of Napoleon I Bonaparte is:", "Ajaccio", ["Marseille", "Paris", "Toulon"]),
                  Quiz("The first Napoleon's battle was:", "Siege of Toulon",
                       ["Battle of Poitiers", "Battle of Arcole bridge", "Battle of Zaragoza"]),
                  Quiz("The second FIFA World Cup was held in the year 1934 in:", "Italy",
                       ["France", "Spain", "Yugoslavia"]),
                  Quiz("Place of birth of the wheel is:", "Mesopotamia", ["Egypt", "China", "Phoenice"]),
                  Quiz("What was name of Ethiopian emperor Haile Selassie before he was crowned?", "Tafari Makonnen",
                       ["Abebe Bikila", "Kefle Jakob", "Sahle Mariam"]),
                  Quiz("The best Serbian movie in XX century is:", "Who's Singing Over There?",
                       ["The Marathon Family", "Pretty Village, Pretty Flame", "The Meeting Point"])]


def start_quiz():
    corrCount = 0


    random.shuffle(quiz_questions)
    question_count = min(questions_count_per_quiz, len(quiz_questions))
    q_questions = random.sample(quiz_questions, k=question_count)
    for quiz_question in q_questions:
        print(quiz_question.question)
        answer = quiz_question.wrong + [quiz_question.correct]
        random.shuffle(answer)
        count = 0
        while count < len(answer):
            print(str(count + 1) + ':' + answer[count])
            count += 1
        print("Type the number before the correct answer:")
        userAns = input()
        while not userAns.isdigit():
            print("You didn't typed a number. Repeat")
            userAns = input()
        userAns = int(userAns)
        while not (int(userAns) > 0 and int(userAns) <= len(answer)):
            print("No answer at this number. Do again.")
            userAns = input()
        userAns = int(userAns)
        if answer[userAns - 1] == quiz_question.correct:
            print("Correct!")
            corrCount += 1
        else:
            print("You're wrong.")
            print("")
        print("")

    random.choices(quiz_questions, k=5)

    if corrCount == len(q_questions):
        print("You have answered all questions correctly. Bravo!")
    elif corrCount == 0:
        print("You have missed all.")
    else:
        print("You have answered " + str(corrCount) + " out of " + str(len(q_questions)) + " questions correctly.")

start_quiz()