def minion_game(string):
    kevin_pnts = 0
    stuart_points = 0

    cnt = 0

    for char in string:
        if (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
            kevin_pnts += len(string) - cnt
        else:
            stuart_points += len(string) - cnt

        cnt += 1

    if (kevin_pnts > stuart_points):
        print("Kevin", kevin_pnts)
    elif (kevin_pnts < stuart_points):
        print("Stuart", stuart_points)
    else:
        print("Draw")

    # your code goes here


if __name__ == '__main__':
    s = input()
    minion_game(s)