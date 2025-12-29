class WeekDayError(Exception):
    pass

class Weeker:
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    def __init__(self, day):
        if day not in self.DAYS:
            raise WeekDayError(day)
        self.index = self.DAYS.index(day)

    def __str__(self):
        return self.DAYS[self.index]

    def add_days(self, n):
        self.index = (self.index + n) % 7
        return self

    def subtract_days(self, n):
        self.index = (self.index - n) % 7
        return self

if __name__ == "__main__":
    try:
        w = Weeker("Mon")
        print(w)            # Mon
        w.add_days(15); print(w)   # Tue
        w.subtract_days(23); print(w)  # Sun
        Weeker("Monday")    # raises
    except WeekDayError:
        print("Sorry, I can't serve your request.")