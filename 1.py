file = open("1.txt", "r")
text = file.read()
file.close()

list1 = []
list2 = []

for pair in text.split("\n"):
    if pair:
        values = pair.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

list1.sort()
list2.sort()

error = 0

for i in range(len(list1)):
    error += abs(list1[i]-list2[i])

print("Error:", error)


def count(item, array):
    count = 0
    for thing in array:
        if thing == item:
            count += 1
    return count

similarity = 0

for item in list1:
    similarity += item * count(item, list2)

print("Similarity:", similarity)
