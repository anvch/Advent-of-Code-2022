def getTotalScore():
    f = open("RPS Strategy Guide.txt", "r")
    
    score = 0

    for line in f:
        game = line.strip()
        opp_move = game[0]
        my_move = game[1]

        if opp_move == "A": # rock
            if my_move == "X": # rock
                score += 1
                score += 3
            if my_move == "Y": # paper
                score += 2
                score += 6
            if my_move == "Z": # scissors
                score += 3
                score += 0

        if opp_move == "B": # paper
            if my_move == "X": # rock
                score += 1
                score += 0
            if my_move == "Y": # paper
                score += 2
                score += 3
            if my_move == "Z": # scissors
                score += 3
                score += 6

        if opp_move == "C": # scissors
            if my_move == "X": # rock
                score += 1
                score += 6
            if my_move == "Y": # paper
                score += 2
                score += 0
            if my_move == "Z": # scissors
                score += 3
                score += 3

    print(score)


getTotalScore()