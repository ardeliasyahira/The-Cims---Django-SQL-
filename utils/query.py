from django.db import DatabaseError, IntegrityError, transaction
from collections import namedtuple
import psycopg2
from psycopg2 import Error

from psycopg2.extras import RealDictCursor

try:
    # Connect to an existing database

    connection = psycopg2.connect(user="arbssegqzgsvto",
                        password="22bff49c056336a635b02e0a94d8f0ba0add32023b5ba74f054c8b7987ad2728",
                        host="ec2-54-172-175-251.compute-1.amazonaws.com",
                        port="5432",
                        database="d8lkmntmudsje8")

    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()

        
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)


def map_cursor(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]



def query(query_str: str, is_list = False):
    hasil = []
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SET SEARCH_PATH TO THECIMS")

        try:
            cursor.execute(query_str)

            if query_str.strip().lower().startswith("select"):
                print(hasil)
                hasil = cursor.fetchall()
                if len(hasil) > 1 or is_list :
                    hasil = [dict(row) for row in hasil]
                elif len(hasil) == 1:
                    hasil = dict(hasil[0])
                else :
                    hasil = [dict(row) for row in hasil]
                
            else:
                hasil = cursor.rowcount
                connection.commit()
        except Exception as e:
            hasil = e
            transaction.rollback()

    return hasil