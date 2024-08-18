
**generate_age(min_age=0, max_age=100)**
For a patient, this function generates a random age within a given range. It generates ages between 0 and 100 by default. 
The random.randint function in Python is used to choose an integer between the supplied min_age and max_age. 
Creating varied age data for the patients in the database is made possible by this.

**generate_blood_type()**
From a predetermined list of blood types, a random blood type is chosen by this function. Included are the blood types "A+," "A-," "B+," "B-," "AB+," "AB-," "O+," and "O-". 
The function provides patients with a range of blood type information by randomly selecting one of these types using random.choice.

**generate_longitudes_latitudes()**
This function generates a random pair of latitude and longitude coordinates. The latitude ranges from -90 to 90, and longitude ranges from -90 to 90.
These ranges are used to simulate geographic locations.
It employs random.uniform to produce floating-point numbers within these ranges, representing a location for each patient.

**calculate_statistics(data_source)**
Using a dictionary or a list of named tuples as the data source, this function computes many statistics. It calculates the mean blood type among the patients, their average age, and their mean location (latitude and longitude). 
The function returns the average age, execution time, and memory size of the data source after measuring how long it takes to complete these computations. It processes lists (of named tuples) and dictionaries (with nested dictionaries holding patient details) by looping over the data source, aggregating values, and computing statistics as necessary.

**open_price(seed, circuit=0.1)**
With a specified randomness seed, this method mimics stock price fluctuations. It determines a stock's opening, high, and closing prices. A circuit breaker, represented by the circuit parameter, sets a maximum percentage limit on price changes. 
It generates a random open price first, and then uses a random percentage change (positive or negative) from the open price to calculate the close price. 
The maximum of the open and close prices, plus an extra random percentage, is used to determine the high price. This function uses random values to simulate fluctuations in stock prices.

**metrics_for_stock_exchange(Database)**
The weighted average high, close, and open prices for a given list of stock exchange data are calculated by this function. It allocates a random weight between 10,000 and 100,000 to every stock in the database. Based on these weights, the function determines the overall market value of the high, close, and open prices. 
Lastly, it divides the entire market values by the total weights to yield the weighted average values for the open, close, and high prices. This gives a general picture of the performance of the stock market, assuming that all equities reached their peak values at the same time.

**Execution speed and memory of Named_tuples vs Dictionary**
Memory required for Patient_data with Named_tuples :85176
Memory required for Patient_data with Dictionary :295000

Time required for calculating metrics with Named_Tuples: 0.024099111557006836
Time required for calculating metrics with Dictionary: 0.017008304595947266

**We can conclude that for both memory and execution purposes Named_Tuples are much more efficient. I tried crunching metrics using
tuple of tuples(Generator) as well, but it was relatively slower when compared to Named_tuples enclosed by lists. However,
memory wise generators are the most efficient data sources**
