import sqlite3

def init_db():
    # Simulate database initialization (e.g., creating tables)
    conn = sqlite3.connect("Vehicle_Incidents.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY,
            vehicle TEXT,
            issue TEXT,
            category TEXT,
            status TEXT,
            action TEXT
        )
    ''')
    conn.commit()
    conn.close()


def get_incidents_db():
        conn = sqlite3.connect("Vehicle_Incidents.db")
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
                "status": row[4],
                "action": row[5]
            }
            incidents.append(incident)
        return incidents 

def create_incident_db(incident_data):
    try:
        conn = sqlite3.connect("Vehicle_Incidents.db")
        cursor = conn.cursor()
        cursor.execute('''Insert into incidents ( vehicle, issue, category, status, action) values ( ?, ?, ?, ?, ?)''',( incident_data["vehicle"], incident_data["issue"], incident_data["category"], incident_data["status"], incident_data["action"]))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating incident: {e}")

def get_incident_by_id_db(id):
    try:
        conn = sqlite3.connect("Vehicle_Incidents.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM incidents WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            incident = {
                "id": row[0],
                "vehicle": row[1],
                "issue": row[2],
                "category": row[3],
                "status": row[4],
                "action": row[5]
            }
            return [incident]
        else:
            return []
    except Exception as e:
        print(f"Error fetching incident by ID: {e}")
        return []
    
def update_incident_id_db(id, data):
    try:
        conn = sqlite3.connect("Vehicle_Incidents.db")
        cursor = conn.cursor()
        cursor.execute('''UPDATE incidents SET status=?, action=? WHERE id=?''', (data["status"], data["action"], id))
        conn.commit()
        conn.close()
        return {"message": "Incident updated successfully"}
    except Exception as e:
        print(f"Error updating incident: {e}")

def delete_incident_id_db(id):
    try:
        conn = sqlite3.connect("Vehicle_Incidents.db")
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM incidents WHERE id=?''', (id,))
        conn.commit()
        conn.close()
        return {"message": "Incident deleted successfully"}
    except Exception as e:
        print(f"Error deleting incident: {e}")