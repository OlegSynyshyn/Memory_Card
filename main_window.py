from PyQt5.QtWidgets import  (
    QApplication,
    QWidget,
    QGroupBox, 
    QLabel, 
    QRadioButton, 
    QSpinBox, 
    QHBoxLayout,
    QPushButton, 
    QVBoxLayout, 
    QLayout, 
    QButtonGroup
    )
from PyQt5.QtCore import Qt

card_width, card_height = 600, 500
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_box.setValue(50)
time_1b = QLabel("хвилин")

line1=QHBoxLayout()
line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(rest_btn)
line1.addWidget(time_box)
line1.addWidget(time_1b)

btn1 = QRadioButton("1")
btn2 = QRadioButton("2")
btn3 = QRadioButton("3")
btn4 = QRadioButton("4")

radioGrouBox = QGroupBox("Варіанти відповідей:")
radioGroup = QButtonGroup()

radioGroup.addButton(btn1)
radioGroup.addButton(btn2)
radioGroup.addButton(btn3)
radioGroup.addButton(btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

layout_ans1.addWidget(btn1)
layout_ans1.addWidget(btn2)

layout_ans2.addWidget(btn3)
layout_ans2.addWidget(btn4)

layout_ans_main = QVBoxLayout()

ansGroupBox = QGroupBox("Результат:")
ld_result = QLabel("Правильно")
ld_correct = QLabel("Правильна відповідь тут")

layout_result = QVBoxLayout()
layout_result.addWidget(ld_result, alignment=Qt.AlignTop)
layout_result.addWidget(ld_correct, alignment=Qt.AlignHCenter, stretch=2)
ansGroupBox.setLayout(layout_result)
ansGroupBox.hide()

layout_ans_main.addLayout(layout_ans1)
layout_ans_main.addLayout(layout_ans2)
radioGrouBox.setLayout(layout_ans_main)

question = QLabel("питання тут?")

checkBtn = QPushButton("Перевірити")


main_line = QVBoxLayout()
main_line.addLayout(line1, stretch=1)

main_line.addWidget(question, stretch=1, alignment= Qt.AlignHCenter)

main_line.addWidget(radioGrouBox, stretch=3)
main_line.addWidget(ansGroupBox, stretch=3)
main_line.addStretch(1)
main_line.addWidget(checkBtn, stretch=1)

win_card.setLayout(main_line)


def show_results():
    radioGrouBox.hide()
    ansGroupBox.show()

    checkBtn.setText("Наступне питання")


def show_question():
    radioGrouBox.show()
    ansGroupBox.hide()
    checkBtn.setText("Перевірити")
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)