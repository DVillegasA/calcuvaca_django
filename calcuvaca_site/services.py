from datetime import date, datetime

VACATION_FACTOR: float = 15.0/365.0

def get_vacation_days(start_date: date, days_taken: int):
    current_date = datetime.now().date()
    days_worked = (current_date - start_date).days
    vacation_days = days_worked*VACATION_FACTOR - days_taken

    return vacation_days
