import sqlite3
import smtplib
from email.message import EmailMessage


def save_register(name, phone, date, login, passw, email):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL PRIMARY KEY, Name TEXT, Phone NUMBER, \
            Nascimento DATE, User TEXT, Password TEXT, Email TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS user_session(id INTEGER NOT NULL PRIMARY KEY, User TEXT)")
        cursor.execute(
            "INSERT OR REPLACE INTO user_session(id) VALUES(?)", (1,))
        if name != "" and phone != "" and date != "" and login != "" and passw != "" and email != "":
            cursor.execute("INSERT INTO users(Name, Phone, Birth, User, Password, Email) VALUES(?,?,?,?,?,?)",
                           (name, phone, date, login, passw, email,))
            connect.commit()
            connect.close()
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def recovery_password(user_email):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute(
            "SELECT Name, Password FROM users WHERE Email =?", (user_email,))
        user_info = cursor.fetchone()
        connect.close()
        msg = EmailMessage()
        msg.set_content("email message")
        msg['subject'] = "Password recovery."
        msg['from'] = "system email"
        msg['to'] = user_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("system email", "system login")
        server.send_message(msg)
        msg = "success"
        return msg

    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def login_user(user_name, password):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute(
            "SELECT Password FROM users WHERE User =?", (user_name,))
        get_password = cursor.fetchone()
        if password == get_password[0]:
            cursor.execute(
                "SELECT Name FROM users WHERE User =?", (user_name,))
            user = cursor.fetchone()
            cursor.execute(
                "UPDATE user_session SET User = = WHERE id =?", (user[0], 1,))
            connect.commit()
            msg = "success"
            connect.close()
            return msg
        else:
            msg = "failure"
            connect.close()
            return msg

    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg


def login_session():
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT User FROM user_session WHERE id =?", (1,))
        get_user_online = cursor.fetchone()
        user_online = []
        for name in get_user_online:
            user_online.append(name)
        connect.close()
        return user_online[0]
    except Exception as error:
        user_online = "error"
        print(error)
        return user_online
