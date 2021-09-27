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

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        res = d_service.get_by_prefix("cc6156_TBD", "users",
                                         "first_name", name_prefix)
        return res