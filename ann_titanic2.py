import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier


# read train data
train = pd.read_csv(
    "ANN TP/train.csv",
    dtype={"Age": np.float64},
)

# read test data
test = pd.read_csv(
    "ANN TP/test.csv",
    dtype={"Age": np.float64},
)


predictor = [
    "Age",
    "Fare",
    "SibSp",
    "Parch",
    "FamilySize",
    "male",
    "female",
    "pclass_1",
    "pclass_2",
    "pclass_3",
]


# function that correct data
def correct_data_MF(titanic_data):
    # titanic_data.Sex = titanic_data.Sex.replace(['male', 'female'], [0, 1])
    titanic_data.Embarked = titanic_data.Embarked.fillna("S")
    # titanic_data.Embarked = titanic_data.Embarked.replace(['C', 'S', 'Q'], [0, 1, 2])
    titanic_data.Age = titanic_data.Age.fillna(titanic_data.Age.median())

    # Trying to add FamilySize
    titanic_data["FamilySize"] = titanic_data["SibSp"] + titanic_data["Parch"] + 1

    # add Male & Female one-hot-encoding
    sex_dummy = pd.get_dummies(titanic_data.Sex)
    titanic_data["male"] = sex_dummy.male
    titanic_data["female"] = sex_dummy.female

    # add Embarked one-hot-encoding
    embarked_dummy = pd.get_dummies(titanic_data.Embarked)
    titanic_data["embarked_C"] = embarked_dummy.C
    titanic_data["embarked_S"] = embarked_dummy.S
    titanic_data["embarked_Q"] = embarked_dummy.Q

    # add Pclass one-hot-encoding
    pclass_dummy = pd.get_dummies(titanic_data.Pclass)
    titanic_data["pclass_1"] = pclass_dummy[1]
    titanic_data["pclass_2"] = pclass_dummy[2]
    titanic_data["pclass_3"] = pclass_dummy[3]

    # Cabin
    titanic_data.Cabin = titanic_data.Cabin.fillna("N")
    titanic_data["CabinDeck"] = titanic_data.Cabin.str.slice(0, 1)
    cabindeck_dummy = pd.get_dummies(titanic_data.CabinDeck)

    titanic_data["CabinDeck_A"] = cabindeck_dummy.A
    titanic_data["CabinDeck_B"] = cabindeck_dummy.B
    titanic_data["CabinDeck_C"] = cabindeck_dummy.C
    titanic_data["CabinDeck_D"] = cabindeck_dummy.D
    titanic_data["CabinDeck_E"] = cabindeck_dummy.E
    titanic_data["CabinDeck_F"] = cabindeck_dummy.F
    titanic_data["CabinDeck_G"] = cabindeck_dummy.G
    titanic_data["CabinDeck_NaN"] = cabindeck_dummy.N

    titanic_data.Fare = titanic_data.Fare.fillna(titanic_data.Fare.median())

    return titanic_data


# correct data
correct_train_MF = correct_data_MF(train).sample(frac=1)
trainX = correct_train_MF[predictor].values
trainY = correct_train_MF.Survived.values

# create model
aiot4 = MLPClassifier(
    activation="relu",
    solver="adam",
    max_iter=5000,
    alpha=1e-4,
    hidden_layer_sizes=(15, 8),
    random_state=7,
)

# train model
trained = aiot4.fit(trainX, trainY)

# Test set score for train data
print("Test set score: {:.3f}".format(aiot4.score(trainX, trainY)))

# predict result
predict_manual = aiot4.predict([[80, 10, 0, 0, 2, 1, 0, 0, 0, 1]])

print("Predict result: {}".format(predict_manual))
