import database_services.RDBService as db_service


def t1():

    res = db_service.get_by_prefix(
        "imdbfixed", "names_basic", "primary_name", "Tom H"
    )
    print("t1 resule = ", res)


def t2():

    res = db_service.find_by_template(
        "imdbfixed", "name_basics", {"primaryName": "Tom Hanks"}, None
    )
    print("t2 resuls = ", res)



t2()


