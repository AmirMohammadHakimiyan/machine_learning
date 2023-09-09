import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

df=pd.read_csv("data.csv")
df["chahat"]=df["act1"]
for i in df.index:
    if df.loc[i,"act1"]==-1 and df.loc[i,"act2"]==0:
        df.loc[i,"chahat"]=0
    elif df.loc[i,"act1"]==0 and df.loc[i,"act2"]==-1:
        df.loc[i,"chahat"]=1
    elif df.loc[i,"act1"]==1 and df.loc[i,"act2"]==0:
        df.loc[i,"chahat"]=2
    elif df.loc[i,"act1"]==0 and df.loc[i,"act2"]==1:
        df.loc[i,"chahat"]=3

df.drop("act1",axis=1,inplace=True)
df.drop("act2",axis=1,inplace=True)
X=df.drop("chahat",axis=1).to_numpy()
Y=df["chahat"].to_numpy()
X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
model=tf.keras.models.Sequential([tf.keras.layers.Dense(8,activation="relu"),
                                tf.keras.layers.Dense(16,activation="relu"),
                                tf.keras.layers.Dense(4,activation="relu"),
      
                                tf.keras.layers.Dense(4,activation="softmax")])
model.compile(optimizer=tf.keras.optimizers.Adam(),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"])

output=model.fit(X_train,Y_train,epochs=200)
accuracy=model.evaluate(X_test,Y_test)
print("accuracy on data test:",accuracy)
plt.plot(output.history["accuracy"])
plt.plot(output.history["loss"])
plt.legend(["accuracy","loss"])
plt.show()
model.save("weights/neural_network.h5")