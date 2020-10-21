import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

import pytest
import pandas as pd
from functions import get_cases, get_deaths, cumm_cases, cumm_deaths, death_rate

def test_get_cases():
    d = {"date": ["2020-01-25"], "state": ["California"], "cases": [1], "deaths":[0]}
    data = pd.DataFrame(data=d)
    date = "2020-01-25"
    name = "California"
    region = "state"
    assert get_cases(data, date, name, region) == 1

def test_get_deaths():
    d = {"date": ["2020-01-25"], "state": ["California"], "cases": [1], "deaths":[0]}
    data = pd.DataFrame(data=d)
    date = "2020-01-25"
    name = "California"
    region = "state"
    assert get_deaths(data, date, name, region) == 0

def test_cumm_cases():
    d = {"date": ["2020-01-25", "2020-01-26", "2020-01-27"], "cases": [3, 5, 5]}
    data = pd.DataFrame(data=d)
    start_date = "2020-01-25"
    end_date = "2020-01-26"
    result = cumm_cases(data, start_date, end_date)
    assert result == 8


def test_cumm_deaths():
    d = {"date": ["2020-03-25", "2020-03-26", "2020-03-27"], "deaths": [1054, 1353, 1770]}
    data = pd.DataFrame(data=d)
    start_date = "2020-03-26"
    end_date = "2020-03-27"
    result = cumm_deaths(data, start_date, end_date)
    assert result == 3123

def test_death_rate():
    d = {"deaths": [2, 4, 6], "cases": [1, 2, 3]}
    data = pd.DataFrame(data=d)
    result = death_rate(data)
    assert result == 2