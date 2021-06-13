"""
    A simple neural network written in Keras (TensorFlow backend) to classify the IRIS data
"""
#this code explains how the model file is created to simplify the code and implementation of neural network

import numpy as np #numerical analysis library of python

from keras.models import Sequential #sequential neural network are used for creation of simple neural network
from keras.layers import Dense #this is the neuron layer
from keras.optimizers import Adam #common optimization algorithm of neural network
from tensorflow import keras

def processCsv(filename): #a function i created to convert the score points into numpy array because only numpy array data type is accepted in neural network because at the back of this library the algorithm used commonly is dot product or matrix multuplication
    xy = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print(type(csv_reader))
        line_count = 0
        for row in csv_reader:
            #print(row[0])
            x = row[0].split(',')
            xy.append(x)
            #print(x_arr)
    print(xy)
    xy.pop(0)
    x_arr = np.array(xy, dtype=np.float32)
    print(x_arr.shape)
    return x_arr

# Build the model
train_x = processCsv('x_train.csv') #train_x was the input
train_y = processCsv('y_train.csv') #train_y was the output
model = Sequential() #define model as sequential

model.add(Dense(20, input_shape=(10,), activation='relu', name='fc1')) #first layer consist of 20 output node and input shape of 10 because in the dataset it uses 10 subject scores
model.add(Dense(20, activation='relu', name='fc2')) #second layer to be connected to output
model.add(Dense(9, activation='softmax', name='output')) #output layer

# Adam optimizer with learning rate of 0.001
optimizer = Adam(lr=0.001) #learning rate define the network ratio between speed and accuracy
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy']) #categorical_crossentropy is commonly used in multiple choice output

print('Neural Network Model Summary: ')
print(model.summary()) #summary of the structure

# Train the model
model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=200) #train or teach the neural network algorithm to map the relationship of scores to the chosen course

# Test on unseen data
model.save('model.h5') #uhm save
print("Model file saved")
