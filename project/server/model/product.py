from project.server.config.dbconfig import pg_config
import psycopg2


class ProductDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'], pg_config['user'],
                                                                            pg_config['password'], pg_config['port'],
                                                                            pg_config['host'])
        print("connection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def add_new_product(self, product_name, product_price, product_stock, product_description):
        cursor = self.conn.cursor()
        query = "insert into product (product_name, product_price, product_stock,"\
                                        "product_description) values (%s, %s, %s, %s) returning product_id;"
        cursor.execute(query, (product_name, product_price, product_stock, product_description))
        product_id = cursor.fetchone()[0]
        self.conn.commit()
        return product_id

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        query = "select * from product where product_id = %s;"
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        return result

    def get_product_price_by_id(self, product_id):
        cursor = self.conn.cursor()
        query = "select product_price from product where product_id = %s;"
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        return result

    def get_product(self):
        cursor = self.conn.cursor()
        query = "select * from product;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        query = "delete from product where product_id = %s;"
        cursor.execute(query, (product_id,))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows != 0
