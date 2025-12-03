from get_data import get_data

lines = ["987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"]

lines = get_data().splitlines()

def part1(lines):
    tot_joltage = 0
    for l in lines:
        max = 0
        scnd_max = 0
        index = 0
        for i in range(len(l)-1):
            if int(l[i])>max:
                max = int(l[i])
                index = i
        for i in range(index+1, len(l)):
            if int(l[i])>scnd_max:
                scnd_max = int(l[i])
        joltage = str(max)+str(scnd_max)
        tot_joltage += int(joltage)
    return tot_joltage

def part2(lines):
    tot_joltage = 0
    for l in lines:
        index = 0
        joltage = ""
        for j in range(11, -1, -1):
            max = 0
            for i in range(index,len(l)-j):
                if int(l[i])>max:
                    max = int(l[i])
                    index = i+1
            joltage += str(max)
        tot_joltage += int(joltage)
    return tot_joltage

print(part1(lines))
print(part2(lines))