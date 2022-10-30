# 5.3 Создайте программу для игры в ""Крестики-нолики"".
#
print('\033[95m' + "Игра Крестики-нолики" + '\033[0m')

board = list(range(1,10))

def draw_board(board):
   print("-*-" * 5)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-*-" * 5)

def take_input(player_token1):
   valid = False
   while not valid:
      player_answer = input('\033[93m' + "Куда поставим: "  + '\033[0m' + player_token1+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token1
            valid = True
         else:
            print('\033[91m' + "Нельзя поставить в занятую клетку!" + '\033[0m')
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input('\033[1m' + "Х" + '\033[0m')
        else:
           take_input('\033[1m' + "O" + '\033[0m')
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print('\033[94m' + "Игрок" + '\033[0m', tmp, '\033[94m' + "выиграл!" + '\033[0m')
              win = True
              break
        if counter == 9:
            print('\033[36m' + "Ничья!" + '\033[0m')
            break
    draw_board(board)
main(board)

input('\033[1m'"Спасибо за игру: нажмите Enter для выхода!" + '\033[0m')