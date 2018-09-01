# MLP for Classification Task
import tensorflow
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.models import model_from_json
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X_data = data.data
y_data = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size= 0.3, random_state= 7
)

model = Sequential()

# adding layers

model.add(Dense(10, input_shape=(30,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1,activation='sigmoid'))

# compiling the model

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=10,epochs=150, verbose=2)

result = model.evaluate(X_test,y_test)
print('loss: ',result[0])
print('acc: ',result[1])

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("./mode103.h5")

