{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "music_data=pd.read_csv(\"music.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "X=music_data.drop(columns=['genre'])\n",
    "y=music_data['genre']\n",
    "X_train,x_test,y_train,y_test= train_test_split(X,y, test_size=0.3)\n",
    "\n",
    "\n",
    "model = DecisionTreeClassifier()\n",
    "model.fit(X_train,y_train)\n",
    "prediction=model.predict(x_test)\n",
    "score=accuracy_score(y_test,prediction)\n",
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import tree\n",
    "\n",
    "music_data=pd.read_csv(\"music.csv\")\n",
    "X=music_data.drop(columns=['genre'])\n",
    "y=music_data['genre']\n",
    "\n",
    "model = DecisionTreeClassifier()\n",
    "model.fit(X,y)\n",
    "\n",
    "tree.export_graphviz(model,out_file='music-recommender.dot',\n",
    "                    feature_names=['age', 'gender '],\n",
    "                    class_names=sorted(y.unique()),\n",
    "                    label='all',\n",
    "                    rounded=True,\n",
    "                    filled=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "found\n"
     ]
    }
   ],
   "source": [
    "names = [\"Janny\",\"Marry\"]\n",
    "for name in names:\n",
    "    if name.startswith(\"J\"):\n",
    "        print(\"found\")\n",
    "        break \n",
    "else:\n",
    "    print(\"not Found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
