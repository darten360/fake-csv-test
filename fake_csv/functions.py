import random
from datetime import timedelta, datetime


def random_fullname():
    lst = ["Ivan Ivanov", "Denis Egorov", "Ed Schmidt", "Bruce Willis", "Mariia Ivanova", "Danylo Sagaydachny"]
    return random.choice(lst)


def random_company():
    lst = ["Google", "Microsoft", "Apple", "Xiaomi", "Biedronka", "ATB"]
    return random.choice(lst)


def random_phone():
    lst = ["+380998765432", "+48765456234", "+79901224533", "+380963226744", "+48633285674", "+89981425565"]
    return random.choice(lst)


def random_email():
    lst = ["malchik@gmail.com", "devochka@list.ru", "turbodog@outlook.com",
           "kuzka@ukr.net", "kurliak@mail.ru", "shampinion@gmail.com"]
    return random.choice(lst)


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return datetime.strftime(start + timedelta(seconds=random_second), "%Y-%m-%d")


def random_address():
    lst = ["Koroliuka 25", "1 Maja 23", "Kosmiczna 23a",
           "Sobieskiego 6", "Filarowa 50", "Centralna 132"]

    return random.choice(lst)


def random_text():
    lst = ["doijafghdliughdsfgnsdlfgbitghsifbsldfbgsleitybg", "fogshdifoghsdofighsdofiughsdofiughsdoifuh",
           "fghlighlsdifughsidfuhgsdifghsdifghsidfhgsdifuhgsidfuhgsidufhgsdg", "uhfgsdfuhgisdufhgisdufhgsidufhgsiufh",
           "fdgsnfighsdnfighndihcgmdfuhcgmifONONGNOGOIH", "sgdfpogkdsfigjsdof8gusdi7fgh7ergh"]

    return random.choice(lst)


def random_domain():
    lst = ["youtube.com", "tiktok.com", "etsy.com",
           "gofundme.com", "linktr.ee", "irs.gov"]

    return random.choice(lst)


def random_int():
    return random.randint(-1000, 1000)
