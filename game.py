import random
import sys

SIDE_LEN = 8
grid = [[0 for x in range(SIDE_LEN)] for y in range(SIDE_LEN)]

""" The player will use the white cells
and the AI will use the black ones """
def main():
  init()
  curTurn = 1
  failedMove = 0
  draw()
  while failedMove < 2:
    validMoves = getAvailableMoves(curTurn)
    if len(validMoves) == 0:
      failedMove +=1
      curTurn = 1 - curTurn
      continue
    failedMove = 0
    if curTurn == 0:
      #AI turn
      nextMove = getAIMove(validMoves)
    else:
      nextMove = getPlayerMove(validMoves)
    playAndUpdate(nextMove, curTurn)
    draw()
    if curTurn == 1:
      dummy = input("Well done!!\nPress enter to give the AI his next move.")
    curTurn = 1 - curTurn
  finalScore = calculateScore()
  print("Your score is: %d and the AI score is: %d" %(finalScore[0], finalScore[1]))
  if finalScore[0] > finalScore[1]:
    print("You Won :D !!!")
  elif finalScore[1] > finalScore[0]:
    print("You lose :( !!!")
  else:
    print("Tie game !!!")

""" the values (-1, 0, 1) is equal to empty,
Black and white respectivly """
def init():
  for i in range(SIDE_LEN):
    for j in range(SIDE_LEN):
      grid[i][j] = -1
  grid[3][3] = 0
  grid[3][4] = 1
  grid[4][3] = 1
  grid[4][4] = 0

"""
updated to run on python2
"""
def draw():
  for j in range(SIDE_LEN):
    sys.stdout.write('---')
    #print("---", end = '')
  print('-')
  for i in range(SIDE_LEN):
    sys.stdout.write('|')
    #print("|", end = '')
    for j in range(SIDE_LEN):
      if grid[i][j] == -1:
        sys.stdout.write("%2d" % (i*8+j))
        #print("%2d" % (i*8+j), end = '')
      elif grid[i][j] == 0:
        sys.stdout.write("%2s" % "*")
        #print("%2s" % "*", end = '')
      else:
        sys.stdout.write("%2s" % "@")
        #print("%2s" % "@", end = '')
      sys.stdout.write('|')
      #print("|", end = '')
    print('')
    for j in range(SIDE_LEN):
      sys.stdout.write('---')
      #print("---", end = '')
    print('-')

DIRECTION_COUNT = 8
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def getAvailableMoves(turn):
  validMoves = []
  for i in range(SIDE_LEN):
    for j in range(SIDE_LEN):
      if grid[i][j] != -1 :
        continue
      for k in range(DIRECTION_COUNT):
        ME_Cnt = 0
        AI_Cnt = 0
        cur_X = i + dx[k]
        cur_Y = j + dy[k]
        while cur_X >= 0 and cur_Y >= 0 and cur_X < SIDE_LEN and cur_Y < SIDE_LEN:
          if grid[cur_X][cur_Y] == 1-turn:
            AI_Cnt += 1            
            cur_X += dx[k]
            cur_Y += dy[k]
          elif grid[cur_X][cur_Y] == turn:
            ME_Cnt += 1
            break
          else: break
        if ME_Cnt * AI_Cnt > 0:
          validMoves.append(i*8+j)
          break
  return validMoves

"""****************************************************************************************"""
"""This functoin needs to be updated to handel if return pressed without entering any value"""
"""****************************************************************************************"""
def getPlayerMove(AvailableMoves):
  nextMove = int(input("Please choose your next move.")) 
  while nextMove not in AvailableMoves:
    nextMove = int(input("Wrong move!!!\nPlease choeese your next valid move."))
  return nextMove

def playAndUpdate(cellValue, turn):
  i = cellValue // SIDE_LEN
  j = cellValue % SIDE_LEN
  for k in range(DIRECTION_COUNT):
    ME_Cnt = 0
    AI_Cnt = 0
    cur_X = i + dx[k]
    cur_Y = j + dy[k]
    while cur_X >= 0 and cur_Y >= 0 and cur_X < SIDE_LEN and cur_Y < SIDE_LEN:
      if grid[cur_X][cur_Y] == 1-turn:
        AI_Cnt += 1            
        cur_X += dx[k]
        cur_Y += dy[k]
      elif grid[cur_X][cur_Y] == turn:
          ME_Cnt += 1
          break
      else: break
    if ME_Cnt * AI_Cnt > 0:
      cur_X = i + dx[k]
      cur_Y = j + dy[k]
      while cur_X >= 0 and cur_Y >= 0 and cur_X < SIDE_LEN and cur_Y < SIDE_LEN:
        if grid[cur_X][cur_Y] == 1-turn:
          grid[cur_X][cur_Y] = turn            
          cur_X += dx[k]
          cur_Y += dy[k]
        else: break
  grid[i][j] = turn

def getAIMove(AvailableMoves):
  size = len(AvailableMoves)
  nextMove = random.randint(0,size - 1)
  return AvailableMoves[nextMove]

def calculateScore():
  score = [0, 0]
  for i in range(SIDE_LEN):
    for j in range(SIDE_LEN):
      if grid[i][j] == 1:
        score[0] +=1
      elif grid[i][j] == 0:
        score[1] +=1
  return score

if __name__ == '__main__':
  main()