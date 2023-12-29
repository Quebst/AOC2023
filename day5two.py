raw_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    seeds = []

    _, temp = lines[0].split(":")
    seeds = list(map(int, temp.split()))

    print(seeds)
    transforms = []
    mapr = []
    lowest = float('inf')
    # build a list of transforms, each being a list of ranges for that transform
    for line in lines:
        if line.startswith("seeds"):
            pass
        elif line == "seed-to-soil map:":
            seed_soil = []
            transforms.append(seed_soil)
            mapr = seed_soil
        elif line == "soil-to-fertilizer map:":
            soil_fert = []
            transforms.append(soil_fert)
            mapr = soil_fert
        elif line == "fertilizer-to-water map:":
            fert_water = []
            transforms.append(fert_water)
            mapr = fert_water
        elif line == "water-to-light map:":
            water_light = []
            transforms.append(water_light)
            mapr = water_light
        elif line == "light-to-temperature map:":
            light_temp = []
            transforms.append(light_temp)
            mapr = light_temp
        elif line == "temperature-to-humidity map:":
            temp_humid = []
            transforms.append(temp_humid)
            mapr = temp_humid
        elif line == "humidity-to-location map:":
            humid_location = []
            transforms.append(humid_location)
            mapr = humid_location
        elif line == "":
            pass
        else:
            mapper(mapr, line)

    while len(seeds) > 0:
        start = seeds.pop(0)
        value = seeds.pop(0)
        
        for i in range(value):
            answer = start
            for trans in transforms:
                for rang in trans:
                    source, end_source, dest = rang
                    if source <= answer <= end_source:
                        difference = answer - source
                        answer = dest + difference
                        break

            if answer < lowest:
                lowest = answer
                print(lowest)
                
            start += 1

    print(lowest)


def mapper(map_one, line):
    dest, source, length = map(int, line.split())
    end_source = source + length
    rang = [source, end_source, dest]

    map_one.append(rang)


if __name__ == "__main__":
    main()
