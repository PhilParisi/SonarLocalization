import numpy as np
import keras
import scipy.io as scio
from scipy.io import savemat
from keras_applications.resnet import ResNet152
import os
# from resnets_utils import *
from glob import glob
from keras import optimizers
from sklearn.model_selection import train_test_split
from keras.models import Sequential,Model,load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D,GlobalAveragePooling2D
from keras.callbacks import TensorBoard,ReduceLROnPlateau,ModelCheckpoint
from matplotlib import pyplot
import tensorflow as tf
import matplotlib.pyplot as plt
print(tf.__version__)

ClassNumber = 5
epochCNN = 20
HiddenLayerDim = 512 #doesn't really do anything, just for outputs of text?
k_num = 10
strs = str(ClassNumber)
sdr = str(HiddenLayerDim)

#data1 =scio.loadmat('/home/ubuntu/AWSJUNE/allspecmic2dynFMinterplated.mat')
data1 = scio.loadmat("G:/Adam/PythonJackal/allspecmic2dynFM.mat")  # My data
data3 = scio.loadmat("G:/Adam/PythonJackal/yhat" + strs + ".mat")
#data3 = scio.loadmat('/home/ubuntu/AWSJUNE/yhat40.mat')

y = data3['yhat' + strs]  ###
y = np.transpose(y)
x = data1['allspecmic2dynFM']  ###

# y = data3['yhat40']
# y = np.transpose(y)
# x = data1['allspecmic2dynFMinterplated'] # What is interplated ?

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y

img_height,img_width = 32,32

X_train_orig, X_test_orig, Y_train_orig, Y_test_orig = train_test_split(
    x, y, test_size=0.15, random_state=42)

# Normalize image vectors
X_train = X_train_orig
X_test = X_test_orig

# Convert training and test labels to one hot matrices
Y_train = convert_to_one_hot(Y_train_orig, ClassNumber).T
Y_test = convert_to_one_hot(Y_test_orig, ClassNumber).T

print(Y_train)
print(Y_test)

X_train = X_train.reshape([-1,18,15,1])
X_test = X_test.reshape([-1,18,15,1])

X_train = tf.image.resize(X_train, size = (img_height, img_width))
X_test =  tf.image.resize(X_test, size = (img_height, img_width))

print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))


num_classes = ClassNumber
#If imagenet weights are being loaded,
#input must have a static square shape (one of (128, 128), (160, 160), (192, 192), or (224, 224))
base_model = ResNet152(include_top=None,
                    weights=None,
                    input_shape=(img_height, img_width, 1),
                       backend=keras.backend,
                       layers=keras.layers,
                       models=keras.models,
                       utils=keras.utils
                       )
backend=keras.backend

x = base_model.output
print(x)
x = GlobalAveragePooling2D()(x)
print(x)
x = Dropout(0.3)(x)
print(x)

predictions = Dense(num_classes, activation= 'softmax')(x)
model = Model(inputs = base_model.input, outputs = predictions)
#model.summary()

from tensorflow.keras.optimizers import SGD, Adam ## modification 4/5/23 for testing tf-gpu

# sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
adam = Adam(lr=0.00005)

# model compile
model.compile(optimizer= adam, loss='categorical_crossentropy', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, verbose='auto', epochs = epochCNN, validation_data=(X_test, Y_test), batch_size = 64)

preds = model.evaluate(X_test, Y_test)
print ("Loss = " + str(preds[0]))
savemat("preds-"+strs+".mat", {'preds': preds})

model.save('Output/resnet152_2-'+strs+"-"+sdr+'.h5')
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('accuracy - CNN(Resnet 152) - Sections: ' + strs + ' Dim:' + sdr)
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss - CNN(Resnet 50)  - Sections: ' + strs + ' Dim:' + sdr)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()