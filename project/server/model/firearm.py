from project.server.config.dbconfig import pg_config
import psycopg2


class FirearmDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'], pg_config['user'],
                                                                            pg_config['password'], pg_config['port'],
                                                                            pg_config['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def add_new_firearm(self, firearm_caliber, firearm_optic, firearm_magazinecapacity,
                        firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail,
                        firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial,
                        firearm_framefinish, firearm_framematerial, firearm_magazinetype,
                        firearm_actiontype, equipment_id):
        cursor = self.conn.cursor()
        query = "insert into firearm (firearm_caliber, firearm_optic, firearm_magazinecapacity," \
                "firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail," \
                "firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial," \
                "firearm_framefinish, firearm_framematerial, firearm_magazinetype," \
                "firearm_actiontype, equipment_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" \
                "returning firearm_id;"
        cursor.execute(query, (firearm_caliber, firearm_optic, firearm_magazinecapacity,
                               firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail,
                               firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial,
                               firearm_framefinish, firearm_framematerial, firearm_magazinetype,
                               firearm_actiontype, equipment_id))
        firearm_id = cursor.fetchone()[0]
        self.conn.commit()
        return firearm_id

    def get_likes_by_id(self, m_id):
        cursor = self.conn.cursor()
        query = "select m_id, u_id, like_date, like_id from \"like\" where m_id = %s;"
        cursor.execute(query, (m_id,))
        result = cursor.fetchone()
        return result

    def get_equipment(self):
        cursor = self.conn.cursor()
        query = "select * from equipment natural inner join firearm;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete_firearm(self, firearm_id):
        cursor = self.conn.cursor()
        query = "select equipment_id from firearm where firearm_id = %s;"
        cursor.execute(query, (firearm_id,))
        equipment_id = cursor.fetchone()
        query = "delete from firearm where firearm_id = %s;"
        cursor.execute(query, (firearm_id,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        if affected_rows == 0:
            return False
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        else:
            return equipment_id
