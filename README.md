# grab_safety

Run predictions and get score by running script with command

`python3 safety.py name_of_features_file.csv name_of_labels_file.csv`

Given multiple datapoints for a single trip, how can we make use of the data collected to predict dangerous driving, a single label for the entire trip? For all the 20,000+ trips, there is no fixed number of datapoints being collected per trip since every trip is obviously different.

My first approach, which I think is the simplest to start with, is to just condense all the datapoints of a trip into a single datapoint by taking the max value of each variable. Using this dataset means that we are trying to identify dangerous driving using discrete events within a journey (such as high speed, sudden accelerations), as opposed to data from continuously tracking a vehicle. A model will hopefully help identify preliminary threshold values that we can use moving forward. However, the best performance I could get using a classification model was around 70+%. I think this is because I am throwing away a lot of information by simplifying information collected over possibly hundreds of datapoints into a single datapoint.

I then engineered features that counted how many times during a trip did a particular predictor exceed a certain percentile of that predictor's entire distribution of values. This is because if a driver's readings tend to be on the higher side of the distributions, he/she is likely to be classified as driving dangerously. I did that for all the gyroscope and accelerometer readings, and played around with the threshold percentiles, but still am unable to get a performance above 80%.

Going forward, I will probably try to consider each set of gyroscope/accelerometer readings together or engineer some sort of interaction term. I might also explore some sort of change detection algorithm.
