import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from courts import Court

def test_add_free_time():
    court = Court(1)
    court.add_free_time("10:00", "12:00", 15)
    assert len(court.free_slots) == 1
    assert court.free_slots[0] == (datetime.strptime("10:00", "%H:%M"), datetime.strptime("12:00", "%H:%M"), 15)

def test_get_free_time_slots_longer_than_hour():
    court = Court(1)
    court.add_free_time("10:00", "12:00", 10)
    court.add_free_time("13:00", "14:00", 10)
    court.add_free_time("12:30", "13:30", 10)
    free_slots = court.get_free_time_slots_longer_than_hour()
    assert len(free_slots) == 2
    assert free_slots[0] == (10, datetime.strptime("10:00", "%H:%M"), datetime.strptime("12:00", "%H:%M"))
    assert free_slots[1] == (10, datetime.strptime("12:30", "%H:%M"), datetime.strptime("14:00", "%H:%M"))

def test_get_free_time_slots_shorter_than_hour():
    court = Court(1)
    court.add_free_time("10:00", "10:30", 12)
    court.add_free_time("12:00", "13:00", 12)
    free_slots = court.get_free_time_slots_longer_than_hour()
    assert len(free_slots) == 0

def test_slots_merge():
    court = Court(1)
    court.add_free_time("10:00", "12:00", 1)
    court.add_free_time("12:00", "14:00", 1)
    free_slots = court.get_free_time_slots_longer_than_hour()
    assert len(free_slots) == 1
    assert free_slots[0] == (1, datetime.strptime("10:00", "%H:%M"), datetime.strptime("14:00", "%H:%M"))