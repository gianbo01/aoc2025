from get_data import get_data, answer

database = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]

database = get_data(5).splitlines()

id_ranges = database[:database.index("")]
ids = database[database.index("") + 1 :]
id_ranges = [(int(id.split("-")[0]), int(id.split("-")[1])) for id in id_ranges]

#print(id_ranges)

def part1(id_ranges, ids):
    count = 0
    for id in ids:
        for id_range in id_ranges:
            if int(id) >= id_range[0] and int(id) <= id_range[1]:
                count += 1
                break
    return count

def part2(id_ranges):
    count = 0
    no_overlap = True
    
    while no_overlap:
        no_overlap = False
        new_ranges = []
        for id_range in id_ranges:
            added = False
            for i in range(len(new_ranges)):
                if id_range[0] <= new_ranges[i][1] + 1 and id_range[1] >= new_ranges[i][0] - 1:
                    no_overlap = True
                    new_ranges[i] = (min(id_range[0], new_ranges[i][0]), max(id_range[1], new_ranges[i][1]))
                    added = True
                    break
            if not added:
                new_ranges.append(id_range)
        id_ranges = new_ranges
    
    #print(new_ranges)
    for id_range in new_ranges:
        count += id_range[1] - id_range[0] + 1
    
    return count

print(answer(part1(id_ranges, ids), 1, 5))

print(answer(part2(id_ranges), 2, 5))