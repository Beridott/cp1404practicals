"""
CP1404 Practical 06 - Guitar Test
Estimate time: 30
Actual: 26
"""
from guitar import Guitar

def run_tests():
    """Execute manual test for Guitar class"""
    # Guitar 1: Gibson L-5 CES (Made in 1922)
    # Expected age is current_year - 1922
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"{gibson.name} get_age() - Expected {gibson.get_age()}")
    print(f"{gibson.name} is_vintage( - Expected True. Got {gibson.is_vintage()}")

    print("-" * 30)

    #Guitar 2: Another Guitar (Made in 2015)
    # Expected age is current_year - 2015
    another = Guitar("Another Guitar", 2015, 800.00)
    print(f"{another.name} get_age( - Expected {another.get_age()}. Got {another.get_age()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

    print("-" * 30)

    #Guitar 3: A guitar made exactly 50 years ago
    vintage_boundary = Guitar("50-year old guitar", 1975, 2500.00)
    print(f"{vintage_boundary.name} is_vintage() - Expected True. Got {vintage_boundary.is_vintage()}")

if __name__ == '__main__':
    run_tests()