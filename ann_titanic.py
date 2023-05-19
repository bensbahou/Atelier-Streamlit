import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
import streamlit as st


def correct_data(titanic_data):
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


# set the page title
st.title("Titanic Survival Prediction")

# add a subheader
st.subheader(
    "This is a simple app to predict the survival of passengers on the Titanic"
)


# add a multiselect box for model hyperparameters
# add a input for how many hidden layers
hidden_layer_number = st.number_input("Enter The Number of Hidden Layers", 1, 10, 2, 1)

hidden_layer_sizes = []
# add a input for how many neurons in each hidden layer
for layer in range(hidden_layer_number):
    hidden_layer_size = st.number_input(
        "Enter The Number of Neurons in Hidden Layer " + str(layer + 1), 1, 100, 3, 1
    )
    hidden_layer_sizes.append(hidden_layer_size)


activation = st.selectbox(
    "Select The Activation Function", ["identity", "logistic", "tanh", "relu"]
)
solver = st.selectbox("Select The Solver", ["lbfgs", "sgd", "adam"])
alpha = st.number_input(
    "Enter The Alpha Value", 0.0001, 0.1, 0.01, 0.0001, format="%.4f"
)
learning_rate = st.selectbox(
    "Select The Learning Rate", ["constant", "invscaling", "adaptive"]
)
max_iter = st.number_input("Enter The Maximum Iterations", 100, 1000, 300, 100)

aiot4 = MLPClassifier(
    hidden_layer_sizes=hidden_layer_sizes,
    activation=activation,
    solver=solver,
    alpha=alpha,
    learning_rate=learning_rate,
    max_iter=max_iter,
)


st.write("The Model is as follows:")
st.write(aiot4)

# st.write("The Hyperparameters are as follows:")
# st.write("Hidden Layer Sizes: ", hidden_layer_sizes)
# st.write("Activation Function: ", activation)
# st.write("Solver: ", solver)
# st.write("Alpha: ", alpha)
# st.write("Learning Rate: ", learning_rate)
# st.write("Maximum Iterations: ", max_iter)


# set file input for train data
train_file = st.file_uploader("Upload The Train Data File")

# read the data from the file if the file is uploaded
if train_file is not None:
    train = pd.read_csv(train_file, index_col=0)
    # show the data keys as a list
    # st.write(train.keys().to_list())

    # add multiple select box for the features with all the keys selected by default

    features = st.multiselect(
        "Select The Features to show", train.keys().to_list(), train.keys().to_list()
    )

    # show the data in a table if the features are selected
    if len(features) > 0:
        st.write(train[features])

    # add a button to correct the data
    if st.button("Train The Model and evaluate the accuracy"):
        correct_train = correct_data(train)

        # show the data in a table
        st.write(correct_train)

        # add a button to create trainX and trainY

        trainX = correct_train[predictor].values
        trainY = correct_train.Survived.values

        # show the train data and target data in two columns side by side with proportion 1:2
        col1, col2 = st.columns([4, 1])
        # show the train data in the first column
        col1.write("trainX")
        col1.write(trainX)
        # show the target data in the second column
        col2.write("trainY")
        col2.write(trainY)

        # add loader to show the progress of training the model with the train data and target data
        with st.spinner("Training the model..."):
            aiot4.fit(trainX, trainY)
            # show the score of the model in a success message
            st.success("Model Score: {:.3f}".format(aiot4.score(trainX, trainY)))


# set file input for test data
test_file = st.file_uploader("Upload The Test Data File")

# read the data from the file if the file is uploaded
if test_file is not None:
    test = pd.read_csv(test_file, index_col=0)
    # show the data keys as a list
    st.write(test.keys().to_list())

    # show the data in a table
    st.write(test)
