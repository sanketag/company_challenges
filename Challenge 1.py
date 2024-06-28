small = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}

mid = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

high = {"hundred": 100, "thousand": 1000, "million": 1000000}

def parse_numbers(number):
    parts = number.strip().split()
    total = 0
    negative = False

    if parts[0] == "negative":
        negative = True
        parts = parts[1:]

    curr = 0
    for part in parts:
        if part in small:
            curr += small[part]
        elif part in mid:
            curr += mid[part]
        elif part in high:
            total += curr * high[part]
            curr = 0
        else:
        	continue

    total += curr
    return -total if negative else total

if __name__ == "__main__":
	str_nums = "six, negative nine million four hundred twenty nine, one million one hundred one"
	numbers = str_nums.split(", ")
	numbers = [parse_numbers(num) for num in numbers]
	print(", ".join(map(str, numbers)))
