from datetime import date, datetime, timedelta


def get_business_day():
    now = datetime.now()
    return (now + timedelta(-1 if now.hour < 14 else 0)).date()


def is_same_month(d1, d2):
    return all(getattr(d1, x, -1) == getattr(d2, x, -2) for x in ['year', 'month'])


def get_1st_of_next_month(day):
    year = day.year
    month = day.month
    return date(
        year=year + ([0, 1][month == 12]),
        month=[month + 1, 1][month == 12],
        day=1
    )
