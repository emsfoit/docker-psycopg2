#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import the connect library from psycopg2
from psycopg2 import connect

# declare connection instance
try:
    conn = connect(
        dbname="db", user="postgres", host="postgres", password="password", port="5432"
    )
    print("Database connected successfully")
except Exception as e:
    print(f"we are here: {e}")
    print("----------\nDatabase not connected Volkan\n----------------------")
