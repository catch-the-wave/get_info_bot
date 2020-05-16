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
    add_user = 'INSERT INTO user_id(name, chat_id, sms) VALUES (%(name)s,%(chat_id)s, %(sms)s)'
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
    set = 'SELECT chat_id FROM child WHERE sms="0"'
    cursor.execute(set)
    nit = cursor.fetchall()
    cursor.close()
    return nit
