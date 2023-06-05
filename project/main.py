import sqlite3
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Добро пожаловать')

        self.label = QLabel('Добро пожаловать!')
        self.button_login = QPushButton('Авторизация')
        self.button_signup = QPushButton('Регистрация')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_signup)
        self.setLayout(layout)

        self.button_login.clicked.connect(self.open_login_window)
        self.button_signup.clicked.connect(self.open_registration_window)

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

        self.label_username = QLabel('Логин')
        self.input_username = QLineEdit()
        self.label_password = QLabel('Пароль')
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton('Войти')
        self.button_back = QPushButton('Назад')

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_back)
        self.setLayout(layout)

        self.button_login.clicked.connect(self.login)
        self.button_back.clicked.connect(self.go_back)

    def login(self):
        # Получение введенных значений логина и пароля
        username = self.input_username.text()
        password = self.input_password.text()

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

        self.label_username = QLabel('Логин')
        self.input_username = QLineEdit()
        self.label_password = QLabel('Пароль')
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)  # Скрытие введенного пароля

        self.button_signup = QPushButton('Зарегистрироваться')
        self.button_back = QPushButton('Назад')

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_signup)
        layout.addWidget(self.button_back)
        self.setLayout(layout)

        self.button_signup.clicked.connect(self.signup)
        self.button_back.clicked.connect(self.go_back)

    def signup(self):
        # Получение введенных значений логина и пароля
        username = self.input_username.text()
        password = self.input_password.text()

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
        self.setWindowTitle('Новая страница')

        self.label = QLabel('Выберите Лигу:')
        self.button1 = QPushButton('РПЛ')
        self.button2 = QPushButton('АПЛ')
        self.button3 = QPushButton('ЛЧ')
        self.button4 = QPushButton('БЛ')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

        self.button1.clicked.connect(self.open_rpl_window)
        self.button2.clicked.connect(self.open_apl_window)
        self.button3.clicked.connect(self.open_lch_window)
        self.button4.clicked.connect(self.open_bl_window)

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


class RPLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('РПЛ')

        self.button1 = QPushButton('Ростов')
        self.button2 = QPushButton('Урал')
        self.button3 = QPushButton('Зенит')
        self.button4 = QPushButton('Динамо')
        self.button5 = QPushButton('Ахмат')
        self.button6 = QPushButton('Химки')
        self.button7 = QPushButton('Краснодар')
        self.button8 = QPushButton('ЦСКА')
        self.button9 = QPushButton('Сочи')
        self.button10 = QPushButton('Записать исход матча')

        self.button10.clicked.connect(self.open_save_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        self.setLayout(layout)

    def open_save_window(self):
        self.save_window = SaveWindow()
        self.save_window.show()


class SaveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')

        self.label_team1 = QLabel('Команда 1')
        self.input_team1 = QLineEdit()
        self.label_team2 = QLabel('Команда 2')
        self.input_team2 = QLineEdit()
        self.label_result = QLabel('Результат')
        self.input_result = QLineEdit()

        self.button_save = QPushButton('Сохранить')

        layout = QVBoxLayout()
        layout.addWidget(self.label_team1)
        layout.addWidget(self.input_team1)
        layout.addWidget(self.label_team2)
        layout.addWidget(self.input_team2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.input_result)
        layout.addWidget(self.button_save)
        self.setLayout(layout)

        self.button_save.clicked.connect(self.save_match_result)

    def save_match_result(self):
        team1 = self.input_team1.text()
        team2 = self.input_team2.text()
        result = self.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS rpl_results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO rpl_results VALUES (?, ?, ?)", (team1, team2, result))

        conn.commit()
        conn.close()

        self.close()

class APLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('АПЛ')

        self.button1 = QPushButton('Манчестер Сити')
        self.button2 = QPushButton('Арсенал')
        self.button3 = QPushButton('Манчестер Юнайтед')
        self.button4 = QPushButton('Ливерпуль')
        self.button5 = QPushButton('Тоттенхэм')
        self.button6 = QPushButton('Лестер Сити')
        self.button7 = QPushButton('Эвертон')
        self.button8 = QPushButton('Фулхэм')
        self.button9 = QPushButton('Челси')
        self.button10 = QPushButton('Записать исход матча')

        self.button10.clicked.connect(self.open_save_window2)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        self.setLayout(layout)


    def open_save_window2(self):
        self.save_window = SaveWindow2()
        self.save_window.show()

class SaveWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')

        self.label_team1 = QLabel('Команда 1')
        self.input_team1 = QLineEdit()
        self.label_team2 = QLabel('Команда 2')
        self.input_team2 = QLineEdit()
        self.label_result = QLabel('Результат')
        self.input_result = QLineEdit()

        self.button_save = QPushButton('Сохранить')

        layout = QVBoxLayout()
        layout.addWidget(self.label_team1)
        layout.addWidget(self.input_team1)
        layout.addWidget(self.label_team2)
        layout.addWidget(self.input_team2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.input_result)
        layout.addWidget(self.button_save)
        self.setLayout(layout)

        self.button_save.clicked.connect(self.save_match_result2)

    def save_match_result2(self):
        team1 = self.input_team1.text()
        team2 = self.input_team2.text()
        result = self.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS apl_results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO apl_results VALUES (?, ?, ?)", (team1, team2, result))

        conn.commit()
        conn.close()

        self.close()




class LCHWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛЧ')

        self.button1 = QPushButton('Наполи')
        self.button2 = QPushButton('Аякс')
        self.button3 = QPushButton('Рейнджерс')
        self.button4 = QPushButton('Байер')
        self.button5 = QPushButton('Бавария')
        self.button6 = QPushButton('Барселона')
        self.button7 = QPushButton('Интер')
        self.button8 = QPushButton('Спортинг')
        self.button9 = QPushButton('Марсель')
        self.button10 = QPushButton('Записать исход матча')

        self.button10.clicked.connect(self.open_save_window3)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        self.setLayout(layout)

    def open_save_window3(self):
        self.save_window = SaveWindow3()
        self.save_window.show()



class SaveWindow3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')

        self.label_team1 = QLabel('Команда 1')
        self.input_team1 = QLineEdit()
        self.label_team2 = QLabel('Команда 2')
        self.input_team2 = QLineEdit()
        self.label_result = QLabel('Результат')
        self.input_result = QLineEdit()

        self.button_save = QPushButton('Сохранить')

        layout = QVBoxLayout()
        layout.addWidget(self.label_team1)
        layout.addWidget(self.input_team1)
        layout.addWidget(self.label_team2)
        layout.addWidget(self.input_team2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.input_result)
        layout.addWidget(self.button_save)
        self.setLayout(layout)

        self.button_save.clicked.connect(self.save_match_result3)

    def save_match_result3(self):
        team1 = self.input_team1.text()
        team2 = self.input_team2.text()
        result = self.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS lch_results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO lch_results VALUES (?, ?, ?)", (team1, team2, result))

        conn.commit()
        conn.close()

        self.close()



class BLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('БЛ')

        self.button1 = QPushButton('Боруссия (Дортмунд)')
        self.button2 = QPushButton('Бавария')
        self.button3 = QPushButton('РБ Лейпциг')
        self.button4 = QPushButton('Фрайбург')
        self.button5 = QPushButton('Байер')
        self.button6 = QPushButton('Кёльн')
        self.button7 = QPushButton('Бохум')
        self.button8 = QPushButton('Унион (Берлин)')
        self.button9 = QPushButton('Вольфсбург')
        self.button10 = QPushButton('Записать исход матча')

        self.button10.clicked.connect(self.open_save_window4)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button10)
        self.setLayout(layout)

    def open_save_window4(self):
        self.save_window = SaveWindow4()
        self.save_window.show()

class SaveWindow4(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Сохранить')

        self.label_team1 = QLabel('Команда 1')
        self.input_team1 = QLineEdit()
        self.label_team2 = QLabel('Команда 2')
        self.input_team2 = QLineEdit()
        self.label_result = QLabel('Результат')
        self.input_result = QLineEdit()

        self.button_save = QPushButton('Сохранить')

        layout = QVBoxLayout()
        layout.addWidget(self.label_team1)
        layout.addWidget(self.input_team1)
        layout.addWidget(self.label_team2)
        layout.addWidget(self.input_team2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.input_result)
        layout.addWidget(self.button_save)
        self.setLayout(layout)

        self.button_save.clicked.connect(self.save_match_result4)

    def save_match_result4(self):
        team1 = self.input_team1.text()
        team2 = self.input_team2.text()
        result = self.input_result.text()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS bl_results (team1 TEXT, team2 TEXT, result TEXT)")
        c.execute("INSERT INTO bl_results VALUES (?, ?, ?)", (team1, team2, result))

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
