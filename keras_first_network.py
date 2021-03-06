# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# split into input (X) and output (y) variables
x = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation= 'relu'))
model.add(Dense(6, activation= 'relu'))
model.add(Dense(4, activation= 'relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(x, y, epochs=150, batch_size=1) #this gets the ACC up to 80%

# evaluate the keras model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

# make class predictions with the model (model.predict_classes(x) deprecated version)
predictions = (model.predict(x) > 0.5).astype("int32")

# summarize the first 5 cases
for i in range(5):
  print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))