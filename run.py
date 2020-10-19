numbers = [2, 3, 10, 11, 12, 22, 33, 297, 3045]

def sum_digits_by_three(n):
    """
    Takes single int argument
    Adds all decimal notation 
    Returns True if sum is divisable by 3
    """
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r % 3 == 0


def sum_digits_by_eleven(n):
    """
    Takes single int argument
    Formats To string, reverses it for the pairs
    then reverses again for pairs to read correct way and as int
    Adds all pairs of numbers
    Returns True if sum is divisable by 11
    """
    a, total = 2, 0
    num_string = str(n)[::-1]
    reversed_string = [num_string[i:i+a] for i in range(0, len(num_string), a)]
    sorted_numbers = [int(r[::-1]) for r in reversed_string]
    for num in sorted_numbers:
        total += num
    return total % 11 == 0


def fizz_buzz(array):
    """ 
    Takes array of ints
    Returns array with string value per number
    """
    results = []
    for n in array:
        if sum_digits_by_three(n) == True and sum_digits_by_eleven(n) == True:
            results.append("Fizzbuzz")
        elif sum_digits_by_three(n) == True:
            results.append("Fizz")
        elif sum_digits_by_eleven(n) == True:
            results.append("Buzz")
        else:
            results.append("Baz")
    return results


def run():
    print(f"Current Numbers: {numbers}")
    cmd = input(f"Input 'run' or 'q' to quit: ")
    if cmd == 'run':
        output = fizz_buzz(numbers)
        print(f"Output: {output}")
        repeat = input("Run again? (y): ")
        if repeat == 'y':
            run()
        else:
            print("Thanks!")
    elif cmd == 'q':
        print("Thanks!")
    else:
        print()
        print("Invalid command!")
        print()
        run()

run()


"""
Doing this task in python was eaiser for me, list comprehensions working with data
is eaiser to read to me. I would refactor the return functions to return 'fizz' or
'buzz' directly then append together if both conditions are met
"""
