import cv2
import os
import numpy as np
from random import shuffle
from tqdm import tqdm

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
from sklearn.model_selection import train_test_split


TRAIN_DIR = 'dataset'
IMG_SIZE = 100
LR = 1e-3
MODEL_NAME = 'sunburst_classifier-{}-{}.model'.format(LR, '6conv-basic')

def label_img(img):
    word_label = img[:3]
    # DIY One hot encoder
    if word_label == 'sun': return [1, 0]
    else : return [0, 1]

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
            training_data_sun.append([np.array(img), np.array(label)])

        elif(img[0:3] == 'bar'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_bar.append([np.array(img), np.array(label)])

        elif(img[0:3] == 'sca'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_sca.append([np.array(img), np.array(label)])

        elif(img[0:3] == 'bub'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_bub.append([np.array(img), np.array(label)])

        elif(img[0:3] == 'pie'):
             # loading the image from the path and then converting them into
            # grayscale for easier covnet prob
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
            # resizing the image for processing them in the covnet
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
  
            # final step-forming the training data list with numpy array of the images
            training_data_pie.append([np.array(img), np.array(label)])


  
    # shuffling of the training data to preserve the random state of our data
    shuffle(training_data_sun)
    shuffle(training_data_bar)
    shuffle(training_data_sca)
    shuffle(training_data_bub)
    shuffle(training_data_pie)
  
    # saving our trained data for further uses if required
    # np.save('train_data.npy', training_data)
    return training_data_sun,training_data_bar,training_data_sca,training_data_bub,training_data_pie

# print('chutiya hu')
train_data_sun, train_data_bar, train_data_sca, train_data_bub, train_data_pie = create_train_data()


# tf.reset_default_graph()
convnet = input_data(shape =[None, IMG_SIZE, IMG_SIZE, 1], name ='input')
  
convnet = conv_2d(convnet, 32, 5, activation ='relu')
convnet = max_pool_2d(convnet, 5)
  
convnet = conv_2d(convnet, 64, 5, activation ='relu')
convnet = max_pool_2d(convnet, 5)
  
convnet = conv_2d(convnet, 128, 5, activation ='relu')
convnet = max_pool_2d(convnet, 5)
  
convnet = conv_2d(convnet, 64, 5, activation ='relu')
convnet = max_pool_2d(convnet, 5)
  
convnet = conv_2d(convnet, 32, 5, activation ='relu')
convnet = max_pool_2d(convnet, 5)
  
convnet = fully_connected(convnet, 1024, activation ='relu')
convnet = dropout(convnet, 0.8)
  
convnet = fully_connected(convnet, 2, activation ='softmax')
convnet = regression(convnet, optimizer ='adam', learning_rate = LR,
      loss ='categorical_crossentropy', name ='targets')
  
model = tflearn.DNN(convnet, tensorboard_dir ='log')

print('chutiya hu')
X_sun = np.array([i[0] for i in train_data_sun]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y_sun = [i[1] for i in train_data_sun]
x_sun,test_x_sun,y_sun,test_y_sun = train_test_split(X_sun, Y_sun, test_size=0.20, random_state=42)

X_sca = np.array([i[0] for i in train_data_sca]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y_sca = [i[1] for i in train_data_sca]
x_sca,test_x_sca,y_sca,test_y_sca = train_test_split(X_sca, Y_sca, test_size=0.20, random_state=42)

X_bar = np.array([i[0] for i in train_data_bar]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y_bar = [i[1] for i in train_data_bar]
x_bar,test_x_bar,y_bar,test_y_bar = train_test_split(X_bar, Y_bar, test_size=0.20, random_state=42)

X_pie = np.array([i[0] for i in train_data_pie]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y_pie = [i[1] for i in train_data_pie]
x_pie,test_x_pie,y_pie,test_y_pie = train_test_split(X_pie, Y_pie, test_size=0.20, random_state=42)

X_bub = np.array([i[0] for i in train_data_bub]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y_bub = [i[1] for i in train_data_bub]
x_bub,test_x_bub,y_bub,test_y_bub = train_test_split(X_bub, Y_bub, test_size=0.20, random_state=42)




x_train = np.concatenate((x_sun,x_sca,x_bar,x_pie,x_bub))
x_test = np.concatenate((test_x_sun,test_x_sca,test_x_bar,test_x_pie,test_x_bub))

y_train = np.concatenate((y_sun,y_sca,y_bar,y_pie,y_bub))
y_test = np.concatenate((test_y_sun,test_y_sca,test_y_bar,test_y_pie,test_y_bub))

model.fit({'input': x_train}, {'targets': y_train}, n_epoch = 5, 
    validation_set =({'input': x_test}, {'targets': y_test}), 
    snapshot_step = 500, show_metric = True, run_id = MODEL_NAME)
model.save(MODEL_NAME)




y_pred = []
for data in x_test:
  model_out = model.predict([data])[0]
  if np.argmax(model_out) == 1: y_pred.append([0,1])
  else: y_pred.append([1,0])  


count = 0
tot=0
for i in range(len(y_test)):
  if(y_pred[i]==y_test[i].tolist()):
    count+=1
  tot+=1
print("Accuracy = ",count/tot*100)






# print(x_sun.shape)
# print(x_bar.shape)
# print(x_sca.shape)
# print(x_pie.shape)
# print(x_bub.shape)
# print(x_train.shape)