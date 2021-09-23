travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# write your code below this code
def add_new_country(country_name, num_visits, cities_list):
    travel_log.append(
        {
            "country": country_name,
            "visits": num_visits,
            "cities": cities_list,
        }
    )


#
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)