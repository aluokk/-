import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
from processdata.generatedata import genData
x_train, y_train = genData(batch_size=100)
x_test, y_test = genData(batch_size=50)

x_train = x_train.reshape((-1, 25))
x_test = x_test.reshape((-1, 25))

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.model.add(Dense(320, activation='relu'))
model.add(Dense(32, activation='relu', input_dim=25))
model.add(Dropout(0.5))
model.add(Dense(20, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=5,
          batch_size=100)
score = model.evaluate(x_test, y_test, batch_size=50)

from keras.models import model_from_json

# json_string = model.to_json()
# model = model_from_json(json_string)
model.save_weights('./weights')