from database_services.RDBService import RDBService


class UserRDBService(RDBService):

    def __init__(self):
        pass

    @classmethod
    def get_user_and_address(cls, template):

        wc, args = RDBService.get_where_clause_args(template)
        sql = "select * from aaaaF21.users left join aaaaF21.addresses on " + \
                "aaaaF21.primary_address_id = aaaaF21.addresses.id"

        res = RDBService.run_sql(sql, args, fetch=True)
        return res

