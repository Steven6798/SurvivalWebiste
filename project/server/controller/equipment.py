from flask import jsonify
from project.server.model.equipment import EquipmentDAO


class Equipment:
    @staticmethod
    def build_map_dict(row):
        result = {'equipment_id': row[0], 'equipment_price': row[1], 'equipment_manufacturer': row[2],
                  'equipment_model': row[3], 'equipment_overalllength': row[4], 'equipment_overallWidth': row[5],
                  'equipment_height': row[6], 'equipment_weight': row[7]}
        return result

    @staticmethod
    def build_attr_dict(equipment_id, equipment_price, equipment_manufacturer, equipment_model,
                        equipment_overalllength, equipment_overallwidth, equipment_height,
                        equipment_weight):
        result = {'equipment_id': equipment_id, 'equipment_price': equipment_price,
                  'equipment_manufacturer': equipment_manufacturer, 'equipment_model': equipment_model,
                  'equipment_overallLength': equipment_overalllength, 'equipment_overallwidth': equipment_overallwidth,
                  'equipment_height': equipment_height, 'equipment_weight': equipment_weight}
        return result

    def add_new_equipment(self, json):
        equipment_price = json['equipment_price']
        equipment_manufacturer = json['equipment_manufacturer']
        equipment_model = json['equipment_model']
        equipment_overalllength = json['equipment_overalllength']
        equipment_overallwidth = json['equipment_overallwidth']
        equipment_height = json['equipment_height']
        equipment_weight = json['equipment_weight']
        dao = EquipmentDAO()
        equipment_id = dao.add_new_equipment(equipment_price, equipment_manufacturer, equipment_model,
                                        equipment_overalllength, equipment_overallwidth, equipment_height,
                                        equipment_weight)
        result = self.build_attr_dict(equipment_id, equipment_price, equipment_manufacturer, equipment_model,
                                        equipment_overalllength, equipment_overallwidth, equipment_height,
                                        equipment_weight)
        return jsonify(result), 201

    def get_likes_by_id(self, m_id):
        dao = EquipmentDAO()
        part_tuple = dao.get_likes_by_id(m_id)
        if not part_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(part_tuple)
            return jsonify(result), 200

    def get_equipment(self):
        dao = EquipmentDAO()
        equipment_list = dao.get_equipment()
        result_list = []
        for row in equipment_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    @staticmethod
    def delete_like(m_id):
        dao = EquipmentDAO()
        result = dao.delete_like(m_id)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
