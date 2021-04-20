from flask import jsonify
from project.server.model.pistol import PistolDAO


class Pistol:
    @staticmethod
    def build_map_dict(row):
        result = {'equipment_id': row[0], 'equipment_price': row[1], 'equipment_manufacturer': row[2],
                  'equipment_model': row[3], 'equipment_overallLength': row[4], 'equipment_overallWidth': row[5],
                  'equipment_height': row[6], 'equipment_weight': row[7], 'firearm_id': row[8],
                  'firearm_caliber': row[9], 'firearm_optic': row[10], 'firearm_magazinecapacity': row[11],
                  'firearm_threadedbarrel': row[12], 'firearm_barrelLength': row[13], 'firearm_accessoryrail': row[14],
                  'firearm_triggeraction': row[15], 'firearm_triggertype': row[16], 'firearm_barrelmaterial': row[17],
                  'firearm_framefinish': row[18], 'firearm_framematerial': row[19], 'firearm_magazinetype': row[20],
                  'firearm_actiontype': row[21], 'pistol_id': row[22], 'pistol_gripmodule': row[23],
                  'pistol_gripcolor': row[24], 'pistol_slidefinish': row[25], 'pistol_slidematerial': row[26]}
        return result

    @staticmethod
    def build_attr_dict(pistol_id, pistol_gripmodule, pistol_gripcolor, pistol_slidefinish, pistol_slidematerial,
                        firearm_id):
        result = {'pistol_id': pistol_id, 'pistol_gripmodule': pistol_gripmodule, 'pistol_gripcolor': pistol_gripcolor,
                  'pistol_slidefinish': pistol_slidefinish, 'pistol_slidematerial': pistol_slidematerial,
                  'firearm_id': firearm_id}
        return result

    def add_new_pistol(self, json, firearm_id):
        pistol_gripmodule = json['pistol_gripmodule']
        pistol_gripcolor = json['pistol_gripcolor']
        pistol_slidefinish = json['pistol_slidefinish']
        pistol_slidematerial = json['pistol_slidematerial']
        dao = PistolDAO()
        pistol_id = dao.add_new_pistol(pistol_gripmodule, pistol_gripcolor, pistol_slidefinish, pistol_slidematerial,
                                       firearm_id)
        result = self.build_attr_dict(pistol_id, pistol_gripmodule, pistol_gripcolor, pistol_slidefinish,
                                      pistol_slidematerial, firearm_id)
        return jsonify(result), 201

    def get_pistols(self):
        dao = PistolDAO()
        pistol_list = dao.get_pistols()
        result_list = []
        for row in pistol_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def get_pistol_by_id(self, pistol_id):
        dao = PistolDAO()
        part_tuple = dao.get_pistol_by_id(pistol_id)
        if not part_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(part_tuple)
            return jsonify(result), 200

    @staticmethod
    def delete_pistol(pistol_id):
        dao = PistolDAO()
        result = dao.delete_pistol(pistol_id)
        if not result:
            return jsonify("NOT FOUND"), 404
        else:
            return jsonify(result), 200
