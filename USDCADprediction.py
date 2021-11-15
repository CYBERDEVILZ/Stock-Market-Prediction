import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt

DAYS = 30
BATCH_SIZE = 32
EPOCHS = 10

training_set = pd.read_csv(r"Dataset\USDCADtrain.csv", index_col="Date")
training_set.dropna(inplace=True)

training_set = training_set.iloc[:, 0:1].values ## contains only open values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler((0,1))
training_set_sc = sc.fit_transform(training_set)

X_train = []
y_train = []
for i in range(DAYS, len(training_set_sc)):
    X_train.append(training_set_sc[i-DAYS:i, 0])
    y_train.append(training_set_sc[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)


rnn = tf.keras.models.Sequential()

rnn.add(tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(DAYS, 1)))

rnn.add(tf.keras.layers.Dropout(0.2))
rnn.add(tf.keras.layers.LSTM(75, return_sequences=True))
rnn.add(tf.keras.layers.Dropout(0.2))
rnn.add(tf.keras.layers.LSTM(75, return_sequences=True))
rnn.add(tf.keras.layers.Dropout(0.2))
rnn.add(tf.keras.layers.LSTM(75, return_sequences=True))
rnn.add(tf.keras.layers.Dropout(0.2))
rnn.add(tf.keras.layers.LSTM(75, return_sequences=True))
rnn.add(tf.keras.layers.Dropout(0.2))
rnn.add(tf.keras.layers.LSTM(75))
rnn.add(tf.keras.layers.Dropout(0.2))

rnn.add(tf.keras.layers.Dense(1))

rnn.compile(optimizer="adam", loss="mean_squared_error")

X_train = X_train.reshape(len(X_train), DAYS, 1)
rnn.fit(X_train, y_train, batch_size=BATCH_SIZE , epochs=EPOCHS)


train_set = pd.read_csv(r"Dataset\USDCADtrain.csv", index_col="Date")
train_set.dropna(inplace=True)

test_set = pd.read_csv(r"Dataset\USDCADtest.csv", index_col="Date")
test_set.dropna(inplace=True)

whole_dataset = pd.concat((train_set, test_set), 0)
whole_dataset1 = pd.concat((train_set, test_set), 0)
whole_dataset = whole_dataset.iloc[:, 0:1].values

previous30days = []
for i in range(len(whole_dataset)-len(test_set), len(whole_dataset)):
    previous30days.append(whole_dataset[i-DAYS:i, 0])
previous30days = np.array(previous30days)

scaled_test_data = sc.transform(previous30days.reshape(-1, 1))
scaled_test_data = scaled_test_data.reshape(-1, DAYS)
scaled_test_data = scaled_test_data.reshape(scaled_test_data.shape[0], DAYS, 1)

y_pred = sc.inverse_transform(rnn.predict(scaled_test_data))
y_pred = y_pred.reshape(-1,)

predicted_data = pd.DataFrame({"Predicted": y_pred}, index=test_set.index)
plotdata = pd.concat((whole_dataset1["Open"], predicted_data), 1)
plotdata = plotdata.iloc[500:, :]

sns.set(rc={"figure.dpi":300, 'savefig.dpi':300})
sns.set_context('notebook')
sns.set_style("ticks")
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

sns.lineplot(data=plotdata["Open"])
sns.lineplot(data=plotdata["Predicted"])
plt.show()
