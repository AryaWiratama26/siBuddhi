import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
USER_DB = os.getenv("USER_DB")
PASS_DB = os.getenv("PASS_DB")
DB_NAME = os.getenv("DB_NAME")

DB = {
    "host": "localhost",
    "user" : USER_DB,
    "password" : PASS_DB, 
    "database" : DB_NAME,
}


def get_con():
    return mysql.connector.connect(**DB)

def add_questions(question, response):
    conn = get_con()
    cursor = conn.cursor()
    query = "INSERT INTO questions (question, response) VALUES (%s, %s)"
    cursor.execute(query, (question, response))
    conn.commit()
    cursor.close()
    conn.close()
    
def get_all_questions():
    conn = get_con()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data
    
    
