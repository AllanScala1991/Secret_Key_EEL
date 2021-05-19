import sqlite3

# REGISTRATION FUNCTIONS


def register_key(category, application, user, password):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO keys (category, Application, User, Password) VALUES (?,?,?,?)",
                         (category, application, user, password,))
        connect.commit()
        connect.close()
        msg = "Registration was successful"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Failed to register"
        return msg


def register_cards(category, number, validity, holder, cod_seg, flag, password):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        if flag == "":
            flag = "Visa"
        cursor.execute("INSERT INTO cards (category, Number, Validity, Holder, Cod_Seg, Flag, Password) VALUES (?,?,?,?,?,?,?)",
                         (category, number, validity, holder, cod_seg, flag, password))
        connect.commit()
        connect.close()
        msg = "Registration was successful"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Failed to register"
        return msg


def register_banks(category, bank, agency, account, key, password):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO banks (category, Bank, Agency, Account, Key, Password) VALUES (?,?,?,?,?,?)",
                         (category, bank, agency, account, key, password,))
        connect.commit()
        connect.close()
        msg = "Registration was successful"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Failed to register"
        return msg


def register_documents(category, name, number, issue, validity, observation):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO documents (category, Name, Number, Issue, Validity, Observation) VALUES (?,?,?,?,?,?)",
                         (category, name, number, issue, validity, observation))
        connect.commit()
        connect.close()
        msg = "Registration was successful"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Failed to register"
        return msg

# INFORMATION UPDATE FUNCTIONS


def update_all():
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS keys (id INTEGER NOT NULL PRIMARY KEY, category TEXT, Application TEXT, User TEXT, Password TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS cards (id INTEGER NOT NULL PRIMARY KEY, TEXT category, NUMBER Number, TEXT Validity, TEXT Holder, \
            Cod_Seg NUMBER, Flag TEXT, Password TEXT) ")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS banks (id INTEGER NOT NULL PRIMARY KEY, TEXT category, TEXT Bank, TEXT Agency, TEXT Account, TEXT Key, TEXT Password)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS documents (id INTEGER NOT NULL PRIMARY KEY, TEXT category, TEXT Name, NUMBER Number, TEXT Issue, TEXT Validity, TEXT Observation)")
        emails_items = []
        socials_items = []
        games_items = []
        sites_items = []
        app_items = []
        cards_items = []
        banks_items = []
        documents_items = []
        cursor.execute("SELECT * FROM keys WHERE category =?", ("Emails",))
        for item in cursor.fetchall():
            emails_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE category =?",
                         ("Social Networks",))
        for item in cursor.fetchall():
            socials_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE category =?", ("Games",))
        for item in cursor.fetchall():
            games_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE category =?", ("Sites",))
        for item in cursor.fetchall():
            sites_items.append(item)
        cursor.execute(
            "SELECT * FROM keys WHERE category =?", ("Applications",))
        for item in cursor.fetchall():
            app_items.append(item)
        cursor.execute("SELECT * FROM cards")
        for item in cursor.fetchall():
            cards_items.append(item)
        cursor.execute("SELECT * FROM banks")
        for item in cursor.fetchall():
            banks_items.append(item)
        cursor.execute("SELECT * FROM documents")
        for item in cursor.fetchall():
            documents_items.append(item)
        connect.close()
        return emails_items, socials_items, games_items, sites_items, app_items, cards_items, banks_items, documents_items

    except Exception as Error:
        print(Error)
        msg = "Failed to register"
        return msg

# FUNCTIONS OF SELECTING, EDITING AND DELETING RECORDS


def select_registers(id, table):
    try:
        if table == "keys":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM keys WHERE id =?", (id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers

        if table == "cards":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM cards WHERE id =?", (id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers

        if table == "banks":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM banks WHERE id =?", (id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers

        if table == "documents":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM documents WHERE id =?", (id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers
    except Exception as error:
        print(error)
        msg = "Error"
        return msg


def edit_registers(id, table, infos):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        if table == "keys":
            cursor.execute("UPDATE keys SET Application =?, User =?, Password =? WHERE id =?",
                             (infos[0], infos[1], infos[2], id,))
            connect.commit()
            connect.close()
            msg = "Changed successfully!"
            return msg
        if table == "cards":
            cursor.execute("UPDATE cards SET Number =?, Validity =?, Holder =?, Cod_Seg =?, Flag =?, Password =? \
                 WHERE id =? ", (infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], id,))
            connect.commit()
            connect.close()
            msg = "Changed successfully!"
            return msg
        if table == "banks":
            cursor.execute("UPDATE banks SET Bank =?, Agency =?, Account =?, Key =?, Password =? \
                 WHERE id =? ", (infos[0], infos[1], infos[2], infos[3], infos[4], id,))
            connect.commit()
            connect.close()
            msg = "Changed successfully!"
            return msg
        if table == "documents":
            cursor.execute("UPDATE banks SET Name =?, Number =?, Issue =?, Validity =?, Observation =? \
                 WHERE id =? ", (infos[0], infos[1], infos[2], infos[3], infos[4], id,))
            connect.commit()
            connect.close()
            msg = "Changed successfully!"
            return msg
    except Exception as error:
        print(error)
        msg = "Error while changing!"
        return msg


def delete_registers(id, table):
    try:
        if table == "keys":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM keys WHERE id =?", (id,))
            connect.commit()
            connect.close()
            msg = "Successfully deleted!"
            return msg
        if table == "cards":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM cards WHERE id =?", (id,))
            connect.commit()
            connect.close()
            msg = "Successfully deleted!"
            return msg
        if table == "banks":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM banks WHERE id =?", (id,))
            connect.commit()
            connect.close()
            msg = "Successfully deleted!"
            return msg
        if table == "documents":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM documents WHERE id =?", (id,))
            connect.commit()
            connect.close()
            msg = "Successfully deleted!"
            return msg
    except Exception as error:
        print(error)
        msg = "Error while deleting!"
        return msg
