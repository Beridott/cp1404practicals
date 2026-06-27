"""
CP1404 Practical 05
Hexadecimal colour lookup program
Estimate: 15 mins
Actual:   16 mins
"""

COLOR_TO_CODE = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}

def main():
    color_name = input("Enter colour name: ").strip().upper()

    while color_name != "":
        try:
            print(f"The code for {}")