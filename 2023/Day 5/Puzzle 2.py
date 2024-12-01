#Advent of Code 2023 Day 5 Puzzle 1
import re

inputs = []
score = 0
result = 0

with open("2023/Day 5/data.txt") as f:
    inputs = f.read().replace("seeds: ", "").replace("seed-to-soil map:\n", "").replace("soil-to-fertilizer map:\n", "").replace("fertilizer-to-water map:\n", "").replace("water-to-light map:\n", "").replace("light-to-temperature map:\n", "").replace("humidity-to-location map:\n", "").replace("temperature-to-humidity map:\n", "").split("\n\n")


seeds = inputs[0].split(" ")
seed_2_soil = inputs[1].split("\n")
soil_2_fertilizer = inputs[2].split("\n")
fertilizer_2_water = inputs[3].split("\n")
water_2_light = inputs[4].split("\n")
light_2_temp = inputs[5].split("\n")
temp_2_humidity = inputs[6].split("\n")
humidity_2_location = inputs[7].split("\n")

maps = [seed_2_soil, soil_2_fertilizer, fertilizer_2_water, water_2_light, light_2_temp, temp_2_humidity, humidity_2_location]

def getNewNumbers(locs: list, map: list) -> list:

    for i, location in enumerate(locs):

        print(i, end="\r")
        for entry in map:

            tmp = entry.split(" ")

            if int(tmp[1]) <= location and location < (int(tmp[1]) + int(tmp[2])):
                
                locs[i] = int(tmp[0]) - int(tmp[1]) + location
                break

    return locs
            

locations = []
nearest_locations = []

for i in range(int(len(seeds) / 2)):

    locations = list(range(int(seeds[2 * i]), int(seeds[2 * i]) + int(seeds[2 * i + 1])))
    
    for map in maps:

        print("new map")
        locations = getNewNumbers(locations, map)

    nearest_locations.append(min(locations))
    print(nearest_locations)



print(min(nearest_locations)) #324724204