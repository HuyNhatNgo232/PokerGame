print "(Notice that 0 will represent 10). please enter 0 instead of 10 or program will get error"
input = raw_input("Enter input: ")

suits = {'H': 0, 'D': 0, 'S': 0, 'C': 0}
ranks = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0, 'A': 0, 'J': 0, 'Q': 0, 'K': 0}

i = 0


while(i < len(input)):
    suit = input[i:i+1]
    rank = input[i+1:i+2]
    suits[suit] += 1
    ranks[rank] += 1
    i = i+2


def checkFourRank(ranks):
    count = 0
    for i in ranks:
        if ranks[i] == 4:
            count += 1

    if count == 1:
        return True
    else:
        return False

def checkFullHouse(ranks):
    count2 = 0
    count3 = 0
    for i in ranks:
        if ranks[i] == 2:
            count2 += 1
        if ranks[i] == 3:
            count3 += 1

    if count2 == 1 and count3 == 1:
        return True
    else:
        return False

def checkThreeCard(ranks):
    count = 0

    for i in ranks:
        if ranks[i] == 3:
            count += 1

    if count == 1:
        return True
    else:
        return False

def checkTwoPair(ranks):
    count = 0

    for i in ranks:
        if ranks[i] == 2:
            count += 1

    if count == 2:
        return True
    else:
        return False

def checkOnePair(ranks):
    count = 0

    for i in ranks:
        if ranks[i] == 2:
            count += 1

    if count == 1:
        return True
    else:
        return False


check4C = checkFourRank(ranks)
checkFH = checkFullHouse(ranks)
check3C = checkThreeCard(ranks)
check2P = checkTwoPair(ranks)
check1P = checkOnePair(ranks)


if(check4C):
    print "4C"
elif(checkFH):
    print "FH"
elif(check3C):
    print "3C"
elif(check2P):
    print "2P"
elif(check1P):
    print "1P"
else:
    print "nothing"





