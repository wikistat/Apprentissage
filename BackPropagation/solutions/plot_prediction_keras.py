sample_idx = 42
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(1,2,1)
ax.imshow(scaler.inverse_transform(X_test[sample_idx]).reshape(8, 8),
           cmap=plt.cm.gray_r, interpolation='nearest')
ax.set_title("true label: %d" %y_test[sample_idx])
ax.axis("off")
ax.grid(False)

ax1 = fig.add_subplot(1,2,2)
classes = np.arange(10)
probabilities = keras_model.predict_proba(X_test, verbose=0)
ax1.bar(classes, one_hot(len(classes), y_test[sample_idx]), label='true')
ax1.bar(classes, probabilities[sample_idx], label='prediction', color="red")
ax1.set_xticks(classes)
prediction = model.predict(X_test[sample_idx])
ax1.set_title('Output probabilities (prediction: %d)'
              % prediction)
ax1.set_xlabel('Digit class')
ax1.legend()
