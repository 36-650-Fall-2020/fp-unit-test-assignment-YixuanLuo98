from functools import reduce

def get_cases(data, date, name, region):
    if region not in data:
        return data.loc[data["date"] == date, "cases"].item()
    else:
        state_by_date = data[data["date"] == date]
        cases = state_by_date.loc[state_by_date[region] == name, "cases"].item()
        return cases

def get_deaths(data, date, name, region):
    if region not in data:
        return data.loc[data["date"] == date, "deaths"].item()
    else:
        state_by_date = data[data["date"] == date]
        deaths = state_by_date.loc[state_by_date[region] == name, "deaths"].item()
        return deaths

def cumm_cases(data, start_date, end_date):
    sub = data.loc[(data["date"] >= start_date) & (data["date"] <= end_date)]
    return reduce(lambda x,y: x+y, sub["cases"])

def cumm_deaths(data, start_date, end_date):
    sub = data.loc[(data["date"] >= start_date) & (data["date"] <= end_date)]
    return reduce(lambda x,y: x+y, sub["deaths"])

def death_rate(data):
    x = map(sum, (data["deaths"], data["cases"]))
    y = list(x)
    return y[0] / y[1]








