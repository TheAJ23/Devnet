#python script for data manipluation#
#psycopg2 is a PostgreSQL adapter for Python. if wasn't postgresql use pyodbc instead

import psycopg2
from psycopg2 import sql

#Define function to connect to POSTSQL database - template below

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="psqldb", 
            user="theaj23", 
            password="DDcupcake1805", 
            host="localhost"
        )
        return conn
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    
#Functions below   
#Function to Insert Data into users Table: 
def insert_user(conn, username, email, join_date, age, gender):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (username, email, join_date, age, gender) VALUES (%s, %s, %s, %s, %s)",
                    (username, email, join_date, age, gender))
        conn.commit()

#Function to Insert Data into activities Table:
def insert_activity(conn, activity_name, activity_type, description):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO activities (activity_name, activity_type, description) VALUES (%s, %s, %s)",
                    (activity_name, activity_type, description))
        conn.commit()
#Function to Insert Data into workouts Table:
def insert_workout(conn, user_id, workout_date, workout_type, duration_minutes):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO workouts (user_id, workout_date, workout_type, duration_minutes) VALUES (%s, %s, %s, %s)",
                    (user_id, workout_date, workout_type, duration_minutes))
        conn.commit()

#Function to Insert Data into performance_metrics Table:
def insert_performance_metric(conn, workout_id, activity_id, sets, reps, weight, duration, distance):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO performance_metrics (workout_id, activity_id, sets, reps, weight, duration, distance) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (workout_id, activity_id, sets, reps, weight, duration, distance))
        conn.commit()

#Function to Insert Data into progress Table:
def insert_progress(conn, user_id, date, metric, value):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO progress (user_id, date, metric, value) VALUES (%s, %s, %s, %s)",
                    (user_id, date, metric, value))
        conn.commit()

def main():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return
    else:
        print("Database connection established.")


    # Example data insertion
    insert_user(conn, 'Alice', 'alice@email.com', '2023-01-01', 30, 'Female')
    insert_user(conn, 'Bob', 'bob@email.com', '2023-01-02', 28, 'Male')
    insert_user(conn, 'Charlie', 'charlie@email.com', '2023-01-03', 35, 'Other')

    insert_activity(conn, 'Running', 'Cardio', 'Outdoor or treadmill running')
    insert_activity(conn, 'Swimming', 'Cardio', 'Pool or open water swimming')
    insert_activity(conn, 'Cycling', 'Cardio', 'Road or stationary cycling')

    insert_workout(conn, 1, '2023-02-01', 'Running', 60)
    insert_workout(conn, 2, '2023-02-02', 'Swimming', 30)
    insert_workout(conn, 3, '2023-02-03', 'Cycling', 45)

    insert_performance_metric(conn, 1, 1, 3, 10, 100, None, None)  # Running
    insert_performance_metric(conn, 2, 2, None, None, None, 30, 500)  # Swimming
    insert_performance_metric(conn, 3, 3, None, None, None, 45, 20)  # Cycling

    insert_progress(conn, 1, '2023-02-01', 'Weight', 150)
    insert_progress(conn, 2, '2023-02-02', 'Body Fat', 20)
    insert_progress(conn, 3, '2023-02-03', 'Muscle Mass', 45)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
