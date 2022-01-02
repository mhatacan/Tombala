###########################################
# Filename    :  Driver.py
# Author      :  Muhammet Harun ATACAN
# Date        :  06.06.2021
# Description :  Driver Code
###########################################

import Interface
import Operation
import sys

## main function creates object and calls that object's function

def main():
    
    app = Interface.QtWidgets.QApplication(sys.argv)
    tombala=Operation.Operation()
    tombala.setup_initCard()
    tombala.setup_pickedNumber()
    tombala.show()
    sys.exit(app.exec_()) 

main()