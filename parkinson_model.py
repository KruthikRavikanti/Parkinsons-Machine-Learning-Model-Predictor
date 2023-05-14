from imutils import paths
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from skimage import feature
import cv2
import numpy as np
import os
def hog_quantifier(image):
    features = feature.hog(image, orientations=9,
                           pixels_per_cell=(10, 10), cells_per_block=(2, 2),
                           transform_sqrt=True, block_norm="L1")
    return features


def processing_split(path):
    imagePaths = list(paths.list_images(path))
    data = []
    labels = []
    for imagePath in imagePaths:
        label = imagePath.split(os.path.sep)[-2]
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (250, 250), fx=0.5, fy=0.5)
        img = cv2.threshold(img, 0, 255,
                              cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        features = hog_quantifier(img)
        data.append(features)
        labels.append(label)
    return (np.array(data), np.array(labels))


def train(data):
    model = RandomForestClassifier(random_state = 2)
    path = "/Users/erikli/Desktop/Hackathon/Parkinson/data/drawings/" + data
    trainingPath = os.path.sep.join([path, "training"])
    testingPath = os.path.sep.join([path, "testing"])
    (trainX, trainY) = processing_split(trainingPath)
    (testX, testY) = processing_split(testingPath)
    encoder = LabelEncoder()
    trainY = encoder.fit_transform(trainY)
    testY = encoder.transform(testY)
    model.fit(trainX, trainY)
    predictions = model.predict(testX)
    accuracy = accuracy_score(testY, predictions)
    return model

def predictionTester(model, testingPath):    
    img = cv2.imread(testingPath)
    # The image being displayed still needs to be the original saved here
    # Converts images to greyscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (250, 250), fx=0.5, fy=0.5)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # Make prediction here as Normal or Abnormal
    modelsetter = hog_quantifier(img)
    prediction = model.predict([modelsetter])
    return prediction
