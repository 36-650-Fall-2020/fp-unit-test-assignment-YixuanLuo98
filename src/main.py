import pandas as pd
from readers import *
from functions import *

us = pd.read_csv("~/Desktop/650/fp-unit-test-assignment-YixuanLuo98/data/us.csv")
us_states = pd.read_csv("~/Desktop/650/fp-unit-test-assignment-YixuanLuo98/data/us-states.csv")
us_counties = pd.read_csv("~/Desktop/650/fp-unit-test-assignment-YixuanLuo98/data/us-counties.csv")

print("Hello! This is where you can get the 2020 COVID-19 data!")

select_data = input("Please select a dataset (nationwide/state/county): ")

if select_data == "state":
    select_state = input("Please enter a State Name: ")
    print_death_rate(us_states, select_state, "state")
    earliest_date_s = us_states.loc[us_states["state"] == select_state, "date"].iloc[0]
    print("The earliest date available is " + earliest_date_s)
elif select_data == "county":
    select_county = input("Please enter a County Name: ")
    print_death_rate(us_counties, select_county, "county")
    earliest_date_c = us_counties.loc[us_counties["county"] == select_county, "date"].iloc[0]
    print("The earliest date available is " + earliest_date_c)
else:
    print_death_rate(us, "","")
    print("The earliest date available is 2020-01-21")


date = input("Please select a Date (yyyy-mm-dd): ")

if select_data == "nationwide":
    print_covid_information(us, date, "", "")

elif select_data == "state":
    print_covid_information(us_states, date, select_state, select_data)
else:
    print_covid_information(us_counties, date, select_county, select_data)
    
print("Please select a time range to display the cummulated counts for cases/deaths")
start_date = input("Please enter a Start Date (yyyy-mm-dd): ")
end_date = input("Please enter an End Date (yyyy-mm-dd): ")

if select_data == "nationwide":
    print_cumm_information(us, start_date, end_date, "", "")

elif select_data == "state":
    print_cumm_information(us_states, start_date, end_date, select_state, "state")
else:
    print_cumm_information(us_counties, start_date, end_date, select_county, "county")