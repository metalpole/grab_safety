import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from statistics import mean, median
import sys
import pickle

model = pickle.load(open('RF.sav', 'rb'))

if __name__== "__main__":
    # Argument 1: Features csv, Argument 2: Labels csv
    test_features = pd.read_csv(sys.argv[1])
    test_labels = pd.read_csv(sys.argv[2])

    acc_x_pc = 0.203518
    acc_y_pc = 8.599224
    acc_z_pc = 0.666931
    gyro_x_pc = 0.006300
    gyro_y_pc = 0.006821
    gyro_z_pc = 0.004745

    # Feature engineering
    condensed_counts = pd.DataFrame(0.0, index=np.arange(len(test_labels)), columns=['bookingID', 'acc_x_count', 'acc_y_count', 'acc_z_count', 'gyro_x_count', 'gyro_y_count', 'gyro_z_count', 'acc_x_max', 'acc_y_max', 'acc_z_max', 'gyro_x_max', 'gyro_y_max', 'gyro_z_max', 'label', 'speed'])

    for i in range(len(test_labels)):
        condensed_counts.iloc[i,0] = test_labels.iloc[i,0]
        condensed_counts.iloc[i,13] = test_labels.iloc[i,1]
        df = test_features[test_features['bookingID']==test_labels.iloc[i,0]]
        condensed_counts.iloc[i,14] = max(df['Speed'])
        # Get counts
        condensed_counts.iloc[i,1] = np.sum(abs(df['acceleration_x'])>acc_x_pc)
        condensed_counts.iloc[i,2] = np.sum(abs(df['acceleration_y'])>acc_y_pc)
        condensed_counts.iloc[i,3] = np.sum(abs(df['acceleration_z'])>acc_z_pc)
        condensed_counts.iloc[i,4] = np.sum(abs(df['gyro_x'])>gyro_x_pc)
        condensed_counts.iloc[i,5] = np.sum(abs(df['gyro_y'])>gyro_y_pc)
        condensed_counts.iloc[i,6] = np.sum(abs(df['gyro_z'])>gyro_z_pc)
        # Get max
        condensed_counts.iloc[i,7] = max(abs(df['acceleration_x']))
        condensed_counts.iloc[i,8] = max(abs(df['acceleration_y']))
        condensed_counts.iloc[i,9] = max(abs(df['acceleration_z']))
        condensed_counts.iloc[i,10] = max(abs(df['gyro_x']))
        condensed_counts.iloc[i,11] = max(abs(df['gyro_y']))
        condensed_counts.iloc[i,12] = max(abs(df['gyro_z']))

    result = model.score(condensed_counts[['acc_x_count', 'acc_y_count', 'acc_z_count', 'gyro_x_count', 'gyro_y_count', 'gyro_z_count', 'acc_x_max', 'acc_y_max', 'acc_z_max', 'gyro_x_max', 'gyro_y_max', 'gyro_z_max', 'speed']], condensed_counts['label'])
    print(result)