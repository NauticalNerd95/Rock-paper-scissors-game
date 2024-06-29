import random
while True:
 case = (random.randint(1,3))
 if case == 1:
   GUESS = 'paper'
 elif case == 2:
   GUESS = 'scissor'
 else:
   GUESS = 'rock'
   print('Let us play ROCK PAPERS SCISSORS?')
   print('What is your move(R,S,P)')
   move = str(input())
   if move == 'R':
    if move == 'R' and case == 1:
      print(str(GUESS) + '...')
      print('YOU LOST,want to play again?(Y/N)')
      print('WANNA PLAY AGAIN?(Y/N)')
      option = str(input())
      if option == 'Y':
        continue
      elif option == 'N':
        break
      else:
        print('Wrong input mate, Go get some rest')
    elif move == 'R' and case == 2:
     print(str(GUESS) + '...')
     print('YOU WON')
     print('WANNA PLAY AGAIN?(Y/N)')
     option = str(input())
     if option == 'Y':
       continue
     elif option == 'N':
       break
     else:
       print('Wrong input mate, Go get some rest')
    else:
     print(str(GUESS) +'...')
     print('THAT IS A TIE')
     print('WANNA PLAY AGAIN?(Y/N)')
     option = str(input())
     if option == 'Y':
       continue
     elif option == 'N':
       break
     else:
       print('Wrong input mate, Go get some rest')
   if move == 'S':
    if move == 'S' and case == 1:
       print(str(GUESS) + '...')
       print('You WON!!')
       print('WANNA PLAY AGAIN?(Y/N)')
       option = str(input())
       if option == 'Y':
         continue
       elif option == 'N':
         break
       else:
         print('Wrong input mate, Go get some rest')
    elif move == 'S' and case == 2:
      print(str(GUESS) + '...')
      print('That is a TIE! phewww')
      print('WANNA PLAY AGAIN?(Y/N)')
      option = str(input())
      if option == 'Y':
        continue
      elif option == 'N':
        break
      else:
        print('Wrong input mate, Go get some rest')
    else:
      print(str(GUESS) + '...')
      print('you LOST..better luck next time buddy')
      print('WANNA PLAY AGAIN?(Y/N)')
      option = str(input())
      if option == 'Y':
        continue
      elif option == 'N':
        break
      else:
        print('Wrong input mate, Go get some rest')
   if move == 'P':
    if move == 'P' and case == 3:
       print(str(GUESS) + '...')
       print('You WON!!')
       print('WANNA PLAY AGAIN?(Y/N)')
       option = str(input())
       if option == 'Y':
         continue
       elif option == 'N':
         break
       else:
         print('Wrong input mate, Go get some rest')
    elif move == 'P' and case == 1:
      print(str(GUESS) + '...')
      print('That is a TIE! phewww')
      print('WANNA PLAY AGAIN?(Y/N)')
      option = str(input())
      if option == 'Y':
        continue
      elif option == 'N':
        break
      else:
        print('Wrong input mate, Go get some rest')
    else:
      print(str(GUESS) + '...')
      print('you LOST..better luck next time buddy')
      print('WANNA PLAY AGAIN?(Y/N)')
      option = str(input())
      if option == 'Y':
        continue
      elif option == 'N':
        break
      else:
        print('Wrong input mate, Go get some rest')