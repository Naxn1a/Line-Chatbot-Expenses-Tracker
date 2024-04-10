from src.database import db
from datetime import datetime

from src.command.total import total as tt


def history():
    conn = db.connected()
    cursor = conn.cursor()

    query = "SELECT amount, time  FROM 'Tracker' ORDER BY time DESC LIMIT 10"
    cursor.execute(query)
    result = cursor.fetchall()
    contents = []
    for result_item in result:
        if result_item[0] > 0.0:
            color = "#58D68D"
        elif result_item[0] < 0.0:
            color = "#EC7063"
        time = datetime.strptime(result_item[1], "%d-%m-%Y %H:%M:%S.%f")
        time = time.strftime("%d/%m/%y %H:%M:%S")
        contents.append(
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": time,
                        "size": "sm",
                        "weight": "bold",
                        "color": "#1e1e1e",
                    },
                    {
                        "type": "text",
                        "text": str(result_item[0]),
                        "size": "sm",
                        "weight": "bold",
                        "color": color,
                        "align": "end",
                    },
                ],
            }
        )

    total = tt()[2]
    contents.append(
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": "Total",
                    "size": "lg",
                    "weight": "bold",
                    "color": "#FFAF45",
                },
                {
                    "type": "text",
                    "text": str(total),
                    "size": "lg",
                    "weight": "bold",
                    "color": "#5356FF",
                    "align": "end",
                },
            ],
        }
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ["History", contents]
