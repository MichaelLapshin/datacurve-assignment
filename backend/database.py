import mysql.connector

import config

class Database:
    def __init__(self):
        # Connect
        self.conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )

    def save_submission(self, submission: str):
        cursor = self.conn.cursor(prepared=True)
        cursor.execute(
            "INSERT INTO submissions (submission) VALUES (?)",
            (submission)
        )
        self.conn.commit()

    def save_run(self, submission_id: int, std_in: str, std_out: str, std_err: str, status_code: int):
        cursor = self.conn.cursor(prepared=True)
        cursor.execute(
            "INSERT INTO runs (submission_id, std_in, std_out, std_err, status_code) VALUES (?, ?, ?, ?, ?)",
            (submission_id, std_in, std_out, std_err, status_code)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
