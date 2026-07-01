
def main():
    filename = input("Enter filename: ")
    try:
        line_count = count_line(filename)
        print(f"{filename} has {line_count} lines")
    except FileNotFoundError:
        print(f"ERROR: {filename} does not exist")

def count_line(filename):
    count = 0

    with open(filename, "r") as in_file:
        for line in in_file:
            count += 1

    return count

main()