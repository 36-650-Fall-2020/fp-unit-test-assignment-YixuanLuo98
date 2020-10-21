import functions *


def print_death_rate(data, name, region):
    if data is us:
        data = data
    else:
        data = data[data[region] == name]
    print("The death rate till now is ", death_rate(data))

def print_covid_information(data, date, name, region):
    print("Date: " + date)
    print("The total number of cases is ", get_cases(data, date, name, region))
    print("The total number of deaths is ", get_deaths(data, date, name, region))

def print_cumm_information(data, start_date, end_date, name, region):
    print("Time Range: " + start_date + " - " + end_date)
    if data is us:
        data = data
    else:
        data = data[data[region] == name]
    print("The acummulatied number of cases is ", cumm_cases(data, start_date, end_date))
    print("The acummulatied number of deaths is ", cumm_deaths(data, start_date, end_date))


