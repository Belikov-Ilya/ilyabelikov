import sqlite3
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QComboBox
from PyQt5.QtWidgets import QTableView, QWidget, QVBoxLayout, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from auth import Ui_WelcomeWindow
from registr import Ui_RegistrationWindow
from entr import Ui_LoginWindow
from selectionleague import Ui_MainPage
from rpl import Ui_RPLWindow
from apl import Ui_APLWindow
from lch import Ui_LCHWindow
from bl import Ui_BLWindow
from saver import Ui_SaveWindow
from save2 import Ui_SaveWindow2
from save3 import Ui_SaveWindow3
from save4 import Ui_SaveWindow4





class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное окно')
        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)

        self.ui.button_login.clicked.connect(self.open_login_window)
        self.ui.button_signup.clicked.connect(self.open_registration_window)

    def open_login_window(self):
        self.login_window = LoginWindow(self)
        self.login_window.show()
        self.hide()

    def open_registration_window(self):
        self.registration_window = RegistrationWindow(self)
        self.registration_window.show()
        self.hide()


class LoginWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.parent = parent

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)


        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_back.clicked.connect(self.go_back)

    def login(self):
        # Получение введенных значений логина и пароля
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()

        # Проверка логина и пароля в базе данных
        if check_credentials(username, password):
            self.parent.hide()
            self.main_page = MainPage()
            self.main_page.show()
        else:
            QMessageBox.warning(self, 'Авторизация', 'Неправильный логин или пароль')

    def go_back(self):
        self.parent.show()
        self.close()

class RegistrationWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle('Регистрация')
        self.parent = parent
        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)

        self.ui.button_signup.clicked.connect(self.signup)
        self.ui.button_back.clicked.connect(self.go_back)

    def signup(self):
        # Получение введенных значений логина и пароля
        username = self.ui.input_username.text()
        password = self.ui.input_password.text()

        # Регистрация аккаунта в базе данных
        if register_account(username, password):
            QMessageBox.information(self, 'Регистрация', 'Аккаунт успешно зарегистрирован')
            self.parent.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Регистрация', 'Ошибка регистрации')

    def go_back(self):
        self.parent.show()
        self.close()


def create_accounts_table():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Создание таблицы аккаунтов, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Закрытие соединения с базой данных
    conn.commit()
    conn.close()


def check_credentials(username, password):
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Проверка логина и пароля в таблице аккаунтов
    cursor.execute("SELECT * FROM accounts WHERE username=? AND password=?", (username, password))
    account = cursor.fetchone()

    # Закрытие соединения с базой данных
    conn.close()

    return account is not None


def register_account(username, password):
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Добавление нового аккаунта в таблицу аккаунтов
    cursor.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))

    # Закрытие соединения с базой данных
    conn.commit()
    conn.close()

    return True

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выбор Лиги')
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)


        self.ui.button1.clicked.connect(self.open_rpl_window)
        self.ui.button2.clicked.connect(self.open_apl_window)
        self.ui.button3.clicked.connect(self.open_lch_window)
        self.ui.button4.clicked.connect(self.open_bl_window)
        self.ui.new_button.clicked.connect(self.open_new_window)  # Connect the new button to the slot method

    def open_rpl_window(self):
        self.rpl_window = RPLWindow()
        self.rpl_window.show()

    def open_apl_window(self):
        self.apl_window = APLWindow()
        self.apl_window.show()

    def open_lch_window(self):
        self.lch_window = LCHWindow()
        self.lch_window.show()

    def open_bl_window(self):
        self.bl_window = BLWindow()
        self.bl_window.show()

    def open_new_window(self):  # Slot method for the new button
        self.new_window = NewWindow()
        self.new_window.show()

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Все исходы матчей')

        layout = QVBoxLayout()
        database = QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('database.db')

        if database.open():
            query = QSqlQuery()
            if query.exec_("SELECT * FROM results"):
                model = QSqlTableModel()
                model.setQuery(query)

                self.table_view = QTableView()
                self.table_view.setModel(model)
                layout.addWidget(self.table_view)
            else:
                error_label = QLabel("Ошибка выполнения запроса.")
                layout.addWidget(error_label)
        else:
            error_label = QLabel("Не удалось открыть базу данных.")
            layout.addWidget(error_label)
        self.table_view.horizontalHeader().setVisible(False)
        self.table_view.verticalHeader().setVisible(False)
        self.setLayout(layout)

class RPLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('РПЛ')
        self.ui = Ui_RPLWindow()
        self.ui.setupUi(self)

        self.ui.button10.clicked.connect(self.open_save_window)

    def open_save_window(self):
        self.save_window = SaveWindow()
        self.save_window.show()


class SaveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')
        self.ui = Ui_SaveWindow()
        self.ui.setupUi(self)

    
        teams = ['Ростов','Урал','Зенит','Динамо','Ахмат','Химки','Краснодар','ЦСКА','Сочи']
        self.ui.input_team1.addItems(teams)
        self.ui.input_team2.addItems(teams)

        layout = QVBoxLayout()
        layout.addWidget(self.ui.label_team1)
        layout.addWidget(self.ui.input_team1)
        layout.addWidget(self.ui.label_team2)
        layout.addWidget(self.ui.input_team2)
        layout.addWidget(self.ui.label_result)
        layout.addWidget(self.ui.input_result)
        layout.addWidget(self.ui.button_save)
        self.setLayout(layout)

        self.ui.button_save.clicked.connect(self.save_match_result)

    def save_match_result(self):
        team1 = self.ui.input_team1.currentText()
        team2 = self.ui.input_team2.currentText()
        result = self.ui.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO results VALUES (?, ?, ?)", (team1, team2, result))
        conn.commit()
        conn.close()
        self.close()

class APLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('АПЛ')
        self.ui = Ui_APLWindow()
        self.ui.setupUi(self)

        
        self.ui.button10.clicked.connect(self.open_save_window2)

        

    def open_save_window2(self):
        self.save_window = SaveWindow2()
        self.save_window.show()

class SaveWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')
        self.ui = Ui_SaveWindow2()
        self.ui.setupUi(self)
        teams = ['Манчестер Сити','Арсенал','Манчестер Юнайтед','Ливерпуль','Тоттенхэм','Лестер Сити','Эвертон','Фулхэм','Челси']
        self.ui.input_team1.addItems(teams)
        self.ui.input_team2.addItems(teams)

        layout = QVBoxLayout()
        layout.addWidget(self.ui.label_team1)
        layout.addWidget(self.ui.input_team1)
        layout.addWidget(self.ui.label_team2)
        layout.addWidget(self.ui.input_team2)
        layout.addWidget(self.ui.label_result)
        layout.addWidget(self.ui.input_result)
        layout.addWidget(self.ui.button_save)
        self.setLayout(layout)

        self.ui.button_save.clicked.connect(self.save_match_result2)

    def save_match_result2(self):
        team1 = self.ui.input_team1.currentText()
        team2 = self.ui.input_team2.currentText()
        result = self.ui.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO results VALUES (?, ?, ?)", (team1, team2, result))
        conn.commit()
        conn.close()
        self.close()




class LCHWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛЧ')
        self.ui = Ui_LCHWindow()
        self.ui.setupUi(self)


        self.ui.button10.clicked.connect(self.open_save_window3)


    def open_save_window3(self):
        self.save_window = SaveWindow3()
        self.save_window.show()



class SaveWindow3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')
        self.ui = Ui_SaveWindow3()
        self.ui.setupUi(self)
        
        teams = ['Наполи','Аякс','Рейнджерс','Байер','Бавария','Барселона','Интер','Спортинг','Марсель']
        self.ui.input_team1.addItems(teams)
        self.ui.input_team2.addItems(teams)

        layout = QVBoxLayout()
        layout.addWidget(self.ui.label_team1)
        layout.addWidget(self.ui.input_team1)
        layout.addWidget(self.ui.label_team2)
        layout.addWidget(self.ui.input_team2)
        layout.addWidget(self.ui.label_result)
        layout.addWidget(self.ui.input_result)
        layout.addWidget(self.ui.button_save)
        self.setLayout(layout)

        self.ui.button_save.clicked.connect(self.save_match_result3)

    def save_match_result3(self):
        team1 = self.ui.input_team1.currentText()
        team2 = self.ui.input_team2.currentText()
        result = self.ui.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO results VALUES (?, ?, ?)", (team1, team2, result))
        conn.commit()
        conn.close()
        self.close()



class BLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('БЛ')
        self.ui = Ui_BLWindow()
        self.ui.setupUi(self)

        
        self.ui.button10.clicked.connect(self.open_save_window4)

    def open_save_window4(self):
        self.save_window = SaveWindow4()
        self.save_window.show()

class SaveWindow4(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')
        self.ui = Ui_SaveWindow4()
        self.ui.setupUi(self)
        teams = ['Боруссия (Дортмунд)','Бавария','РБ Лейпциг','Фрайбург','Байер','Кёльн','Бохум','Унион (Берлин)','Вольфсбург']
        self.ui.input_team1.addItems(teams)
        self.ui.input_team2.addItems(teams)

        layout = QVBoxLayout()
        layout.addWidget(self.ui.label_team1)
        layout.addWidget(self.ui.input_team1)
        layout.addWidget(self.ui.label_team2)
        layout.addWidget(self.ui.input_team2)
        layout.addWidget(self.ui.label_result)
        layout.addWidget(self.ui.input_result)
        layout.addWidget(self.ui.button_save)
        self.setLayout(layout)

        self.ui.button_save.clicked.connect(self.save_match_result4)

    def save_match_result4(self):
        team1 = self.ui.input_team1.currentText()
        team2 = self.ui.input_team2.currentText()
        result = self.ui.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO results VALUES (?, ?, ?)", (team1, team2, result))
        conn.commit()
        conn.close()
        self.close()





if __name__ == '__main__':
    # Создание таблицы аккаунтов при запуске приложения
    create_accounts_table()

    app = QApplication([])
    welcome_window = WelcomeWindow()
    welcome_window.show()
    app.exec_()
