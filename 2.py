file = open("2.txt", "r")
text = file.read()
file.close()

part1_count = 0
count = 0

def check_case(numbers):
    good_case = True
    assending = numbers[1] > numbers[0]
    prev = numbers[0]
    for n in numbers[1:]:
        change = abs(prev - n)
        if change > 3 or change == 0:
            good_case = False
        if assending != (n > prev):
            good_case = False
        prev = n
    return good_case

for case in text.split("\n")[:-1]:
    good_case = False
    numbers = [int(a) for a in case.split()]
    for i in range(len(numbers)):
        new_numbers = numbers[:]
        new_numbers.pop(i)
        if check_case(new_numbers):
            good_case = True
    regular_case = check_case(numbers)
    if regular_case:
        part1_count += 1
    if good_case or regular_case:
        count += 1

print("1 Count:", part1_count)
print("2 Count:", count)
