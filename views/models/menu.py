import sqlite3

# FUNÇÕES DE REGISTRO 
def register_key(categoria, aplicacao, usuario, senha):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO keys (Categoria, Aplicacao, Usuario, Senha) VALUES (?,?,?,?)",(categoria, aplicacao, usuario,senha,))
        connect.commit()
        connect.close()
        msg = "Registro efetuado com sucesso"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Falha ao registrar"
        return msg
        
def register_cards(categoria,numero, validade, titular, cod_seg, bandeira, senha):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        if bandeira == "":
            bandeira = "Visa"
        cursor.execute("INSERT INTO cards (Categoria, Numero, Validade, Titular, Cod_Seg, Bandeira, Senha) VALUES (?,?,?,?,?,?,?)"\
            ,(categoria, numero, validade, titular, cod_seg, bandeira, senha,))
        connect.commit()
        connect.close()
        msg = "Registro efetuado com sucesso"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Falha ao registrar"
        return msg

def register_banks(categoria, banco, agencia, conta, chave, senha):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("INSERT INTO banks (Categoria, Banco, Agencia, Conta, Chave, Senha) VALUES (?,?,?,?,?,?)",(categoria, banco, agencia, conta, chave, senha,))
        connect.commit()
        connect.close()
        msg = "Registro efetuado com sucesso"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Falha ao registrar"
        return msg

def register_documents(categoria, nome, numero, emissao, validade,observacao):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()    
        cursor.execute("INSERT INTO documents (Categoria, Nome, Numero, Emissao, Validade, Observacao) VALUES (?,?,?,?,?,?)",(categoria, nome, numero, emissao, validade, observacao,))
        connect.commit()
        connect.close()
        msg = "Registro efetuado com sucesso"
        return msg
    except Exception as Error:
        print(Error)
        msg = "Falha ao registrar"
        return msg

# FUNÇÕES DE UPDATE DE INFORMAÇÕES
def update_all():
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS keys (id INTEGER NOT NULL PRIMARY KEY, Categoria TEXT, Aplicacao TEXT, Usuario TEXT, Senha TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS cards (id INTEGER NOT NULL PRIMARY KEY,Categoria TEXT, Numero NUMBER, Validade TEXT, Titular TEXT,\
            Cod_Seg NUMBER, Bandeira TEXT, Senha TEXT )")
        cursor.execute("CREATE TABLE IF NOT EXISTS banks (id INTEGER NOT NULL PRIMARY KEY,Categoria TEXT, Banco TEXT, Agencia TEXT, Conta TEXT, Chave TEXT, Senha TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS documents (id INTEGER NOT NULL PRIMARY KEY,Categoria TEXT, Nome TEXT, Numero NUMBER, Emissao TEXT, Validade TEXT, Observacao TEXT )")  
        emails_items = []
        socials_items = []
        games_items = []
        sites_items = []
        app_items = []
        cards_items = []
        banks_items = []
        documents_items = []
        cursor.execute("SELECT * FROM keys WHERE Categoria = ?",("Emails",))
        for item in cursor.fetchall():
            emails_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE Categoria = ?",("Redes Sociais",))
        for item in cursor.fetchall():
            socials_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE Categoria = ?",("Jogos",))
        for item in cursor.fetchall():
            games_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE Categoria = ?",("Sites",))
        for item in cursor.fetchall():
            sites_items.append(item)
        cursor.execute("SELECT * FROM keys WHERE Categoria = ?",("Aplicativos",))
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
        msg = "Falha ao registrar"
        return msg

# FUNCOES DE SELECIONAR, EDITAR E DELETAR REGISTROS
def select_registers(id, table):
    try:
        if table == "keys":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM keys WHERE id=?",(id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers
        
        if table == "cards":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM cards WHERE id=?",(id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers
        
        if table == "banks":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM banks WHERE id=?",(id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers
        
        if table == "documents":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM documents WHERE id=?",(id,))
            registers = []
            for item in cursor.fetchone():
                registers.append(item)
            return registers
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg
                
def edit_registers(id, table, infos):
    try:
        connect = sqlite3.connect("views/database/storage.db")
        cursor = connect.cursor()
        if table == "keys":
            cursor.execute("UPDATE keys SET Aplicacao = ?, Usuario = ?, Senha = ? WHERE id=?",(infos[0],infos[1],infos[2],id,))
            connect.commit()
            connect.close()
            msg = "Alterado com sucesso!"
            return msg
        if table == "cards":
            cursor.execute("UPDATE cards SET Numero = ?, Validade = ?, Titular = ?, Cod_Seg = ?, Bandeira = ?, Senha = ?\
                 WHERE id=?",(infos[0],infos[1],infos[2],infos[3],infos[4],infos[5],id,))
            connect.commit()
            connect.close()
            msg = "Alterado com sucesso!"
            return msg
        if table == "banks":
            cursor.execute("UPDATE banks SET Banco = ?, Agencia = ?, Conta = ?, Chave = ?, Senha = ?\
                 WHERE id=?",(infos[0],infos[1],infos[2],infos[3],infos[4],id,))
            connect.commit()
            connect.close()
            msg = "Alterado com sucesso!"
            return msg
        if table == "documents":
            cursor.execute("UPDATE banks SET Nome = ?, Numero = ?, Emissao = ?, Validade = ?, Observacao = ?\
                 WHERE id=?",(infos[0],infos[1],infos[2],infos[3],infos[4],id,))
            connect.commit()
            connect.close()
            msg = "Alterado com sucesso!"
            return msg
    except Exception as error:
        print(error)
        msg = "Erro ao alterar!"
        return msg

def delete_registers(id, table):
    try:
        if table == "keys":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM keys WHERE id = ?",(id,))
            connect.commit()
            connect.close()
            msg = "Deletado com sucesso!"
            return msg
        if table == "cards":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM cards WHERE id = ?",(id,))
            connect.commit()
            connect.close()
            msg = "Deletado com sucesso!"
            return msg
        if table == "banks":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM banks WHERE id = ?",(id,))
            connect.commit()
            connect.close()
            msg = "Deletado com sucesso!"
            return msg
        if table == "documents":
            connect = sqlite3.connect("views/database/storage.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM documents WHERE id = ?",(id,))
            connect.commit()
            connect.close()
            msg = "Deletado com sucesso!"
            return msg
    except Exception as error:
        print(error)
        msg = "Erro ao deletar!"
        return msg
