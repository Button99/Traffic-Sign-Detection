import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PIL import Image
import numpy as np
import tensorflow
from keras.models import load_model

model= load_model("trafficModel.h5")

# Creating dictionary
'''
dict= {}

reader= csv.reader(open("LABELS PATH"))

for row in reader:
    dict[row[0]]= row[1:]
'''
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',
            3:'Speed limit (50km/h)',
            4:'Speed limit (60km/h)',
            5:'Speed limit (70km/h)',
            6:'Speed limit (80km/h)',
            7:'End of speed limit (80km/h)',
            8:'Speed limit (100km/h)',
            9:'Speed limit (120km/h)',
            10:'No passing',
            11:'No passing veh over 3.5 tons',
            12:'Right-of-way at intersection',
            13:'Priority road',
            14:'Yield',
            15:'Stop',
            16:'No vehicles',
            17:'Veh > 3.5 tons prohibited',
            18:'No entry',
            19:'General caution',
            20:'Dangerous curve left',
            21:'Dangerous curve right',
            22:'Double curve',
            23:'Bumpy road',
            24:'Slippery road',
            25:'Road narrows on the right',
            26:'Road work',
            27:'Traffic signals',
            28:'Pedestrians',
            29:'Children crossing',
            30:'Bicycles crossing',
            31:'Beware of ice/snow',
            32:'Wild animals crossing',
            33:'End speed + passing limits',
            34:'Turn right ahead',
            35:'Turn left ahead',
            36:'Ahead only',
            37:'Go straight or right',
            38:'Go straight or left',
            39:'Keep right',
            40:'Keep left',
            41:'Roundabout mandatory',
            42:'End of no passing',
            43:'End no passing veh > 3.5 tons' }
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
        image= image.resize((32, 32))
        image= np.expand_dims(image, axis=0)
        image= np.array(image)
        pred= model.predict_classes([image])[0]
        sign = classes[pred + 1]
        print(sign)


if __name__ == "__main__":
    app= QApplication(sys.argv)
    ex= App()
    sys.exit(app.exec_())


'''
    Need to make better the ui -- 
    Function upload img 
    Function Find the sign -- problem with the resize 

'''

