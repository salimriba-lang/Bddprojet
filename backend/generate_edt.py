from backend.db_connect import get_connection
from datetime import datetime, timedelta
import random

def generate_exam_schedule():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM examens")
    conn.commit()

    cur.execute("SELECT id FROM modules")
    modules = cur.fetchall()

    cur.execute("SELECT id FROM salles")
    salles = cur.fetchall()

    start_date = datetime(2026, 1, 20)

    for m in modules:
        salle_id = random.choice(salles)[0]
        cur.execute(
            "INSERT INTO examens(module_id, salle_id, date_exam) VALUES (%s,%s,%s)",
            (m[0], salle_id, start_date.date())
        )

        start_date += timedelta(days=1)
        if start_date.weekday() == 4:
            start_date += timedelta(days=1)

    conn.commit()
    cur.close()
    conn.close()
    print("EDT généré (MySQL)")
