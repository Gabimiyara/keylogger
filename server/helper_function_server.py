from datetime import datetime


def stamp_date():
    return datetime.now().strftime("%d/%m/%Y")

def stamp_time():
    return datetime.now().strftime("%H:%M:%S")