def menu():
    command = [
        ["+<amount>", "INCOME"],
        ["-<amount>", "EXPENSE"],
        ["T or t", "TOTAL"],
        ["H or h", "HISTORY"],
    ]
    contents = []
    for command_item in command:
        contents.append(
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": command_item[0],
                        "size": "lg",
                        "color": "#555555",
                    },
                    {
                        "type": "text",
                        "text": command_item[1],
                        "size": "lg",
                        "color": "#111111",
                        "align": "end",
                    },
                ],
            }
        )

    return ["Menu", contents]
