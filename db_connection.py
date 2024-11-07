
# db_connection.py - Database Connection and Basic Scanning

import mysql.connector
import psycopg2
import json

# Load configuration (database details)
with open("config.json", "r") as config_file:
    config = json.load(config_file)

def connect_mysql():
    try:
        conn = mysql.connector.connect(
            host=config["mysql"]["host"],
            user=config["mysql"]["user"],
            password=config["mysql"]["password"],
            database=config["mysql"]["database"]
        )
        print("[INFO] Connected to MySQL database.")
        return conn
    except mysql.connector.Error as e:
        print(f"[ERROR] MySQL connection error: {e}")
        return None

def connect_postgresql():
    try:
        conn = psycopg2.connect(
            host=config["postgresql"]["host"],
            user=config["postgresql"]["user"],
            password=config["postgresql"]["password"],
            dbname=config["postgresql"]["database"]
        )
        print("[INFO] Connected to PostgreSQL database.")
        return conn
    except psycopg2.Error as e:
        print(f"[ERROR] PostgreSQL connection error: {e}")
        return None
