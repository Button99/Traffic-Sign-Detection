import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from PIL import Image
import numpy as np
from keras.models import load_model
import pickle as pkl
import csv

model= load_model("trafficModel.h5")
labels= pkl.load(open("labels.pickle", "rb"))

# Creating dictionary

dict= {}

reader= csv.reader(labels)
i=0
for row in reader:
    i+=1
    dict[i]=row[0]

# GUI

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title= "Traffic Sign Detection"
        self.left= 50
        self.top= 50
        self.width= 500
        self.height= 500
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # label
        self.label= QLabel(self)
        self.label.move(100, 30)
        self.label.setText("Insert the path of the photo:")

        # in the textbox the user will add the path of the photo
        self.textbox= QLineEdit(self)
        self.textbox.resize(170, 30)
        self.textbox.move(100, 50)

        self.findSign= QPushButton("Find the sign", self)
        self.findSign.setToolTip("Click to search the sign")
        self.findSign.move(125, 200)

        self.label2 = QLabel(self)
        self.label2.setFixedWidth(400)
        self.label2.move(100, 100)
        self.label2.setText("Result")
        self.findSign.clicked.connect(self.click_SearchButton)
        #self.label2.clear()

        self.show()

    @pyqtSlot()

    # function for search button
    def click_SearchButton(self):
        imgPath= self.textbox.text()
        image= Image.open(imgPath)
        image= image.resize((32, 32))
        image= np.expand_dims(image, axis=0)
        image= np.array(image)
        pred= model.predict_classes([image])[0]
        sign = dict[pred+1]
        print(sign)
        self.label2.setText(str(sign))


if __name__ == "__main__":
    app= QApplication(sys.argv)
    ex= App()
    sys.exit(app.exec_())


