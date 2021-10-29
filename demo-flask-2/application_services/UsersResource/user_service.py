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
    def get_by_professor_id(cls,ID):
        res= d_service.get_by_prefix("hw1_2", "Professors", "ID",  ID)
        return res

    @classmethod
    def add_professor(cls, ID, nameFirst, nameLast, email, salary):
        print("123")
        res= d_service.add_by_prefix("hw1_2", "Professors",ID, nameFirst, nameLast, email, salary)
        print(res)
        return res

    @classmethod
    def put_by_user_template(cls, template, id,email):
        res = d_service.put_by_template("hw1", "User", template,
                                        id, email)
        return res

    @classmethod
    def delete_professor_by_ID(cls, id):
        res = d_service.delete_by_template("hw1_2", "Professors",
                                         "ID", id)
        return res

    @classmethod
    def update_salary_by_student_ID(cls, id, salary):
        res = d_service.update_attibute2_by_attribute1("hw1_2", "Students", "Professors", "id", "salary", "professor_id", "ID",
                                           id, salary)
        return res

    @classmethod
    def update_by_professor_id(cls, id, email):
        print("id", id)
        res = d_service.update_by_template("hw1_2", "Professors", "ID", id, "email", email)
        return res
