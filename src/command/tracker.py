import datetime
from src.database import db
from src.command.total import total as tt


def content(text, color, amount, total):
    return [
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": str(text),
                    "size": "lg",
                    "weight": "bold",
                    "color": str(color),
                },
                {
                    "type": "text",
                    "text": str(amount),
                    "size": "lg",
                    "weight": "bold",
                    "color": str(color),
                    "align": "end",
                },
            ],
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": "TOTAL",
                    "size": "lg",
                    "weight": "bold",
                    "color": "#FFAF45",
                },
                {
                    "type": "text",
                    "text": str(total),
                    "size": "lg",
                    "weight": "bold",
                    "color": "#111111",
                    "align": "end",
                },
            ],
        },
    ]


def contents_error(text):
    return [
        "Try again!",
        [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(text),
                        "size": "lg",
                        "weight": "bold",
                        "color": "#FFAF45",
                        "align": "end",
                    }
                ],
            }
        ],
    ]


def tracker(amount, type):
    conn = db.connected()
    cursor = conn.cursor()
    query = "INSERT INTO Tracker (amount, time) VALUES (?, ?)"
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")
    total = tt()[2]
    try:
        if (total + float(amount)) >= 0:
            if float(amount) != 0:
                if type == "+":
                    type_text = "INCOME"
                    color = "#58D68D"
                elif type == "-":
                    type_text = "EXPENSE"
                    color = "#EC7063"
                contents = content(
                    text=type_text,
                    color=color,
                    amount=amount,
                    total=total + float(amount),
                )
                data = (amount, timestamp)
                cursor.execute(query, data)
                conn.commit()
                cursor.close()
                conn.close()
                return ["Receipt", contents]
            else:
                return contents_error("Must not be equal to 0!!")
        else:
            return contents_error("The balance is not enough!!")
    except:
        return contents_error("Incorrect!!")
