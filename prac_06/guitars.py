"""
CP1404 Practical 06 - Guitars
Client program to collect user's guitars and display them in a formatted list.
Estimate time: 40
Actual time: 36
"""
from guitar import Guitar
def main():
    """Collect guitar data and display a formatted list."""
    guitars = []

    print("My guitars!")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))

            new_guitar = Guitar(name, year, cost)
            guitars. append(new_guitar)
            print(f"{new_guitar} added.\n")
        except ValueError:
            print("Invalide input. Please enter valid number for year and cost.")

        name = input("Name: ")

        if guitars:
            print("\nThese are my guitars:")
            for i, guitar in enumerate(guitars, 1):
                vintage_string = " (vintage)" if guitar.is_vintage() else ""

                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
        else:
            print("\nNo guitars entered.")

    if __name__ == '__main__':
        main()