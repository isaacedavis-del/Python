def is_year_leap(year):
    """
    Returns True if the given year is a leap year according to the Gregorian calendar.
    Raises ValueError if the year is not within the Gregorian calendar period (>1582).
    """
    if year <= 1582:
        raise ValueError("Year not within the Gregorian calendar period (>1982).")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main(test_data, test_results): 
    for yr, expected in zip(test_data, test_results):
        print(f"{yr} -> ", end="")
        try:
            result = is_year_leap(yr)
            if result == expected:
                print("OK")
            else:
                print("Failed")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_data = [1900, 2000, 2016, 1987]
    test_results = [False, True, True, False]
    main(test_data, test_results)