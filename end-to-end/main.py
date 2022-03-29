import numpy as np
import device
import model as ppg_model
import matplotlib.pyplot as plt
import pickle
from model import Classifier 

macAddress = "/dev/tty.BITalino-DevB"
training_signal = []


def collect_data():
    training_signal = device.collect_data(macAddress,run_time=90)

    training_signal = np.array(training_signal)

    cleaned_ppg_data_training = device.clean_data(training_signal, doPlot=False)

    # Authentication
    data = np.load("preprocessed_data.npy", allow_pickle=True)
    _, _, authenticator_data = ppg_model.create_dataset(data)

    return authenticator_data,cleaned_ppg_data_training


def train_model(authenticator_data,cleaned_ppg_data_training):
    participant = 24

    print("------  STARTED TRAINING")
    classifier_model = pickle.load(open('./2_Classifier_Model.sav', 'rb'))
    train_accs, val_accs, test_accs, confusion_matrices , trained_model= ppg_model.train_model_for_participant(ppg_model.Authenticator, classifier_model, authenticator_data, cleaned_ppg_data_training ,participant)

    mean = lambda x: sum(x)/len(x)

    print("Average final train accuracy: {}".format(mean(train_accs)))
    print("Average final validation accuracy: {}".format(mean(val_accs)))
    print("Average test accuracy: {}".format(mean(test_accs)))
    print(sum(confusion_matrices))
    print("------  DONE TRAINING")

    return trained_model


def predict(key,model):
    try:

        if key == 'y':
            test_signal = device.collect_data(macAddress,run_time=10)
            test_signal = np.array(test_signal)
            cleaned_test_signal= device.clean_data(test_signal, doPlot=False)
            model_pred3 = ppg_model.prediction(data=cleaned_test_signal, model=model)
            print("MODEL 3: ",model_pred3.argmax(dim=1))

        elif key == 's':
            test_signal = device.collect_data(macAddress,run_time=20)
            test_signal = np.array(test_signal)
            cleaned_test_signal= device.clean_data(test_signal, doPlot=False)
            model_pred3 = ppg_model.prediction(data=cleaned_test_signal, model=model)
            print("MODEL 3: ",model_pred3.argmax(dim=1))  

        elif key == 'r':
            test_signal = device.collect_data(macAddress,run_time=10)
            test_signal = np.array(test_signal)
            cleaned_test_signal= device.clean_data(test_signal, doPlot=False, filter=False)
            model_pred3 = ppg_model.prediction(data=cleaned_test_signal, model=model)
            print("MODEL 3: ",model_pred3.argmax(dim=1))   
        
    except:
        pass


