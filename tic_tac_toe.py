import random

class tic_tac_toe(object):
    '''Class to implement tic-tac-toe game'''
    
    def __init__(self,player1 = None, player2 = None):
        '''Initial setup. Two players, player marks, board and available spots on the board'''
        self.player = [None,player1,player2]
        self.player_mark = [None, '','']
        self.board = [' ' for i in range(10)]
        self.available =  [str(i) for i in range(10)]
        
                                
    def display_board(self):
        '''Displays board and available sports for the players'''
        b = self.board
        a = self.available
        print()
        print('Available' + '    ' + 'Board')
        print(' Moves\n')
        print(a[7] + '|' + a[8] + '|' + a[9] + '        ' + b[7] + '|' + b[8] + '|' + b[9])
        print('-'*5 + '        ' + '-'*5)
        print(a[4] + '|' + a[5] + '|' + a[6] + '        ' + b[4] + '|' + b[5] + '|' + b[6])
        print('-'*5 + '        ' + '-'*5)
        print(a[1] + '|' + a[2] + '|' + a[3] + '        ' + b[1] + '|' + b[2] + '|' + b[3])
        print()
        
    def get_player_info(self):
        '''Get player names and mark for each player. Randomly choose who will play first. If playing again'''
        if None in self.player[1:]:
            self.player[1] = input('Player1, please input your name: ').capitalize()
            self.player[2] = input('Player2, please input your name: ').capitalize()
        
        
        self.going_first = random.randint(1,2)
        
        print(f"{self.player[self.going_first]} you will be playing first!!!")
        self.player_mark[1] = input(f"{self.player[self.going_first]} Please, choose your symbol 'X' or 'O': ").upper()
        
        while self.player_mark[1] not in ['X','O']:
                self.player_mark[1] = input(f"{self.player[self.going_first]} Please, choose your symbol 'X' or 'O': ").upper()
        
        ## Storing the players in the list in the order they will be playing
        if self.going_first == 2: self.player[1:2] = self.player[:-3:-1]  
        self.player_mark[1:] = ['X','O'] if self.player_mark[1] == 'X' else ['O','X'] 
        
     
    def update_board(self,loc,mark):
        '''Input: location on the board and mark to be placed
            Updates the board and available spots based on the user input.
        '''
        self.board[loc] = mark
        self.available[loc] = ' '
        
        
    def win_check(self,mark):
        '''Checks board to see if anybody won'''
        # Checks 3 rows , 3 columns and 2 diagonals
        list_of_indices_to_check = [
                                    [1,2,3],[4,5,6],[7,8,9],
                                    [1,4,7],[2,5,8],[3,6,9],
                                    [3,5,7],[1,5,9]
                                   ]
        for indx in list_of_indices_to_check:
            if [self.board[i] for i in indx] == [mark]*3:
                return True
        return False

    def is_board_full(self):
        '''Check to see if board is full'''
        for i in self.available[1:]:
            if i != ' ':
                return False
        return True
    
    def is_spot_open(self,spot):
        '''Returns boolean based on if input spot is taken or empty'''
        return self.board[spot] == ' '
            
    
    def interact_with_player(self):
        '''Interact with palyer to get player choices. Update the board based on player choice. Displays the board and available choices.
           After each player chose, checks to see if anyone Won or board is full. 
        '''
        game_on = True
        who_is_playing = 1
            
        while game_on:
            spot = int(input(f'{self.player[who_is_playing]} Please, choose a number between (1-9) to place your mark: '))
            
            while not self.is_spot_open(spot):
                spot = int(input(f'{self.player[who_is_playing]} Please, choose a different number. Spot you chose is already taken. '))
                
            self.update_board(spot,self.player_mark[who_is_playing])
            self.display_board()
            if self.win_check(self.player_mark[who_is_playing]):
                print(f'Congratualtions.... {self.player[who_is_playing]}. You Won!!!')
                break
            
            if self.is_board_full():
                print(f'Game draw')
                break
            ## Switing to a different player
            who_is_playing = 2 if who_is_playing == 1 else 1
    
    def play_another_game(self):
        '''Asks players for play again. Resets board and available moves if palying again'''
        if input('Do you want to play another game? ').lower().startswith('y'):
            print()
            self.board = [' ' for i in range(10)]
            self.available =  [str(i) for i in range(10)]
            return True
        else:
            print()
            return False
        
            
        
if __name__ == '__main__':
    ## Driver code
    game = tic_tac_toe()
    game.get_player_info()
    game.interact_with_player()
    while game.play_another_game():
        game.get_player_info()
        game.interact_with_player()
    else:
        print('Thanks for Playing')
    
