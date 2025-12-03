from get_data import get_data

STARTING_POINT = 50

def part1(actions):
    dial = STARTING_POINT
    count = 0

    for action in actions:
        n = int(action[1:]) if action[0] == "R" else -int(action[1:])
        
        dial += n
        if dial < 0 or dial > 99:
            dial = dial % 100

        count += 1 if dial == 0 else 0

    return count

def part2(actions):
    count = 0
    dial = STARTING_POINT
    

    for action in actions:
        n = int(action[1:]) if action[0] == "R" else -int(action[1:])
        tmp = dial + n
        if tmp <= 0:
            count += abs(tmp//100)
            if tmp % 100 == 0:
                count += 1
            if dial == 0:
                count -= 1
        elif tmp >= 100:
            count += tmp//100
        dial = tmp % 100
    return count

actions = get_data().splitlines()
print("Part 1:", part1(actions))
print("Part 2:", part2(actions))
