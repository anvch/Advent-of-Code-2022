def getMaxCalories():

    f = open("Elf Calorie List.txt", "r")

    total_calories = []
    total = 0

    for line in f:
        if not(line.strip() == ""):
            line = line.strip()
            calories = int(line)
            total += calories
        else:
            total_calories.append(total)
            total = 0

    f.close()

    max_cal = max(total_calories)

    print(max_cal)


getMaxCalories()

