from flask import jsonify
from project.server.model.product import ProductDAO


class Product:
    @staticmethod
    def build_map_dict(row):
        result = {'product_id': row[0], 'product_name': row[1], 'product_price': row[2],
                  'product_stock': row[3], 'product_description': row[4]}
        return result

    @staticmethod
    def build_attr_dict(product_id, product_name, product_price, product_stock, product_description):
        result = {'product_id': product_id, 'product_name': product_name,
                  'product_price': product_price, 'product_stock': product_stock,
                  'product_description': product_description}
        return result

    @staticmethod
    def build_attr_dict_price(product_price):
        result = {'product_price': product_price}
        return result

    def add_new_product(self, json):
        product_name = json['product_name']
        product_price = json['product_price']
        product_stock = json['product_stock']
        product_description = json['product_description']
        dao = ProductDAO()
        product_id = dao.add_new_product(product_name, product_price, product_stock, product_description)
        result = self.build_attr_dict(product_id, product_name, product_price, product_stock, product_description)
        return jsonify(result), 201

    def get_product_by_id(self, product_id):
        dao = ProductDAO()
        part_tuple = dao.get_product_by_id(product_id)
        if not part_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(part_tuple)
            return jsonify(result), 200

    def get_product_price_by_id(self, product_id):
        dao = ProductDAO()
        product_price = dao.get_product_price_by_id(product_id)
        result = self.build_attr_dict_price(product_price)
        return jsonify(result)

    def get_product(self):
        dao = ProductDAO()
        product_list = dao.get_product()
        result_list = []
        for row in product_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    @staticmethod
    def delete_product(product_id):
        dao = ProductDAO()
        result = dao.delete_product(product_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
