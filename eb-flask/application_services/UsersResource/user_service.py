from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template):
        res = d_service.find_by_template("aaaaF21", "users",
                                       template, None)
        return res
    #
    # @classmethod
    # def get_by_name_prefix(cls, name_prefix):
    #     res = d_service.get_by_prefix("cc6156_TBD", "users",
    #                                      "first_name", name_prefix)
    #     return res
    @classmethod
    def get_by_lastname(cls, nameLast):
        res= d_service.get_by_prefix(("hw1", "User","nameLast", nameLast))
        return  res
    @classmethod
    def get_by_user_id(cls,ID):
        res= d_service.get_by_prefix("hw1", "User", "ID",  ID)
        return res
    @classmethod
    def add_user(cls, ID, nameFirst, nameLast, email, addressID):
        print("123")
        res= d_service.add_by_prefix("hw1", "User",ID, nameFirst, nameLast, email, addressID)
        print(res)
        return res

    @classmethod
    def put_by_user_template(cls, template, id,email):
        res = d_service.put_by_template("hw1", "User", template,
                                        id, email)
        return res

    @classmethod
    def delete_by_user_id(cls, id):
        print('hh', id)
        res = d_service.delete_by_template("hw1", "User",
                                         "ID", id)
        return res

    @classmethod
    def select_adress_by_user_id(cls, id):
        res = d_service.select_attibute2_by_attribute1("hw1", "User", "Address", "ID", "postalCode", "addressID", "ID",
                                           id)
        return res

    @classmethod
    def update_by_user_id(cls, id, email):
        print("id", id)
        res = d_service.update_by_template("hw1", "User", "ID", id, "email", email)
        return res
