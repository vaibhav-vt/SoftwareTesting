import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from tqdm import tqdm
from random import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
TRAIN_DIR = 'dataset'
IMG_SIZE=100

def label_img(img):
    word_label = img[:3]
    # DIY One hot encoder
    if word_label == 'sun': return 1
    else : return 0


def create_train_data():
    # Creating an empty list where we should store the training data
    # after a little preprocessing of the data
    training_data_sun = []
    training_data_bar = []
    training_data_sca = []
    training_data_bub = []
    training_data_pie = []
  
    # tqdm is only used for interactive loading
    # loading the training data
    for img in tqdm(os.listdir(TRAIN_DIR)):
  
        # labeling the images
        label = label_img(img)
  
        path = os.path.join(TRAIN_DIR, img)

        if(img[0:3] == 'sun'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_sun.append([img, label])

        elif(img[0:3] == 'bar'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_bar.append([img, label])

        elif(img[0:3] == 'sca'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_sca.append([img,label])

        elif(img[0:3] == 'bub'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_bub.append([img,label])

        elif(img[0:3] == 'pie'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_pie.append([img,label])


  
    # shuffling of the training data to preserve the random state of our data
    shuffle(training_data_sun)
    shuffle(training_data_bar)
    shuffle(training_data_sca)
    shuffle(training_data_bub)
    shuffle(training_data_pie)
  
    # saving our trained data for further uses if required
    # np.save('train_data.npy', training_data)
    return training_data_sun,training_data_bar,training_data_sca,training_data_bub,training_data_pie

train_data_sun, train_data_bar, train_data_sca, train_data_bub, train_data_pie = create_train_data()

x_train_sun = []
y_train_sun = []

for categories, label in train_data_sun:
    x_train_sun.append(categories)
    y_train_sun.append(label) 

x_train_bar = []
y_train_bar = []

for categories, label in train_data_bar:
    x_train_bar.append(categories)
    y_train_bar.append(label) 

x_train_sca = []
y_train_sca = []

for categories, label in train_data_sca:
    x_train_sca.append(categories)
    y_train_sca.append(label) 

x_train_bub = []
y_train_bub = []

for categories, label in train_data_bub:
    x_train_bub.append(categories)
    y_train_bub.append(label) 

x_train_pie = []
y_train_pie = []

for categories, label in train_data_pie:
    x_train_pie.append(categories)
    y_train_pie.append(label) 

x_train_bar = np.array(x_train_bar).reshape(len(x_train_bar),-1)
x_train_sca = np.array(x_train_sca).reshape(len(x_train_sca),-1)
x_train_sun = np.array(x_train_sun).reshape(len(x_train_sun),-1)
x_train_pie = np.array(x_train_pie).reshape(len(x_train_pie),-1)
x_train_bub = np.array(x_train_bub).reshape(len(x_train_bub),-1)

x_train_bar = (x_train_bar)/255
x_train_sca = (x_train_sca)/255
x_train_sun = (x_train_sun)/255
x_train_pie = (x_train_pie)/255
x_train_bub = (x_train_bub)/255

y_train_bar = np.array(y_train_bar)
y_train_sca = np.array(y_train_sca)
y_train_sun = np.array(y_train_sun)
y_train_pie = np.array(y_train_pie)
y_train_bub = np.array(y_train_bub)


x_train_sun, x_test_sun, y_train_sun, y_test_sun = train_test_split(x_train_sun,y_train_sun, test_size=0.20,random_state=42)
x_train_sca, x_test_sca, y_train_sca, y_test_sca = train_test_split(x_train_sca,y_train_sca, test_size=0.20,random_state=42)
x_train_bub, x_test_bub, y_train_bub, y_test_bub = train_test_split(x_train_bub,y_train_bub, test_size=0.20,random_state=42)
x_train_bar, x_test_bar, y_train_bar, y_test_bar = train_test_split(x_train_bar,y_train_bar, test_size=0.20,random_state=42)
x_train_pie, x_test_pie, y_train_pie, y_test_pie = train_test_split(x_train_pie,y_train_pie, test_size=0.20,random_state=42)

X_train = np.concatenate((x_train_sun,x_train_sca,x_train_bar,x_train_pie,x_train_bub))
X_test = np.concatenate((x_test_sun,x_test_sca,x_test_bar,x_test_pie,x_test_bub))

Y_train = np.concatenate((y_train_sun,y_train_sca,y_train_bar,y_train_pie,y_train_bub))
Y_test = np.concatenate((y_test_sun,y_test_sca,y_test_bar,y_test_pie,y_test_bub))

print(X_train.shape)
print(Y_train.shape)
print(Y_test.shape)

svc = SVC(kernel='linear',gamma='auto')
svc.fit(X_train, Y_train)

y_pred = svc.predict(X_test)


count = 0
tot=0
for i in range(len(Y_test)):
  if(y_pred[i]==Y_test[i]):
    count+=1
  tot+=1
print("Accuracy = ",count/tot*100)