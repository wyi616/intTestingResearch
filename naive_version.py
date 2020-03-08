from scipy import special
# import matplotlib.pyplot as rowPlot
import math
import random

# Research Attempt #1
# approach is to pick random symbol from v, then constructively add one column & one row at a time
# to CA via adding one value to right of rightmost topmost value, and one value underneath leftmost bottommost
# value then find best position to add for every don't care position (or random if you can't add any new interactions)

def interCounter(row, seenInteractions):
  CA = []
  newInters = set()
  for i in range(len(row)):
      for j in range(i+1,len(row)):
          if row[i] != -1 and row[j] != -1:
              interaction = ''.join([str(row[i]),str(row[j]),'r',str(i),'c',str(j)]);
              if interaction not in seenInteractions:
                  newInters.add(interaction)
  return newInters

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
                if row[i] == -1:
                    greatestSeen, toAdd = -1, -1
                    for sym in range(v):
                        row[i] = sym
                        if interCounter(row,seenInteractions) > greatestSeen:
                            toAdd = sym
                    if toAdd == -1:
                        toAdd = random.randint(0,v-1)
                    row[i] = toAdd
                    seenInteractions.update(interCounter(row,seenInteractions))
    return CA


if __name__ == '__main__':
    naiveDiagonalApproach(2,7,2)
