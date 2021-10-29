import pymysql
import json
import logging

import middleware.context as context

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _get_db_connection():

    db_connect_info = context.get_db_info()

    logger.info("RDBService._get_db_connection:")
    logger.info("\t HOST = " + db_connect_info['host'])

    db_info = context.get_db_info()
    db_connection = pymysql.connect(
       **db_info
    )
    return db_connection


def get_by_prefix(db_schema, table_name, column_name, value_prefix):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "select * from " + db_schema + "." + table_name + " where " + \
        column_name + " like " + "'" + value_prefix + "%'"
    print("SQL Statement = " + cur.mogrify(sql, None))

    res = cur.execute(sql)
    res = cur.fetchall()

    conn.close()

    return res


def _get_where_clause_args(template):

    terms = []
    args = []
    clause = None

    if template is None or template == {}:
        clause = ""
        args = None
    else:
        for k,v in template.items():
            terms.append(k + "=%s")
            args.append(v)

        clause = " where " +  " AND ".join(terms)


    return clause, args


def find_by_template(db_schema, table_name, template, field_list):

    wc,args = _get_where_clause_args(template)

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "select * from " + db_schema + "." + table_name + " " + wc
    res = cur.execute(sql, args=args)
    res = cur.fetchall()

    conn.close()

    return res


# def put_by_template(db_schema, table_name, template, id, name, field_list):
#     print(id, name)
#     wc, args = _get_where_clause_args(template)
#
#     conn = _get_db_connection()
#     cur = conn.cursor()
#
#     table = db_schema + "." + table_name
#     # sql = "update " + table + " set Name=" + name + " " + "where idPlayer=" + id + " " + wc
#     sql = f"UPDATE {table} SET Name='{name}' WHERE idPlayer={id}" + " " + wc
#     print(sql)
#     res = cur.execute(sql, args=args)
#     res = cur.fetchall()
#
#     conn.commit()
#     conn.close()
#
#     return res


def delete_by_template(db_schema, table_name, column_name, value_prefix):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "delete from " + db_schema + "." + table_name + " where " + \
        column_name + " = " + value_prefix
    print("SQL Statement = " + cur.mogrify(sql, None))

    res = cur.execute(sql)
    print(res)
    res = cur.fetchall()
    conn.commit()


def add_by_prefix(db_schema, table_name, id, name, nationality, idClub):
    print("1111")
    conn = _get_db_connection()
    cur = conn.cursor()

    sql = " INSERT INTO " + db_schema + "." + table_name +\
          "(`idPlayer`, `Name`, `Nationality`, `idClub`)" +\
        " VALUES(" + ' ' + id + ', "' + name + '" ,"' + nationality + '", ' + \
          idClub + ');'
    print(sql)

    print("SQL Statement = " + cur.mogrify(sql, None))

    res = cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    print(res)
    conn.close()

    return res


def select_attribute2_by_attribute1(db_schema, table1, table2, attribute1, attribute2, reference1, reference2, id):
    conn = _get_db_connection()
    cur = conn.cursor()
    # attribute1: User.ID
    # attribute2: Address.postalCode
    # table1: User
    # table2: Address
    # reference1: User.addressID
    # reference2: address.ID
    sql = "select " + attribute2 + " from " + db_schema + "." + table2 + " where " + reference2 + " = (" \
    + " select " + reference1 + " from " + db_schema + "." + table1 + " where " + attribute1 + " = " + id + ")"
    print("SQL Statement = " + cur.mogrify(sql, None))

    res = cur.execute(sql)
    print(res)
    res = cur.fetchall()

    conn.close()
    return res


def update_by_template(db_schema, table_name, column_name, value_prefix, update_column, value_update):
    conn = _get_db_connection()
    cur = conn.cursor()
    print("2222")

    sql = "update " + db_schema + "." + table_name + \
          " set " + str(update_column) + " = '" + value_update + "' where " + column_name + ' = ' + value_prefix
    print("SQL Statement = " + cur.mogrify(sql, None))
    res = cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
