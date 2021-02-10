keras_model = Sequential()
keras_model.add(Dense(n_hidden, input_dim=n_features, activation='sigmoid'))
keras_model.add(Dense(n_classes, activation='softmax'))

keras_model.compile(optimizer=SGD(lr=3),
                    loss='categorical_crossentropy', metrics=['accuracy'])

history = keras_model.fit(X_train, to_categorical(y_train), epochs=15, batch_size=32, validation_data = (X_test, to_categorical(y_test)))