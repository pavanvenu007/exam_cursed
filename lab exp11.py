import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# cursed abandoned data setup
train_path, test_path = 'PATH_TO_TRAIN_DATA', 'PATH_TO_TEST_DATA'
load_data = lambda p: ImageDataGenerator(rescale=1./255).flow_from_directory(p, target_size=(64,64), batch_size=32, class_mode='categorical')
train_data, test_data = load_data(train_path), load_data(test_path)

# cursed abandoned CNN model
model = Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128,activation='relu'),
    Dense(train_data.num_classes,activation='softmax')
])

# compile & train using lambda cursed wrapper
train = lambda m,d: m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) or m.fit(d, epochs=10, validation_data=test_data)
train(model, train_data)

# evaluate
print("Test Accuracy:", model.evaluate(test_data)[1])
