import sqlite3

from TheQuest import DBM_PATH


class DBManager():
    def __init__(self):
        pass

    def select_best_players(self):
        query = 'SELECT * FROM scoreboard ORDER BY score DESC LIMIT 5'
        connection = sqlite3.connect(DBM_PATH)
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        for row in result:
            print(row)
        connection.close()
        return result

    def insert_update_info(self, name, score, level):
        insert_update = ''
        if self.exist_player(name):
            insert_update = f'UPDATE scoreboard SET score={score}, last_level={level} WHERE player=\'{name}\''
        else:
            insert_update = f'INSERT INTO scoreboard VALUES(\'{name}\',{score},{level})'
        connection = sqlite3.connect(DBM_PATH)
        cur = connection.cursor()
        cur.execute(insert_update)
        connection.commit()
        connection.close()

    def exist_player(self, name):
        connection = sqlite3.connect(DBM_PATH)
        cur = connection.cursor()
        query = f'SELECT COUNT(*) FROM scoreboard WHERE player=\'{name}\''
        cur.execute(query)
        count = cur.fetchall()[0][0]
        connection.close()
        return count > 0
