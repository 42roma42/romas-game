#создай приложение для запоминания информацииfrom PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout , QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle


app = QApplication([]) 
main_win = QWidget() 
v_line = QVBoxLayout()
app.correct_ans = 0
app.total_ans = 0
class QuestionCLass():
    def __init__(self, question_list, right_aans, wrong1, wrong2, wrong3 ):
        self.question_list = question_list
        self.right_aans = right_aans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#создание приложения и главного окна
main_win.resize(400,200)
main_win.setWindowTitle('название приложения')
#создание виджетов главного окна
RadioGroupBox = QGroupBox('Варианты ответов')

answer1 = QRadioButton('1')
answer2 = QRadioButton('2')
answer3 = QRadioButton('3')
answer4 = QRadioButton('4')
#расположение виджетов по лэйаутам


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(answer1)
layout_ans2.addWidget(answer2)
layout_ans3.addWidget(answer3)
layout_ans3.addWidget(answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
result = QLabel("Правильно\неправильно")
itog = QLabel('Верный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, Qt.AlignHCenter |Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
lb_question = QLabel("вопрос") 
first_line = QHBoxLayout()
first_line.addWidget(lb_question, alignment=(Qt. AlignHCenter | Qt.AlignVCenter))
second_line = QHBoxLayout()

second_line.addWidget(RadioGroupBox)
second_line.addWidget(AnsGroupBox)
third_line = QHBoxLayout()
button = QPushButton('Ответить')
third_line.addWidget(button, alignment=(Qt.AlignHCenter |Qt.AlignVCenter))


main_win.setLayout(v_line)
v_line.addLayout(first_line)
v_line.addLayout(second_line)
v_line.addLayout(third_line)












#обработка нажатий на переключатели
answers = [answer1,answer2,answer3,answer4]

def show_q():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')   

    
def show_resul():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
    
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(answer1)
    RadioGroup.addButton(answer2)
    RadioGroup.addButton(answer3)
    RadioGroup.addButton(answer4)
    
    
    RadioGroup.setExclusive(False)
    answer1. setChecked(False)
    answer2.setChecked(False)
    answer3. setChecked(False) 
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def win():
    victory_win = QMessageBox()
    victory_win.setText('Верно!!!')
    victory_win.show()
    victory_win.exec_()
def lose():
    lose_win = QMessageBox()
    lose_win.setText('Неверно')
    lose_win.show()
    lose_win.exec_()
def show_correct(res):
    result.setText(res)
    show_resul()
def check_answer():
    if answers[0].isChecked():
        show_correct('ответ верно')
        app.correct_ans += 1
        app.total_ans += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('ответ неверный')
        app.total_ans += 1
   

def ask(q:QuestionCLass):
    shuffle(answers)
    answers[0].setText(q.right_aans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question_list)
    itog.setText(q.right_aans)
    show_q()

def next_question():
    app.cur_question += 1
    if app.cur_question >= len(questions):
        app.cur_question = 0
        print(app.correct_ans/app.total_ans*100 , '% верных')
        print('из',app.total_ans,'вопросов',app.correct_ans,'верных')
    q = questions[app.cur_question]
    ask(q)
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

questions = []
questions.append(QuestionCLass('колесо едет 78км/ч, за сколько машина проедет час?','за час','за два часа','завтра','вчера'))
questions.append(QuestionCLass('одно яйцо варится 3 минуты, за сколько сварятся 3 яйца?','3 минуты','9 минут','пару часов','42'))
questions.append(QuestionCLass('мы считали дврки в сыре 3+2=?','5','4','42','сыр'))
questions.append(QuestionCLass('в скольки масяцвх есть 28 дней','12','1','6','0'))

app.cur_question = -1
next_question()
button.clicked.connect(click_ok)
#отображение окна приложения 
main_win.show() 
app.exec_()