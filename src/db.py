import MySQLdb as mysql

class City:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = mysql.connect(
            self.host,
            self.username,
            self.password,
            self.database
        )
        self._cursor = self._connection.cursor()

    def disconnect(self):
        self._connection.close()

    def create_city(self, name):
        self._cursor.execute(
            'insert into jscity.tb_city (name, tooltip) values (%s, %s)',
            (name, name)
        )
        self._connection.commit()
        return self._cursor.lastrowid

    def create_district(self, name, city_id, parent_district_id=None,
                        color='0xD9534F'):
        if parent_district_id:
            self._cursor.execute(
                """insert into jscity.tb_district
                    (name, color, tooltip, city_id, district_id)
                    values ('%s', '%s', '%s', %d, %d)""" % \
                    (name, color, name, city_id, parent_district_id)
            )
        else:
            self._cursor.execute(
                """insert into jscity.tb_district
                    (name, color, tooltip, city_id)
                    values ('%s', '%s', '%s', %d)""" % \
                    (name, color, name, city_id)
            )

        self._connection.commit()
        return self._cursor.lastrowid

    def create_building(self, name, height, width, district_id, color='0x337AB7'):
        self._cursor.execute(
            """insert into jscity.tb_building
                (name, height, width, color, tooltip, district_id)
                values ('%s', %d, %d, '%s', '%s', %d)""" % \
                (name, height, width, color, name, district_id)
        )
        self._connection.commit()
        return self._cursor.lastrowid
