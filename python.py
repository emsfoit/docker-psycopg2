#!/usr/bin/python3
import psycopg2


def print_employers_table(cur):
    postgreSQL_select_Query = "select * from employers"
    cur.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    records = cur.fetchall()
    print("Print each row and it's columns values", len(records))
    for row in records:
        print(
            "id = ",
            row[0],
        )
        print("Name = ", row[1])


def delete_employer(cur, id):
    cur.execute("DELETE FROM employers WHERE id = %s", (id,))


def delete_all_employers(conn, cur):
    postgreSQL_select_Query = "select * from employers"
    cur.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    records = cur.fetchall()
    for row in records:
        delete_employer(cur, row[0])


def insert_employer(conn, cur, name):
    sql = """INSERT INTO employers(name)
              VALUES(%s) RETURNING id;"""
    cur.execute(sql, (name,))
    conn.commit()


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS employers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
    )
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname="db",
            user="postgres",
            host="postgres",
            password="password",
            port="5432",
        )
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        print("TABLES HAS BEEN CREATED")

        # Insert a new record
        insert_employer(conn, cur, "MOE")
        # print employers
        print_employers_table(cur)
        # Delete Records
        delete_employer(cur, 1)
        # print employers
        print_employers_table(cur)

        # Delete all
        delete_all_employers(conn, cur)
        # print employers
        print_employers_table(cur)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("we have an error here")
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("we are done")


if __name__ == "__main__":
    create_tables()