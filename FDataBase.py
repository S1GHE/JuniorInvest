
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getFeedback(self):
        try:
            self.__cur.execute("SELECT * FROM FEEDBACK")
            res = self.__cur.fetchall()
            if res: return res
        except Exception as e:
            print(f"Ошибка чтения бд {e}")

        return []


    def addMessage(self, first_name, last_name, telephone_number, email_address, address, subject, message):
        try:
            self.__cur.execute("INSERT INTO FEEDBACK VALUES (?, ?, ?, ?, ?, ?, ?)",(
                first_name, last_name,telephone_number, email_address, address, subject, message
            ))
            self.__db.commit()

        except Exception as e:
            print(f"Ошибка записи в бд {e}")
            return False

        return True


    def addUser(self, first_name, last_name, username, telephone_number, email_address, password):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM USERS WHERE EMAIL_ADDRESS LIKE '{email_address}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False


            self.__cur.execute("INSERT INTO USERS VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                first_name, last_name, username, telephone_number, email_address, password, 0, "None", "None"
            ))
            self.__db.commit()

        except Exception as e:
            print(f"Ошибка записи в бд {e}")
            return False

        return True

    def addProject(self, name_project, category_project, description_project,
                   author_user_id, author_first_name, author_last_name,author_username, date_of_creation):
        try:
            self.__cur.execute("INSERT INTO PROJECT VALUES (NULL, ?, ?, ?, NUll, ?, ?, ?, ?, ?)",(
                name_project, category_project, description_project,
                author_user_id, author_first_name, author_last_name,
                author_username, date_of_creation
            ))
            self.__db.commit()
        except Exception as e:
            print(f"Ошибка записи в бд {e}")
            return False
        return True

    def getProjects(self):
        try:
            self.__cur.execute("SELECT * FROM PROJECT")
            res = self.__cur.fetchall()
            if res: return res
        except Exception as e:
            print(f"Ошибка чтения бд {e}")
        return []


    def getProject(self, postId):
        try:
            self.__cur.execute(f"SELECT * FROM PROJECT WHERE ID = {postId} LIMIT 1")
            res = self.__cur.fetchone()
            print(res)
            if res: return res
        except Exception as e:
            print(f"Ошибка получения данных с бд {e}")
        return False

    def getUsers(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE ID = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except Exception as e:
            print(f"Ошибка получения данных с бд {e}")

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE EMAIL_ADDRESS = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except Exception as e:
            print(f"Ошибка получения данных из БД {e}")

        return False

    def getUserInfo(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM USERS WHERE ID = '{id}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except Exception as e:
            print(f"Ошибка получения данных из БД {e}")

        return False