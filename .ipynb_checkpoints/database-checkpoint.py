import pymysql

def save_to_db(name,skills,role,score):
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="resume_db"
    )

    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        skills TEXT,
        role VARCHAR(50),
        score FLOAT
    )
    """)

    cur.execute(
        "INSERT INTO candidates (name, skills, role, score) VALUES (%s,%s,%s,%s)",
        (name, ",".join(skills), role, score)
    )

    conn.commit()
    conn.close()
    

    