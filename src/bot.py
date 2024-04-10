from src.reply import reply
from src.command import command


def bot(e):
    if e["message"]["type"] == "text":
        option = e["message"]["text"][0]
        if option == "+" or option == "-":
            contents = command.tracker(amount=e["message"]["text"], type=option)
        elif option.lower() == "t":
            contents = command.total()
        elif option.lower() == "h":
            contents = command.history()
        else:
            contents = command.menu()
    else:
        contents = command.menu()

    reply(replyToken=e["replyToken"], title=contents[0], contents=contents[1])
