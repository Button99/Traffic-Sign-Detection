import tkinter as tk
from PIL import Image
import numpy as np
import csv
from keras.models import load_model

model= ("PATH")

# Creating dictionary

dict= {}

reader= csv.reader(open("LABELS PATH"))

for row in reader:
    dict[row[0]]= row[1:]



''' Need to create the gui and the buttons '''