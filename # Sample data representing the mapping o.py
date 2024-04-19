# Sample data representing the mapping of district, mandal, village, and survey numbers
survey_data = {
    "Hyderabad": {
        "Ranga Reddy": {
            "Gachibowli": ["001", "002", "003"],
            "Kondapur": ["004", "005", "006"]
        },
        "Medchal": {
            "Kompally": ["007", "008", "009"],
            "Shamirpet": ["010", "011", "012"]
        }
    },
    "Warangal": {
        "Hanamkonda": {
            "Kazipet": ["101", "102", "103"],
            "Subedari": ["104", "105", "106"]
        },
        "Warangal": {
            "Narsampet": ["107", "108", "109"],
            "Parkal": ["110", "111", "112"]
        }
    }
}

def get_survey_numbers(district, mandal, village):
    try:
        survey_numbers = survey_data[district][mandal][village]
        return survey_numbers
    except KeyError:
        return []

# Example usage
district = "Hyderabad"
mandal = "Ranga Reddy"
village = "Gachibowli"

result = get_survey_numbers(district, mandal, village)
if result:
    print(f"Survey numbers for {district}, {mandal}, {village}: {', '.join(result)}")
else:
    print(f"No survey numbers found for {district}, {mandal}, {village}.")
