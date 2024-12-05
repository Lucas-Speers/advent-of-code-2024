import itertools

file = open("5_1.txt", "r")
r = file.read()
file.close()
file = open("5_2.txt", "r")
p = file.read()
file.close()

count = 0
count2 = 0

rules = {}
for item in r.split("\n"):
    if item == "": continue
    items = item.split("|")
    if items[0] not in rules:
        rules[items[0]] = []
    rules[items[0]].append(items[1])

print(rules)

def check(pages):
    rule_breaker = False
    for i in range(len(pages)):
        if pages[i] in rules:
            for rule in rules[pages[i]]:
                if rule in pages[:i]:
                    rule_breaker = True
    return rule_breaker

def fix(pages):
    for first in range(len(pages)):
        for second in range(first, len(pages)):
            if pages[first] in rules[pages[second]]:
                temp = pages[first]
                pages[first] = pages[second]
                pages[second] = temp


for update in p.split("\n"):
    if update == "": continue
    pages = update.split(",")
    if not check(pages):
        count += int(pages[(len(pages)-1)//2])
    else:
        fix(pages)
        count2 += int(pages[(len(pages)-1)//2])
print(count, count2)
