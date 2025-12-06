from get_data import get_data, answer

data = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   + "]

data = get_data(6).splitlines()


def part1(data):
    rows = [row.strip().split() for row in data]
    final_sum = 0
    tot = [int(r) for r in rows[0]]
    op = rows[-1]
    rows = rows[1:-1]

    #print(op)

    for row in rows:
        for i in range(len(row)):
            if op[i] == "+":
                tot[i] += int(row[i])
            if op[i] == "*":
                tot[i] *= int(row[i])
    #print(tot)
    
    for t in tot:
        final_sum += t


    return final_sum

def part2(data):
    final_sum = 0
    op = data[-1].strip().split()
    count_op = len(op)-1
    rows = data[:-1]
    num = []
    for i in range(len(rows[0])-1, -1, -1):
        n = ""
        if all(rows[j][i] == " " for j in range(len(rows))):
            if op[count_op] == "+":
                final_sum += sum(num)
            if op[count_op] == "*":
                prod = 1
                for number in num:
                    prod *= number
                final_sum += prod
            num = []
            count_op -= 1
        else: 
            for j in range(len(rows)-1, -1, -1):
                if rows[j][i] != " ":
                    n = rows[j][i] + n
            
            num.append(int(n))
    
    if op[count_op] == "+":
        final_sum += sum(num)
    if op[count_op] == "*":
        prod = 1
        for number in num:
            prod *= number
        final_sum += prod
    num = []
    count_op -= 1    


    return final_sum

print(answer(part1(data),1,6))

print(answer(part2(data),2,6))