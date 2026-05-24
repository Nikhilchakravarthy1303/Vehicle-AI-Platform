import sqlite3
import os

DATABASE_PATH = os.getenv("DATABASE_PATH", "Vehicle_Incidents.db")


def init_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS incidents (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            vehicle TEXT,
                            issue TEXT,
                            category TEXT,
                            severity TEXT,
                            status TEXT,
                            action TEXT)''')
        conn.commit()
        conn.close()
    except Exception as e:
        raise e



def get_incidents_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM incidents")
        rows = cursor.fetchall()
        incidents = []
        for row in rows:
            incident = {
                "id": row[0],
                "vehicle": row[1],
                "issue": row[2],
                "category": row[3],
                "severity": row[4],
                "status": row[5],
                "action": row[6]
            }
            incidents.append(incident)
        conn.close()
        return incidents
    except Exception as e:
        raise e



def create_incident_db(incident_data):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''Insert into incidents ( vehicle, issue, category, severity, status, action) values ( ?, ?, ?, ?, ?, ?)''',( incident_data["vehicle"], incident_data["issue"], incident_data["category"], incident_data["severity"], incident_data["status"], incident_data["action"]))
        conn.commit()
        incident_id = cursor.lastrowid
        conn.close()
        return incident_id
    except Exception as e:
        raise e



def get_incident_by_id_db(id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM incidents WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            incident = {
                "id": row[0],
                "vehicle": row[1],
                "issue": row[2],
                "category": row[3],
                "severity": row[4],
                "status": row[5],
                "action": row[6]
            }
            return [incident]
        else:
            return []
    except Exception as e:
        raise e



def update_incident_id_db(id, data):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''UPDATE incidents SET status=?, action=? WHERE id=?''', (data["status"], data["action"], id))
        conn.commit()
        conn.close()
        return {"message": "Incident updated successfully"}
    except Exception as e:
        raise e




def delete_incident_id_db(id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM incidents WHERE id=?''', (id,))
        conn.commit()
        conn.close()
        return {"message": "Incident deleted successfully"}
    except Exception as e:
        raise e