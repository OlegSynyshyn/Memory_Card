from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from data import Question, QuestionView
from random import shuffle

app = QApplication([])

from main_window import *

qst1 = Question("Скільки років було Садовому Назарію коли розпочалась 2 битва за Харків від атаки ГІТЛЕРА в 1942", "правильна відповідь", 
                "не правильна", "теж не правильна", "і ця не правильна")

radio_list=[btn1, btn2, btn3, btn4]
shuffle(radio_list)

from_card = QuestionView(qst1, question,
                        radio_list[0],
                        radio_list[1],
                        radio_list[2],
                        radio_list[3])
          
from_card.show                     
win_card.show()
app.exec_()