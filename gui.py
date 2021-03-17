import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PIL import Image
import numpy as np
import csv

model= ("PATH")

# Creating dictionary
'''
dict= {}

reader= csv.reader(open("LABELS PATH"))

for row in reader:
    dict[row[0]]= row[1:]
'''

# GUI

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title= "Traffic Sign Detection"
        self.left= 50
        self.top= 50
        self.width= 400
        self.height= 400
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # in the textbox the user will add the path of the photo
        self.textbox= QLineEdit(self)
        self.textbox.resize(170, 30)
        self.textbox.move(100, 50)

        self.findSign= QPushButton("Find the sign", self)
        self.findSign.setToolTip("Click to search the sign")
        self.findSign.move(100, 200)
        self.findSign.clicked.connect(self.click_SearchButton)

        self.upldImg= QPushButton("Upload image", self)
        self.upldImg.move(200, 200)
       # self.button2.clicked.connect(self.click_CancelButton)

        self.show()
    @pyqtSlot()

    # function for search button
    def click_SearchButton(self):
        print("Search button clicked")
        imgPath= self.textbox.text()
        image= Image.open(imgPath)
        image= image.resize(32, 32)
        image= np.expand_dims(image, axis=0)    
        image= np.array(image)
        pred= model.predict_classes([image])[0]
        print(pred)





if __name__ == "__main__":
    app= QApplication(sys.argv)
    ex= App()
    sys.exit(app.exec_())


'''
    Need to make better the ui -- 
    Function upload img 
    Function Find the sign -- problem with the resize 

'''

