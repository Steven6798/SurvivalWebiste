from project.server.config.dbconfig import pg_config
import psycopg2


class EquipmentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'], pg_config['user'],
                                                                            pg_config['password'], pg_config['port'],
                                                                            pg_config['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def add_new_equipment(self, equipment_price, equipment_manufacturer, equipment_model,
                                        equipment_overalllength, equipment_overallwidth, equipment_height,
                                        equipment_weight):
        cursor = self.conn.cursor()
        query = "insert into equipment (equipment_price, equipment_manufacturer, equipment_model,"\
                                        "equipment_overallLength, equipment_overallWidth, equipment_height,"\
                                        "equipment_weight) values (%s, %s, %s, %s, %s, %s, %s) returning equipment_id;"
        cursor.execute(query, (equipment_price, equipment_manufacturer, equipment_model, equipment_overalllength,
                                        equipment_overallwidth, equipment_height, equipment_weight))
        equipment_id = cursor.fetchone()[0]
        self.conn.commit()
        return equipment_id

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

    def delete_equipment(self, equipment_id):
        cursor = self.conn.cursor()
        query = "delete from equipment where equipment_id = %s;"
        cursor.execute(query, (equipment_id,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0
