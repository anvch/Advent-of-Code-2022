def getMaxCalories() -> list():

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

    return total_calories


def getTopThree(total_calories: list()):
    
    top3 = 0

    for i in range(3):
        top = max(total_calories)
        top3 += top
        total_calories.remove(top)

    print(top3)

getTopThree(getMaxCalories())

