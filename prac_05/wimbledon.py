"""
Wimbledon Champions Data Processing
Estimate: 45 minutes
Actual:
"""

FILENAME = "wimbledon.csv"

def main():
    """process champions and countries, and display results."""
    records = load_data(FILENAME)

    champion_to_count, countries = process_records(records)

    display_results(champion_to_count, countries)

def load_data(filename):
    """Read data from file into a list of lists, handling with UTF-8"""
    records = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:

        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)

    return records

def process_records(records):
    """Process data to create a dictionary of champions and a set of countries."""
    champion_to_count = {}

    countries = set()

    for record in records:

        country = record[1]
        champion = record[2]

        countries.add(country)

        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display champions and sorted countries neatly."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print()

    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")

    countries_string = ", ".join(sorted_countries)
    print(countries_string)

main()


