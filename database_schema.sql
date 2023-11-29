--Define PostgresSQL tables below
--project gym workoouts which details my workouts


--#tables needed: Exercises, workouts & performancemetrics


CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL,
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE activities (
    activity_id SERIAL PRIMARY KEY,
    activity_name VARCHAR(100) NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE workouts (
    workout_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    workout_date DATE NOT NULL,
    workout_type VARCHAR(50),
    duration_minutes INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE performance_metrics (
    metric_id SERIAL PRIMARY KEY,
    workout_id INT NOT NULL,
    activity_id INT NOT NULL,
    sets INT,
    reps INT,
    weight DECIMAL,
    duration INT,
    distance DECIMAL,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id)
);

CREATE TABLE progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    date DATE NOT NULL,
    metric VARCHAR(255) NOT NULL,
    value DECIMAL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);