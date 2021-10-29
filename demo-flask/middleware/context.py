
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)
    db_user = os.environ.get("DBUSER", None)
    db_password = os.environ.get("DBPASSWORD", None)

    if db_host is not None:
        db_info = {
            "host": db_host,
            "user": db_user,
            "password": db_password,
            "cursorclass": pymysql.cursors.DictCursor
        }
    else:
        db_info = {
            "host": "coms6156-tbd.c9mn8aa0ohwq.us-east-2.rds.amazonaws.com",
            "user": "admin",
            "password": "Ly121302!",
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
