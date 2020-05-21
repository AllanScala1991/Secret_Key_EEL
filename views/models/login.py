import sqlite3
import smtplib
from email.message import EmailMessage
def save_register(name,phone,date,login,passw,email):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY, Nome TEXT, Telefone NUMBER,\
            Nascimento DATE, Usuario TEXT, Senha TEXT, Email TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS user_session (id INTEGER NOT NULL PRIMARY KEY, Usuario TEXT)")
        cursor.execute("INSERT OR REPLACE INTO user_session (id) VALUES (?)",(1,))
        if name != "" and phone != "" and date != "" and login != "" and passw != "" and email != "":     
            cursor.execute("INSERT INTO users (Nome, Telefone, Nascimento, Usuario, Senha, Email) VALUES (?,?,?,?,?,?)",\
                (name,phone,date,login,passw,email,))
            connect.commit()
            connect.close()
            msg = "sucesso"
            return msg
        else:
            msg = "falha"
            return msg
    except Exception as Error:
        print(Error)
        msg = "falha"
        return msg


def recovery_password(user_email):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Nome, Senha FROM users WHERE Email = ?",(user_email,))
        user_info = cursor.fetchone()
        connect.close()
        msg = EmailMessage()
        msg.set_content("mensagem do email")
        msg['subject'] = "Recuperação de senha."
        msg['from'] = "email do sistema"
        msg['to'] = user_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("email do sistema", "login do sistema")
        server.send_message(msg)
        msg = "sucesso"
        return msg
        
    except Exception as Error:
        print(Error)
        msg = "falha"
        return msg
    

def login_user(user_name, password):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Senha FROM users WHERE Usuario = ?", (user_name,))
        get_password = cursor.fetchone()
        if password == get_password[0]:
            cursor.execute("SELECT Nome FROM users WHERE Usuario = ?",(user_name,))
            user = cursor.fetchone()
            cursor.execute("UPDATE user_session SET Usuario = ? WHERE id = ?",(user[0],1,))
            connect.commit()
            msg = "sucesso"
            connect.close()
            return msg
        else:
            msg = "falha"
            connect.close()
            return msg
        
    except Exception as Error:
        print(Error)
        msg = "falha"
        return msg

def login_session():
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT Usuario FROM user_session WHERE id=?",(1,))
        get_user_online = cursor.fetchone()
        user_online = []
        for name in get_user_online:
            user_online.append(name)
        connect.close()
        return user_online[0]
    except Exception as error:
        user_online = "erro"
        print(error)
        return user_online
    
    
    
    
