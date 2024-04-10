from src.database import db


def total():
    conn = db.connected()
    cursor = conn.cursor()

    query = "SELECT SUM(amount) FROM 'Tracker'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    if result == None:
        result = 0
    contents = [
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": str(result),
                    "size": "xl",
                    "weight": "bold",
                    "color": "#5356FF",
                    "align": "end",
                }
            ],
        }
    ]

    conn.commit()
    cursor.close()
    conn.close()
    return ["Total", contents, result]
