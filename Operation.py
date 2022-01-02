###########################################
# Filename    :  Operation.py
# Author      :  Muhammet Harun ATACAN
# Date        :  06.06.2021
# Description :  Operation Code
###########################################

import Interface
import numpy as np
from random import choice, randint
from PyQt5 import QtCore, QtWidgets

class Operation(QtWidgets.QWidget,Interface.Ui_tombala):
    
    def __init__(self):
        super(Operation,self).__init__()
        self.setupUi(self)                                                                  # Calls setupUi function
        self.set_clear()                                                                    # Calls set_clear function for reset the system
    
    ## Sets default features the game area
    
    def set_clear(self):
        
        self.xxyy = [ list(range(1,10)),                                                    # Defines list for 1th column
                      list(range(10,20)),                                                   # Defines list for 2nd column
                      list(range(20,30)),                                                   # Defines list for 3rd column
                      list(range(30,40)),                                                   # Defines list for 4th column
                      list(range(40,50)),                                                   # Defines list for 5th column
                      list(range(50,60)),                                                   # Defines list for 6th column
                      list(range(60,70)),                                                   # Defines list for 7th column
                      list(range(70,80)),                                                   # Defines list for 8th column
                      list(range(80,91)) ]                                                  # Defines list for 9th column
        
        self.player1Card_numbers = np.array( [[1, 0, 1, 0, 1, 0, 1, 1, 0],                  # Defines numpy array for gamer card-1
                                              [1, 1, 0, 1, 0, 1, 0, 1, 1],                  #
                                              [1, 0, 1, 0, 1, 0, 1, 0, 1]] )                #
        
        self.player2Card_numbers = np.array( [[1, 0, 1, 0, 1, 0, 1, 1, 0],                  # Defines numpy array for gamer card-2
                                              [1, 1, 0, 1, 0, 1, 0, 1, 1],                  #
                                              [1, 0, 1, 0, 1, 0, 1, 0, 1]] )                #
        
        self.pickNumbers = list(range(1, 91))                                               # Defines numberspool for pickNumbers
        self.player1_score = 0                                                              # Defines player1_score
        self.player2_score = 0                                                              # Defines player2_score
        self.retranslateUi(self)                                                            # Calls retranslateUi function
        self.flag = np.zeros(3,int)                                                         # Defines zeros filled numpy array for flags
    
    ## Returns the player1_score
    
    def get_player1_score(self):
        return self.player1_score
    
    ## Returns the player2_score
    
    def get_player2_score(self):
        return self.player2_score
    
    ## Connects the initcardButton with clicked_init_card function
    
    def setup_initCard(self):
        self.initcardButton.clicked.connect(self.clicked_init_card)
    
    ## Connects the pickButton with clicked_pick_btn function
    
    def setup_pickedNumber(self):
        self.pickButton.clicked.connect(self.clicked_pick_btn)
    
    ## Initializes the game area.
    
    def clicked_init_card(self):
        self.set_clear()                                                                    # Calls set_clear function for reset the system
        
        # Sets the first gamer-card (63-73)
        
        for row in range(0,3):
            for column in range(0,9):
                if self.player1Card_numbers[row][column] == 1:
                    self.player1Card_numbers[row][column] = choice(self.xxyy[column])
                    self.xxyy[column].remove(self.player1Card_numbers[row][column])
        self.player1Card_numbers[1][0] = choice(self.xxyy[randint(0,8)])
        
        for row in range(0,3):
            for column in range(0,9):
                if self.player1Card_numbers[row][column] != 0:
                    self.player1Card.item(row,column).setText(str(self.player1Card_numbers[row][column]))
        
        # Sets the second gamer-card (77-87)
        
        for row in range(0,3):
            for column in range(0,9):
                if self.player2Card_numbers[row][column] == 1:
                    self.player2Card_numbers[row][column] = choice(self.xxyy[column])
                    self.xxyy[column].remove(self.player2Card_numbers[row][column])
        self.player2Card_numbers[1][0] = choice(self.xxyy[randint(0,8)])
        
        for row in range(0,3):
            for column in range(0,9):
                if self.player2Card_numbers[row][column] != 0:
                    self.player2Card.item(row,column).setText(str(self.player2Card_numbers[row][column]))
    
    ## When clicked pick button, shows the action taken
        
    def clicked_pick_btn(self):
        
        self.picked_numbers=(choice(self.pickNumbers))
        self.pickNumbers.remove(self.picked_numbers)
        
        self.pickedButton.setText(str(self.picked_numbers))
        
        self.controller()                                                                   # Calls controller function for control the system
        
        self.scoreBox1.setText(str(self.get_player1_score()))
        self.scoreBox2.setText(str(self.get_player2_score()))
        
        self.message_box_win()                                                              # Calls message_box_win function when activate clicked_pick_btn
    
    ## Controls equality between picked number and number sets
   
    def controller(self):
        
        for row in range(0,3):
            for column in range(0,9):
                if ((self.player1Card_numbers[1][0] != self.picked_numbers) & (self.player2Card_numbers[1][0] != self.picked_numbers)):
                    
                    if self.player1Card_numbers[row][column] == self.picked_numbers:
                        self.lbl6.setText("Player 1 has %d" % (self.picked_numbers))
                        self.player1Card.item(row,column).setText("X")
                        self.player1Card_numbers[row][column] = 100
                        break
                        
                    elif self.player2Card_numbers[row][column] == self.picked_numbers:
                        self.lbl6.setText("Player 2 has %d" % (self.picked_numbers))
                        self.player2Card.item(row,column).setText("X")
                        self.player2Card_numbers[row][column] = 100
                        break
                    
                    else:
                        self.lbl6.setText("Players have not %d" % (self.picked_numbers))
            else:
                continue
            break
        
        ctr = np.zeros((2,3),int)                                                           # Defines zeros filled numpy array for counters
        
        
        # Checks player cards if it provides condition, counter will be up (135-140)
        
        for i in range(0,3):
            for j in range(0,9):
                if self.player1Card_numbers[i][j] == 100:
                    ctr[0][i] += 1
                if self.player2Card_numbers[i][j] == 100:
                    ctr[1][i] += 1    
        
        # Controls the counter and sets the players score (142-158)
        
        if (ctr[0][0] == 5) & (ctr[0][1] == 5) & (ctr[0][2] == 5) & (self.flag[2]==0):
            self.player1_score += 40
            self.flag[2] += 1
        elif ((ctr[0][0] == 5) | (ctr[0][1] == 5)) & ((ctr[0][0] == 5) | (ctr[0][2] == 5)) & ((ctr[0][1] == 5) | (ctr[0][2] == 5)) & (self.flag[1]==0):
            self.player1_score += 20
            self.flag[1] += 1
        elif ((ctr[0][0] == 5) | (ctr[0][1] == 5) | (ctr[0][2] == 5)) & (self.flag[0]==0):
            self.player1_score += 10
            self.flag[0] += 1
        
        if (ctr[1][0] == 5) & (ctr[1][1] == 5) & (ctr[1][2] == 5) & (self.flag[2]==0):
            self.player2_score += 40
            self.flag[2] += 1
        elif ((ctr[1][0] == 5) | (ctr[1][1] == 5)) & ((ctr[1][0] == 5) | (ctr[1][2] == 5)) & ((ctr[1][1] == 5) | (ctr[1][2] == 5)) & (self.flag[1]==0):
            self.player2_score += 20
            self.flag[1] += 1
        elif ((ctr[1][0] == 5) | (ctr[1][1] == 5) | (ctr[1][2] == 5)) & (self.flag[0]==0):
            self.player2_score += 10
            self.flag[0] += 1
    
    ## Checks the winning player and prints it on the screen
        
    def message_box_win(self):
        
        if ((self.flag[0]!=0) & (self.flag[1]!=0) & (self.flag[2]!=0)):
            
            msg_win = QtWidgets.QMessageBox()
            msg_win.setWindowTitle('Congratulations')
            msg_win.setIcon(QtWidgets.QMessageBox.Information)
            msg_win.setStandardButtons(QtWidgets.QMessageBox.Ok) 
            
            if (self.get_player1_score() > self.get_player2_score()):
                msg_win.setText('\nPlayer 1 has won.')
                
            else:
                msg_win.setText('\nPlayer 2 has won.')
            
            answer = msg_win.exec_()    
            
            if answer == QtWidgets.QMessageBox.Ok:
                msg_win2 = QtWidgets.QMessageBox()
                msg_win2.setWindowTitle('Information')
                msg_win2.setText('Are you sure to quit ?')
                msg_win2.setIcon(QtWidgets.QMessageBox.Information)
                msg_win2.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Retry)
                msg_win2.setDefaultButton(QtWidgets.QMessageBox.No)
                player_answer = msg_win2.exec_()
                
                if player_answer == QtWidgets.QMessageBox.Yes:
                    QtCore.QCoreApplication.quit()
                    
                if player_answer == QtWidgets.QMessageBox.Retry:
                    self.clicked_init_card()                                                # Calls clicked_init_card function for restart the game