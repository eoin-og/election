import math
from decimal import *

def assignVotes(cands, array, coef):
    
    for vote in array:
        if len(vote) != 0:
            value = vote[0]
            vote.remove(value)
            for cand in cands:
                counted = False
                while counted != True:
                    if cand.name == value:
                        if cand.elected or cand.eliminated:
                            value = vote[0]
                            vote.remove(value)
                        else:
                            counted = True
                            cand.votes += (1000*coef)
                            cand.ballads.append(vote)
                    else: counted = True

def whatNow(cands, numWins, votes):
    threshold = ((1000/(numWins+1))*votes) +1000
    for cand in cands:
        if cand.votes > threshold:
            if cand.elected == False:
                return 1
    return 2
        
def eliminate(cands):
    minCand = cands[0]
    for cand in cands:
        if cand.elected == False and cand.eliminated == False:
            if cand.votes < minCand.votes:
                minCand = cand
    for cand in cands:
        if cand == minCand:
            cand.eliminated = True
    assignVotes(cands, minCand.ballads, 1)

def elect(cands, numWins, votes):
    maxCand = cands[0]
    for cand in cands:
        if cand.elected == False and cand.eliminated == False:
            if cand.votes > maxCand.votes:
                maxCand = cand
    for cand in cands:
        if cand == maxCand:
            cand.elected = True
    threshold = ((1000/(numWins+1))*votes) +1000
    surplus = maxCand.votes - threshold
    coef = Decimal(surplus)/maxCand.votes
    assignVotes(cands, maxCand.ballads, coef)

def printResults(cands):
    print ('\n**********************\n')
    for cand in cands:
        if cand.elected:
            print (cand.name + ': Elected')
        elif cand.eliminated:
            print (cand.name + ': Eliminated')
        else: print (cand.name + ': ' + str(cand.votes))
    


class candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.ballads = []
        self.eliminated = False
        self.elected = False

#below section only needed for testing
"""
Alex = candidate('A')
Bob = candidate('B')
Cat = candidate('C')
Dude = candidate('D')


candidates = (Alex, Bob, Cat, Dude)

#ten voters
votes = [
    ['B', 'C', 'A', 'D'],
    ['B', 'C', 'A', 'D'],
    ['C', 'A', 'D', 'B'],
    ['B', 'C', 'A', 'D'],
    ['B', 'A','C'],
    ['B', 'D', 'A', 'C'],
    ['A', 'B', 'C', 'D'],
    ['D', 'A', 'B', 'C'],
    ['D', 'C', 'A', 'B'],
    ['D', 'A', 'B', 'C'] ]


assignVotes(candidates, votes, 1)


quota = 2
elected = 0
numCands = len(candidates)

while elected < quota:
    printResults(candidates)
    check = whatNow(candidates, 2, 10)
    print (check)
    if  check == 2:
        eliminate(candidates)
        numCands += -1
    else:
        elect(candidates, 2, 10)
        elected += 1
        numCands += -1
    if numCands == 2:
        break
        
    
printResults(candidates)
"""


    

    
