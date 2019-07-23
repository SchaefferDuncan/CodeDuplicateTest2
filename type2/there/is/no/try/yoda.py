from datetime import datetime


def do_or_do_not():
    this_very_moment = datetime.now()
    m = str(this_very_moment.month)
    d = str(this_very_moment.day)
    y = str(this_very_moment.year)
    h = str(this_very_moment.hour)
    mi = str(this_very_moment.minute)
    s = str(this_very_moment.second)
    print(m + "/" + d + "/" + y + " " + h + ":" + mi + ":" + s)
