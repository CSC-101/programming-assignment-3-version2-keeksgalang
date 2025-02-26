from build_data import *
from county_demographics import *
from data import *

# Task 1
def population_total(lst: list[CountyDemographics]) -> int:
    total = 0
    for item in lst:
        population = item.population
        for key in population:
            if key == '2014 Population':
                total += population[key]

    return total

# Task 2
def filter_by_state(lst: list[CountyDemographics], state:str) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        if item.state == state:
            new_list.append(item)

    return new_list

# Task 3
def population_by_education(lst: list[CountyDemographics], education_type:str) -> float:
    edu_total = 0
    for item in lst:
        population = item.population
        percentage = item.education
        total = 0
        for key in population:
            if key == '2014 Population':
                total += population[key]
        for key in percentage:
            if key == education_type:
                total = total*(percentage[key]/100)
        edu_total += total

    return edu_total

def population_by_ethnicity(lst: list[CountyDemographics], ethnicity_type:str) -> float:
    eth_total = 0
    for item in lst:
        population = item.population
        percentage = item.ethnicities
        total = 0
        for key in population:
            if key == '2014 Population':
                total += population[key]
        for key in percentage:
            if key == ethnicity_type:
                total = total*(percentage[key]/100)
        eth_total += total

    return eth_total

def population_below_poverty_level(lst: list[CountyDemographics]) -> float:
    pov_total = 0
    for item in lst:
        population = item.population
        percentage = item.income
        total = 0
        for key in population:
            if key == '2014 Population':
                total += population[key]
        for key in percentage:
            if key == 'Persons Below Poverty Level':
                total = total * (percentage[key] / 100)
        pov_total += total

    return pov_total

# Task 4
def percent_by_education(lst: list[CountyDemographics], education_type:str) -> float:
    try:
        edu_population = population_by_education(lst, education_type)
        population = population_total(lst)
        return (edu_population/population)*100
    except ValueError:
        return 0

def percent_by_ethnicity(lst: list[CountyDemographics], ethnicity_type:str) -> float:
    try:
        eth_population = population_by_ethnicity(lst, ethnicity_type)
        population = population_total(lst)
        return (eth_population/population)*100
    except ValueError:
        return 0

def percent_below_poverty_line(lst: list[CountyDemographics]) -> float:
    try:
        pov_population = population_below_poverty_level(lst)
        population = population_total(lst)
        return (pov_population/population)*100
    except ValueError:
        return 0

# Task 5
def education_greater_than(lst: list[CountyDemographics], education_type:str, threshold:float) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        edu_population = item.education
        for key in edu_population:
            if key == education_type:
                percentage = edu_population[key]
                if percentage > threshold:
                    new_list.append(item)

    return new_list

def education_less_than(lst: list[CountyDemographics], education_type:str, threshold:float) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        edu_population = item.education
        for key in edu_population:
            if key == education_type:
                percentage = edu_population[key]
                if percentage < threshold:
                    new_list.append(item)

    return new_list

def ethnicity_greater_than(lst: list[CountyDemographics], ethnicity_type:str, threshold:float) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        eth_population = item.ethnicities
        for key in eth_population:
            if key == ethnicity_type:
                percentage = eth_population[key]
                if percentage > threshold:
                    new_list.append(item)

    return new_list

def ethnicity_less_than(lst: list[CountyDemographics], ethnicity_type:str, threshold:float) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        eth_population = item.ethnicities
        for key in eth_population:
            if key == ethnicity_type:
                percentage = eth_population[key]
                if percentage < threshold:
                    new_list.append(item)

    return new_list

def below_poverty_level_greater_than(lst: list[CountyDemographics], threshold:float) -> list[CountyDemographics]:
    new_list = []
    for item in lst:
        pov_population = item.income
        for key in pov_population:
            if key == "Persons Below Poverty Level":
                percentage = pov_population[key]
                if percentage > threshold:
                    new_list.append(item)

    return new_list

def below_poverty_level_less_than(lst: list[CountyDemographics], threshold:float) -> list:
    new_list = []
    for item in lst:
        pov_population = item.income
        for key in pov_population:
            if key == "Persons Below Poverty Level":
                percentage = pov_population[key]
                if percentage < threshold:
                    new_list.append(item)

    return new_list