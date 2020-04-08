"""
This is a simple python module that shows the various features of the python programming language
"""
import datetime
import math
import sys
from pprint import pprint as pp


def fetch_words(long):
    """
    the monster that does the magic
    :param long: string
    :return: string
    """
    story = long.split(" ")
    story_words = []
    for line in story:
        line_word = line.decode("utf-8").split()
        for word in line_word:
            story_words.append(word)
    return story_words


def print_story(story):
    for word in story:
        print(word)


def print_border(message, border='='):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def min_max(item):
    return min(item), max(item)


def str_manipulation():
    join = ",".join(["this ", "is ", "getting ", "interesting "])
    split = join.split(",")
    partition = "unforgettable".partition("forget")
    print(partition)
    departure, sep, arrival = "Nigeria:Vancouver".partition(":")
    print("Soon, I would take off from {0} and land in {1}".format(departure, arrival))
    product = 4 * 5
    print(f"The product is {product}")
    print(f"The current datetime is {datetime.datetime.now().isoformat()}")
    print(f"Math Constants: pi={math.pi:4f} e={math.e:4f}")
    print_border(join)
    print_border(split)


def range_function():
    row = ""
    for i in range(10):
        row += f"{i},"
    print(row)

    values = [range(1, 10)]
    print(values)

    even = ""
    for e in range(2, 10, 2):
        even += f"{e},"
    print(even)

    s = [3, 4, 5, 6, 7, 8, 9]
    for i in enumerate(s):
        print(i)

    for k, v in enumerate(s):
        print(f"key = {k}, value = {v}")


def dictionary():
    di = {'goldenrod': 0xDAA520, 'indigo': 0x4B0082}
    id = {"databricks": "Apache Spark", "amazon": "Amazon Web Service"}
    for key in id:
        print(key)

    for value in id.values():
        print(value)

    for key in id:
        print(f"{key} = {id[key]}")

    print(di)
    d = dict(goldenrod=0xDAA520, indigo=0x4B0082)
    g = dict(first=1, second=2)
    e = id.update(di)
    print("Mysterious", e)


def set_structure():
    u = {1, 2, 3, 4, 5}
    u.add(7)
    v = set([6, 7, 8, 9, 0])
    v.add(3)
    print(v.intersection(u))
    print(u.union(v))
    print(v.isdisjoint(u))
    print(u.difference(v))
    print(v.difference(u))
    print(u.symmetric_difference(v))


def slicing():
    arr = [2, 3, 4, 5, 6, 7]
    print(f"{arr}[2:-2] = {arr[2:-2]}")
    print(f"{arr}[1:4] = {arr[1:4]}")
    print(f"{arr}[:3] = {arr[:3]}")
    print(f"{arr}[1:] = {arr[1:]}")


def string_to_number(st):
    digit_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10
    }
    try:
        num_str = ''
        for token in st:
            num_str += str(digit_map[token])
        return int(num_str)
    except(KeyError, TypeError) as e:
        print(f"conversion error: n{e!r}", file=sys.stderr)
        raise
        # return -1


def os_feature():
    try:
        import msvcrt
        return msvcrt.getch()
    except ImportError:
        import termios
        import tty
        fd = sys.stdin.fileno()
        original_attr = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attr)
            return ch


def comprehension_feature(sentence):
    new_list = [len(word) for word in sentence.split()]
    print(new_list)
    factorial_str_len = [len(str(math.factorial(num))) for num in range(20)]
    print(factorial_str_len)
    set_compr = {len(str(math.factorial(num))) for num in range(20)}
    print(set_compr)
    country_to_capitals = {'UK': 'London', 'Sweden': 'Stockholm', 'USA': 'Washington DC'}
    capital_to_country = {capital: country for country, capital in country_to_capitals.items()}
    pp(capital_to_country)
    primes = [n for n in range(20) if is_prime(n)]
    print('primes:', primes)
    prime_square_divisors = {num: (1, num, num * num) for num in range(20) if is_prime(num)}
    pp(prime_square_divisors)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def iteration():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    iterator = iter(iterable)
    print('Next in iterator: ', next(iterator))


def take(count, iterable):
    for item in iterable:
        counter = 0
        if count == counter:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item


def run_pipeline():
    items = [1, 2, 3, 4, 5, 2, 3, 1]
    for item in take(3, distinct(items)):
        print(item)


def fib(n):
    if n < 1:
        return
    sequence = [1]
    a, b = 1, 2
    while n > 0:
        sequence.append(b)
        a, b = b, a + b
        n -= 1
    return sequence


def generator_expr(n):
    return sum(x * x for x in range(n) if is_prime(x))


def main(story):
    """this is the main function
    starts the program
    """
    print_story(story)


if __name__ == '__main__':
    # main(sys.argv[1])  # the 0th arg is the module filenameo
    print('Generator Expression for sum of squares of first prime n numbers: ', generator_expr(1000001))
    print('First 10 fibonnaci sequence', fib(10))
    print("Pipeline Next: ")
    run_pipeline()
    print("Iteration Next: ")
    iteration()
    print("Comprehension Next: ")
    comprehension_feature("Hydrogen Helium Lithium Berryllium Boron Carbon Nitrogen Oxygen Florine Neon")
    # os_feature()
    num = string_to_number("one five ten".split())
    print("String to number: ")
    print(num)
    print("Set Structure: ")
    set_structure()
    print("Dictionary: ")
    dictionary()
    print("Slicing: ")
    slicing()
    print("Range Function: ")
    range_function()
    print("String Manipulation: ")
    str_manipulation()
    (mini, maxi) = min_max([45, 65, 45, 34, 56, 7, 82, 30])
    print(mini, maxi)
    story = "This is my story"
    print_border(story, "*")
    main(story)  # the 0th arg is the module filename
