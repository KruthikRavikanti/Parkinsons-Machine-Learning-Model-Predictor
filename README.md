# Parkinsons-Machine-Learning-Model-Predictor
A program that uses a user-drawn image of a spiral to predict if they have Parkinson's disease through the use of a trained dataset with high accuracy.

Interface.py

This file contains the interactable GUI interface that allows a user to input an image based on the prompt given. The user is expected to upload an image of a spiral that they drew. The image is processed and predicted as "Healthy" or "Parkinsons." After a quick loading screen, the use can expect a text pop-up on the same application window showing the result in green for a healthy prediction and red for an abnormal prediction. After this, the user will be asked if they have been diagnosed with Parkinson's disease or not to validate the prediction. This is essential considering it helps add another data point in an ever-building model.

parkinson_model.py

This file contains the backend of the entire application. This is responsible for training the model using data points (images of spirals) from drawings.zip. The model is trained based on already given predictions helping make newer conclusions. This is where the image is taken in and standardized accordingly, so a prediction can be made. During each iteration, the mode is "re-trained" due to a new data point that could have been potentially added.

drawings.zip

This is the folder where the data set is ever-changing after a user uses the application every time. At the current rate, the accuracy is about 86% which is staying stable. Through more training and more data points, it is likely that this number could go higher. 

Video Walkthrough on Using this Application:

https://youtu.be/y7RCFho4Aac

Created by Erik Li and Kruthik Ravikanti
