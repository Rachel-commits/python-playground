import random

#Write your game of chance functions here

def coin_flip(choice,bet):
  num=random.randint(1,10)

  if num<6 :
    outcome ='heads'
  else:
    outcome = 'tails'
  print(outcome)
  if choice == outcome:
    return bet
  else:
    return -1*bet

def cho_han(choice,bet):
  dice1=random.randint(1,6)
  dice2=random.randint(1,6)
  outcome =dice1+dice2
  if outcome%2 == 0:
    odd_even = 'Even'
  else:
    odd_even = 'Odd'
  print (outcome)
  print (odd_even)

  if choice == odd_even:
    return bet
  else:
    return -1*bet

def roulette(choice,bet):

  #check if they bet odd even or number
  if choice =='Odd' or choice=='Even':
    bet_number =False
    print("You bet ", choice)
  elif type(choice)==int and choice >=0 and choice<=37:
    bet_number =True
    print("you bet a number ", choice)
  else:
    print("Your choice is invalid", choice)
    return 0

  #Randomise numbers 1-36 and 37 is the 0
  outcome=random.randint(1,37)
  if outcome ==37:
    outcome =0;
  print("The wheel landed on ", outcome)

  #Logic if they bet odd/even
  if bet_number== False:
    if outcome%2 == 0:
      odd_even = 'Even'
    else:
      odd_even = 'Odd'
    print("which is", odd_even )
      #if they bet odd even and lands on 0 they lose
    if outcome ==0:
       return -1*bet
       print("It landed on 0 you lose ",bet)
      #else check the odd even vs their bet
    if choice == odd_even:
      print("You win ",bet)
      return bet
    else:
      print("You lose ",bet)
      return -1*bet

    # else check the number logic
  elif bet_number== True:
    if choice == outcome:
      print ("You win ",35*bet)
      return 35*bet
    else:
      print ("You lose ", -1*bet)
      return -1*bet




#Call your game of chance functions here

#print(coin_flip('heads',25))

#print(cho_han('Odd',10))
def play(money,choice, bet):
  if bet>money:
    print ("YOU DON'T HAVE ENOUGH MONEY! You have",money,"and you bet",bet)
    return money
  print("You started with £", money)
  money+=roulette(choice,bet)
  print ("You now have £",money)
  print("")
  return money

money=100
money= play(money,33,10)
money= play(money,'odd',30)
money= play(money,'Odd',30)
money= play(money,'39',30)
money= play(money,'Even',30)
money= play(money,'Even',50)
money= play(money,'Even',50)

# play(False,333,10)
