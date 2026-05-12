def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    for c in plate:
        if c.lower() in [",", ".", "!"]:
            return False
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[0:2].isalpha():
        return False

    found_digit = False
    for c in plate:

        if c.isdigit():
            if not found_digit:
                if c == "0":
                    return False
            found_digit = True

        elif c.isalpha():
            if found_digit:
                return False

    return True



main()