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
    def get_by_player_id(cls, ID):
        res = d_service.get_by_prefix("hw1_3", "player", "idPlayer", ID)
        return res

    @classmethod
    def get_by_name(cls, name):
        res = d_service.get_by_prefix("hw1_3", "player", "Name", name)
        return res

    @classmethod
    def get_by_nationality(cls, nationality):
        res = d_service.get_by_prefix("hw1_3", "player", "Nationality", nationality)
        return res

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        res = d_service.get_by_prefix("hw1_3", "player",
                                      "name", name_prefix)
        return res

    @classmethod
    def delete_by_player_id(cls, id):
        res = d_service.delete_by_template("hw1_3", "player", "idPlayer", id)
        return res

    @classmethod
    def add_player(cls, id, name, nationality, idClub):
        res = d_service.add_by_prefix("hw1_3", "player", id, name, nationality, idClub)
        print(res)
        return res

    @classmethod
    def select_club_by_player_id(cls, id):
        res = d_service.select_attribute2_by_attribute1("hw1_3", "player", "Club", "idPlayer", "name", "idClub", "idClub",
                                                        id)
        return res

    @classmethod
    def update_by_player_id(cls, id, name):
        print("id", id)
        res = d_service.update_by_template("hw1_3", "player", "playerID", id, "Name", name)
        return res


