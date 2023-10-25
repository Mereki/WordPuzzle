def get_valid_letters(x):
    chars = ""
    count = 0
    while count <= 9:
        for i in x:
            if i not in chars and i.isalpha():
                chars += i
                count += 1
    return chars


#print(get_valid_letters("SAG,SOW | GLOSSY,NSAS  ,EGLS ,EOGT ,OTYY,OSSO,OEA"))

def is_valid_guess(x, y):
    checker = ""
    if len(y) != len(x):
        return False
    else:
        for i in y:
            if i not in x:
                return False
            elif i in x and i in checker:
                return False
            else:
                checker += i
    return True

#print(type((is_valid_guess("SAGOWLYNET", "SSSSSSSSSSS"))))

def check_user_guess(a, b, c, d):
    if b * c + d == a:
        return True
    else:
        return False


def make_number(x, y):
    key = ""
    for i in range(len(x)):
        if x[i] in y:
            key += str(y.index(x[i]))
    if key == "":
        return 0
    else:
        return int(key)


# print(make_number("RUE", "TAKEOURSIM"))
# returns 653

def make_numbers(a, b):
    sep = a.split(",")
    divis = []
    for i in sep:
        if "|" in i:
            divis = i.split("|")
    # print(sep)
    # print(divis)
    dividend = make_number(divis[1], b)
    quotient = make_number(sep[0], b)
    divisor = make_number(divis[0], b)
    remainder = make_number(sep[-1], b)
    combine = dividend, quotient, divisor, remainder
    return combine


# print((make_numbers("RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA","RUEAMOSIKT")))

def print_puzzle(puzzle):
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-' * len(puzzle[i]): >16}")


# def main():
#     # The lines below demonstrate what the print_puzzle function outputs.
#     puzzle = "RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA"
#     print()
#     print_puzzle(puzzle)

def main():
    puzzle = input("Enter a word arithmetic puzzle: ")
    # puzzle = "SAG,SOW | GLOSSY,NSAS  ,EGLS ,EOGT ,OTYY,OSSO,OEA"
    # puzzle = "RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA"
    print()
    print_puzzle(puzzle)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    # guess = "TAGOWLNYES"
    # guess = "TAKEOURSIM"
    # guess = "OURMISTAKE"

    valid_chars = get_valid_letters(puzzle)
    valid_guess = is_valid_guess(valid_chars, guess)
    numbers = make_numbers(puzzle, guess)
    # print(valid_guess)
    # print(numbers)
    checker = check_user_guess(int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3]))
    # print(checker)
    if len(guess) != len(valid_chars):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    elif not (valid_guess and checker):
        print("Try again!")
    else:
        print("Good job!")


if __name__ == '__main__':
    main()
