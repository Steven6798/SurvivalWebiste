from project.server.config.dbconfig import pg_config
import psycopg2


class PistolDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'], pg_config['user'],
                                                                            pg_config['password'], pg_config['port'],
                                                                            pg_config['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def add_new_pistol(self, pistol_gripmodule, pistol_gripcolor, pistol_slidefinish, pistol_slidematerial,
                       firearm_id):
        cursor = self.conn.cursor()
        query = "insert into pistol (pistol_gripmodule, pistol_gripcolor, pistol_slidefinish, pistol_slidematerial," \
                "firearm_id) values (%s, %s, %s, %s, %s) returning pistol_id;"
        cursor.execute(query, (pistol_gripmodule, pistol_gripcolor, pistol_slidefinish, pistol_slidematerial,
                               firearm_id))
        pistol_id = cursor.fetchone()[0]
        self.conn.commit()
        return pistol_id

    def get_pistols(self):
        cursor = self.conn.cursor()
        query = "select * from equipment natural inner join firearm natural inner join pistol;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_pistol_by_id(self, pistol_id):
        cursor = self.conn.cursor()
        query = "select * from equipment natural inner join firearm natural inner join pistol where pistol_id = %s;"
        cursor.execute(query, (pistol_id,))
        result = cursor.fetchone()
        return result

    def delete_pistol(self, pistol_id):
        cursor = self.conn.cursor()
        query = "select firearm_id from pistol where pistol_id = %s;"
        cursor.execute(query, (pistol_id,))
        firearm_id = cursor.fetchone()
        query = "delete from pistol where pistol_id = %s;"
        cursor.execute(query, (pistol_id,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        if affected_rows == 0:
            return False
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        else:
            return firearm_id
