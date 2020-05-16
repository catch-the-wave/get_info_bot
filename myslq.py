# from contextlib import closing
import pymysql
from DBUtils.PersistentDB import PersistentDB
from pymysql.cursors import DictCursor

# конец импотов
persist = PersistentDB(creator=pymysql, host='213.79.122.211', user='nail', password='likokil', db='parsing',
                       autocommit=True, charset='utf8mb4', cursorclass=DictCursor)
conn = persist.connection()


def save_user(message):
    cursor = conn.cursor()
    add_user = 'INSERT INTO parents(name, chat_id, sms) VALUES (%(name)s,%(chat_id)s, %(sms)s)'
    # VALUES ('', '55', '454')
    user_id = message.chat.id
    name = message.from_user.first_name

    data_person = {
        'name': name,
        'chat_id': user_id,
        'sms': '1',
    }
    cursor.execute(add_user, data_person)
    conn.commit()
    cursor.close()


def spam_get_date():
    cursor = conn.cursor()
    set = 'SELECT * FROM job_spam WHERE sms="0"'
    cursor.execute(set)
    nit = cursor.fetchall()
    cursor.close()
    return nit


def rasilkas():
    cursor = conn.cursor()
    set = 'SELECT chat_id FROM parents WHERE sms="0"'
    cursor.execute(set)
    nit = cursor.fetchall()
    cursor.close()
    return nit


def smap_not_yes(chat_id):
    cursor = conn.cursor()
    set = 'SELECT sms FROM parents WHERE chat_id="{}"'.format(chat_id)
    cursor.execute(set)
    nit = cursor.fetchall()
    cursor.close()
    return nit[0].get('sms')


def smap_up(chat_id, sms=0):
    cursor = conn.cursor()
    set = 'UPDATE parents SET sms="{}" WHERE chat_id="{}"'.format(sms, chat_id)
    cursor.execute(set)
    conn.commit()
    cursor.close()


def save_favourites(chat_id, first_name, inn):
    cursor = conn.cursor()
    set = 'SELECT id FROM parents WHERE chat_id="{}"'.format(chat_id)
    cursor.execute(set)
    nit = cursor.fetchall()[0]
    add_user = 'INSERT INTO favourites(name_id, first_name, inn) VALUES (%(name_id)s,%(first_name)s, %(inn)s)'
    data_person = {
        'name_id': nit.get('id'),
        'first_name': first_name,
        'inn': inn,
    }
    cursor.execute(add_user, data_person)
    conn.commit()
    cursor.close()


def delete_favourites(chat_id, inn):
    cursor = conn.cursor()
    set = 'SELECT id FROM parents WHERE chat_id="{}"'.format(chat_id)
    cursor.execute(set)
    nit = cursor.fetchall()[0]
    set = ' DELETE FROM favourites  WHERE name_id="{}" AND inn="{}"'.format(nit.get('id'), inn)
    cursor.execute(set)
    conn.commit()
    cursor.close()
