from __future__ import print_function
import eel
from views.models.login import save_register, recovery_password, login_user, login_session
from views.models.menu import register_banks, register_cards, register_documents, register_key, update_all, select_registers, edit_registers, delete_registers


eel.init('views')


@eel.expose  # USED ​​FOR FUNCTION TO BE SEEN IN JS
def btn_save(name, phone, date, login, passw, email):
    msg = save_register(name, phone, date, login, passw, email)
    eel.save_return(str(msg))


@eel.expose
def btn_recovery(email):
    msg = recovery_password(email)
    eel.reco_return(str(msg))


@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    eel.login_return(str(msg))


@eel.expose
def get_user_online():
    get_user = login_session()
    eel.get_user(str(get_user))


@eel.expose
def btn_key(category, application, user, password):
    msg = register_key(category, application, user, password)
    eel.new_register_return(str(msg))


@eel.expose
def btn_cards(category, number, validity, holder, cod_seg, flag, password):
    msg = register_cards(category, number, validity,
                         holder, cod_seg, flag, password)
    eel.new_register_return(str(msg))


@eel.expose
def btn_banks(category, bank, agency, account, key, password):
    msg = register_banks(category, bank, agency, account, key, password)
    eel.new_register_return(str(msg))


@eel.expose
def btn_documets(category, name, number, issue, validity, observation):
    msg = register_documents(category, name, number,
                             issue, validity, observation)
    eel.new_register_return(str(msg))


@eel.expose
def update_all_info():
    get_lists = update_all()
    eel.get_update_all_js(get_lists[0], get_lists[1], get_lists[2],
                          get_lists[3], get_lists[4], get_lists[5], get_lists[6], get_lists[7])


@eel.expose
def get_registers(id, table):
    select_reg = select_registers(id, table)
    eel.action_out(select_reg)


@eel.expose
def reg_edit(id, table, infos):
    edit_reg = edit_registers(id, table, infos)
    eel.save_return(str(edit_reg))


@eel.expose
def reg_delete(id, table):
    delete_reg = delete_registers(id, table)
    eel.delete_return(str(delete_reg))


eel.start("index.html", size=(1366, 743))
