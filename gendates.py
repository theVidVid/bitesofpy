from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    birthday = PYBITES_BORN
    one_hundred_days = timedelta(days=+100)
    one_year_later = timedelta(days=365)
    march_29th = birthday + one_hundred_days
    july_7th = march_29th + one_hundred_days
    october_15th = july_7th + one_hundred_days
    first_birthday = birthday + one_year_later
    january_23rd = october_15th + one_hundred_days
    may_5th = january_23rd + one_hundred_days
    august_8th = may_5th + one_hundred_days
    november_19th = august_8th + one_hundred_days
    second_birthday = first_birthday + one_year_later
    february_27th = november_19th + one_hundred_days

    return [
        march_29th,
        july_7th,
        october_15th,
        first_birthday,
        january_23rd,
        may_5th,
        august_8th,
        november_19th,
        second_birthday,
        february_27th,
    ]


result = gen_special_pybites_dates()
print(result)
