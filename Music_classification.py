import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
music_data=pd.read_csv("music.csv")

X=music_data.drop(columns=['genre'])
y=music_data['genre']
X_train,x_test,y_train,y_test= train_test_split(X,y, test_size=0.3)


model = DecisionTreeClassifier()
model.fit(X_train,y_train)
prediction=model.predict(x_test)
score=accuracy_score(y_test,prediction)
score

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data=pd.read_csv("music.csv")
X=music_data.drop(columns=['genre'])
y=music_data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)

tree.export_graphviz(model,out_file='music-recommender.dot',
                    feature_names=['age', 'gender '],
                    class_names=sorted(y.unique()),
                    label='all',
                    rounded=True,
                    filled=True)

names = ["Janny","Marry"]
for name in names:
    if name.startswith("J"):
        print("found")
        break 
else:
    print("not Found")
