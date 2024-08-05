# Machine Learning

My example is predicting the amount of cars that will pass by a sensor every hour. The data being collected is only the time of day and the amount of cars that passed the sensor. This will show the trend of which hour is the busiest on that street and which is the quietest. This could help people avoid traffic jams by letting the, know which hour to avoid. The data is in the Vechilces.csv file.

**steps**
1. Install the pandas package.
2. Load the data into the data variable.
3. Use functions to get all the necessary information from the timestamp.
4. Display the values, just to check it.
5. Drop the DateTime function, since it is no longer needed.
6.  Seperate the class label for training the data.
7.  Store the class label in target.
8.  Import the randoming forest from sklearn.
9.  Define the the random forest generator.
10.  Start testing with data.
