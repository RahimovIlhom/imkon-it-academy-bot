import sqlite3


class Database:
    def __init__(self, db_path: str = 'db.sqlite3'):
        self.db_path = db_path

    @property
    def connection(self):
        conn = sqlite3.connect(self.db_path)
        return conn

    def column_names_user(self):
        conn = self.connection
        cur = conn.cursor()
        cur.execute("""select * from course_user""")
        res = [column[0] for column in cur.description]
        conn.close()
        return res

    def add_user(self, user_id, fullname):
        conn = self.connection
        cur = conn.cursor()
        cur.execute("""insert into course_user(user_id, fullname) values (?, ?)""", (user_id, fullname))
        conn.commit()
        conn.close()

    def select_users(self):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_user""").fetchall()
        conn.close()
        return res

    def select_user(self, user_id):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_user where user_id=?""", (user_id, )).fetchone()
        conn.close()
        return res

    def column_names_course(self):
        conn = self.connection
        cur = conn.cursor()
        cur.execute("""select * from course_course""")
        res = [column[0] for column in cur.description]
        conn.close()
        return res

    def column_names_category(self):
        conn = self.connection
        cur = conn.cursor()
        cur.execute("""select * from course_category""")
        res = [column[0] for column in cur.description]
        conn.close()
        return res

    def column_names_lesson(self):
        conn = self.connection
        cur = conn.cursor()
        cur.execute("""select * from course_lesson""")
        res = [column[0] for column in cur.description]
        conn.close()
        return res

    def select_courses(self):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_course""").fetchall()
        conn.close()
        return res

    def select_categories(self, course_id):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_category where course_id=?""", (course_id, )).fetchall()
        conn.close()
        return res

    def select_lessons(self, category_id):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_lesson where category_id=?""", (category_id,)).fetchall()
        conn.close()
        return res

    def select_lesson(self, lesson_id):
        conn = self.connection
        cur = conn.cursor()
        res = cur.execute("""select * from course_lesson where id=?""", (lesson_id,)).fetchone()
        conn.close()
        return res


# db = Database()
# print(db.column_names_user())
# print(db.column_names_category())
# print(db.column_names_lesson())
