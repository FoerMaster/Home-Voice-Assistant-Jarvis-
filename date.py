import datetime

def TextType():
    type = "Добрый день"
    now = datetime.datetime.now()
    if now.hour > 5 & now.hour < 12:
        type = "Доброе утро"
    elif now.hour > 12 & now.hour < 18:
        type = "Добрый день"
    elif now.hour > 18 & now.hour < 23:
        type = "Доброй ночи"
    elif now.hour > 0 & now.hour < 5:
        type = "Доброй ночи"

    return type

def Time():
    now = datetime.datetime.now()
    return str(now.hour) + ":" + str(now.minute)