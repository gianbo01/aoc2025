from get_data import get_data

string = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
string = get_data()

ranges = [tuple(map(int, part.split("-"))) for part in string.split(",")]


def part1(ranges):
    count = 0
    for r in ranges:    
        for i in range(r[0], r[1]+1):
            s = str(i)
            h = len(s)//2
            if 2*h > 1 and 2*h % 2 == 0:
                if s[:h] == s[h:]:
                    count += i
    return count

def part2(ranges):
    count = 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            s = str(i)
            l = len(s)
            for div in range(l, 1, -1):
                if l%div == 0:
                    vect = []
                    s_tmp = s
                    for _ in range(div):
                        vect.append(s_tmp[:l//div])
                        s_tmp = s_tmp[l//div:]
                    if all(x == vect[0] for x in vect):
                        count += i
                        break
    return count

print(part1(ranges))
print(part2(ranges))