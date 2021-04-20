from flask import jsonify
from project.server.model.firearm import FirearmDAO


class Firearm:
    @staticmethod
    def build_map_dict(row):
        result = {'firearm_id': row[1], 'firearm_caliber': row[2], 'firearm_optic': row[3],
                  'firearm_magazinecapacity': row[4], 'firearm_threadedbarrel': row[5], 'firearm_barrellength': row[6],
                  'firearm_accessoryrail': row[7], 'firearm_triggeraction': row[8], 'firearm_triggertype': row[9],
                  'firearm_barrelmaterial': row[10], 'firearm_framefinish': row[11], 'firearm_framematerial': row[12],
                  'firearm_magazinetype': row[13], 'firearm_actiontype': row[14]}
        return result

    @staticmethod
    def build_attr_dict(firearm_id, firearm_caliber, firearm_optic, firearm_magazinecapacity,
                        firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail,
                        firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial,
                        firearm_framefinish, firearm_framematerial, firearm_magazinetype,
                        firearm_actiontype, equipment_id):
        result = {'firearm_id': firearm_id, 'firearm_caliber': firearm_caliber, 'firearm_optic': firearm_optic,
                  'firearm_magazinecapacity': firearm_magazinecapacity,
                  'firearm_threadedbarrel': firearm_threadedbarrel, 'firearm_barrellength': firearm_barrellength,
                  'firearm_accessoryrail': firearm_accessoryrail, 'firearm_triggeraction': firearm_triggeraction,
                  'firearm_triggertype': firearm_triggertype, 'firearm_barrelmaterial': firearm_barrelmaterial,
                  'firearm_framefinish': firearm_framefinish, 'firearm_framematerial': firearm_framematerial,
                  'firearm_magazinetype': firearm_magazinetype, 'firearm_actiontype': firearm_actiontype,
                  'equipment_id': equipment_id}
        return result

    def add_new_firearm(self, json, equipment_id):
        firearm_caliber = json['firearm_caliber']
        firearm_optic = json['firearm_optic']
        firearm_magazinecapacity = json['firearm_magazinecapacity']
        firearm_threadedbarrel = json['firearm_threadedbarrel']
        firearm_barrellength = json['firearm_barrellength']
        firearm_accessoryrail = json['firearm_accessoryrail']
        firearm_triggeraction = json['firearm_triggeraction']
        firearm_triggertype = json['firearm_triggertype']
        firearm_barrelmaterial = json['firearm_barrelmaterial']
        firearm_framefinish = json['firearm_framefinish']
        firearm_framematerial = json['firearm_framematerial']
        firearm_magazinetype = json['firearm_magazinetype']
        firearm_actiontype = json['firearm_actiontype']
        dao = FirearmDAO()
        firearm_id = dao.add_new_firearm(firearm_caliber, firearm_optic, firearm_magazinecapacity,
                                         firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail,
                                         firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial,
                                         firearm_framefinish, firearm_framematerial, firearm_magazinetype,
                                         firearm_actiontype, equipment_id)
        result = self.build_attr_dict(firearm_id, firearm_caliber, firearm_optic, firearm_magazinecapacity,
                                      firearm_threadedbarrel, firearm_barrellength, firearm_accessoryrail,
                                      firearm_triggeraction, firearm_triggertype, firearm_barrelmaterial,
                                      firearm_framefinish, firearm_framematerial, firearm_magazinetype,
                                      firearm_actiontype, equipment_id)
        return jsonify(result), 201

    def get_likes_by_id(self, m_id):
        dao = FirearmDAO()
        part_tuple = dao.get_likes_by_id(m_id)
        if not part_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(part_tuple)
            return jsonify(result), 200

    def get_equipment(self):
        dao = FirearmDAO()
        equipment_list = dao.get_equipment()
        result_list = []
        for row in equipment_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    @staticmethod
    def delete_firearm(firearm_id):
        dao = FirearmDAO()
        result = dao.delete_like(firearm_id)
        if not result:
            return jsonify("NOT FOUND"), 404
        else:
            return jsonify(result), 200
