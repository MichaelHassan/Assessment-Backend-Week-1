"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    """Function converts str date into a datetime."""
    try:
        actual_date = datetime.strptime(date_val, "%d.%m.%Y")
    except ValueError:
        raise ValueError("Unable to convert value to datetime.")

    return actual_date


def get_days_between(first: datetime, last: datetime) -> int:
    """Function returns the days between 2 days."""
    if not isinstance(first, datetime) or not isinstance(last, datetime):
        raise TypeError("Datetimes required.")

    delta = last - first

    return delta.days


def get_day_of_week_on(date_val: datetime) -> str:
    """Function returns the day of the week."""

    if not isinstance(date_val, datetime):
        raise TypeError("Datetime required.")

    day = date_val.weekday()
    match day:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"


def get_current_age(birthdate: date) -> int:
    """Function returns current age from birthday."""

    if not isinstance(birthdate, date):
        raise TypeError("Date required.")

    now = date.today()
    if now == birthdate:
        return 0

    age = now.year - birthdate.year - \
        ((now.month, now.day) < (birthdate.month, birthdate.day))

    return age
