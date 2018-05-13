"""
@file
@brief Dummy data for 2016
"""
import random
import uuid
from datetime import datetime, timedelta


first_names = {"M": "Balthazar", "W": "Cendrillon",
               True: "Balthazar", False: "Cendrillon"}


def enumerate_person(hf=0.5, age=(18, 60), n=100):
    """
    enumerate a person randomly chosen

    @param      hf      proportion of men
    @param      age     range for age
    @param      n       number of person to generate
    @return             enumerator of dictionaries
    """
    for _ in range(n):
        hfi = random.random() <= hf
        agei = random.randint(*age)
        namei = first_names[hfi]
        yield dict(gender=(1 if hfi else 0), age=agei, name=namei, idc=uuid.uuid4())


def enumerate_appointments(persons, nb=(1, 4), price=(60., 120.),
                           first_date=None, end_date=None,
                           formula=None):
    """
    enumerate a list of appointments for a given list of ids

    @param      persons     list of persons
    @param      nb          range for the number of appointments
    @param      price       range for prices
    @param      begin_date  first date (or now - 2 months)
    @param      end_date    end date (or now)
    @param      formula     formula for the prices of the appointments
    @return                 enumerator of dictionaries
    """
    if end_date is None:
        end_date = datetime.now()
    if first_date is None:
        first_date = end_date - timedelta(days=60)
    if formula is None:
        def formula_default(age, gender, when, date):
            p = age * 0.5
            p += -2 if gender else 2
            if when is not None:
                if when < 0:
                    raise Exception(
                        "when must be positive, when={0} - date={1}".format(when, date))
                p -= 10 / (when + 1)
            if date.weekday() in (6, 7):
                p += 20
            p += random.gauss(0, 2)
            p += price[0]
            p = int(p / 5) * 5
            return p
        formula = formula_default

    for person in persons:
        age = person["age"]
        gender = person["gender"]
        idc = person["idc"]
        ns = random.randint(*nb)
        fd = first_date
        prev = None
        for n in range(ns):
            nbdays = (end_date - fd).days
            d = random.randint(0, int(max(nbdays * 1.0 / (ns - n), 1)))
            fd = fd + timedelta(days=d)
            last = None if prev is None else (fd - prev).days
            p = formula(age, gender, last, fd)
            p = min(price[1], max(p, price[0]))
            yield dict(idr=uuid.uuid4(), price=p, date=fd, idc=idc)
            prev = fd
