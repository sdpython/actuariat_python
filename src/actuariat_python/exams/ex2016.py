"""
@file
@brief Dummy data for 2016
"""
import random
import uuid


first_names = {"M": "Balthazar", "W": "Cendrillon",
               True: "Balthazar", False: "Cendrillon"}


def enumerate_person(hf=0.5, age=(18, 60), n=100):
    """
    enumerate a person randomly chosen

    @param      hf      proportion of men
    @param      age     range for age
    @param      n       number of person to generate
    @return             enumerator of dictionary
    """
    for i in range(n):
        hfi = random.random() <= hf
        agei = random.randint(*age)
        namei = first_names[hfi]
        yield dict(gender=(1 if hfi else 0), age=agei, name=namei, idc=uuid.uuid4())


def enumerate_appointments(age, gender, nb=2, price=60.):
    """
    enuemrate a list of appointments for a given age
    """
