import sqlite3

conn = sqlite3.connect("bombcrypto.db")
cursor = conn.cursor()


def create():
    """
    Cria a tabela de relatório de não existe
    :return:
    """
    global cursor
    cursor.execute("""
        create table if not exists relatorio (
            id INTEGER PRIMARY KEY autoincrement,
            data text,
            q_token real,
            t_token text,
            login text
        )
    """)


def get():
    """
    Traz listagem de dados
    :return:
    """
    global cursor
    create()
    cursor.execute("""
        select * from relatorio
    """)
    data = []
    for line in cursor.fetchall():
        data.append(line)

    return data


def sum_month(token):
    """
    Traz listagem do somatório do token informado no mês
    :param token:
    :return:
    """
    global cursor
    from datetime import datetime
    cur_month = datetime.now().strftime('%m')
    create()
    cursor.execute(f"""
        select sum(q_token) from relatorio where strftime('%m', data) = '{cur_month}' and t_token = '{token}'
    """)
    return cursor.fetchone()[0]


def add(data, q_token, t_token, login):
    """
    Inserção de dados
    :param data:
    :param q_token:
    :param t_token:
    :param login:
    :return:
    """
    global conn, cursor
    create()
    cursor.execute(f"""
        insert into relatorio (data, q_token, t_token, login) values (?, ?, ?, ?)
    """, (data, q_token, t_token, login))
    conn.commit()
