###########################################
# Filename    :  Interface.py
# Author      :  Muhammet Harun ATACAN
# Date        :  06.06.2021
# Description :  Interface code
###########################################

from PyQt5 import QtCore, QtGui, QtWidgets 

class Ui_tombala(object):
    
    def __init__(self):
        
        self.player1_name = 'Player 1'                                                      # Defines player1_name
        self.player2_name = 'Player 2'                                                      # Defines player2_name
    
    ## Returns the player1_name
    
    def get_player1_name(self):
        return self.player1_name
    
    ## Returns the player2_name
    
    def get_player2_name(self):
        return self.player2_name
    
    ## This Section for first Gamer
    
    def player1_Card(self,tombala):
        
        self.player1Card = QtWidgets.QTableWidget(tombala)                                  # Creates new object
        self.player1Card.setGeometry(QtCore.QRect(20, 110, 362, 122))                       # Sets specifications about card geometry
        self.player1Card.setLayoutDirection(QtCore.Qt.LeftToRight)                          # Sets specifications about card layoutDirection
        self.player1Card.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)        # Sets specifications about card editTriggers
        self.player1Card.setRowCount(3)                                                     # Sets 3 rows
        self.player1Card.setColumnCount(9)                                                  # Sets 9 columns
        self.player1Card.setObjectName("player1Card")                                       # Sets the object name
        self.player1Card.horizontalHeader().setVisible(False)                               # Hides the horizontal header
        self.player1Card.horizontalHeader().setDefaultSectionSize(40)                       # Sets horizontal header size
        self.player1Card.verticalHeader().setVisible(False)                                 # Hides the vertical header
        self.player1Card.verticalHeader().setDefaultSectionSize(40)                         # Sets vertical header size
        self.player1Card.setFont(self.specifyFont("Arial", 15, 1, 75))                      # Sets font properties using specifyFont function
        
        
        for row in range(0,3):
            for column in range(0,9):
                
                item1 = QtWidgets.QTableWidgetItem()                                        # Creates new object
                item2 = QtWidgets.QTableWidgetItem()                                        # Creates new object
                item3 = QtWidgets.QTableWidgetItem()                                        # Creates new object
                brush1 = QtGui.QBrush(QtGui.QColor(255, 0, 127))                            # Sets specific colour
                brush1.setStyle(QtCore.Qt.SolidPattern)
                item1.setBackground(brush1)                                                 # Sets background colour
                item2.setForeground(brush1)                                                 # Sets foreground colour
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item3.setBackground(brush1)                                                 # Sets background colour
                brush1 = QtGui.QBrush(QtGui.QColor(255, 255, 255))                          # Sets specific colour
                brush1.setStyle(QtCore.Qt.SolidPattern)
                item3.setForeground(brush1)                                                 # Sets foreground colour
                item3.setTextAlignment(QtCore.Qt.AlignCenter)                               # Sets alignment
                
                if ((row==1) & (column==0)):
                    self.player1Card.setItem(row, column, item3)
                elif ((row==0) & ((column==1) | (column==3) | (column==5) | (column==8))):
                    self.player1Card.setItem(row, column, item1)
                elif ((row==1) & ((column==0) | (column==2) | (column==4) | (column==6))):
                    self.player1Card.setItem(row, column, item1)
                elif ((row==2) & ((column==1) | (column==3) | (column==5) | (column==7))):
                    self.player1Card.setItem(row, column, item1)
                else:
                    self.player1Card.setItem(row, column, item2)
            
    ## This Section for second Gamer
    
    def player2_Card(self,tombala):
        
        self.player2Card = QtWidgets.QTableWidget(tombala)                                  # Creates new object
        self.player2Card.setGeometry(QtCore.QRect(20, 350, 362, 122))                       # Sets specifications about card geometry
        self.player2Card.setLayoutDirection(QtCore.Qt.LeftToRight)                          # Sets specifications about card layoutDirection
        self.player2Card.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)        # Sets specifications about card editTriggers
        self.player2Card.setRowCount(3)                                                     # Sets 3 rows
        self.player2Card.setColumnCount(9)                                                  # Sets 9 columns
        self.player2Card.setObjectName("player2Card")                                       # Sets the object name
        self.player2Card.horizontalHeader().setVisible(False)                               # Hides the horizontal header
        self.player2Card.horizontalHeader().setDefaultSectionSize(40)                       # Sets horizontal header size
        self.player2Card.verticalHeader().setVisible(False)                                 # Hides the vertical header
        self.player2Card.verticalHeader().setDefaultSectionSize(40)                         # Sets vertical header size
        self.player2Card.setFont(self.specifyFont("Arial", 15, 1, 75))                      # Sets font properties using specifyFont function
        
        
        for row in range(0,3):
            for column in range(0,9):
                
                item1 = QtWidgets.QTableWidgetItem()
                item2 = QtWidgets.QTableWidgetItem()
                item3 = QtWidgets.QTableWidgetItem()
                brush1 = QtGui.QBrush(QtGui.QColor(66, 144, 245))                           # Sets specific colour
                brush1.setStyle(QtCore.Qt.SolidPattern)
                item1.setBackground(brush1)                                                 # Sets background colour
                item2.setForeground(brush1)                                                 # Sets foreground colour
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item3.setBackground(brush1)                                                 # Sets background colour
                brush1 = QtGui.QBrush(QtGui.QColor(255, 255, 255))                          # Sets specific colour
                brush1.setStyle(QtCore.Qt.SolidPattern)
                item3.setForeground(brush1)                                                 # Sets foreground colour
                item3.setTextAlignment(QtCore.Qt.AlignCenter)                               # Sets alignment
                
                if ((row==1) & (column==0)):
                    self.player2Card.setItem(row, column, item3)
                elif ((row==0) & ((column==1) | (column==3) | (column==5) | (column==8))):
                    self.player2Card.setItem(row, column, item1)  
                elif ((row==1) & ((column==0) | (column==2) | (column==4) | (column==6))):
                    self.player2Card.setItem(row, column, item1)
                elif ((row==2) & ((column==1) | (column==3) | (column==5) | (column==7))):
                    self.player2Card.setItem(row, column, item1)
                else:
                    self.player2Card.setItem(row, column, item2)
    
    ## This section for InitCardButton
    
    def init_Card(self,tombala):
                
         self.initcardButton = QtWidgets.QPushButton(tombala)                               # Creates new object
         self.initcardButton.setGeometry(QtCore.QRect(470, 110, 130, 60))                   # Sets specifications about card geometry
         self.initcardButton.setFont(self.specifyFont("Arial", 10, 1, 75))                  # Sets font properties using specifyFont function
    
    ## This section for pick number button and picked number box
    
    def pickNumber(self,tombala):
        
        self.pickButton = QtWidgets.QPushButton(tombala)                                    # Creates new object
        self.pickButton.setGeometry(QtCore.QRect(470, 190, 130, 60))                        # Sets specifications about card geometry
        self.pickButton.setFont(self.specifyFont("Arial", 10, 1, 75))                       # Sets font properties using specifyFont function

        self.pickedButton = QtWidgets.QToolButton(tombala)                                  # Creates new object
        self.pickedButton.setGeometry(QtCore.QRect(740, 150, 100, 100))                     # Sets specifications about card geometry
        self.pickedButton.setFont(self.specifyFont("Arial", 20, 1, 75))                     # Sets font properties using specifyFont function
        self.pickedButton.setStyleSheet("border-radius : 50; border : 2px solid black; background-color: rgb(245, 188, 66);")   # Changes square button to circular button and colour properties

    ## This section for score boxes
    
    def score_box(self,tombala):
        
        self.scoreBox1 = QtWidgets.QToolButton(tombala)                                     # Creates new object
        self.scoreBox1.setGeometry(QtCore.QRect(450, 390, 181, 71))                         # Sets specifications about card geometry
        self.scoreBox1.setFont(self.specifyFont("Arial", 20, 1, 75))                        # Sets font properties using specifyFont function
        
        self.scoreBox2 = QtWidgets.QToolButton(tombala)                                     # Creates new object
        self.scoreBox2.setGeometry(QtCore.QRect(690, 390, 181, 71))                         # Sets specifications about card geometry
        self.scoreBox2.setFont(self.specifyFont("Arial", 20, 1, 75))                        # Sets font properties using specifyFont function
    
    ## This section for labels
    
    def create_labels(self,tombala):
        
        self.lbl1 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl1.setGeometry(QtCore.QRect(20, 60, 362, 30))                                # Sets specifications about card geometry
        self.lbl1.setFont(self.specifyFont("Arial", 15, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl1.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
        
        self.lbl2 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl2.setGeometry(QtCore.QRect(20, 300, 362, 30))                               # Sets specifications about card geometry
        self.lbl2.setFont(self.specifyFont("Arial", 15, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl2.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
        
        self.lbl3 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl3.setGeometry(QtCore.QRect(450, 360, 181, 30))                              # Sets specifications about card geometry
        self.lbl3.setFont(self.specifyFont("Arial", 13, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl3.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
        
        self.lbl4 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl4.setGeometry(QtCore.QRect(690, 360, 181, 30))                              # Sets specifications about card geometry
        self.lbl4.setFont(self.specifyFont("Arial", 13, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl4.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
        
        self.lbl5 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl5.setGeometry(QtCore.QRect(730, 120, 121, 25))                              # Sets specifications about card geometry
        self.lbl5.setFont(self.specifyFont("Arial", 10, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl5.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
        
        self.lbl6 = QtWidgets.QLabel(tombala)                                               # Creates new object
        self.lbl6.setGeometry(QtCore.QRect(470, 60, 371, 30))                               # Sets specifications about card geometry
        self.lbl6.setFont(self.specifyFont("Arial", 15, 1, 75))                             # Sets font properties using specifyFont function
        self.lbl6.setAlignment(QtCore.Qt.AlignCenter)                                       # Sets alignment
    
    ## This section for setup User-interface
    
    def setupUi(self, tombala):
        
        tombala.setObjectName("tombala")                                                    # Sets the object name
        tombala.resize(900, 530)                                                            # Sets size geometry
        
        self.player1_Card(tombala)                                                          # Calls player1_Card function
        self.player2_Card(tombala)                                                          # Calls player2_Card function
        self.init_Card(tombala)                                                             # Calls init_Card function
        self.pickNumber(tombala)                                                            # Calls pickNumber function
        self.score_box(tombala)                                                             # Calls score_box function
        self.create_labels(tombala)                                                         # Calls create_labels function
        
        
        self.retranslateUi(tombala)                                                         # Calls retranslateUi function
        QtCore.QMetaObject.connectSlotsByName(tombala)
    
    ## This section sets the label texts
    
    def retranslateUi(self, tombala):
        
        _translate = QtCore.QCoreApplication.translate
        tombala.setWindowTitle(_translate("tombala", "Tombala of Legends"))                 # Sets the window-title
        
        self.lbl1.setText(_translate("tombala", "Player 1"))                                # Sets the label1-text
        self.lbl2.setText(_translate("tombala", "Player 2"))                                # Sets the label2-text
        self.lbl3.setText(_translate("tombala", "Player 1 Score"))                          # Sets the label3-text
        self.lbl4.setText(_translate("tombala", "Player 2 Score"))                          # Sets the label4-text
        self.lbl5.setText(_translate("tombala", "Picked Number"))                           # Sets the label5-text
        self.lbl6.setText(_translate("tombala", "Welcome to Tombala of Legends .."))        # Sets the label6-text
        self.scoreBox1.setText(_translate("tombala", " "))                                  # Sets the scoreBox1-text
        self.scoreBox2.setText(_translate("tombala", " "))                                  # Sets the scoreBox2-text
        self.pickButton.setText(_translate("tombala", "Pick"))                              # Sets the pickButton-text
        self.pickedButton.setText(_translate("tombala", " "))                               # Sets the pickedButton-text
        self.initcardButton.setText(_translate("tombala", "Initialize Cards"))              # Sets the initcardButton-text
    
    ## This section sets the fonts
    
    def specifyFont(self, Family, PointSize, Bold, Weight):
        
        font = QtGui.QFont()
        font.setFamily(Family)
        font.setPointSize(PointSize)
        font.setBold(Bold)
        font.setWeight(Weight)
        
        return font                                                                         # Returns font features