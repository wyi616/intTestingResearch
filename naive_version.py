from scipy import special
# import matplotlib.pyplot as rowPlot
import math
import random

#Research Attempt #1
# approach is to pick random symbol from v, then constructively add one column & one row at a time
# to CA via adding one value to right of rightmost topmost value, and one value underneath leftmost bottommost
# value then find best position to add for every don't care position (or random if you can't add any new interactions)

def interCounter(row, seenInteractions):
  CA = []
  intSeenCA = []
  intCount = 0
  for cols in itertools.combination(range(len(row), t):
    vals = row[cols]
    CA.append(list(cols), list(vals))

  for cols in CA:
    for index in range(len(seenInteractions)):
      if row[cols] = seenInteraction[index]
        intCount = intCount +1
        intSeen = str(row[cols])+"; "+str(cols)
        intSeenCA.append(intSeen)
  return intSeenCA

#t = 2
def naiveDiagonalApproach(t,k,v):
    CA = []
    # pick random symbol to start the covering array
    random_sym, unseenInterCount, seenInteractions = random.randint(0,v-1), v**t*(special.binom(k,t)), set()
    row = [-1]*(k-1)
    row.insert(0,random_sym)
    CA.append(row)
    # while there's unseen interactions:
    while unseenInterCount > 0:
        # interCounter(row,seenInteractions) > 0:
        # add random symbol to right of topright symbol
        for i in range(len(CA[0])):
            if CA[0][i] == -1:
                CA[0][i] = random.randint(0,v-1)
                break
        # and a random symbol to bottom of leftbottom symbol
        row = [-1]*(k-1)
        row.insert(0,random.randint(0,v-1))
        # for every don't care(-1's), either pick symbol that
        # maximizes coverage, or pick random if coverage can't be maximized
        for row in CA:
            for i in range(len(row)):
                greatestSeen, toAdd = -1 = 0
                for sym in range(v):
                    row[i] = sym
                    if interCounter(row,seenInteractions) > greatestSeen:
                        toAdd = sym
                if toAdd == -1:
                    toAdd = random.randint(0,v-1)
                row[row.index(-1)] = toAdd
                seenInteractions.update(interCounter(row,seenInteractions))

    return CA
