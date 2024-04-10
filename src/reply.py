from src.config.config import *
import json
import requests


def reply(replyToken, title, contents):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(access_token),
    }
    data = json.dumps(
        {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "flex",
                    "altText": "Flex Message",
                    "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": title,
                                    "weight": "bold",
                                    "color": "#1e1e1e",
                                    "size": "xxl",
                                    "margin": "md",
                                },
                                {"type": "separator", "margin": "xxl"},
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "xxl",
                                    "spacing": "sm",
                                    "contents": contents,
                                },
                            ],
                        },
                    },
                }
            ],
        }
    )  # dict -> json object
    r = requests.post(line_api, headers=headers, data=data)
    return r.status_code
