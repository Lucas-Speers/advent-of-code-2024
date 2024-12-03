file = open("3.txt", "r")
text = file.read()
file.close()

count1 = 0
count2 = 0
do = True

def parse_num(buf):
    total = 0
    for i in range(4):
        if buf[i].isnumeric():
            total *= 10
            total += int(buf[i])
        elif i == 0:
            raise Exception("Bad number")
        else:
            return total, i

def check_buf(buf):
    global count1
    global count2
    global do
    if buf[:4] == "do()":
        do = True
    if buf[:7] == "don't()":
        do = False
    if buf[:4] != "mul(":
        return
    num1, index1 = parse_num(buf[4:])
    if buf[index1+4] != ",":
        return
    num2, index2 = parse_num(buf[index1+5:])
    if buf[index1+index2+5] != ")":
        return
    count1 += num1 * num2
    if do:
        count2 += num1 * num2

for i in range(len(text)):
    try:
        check_buf(text[i:])
    except:
        pass

print("Part1:", count1)
print("Part2:", count2)
