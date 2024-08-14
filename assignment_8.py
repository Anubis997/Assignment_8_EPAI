
from collections import namedtuple
import random
import time
from tqdm import tqdm
from faker import Faker
import sys
fake = Faker()

Patient_db=namedtuple('Patient_db','name age location blood_type' )

Patient_db.__docstring__="this is a person class"
Patient_db.name.__doc__="name of the person"
Patient_db.location.__doc__="location of the person"
Patient_db.age.__doc__="age of the person"
Patient_db.blood_type.__doc__="blood type of the person"

# Function to generate age
def generate_age(min_age=0, max_age=100):
    return random.randint(min_age, max_age)

# Function to generate a random blood type
def generate_blood_type():
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    return random.choice(blood_types)

#Function to generate latitudes and longitudes
def generate_longitudes_latitudes():
    return (random.uniform(-90, 90),random.uniform(-90, 90))

#Populating named_tuple db
patient_db_named_tuple=[Patient_db(fake.name(),generate_age(),generate_longitudes_latitudes(),generate_blood_type())for i in range(10000)]


#Populating dictionary db
patient_db_dictionary= {
   fake.name(): {

        'location':generate_longitudes_latitudes(),
        'age': generate_age(),
        'blood_type': generate_blood_type()
    }
    for _ in range(10000)
}
def calculate_statistics(data_source):
    start_time = time.time()

    age_counter = 0
    location_counter_lat = 0
    location_counter_long = 0
    bloodgroup_dict = {}
    count = 0

    if isinstance(data_source, dict):
        # Handle dictionary of dictionaries
        for key, value in data_source.items():
            count += 1
            age_counter += value['age']
            location_counter_lat += value['location'][0]
            location_counter_long += value['location'][1]
            bloodgroup_dict[value['blood_type']] = bloodgroup_dict.get(value['blood_type'], 0) + 1

    elif isinstance(data_source, list):
        # Handle list of objects
        for item in data_source:
            count += 1
            age_counter += item.age
            location_counter_lat += item.location[0]
            location_counter_long += item.location[1]
            bloodgroup_dict[item.blood_type] = bloodgroup_dict.get(item.blood_type, 0) + 1

    average_age = age_counter / count
    mean_location = (location_counter_lat / count ,
                     location_counter_long / count)
    most_common_blood_type = max(bloodgroup_dict, key=bloodgroup_dict.get, default='None')

    end_time = time.time()

    print("Average age of all patients:", average_age)
    print("Mean location of all patients:", mean_location)
    print("Most common blood type:", most_common_blood_type)
    
    return average_age,end_time-start_time,sys.getsizeof(data_source)
    
average_age_dictionary_db,Time_dictionary_db,space_required_dictionary_db=calculate_statistics(patient_db_dictionary)

average_age_named_tuple_db,Time_named_tuple_db,space_required_named_tuple_db=calculate_statistics(patient_db_named_tuple)

def open_price(seed,circuit=0.1):

    ''' Indian Stock Exchanges have a circuit breaker. For the sake of brevity, I am assuming an intial breaker at 10% of the open price.
    This function calculates open , close and high prices'''
    random.seed(seed)

    open_price=random.uniform(0,1000)

    operator=random.choice(["+","-"])
    open_price = random.uniform(0, 1000)

    if operator == '+':
        close_price = open_price * (1 + random.uniform(0, circuit))
    elif operator == '-':
        close_price = open_price * (1 - random.uniform(0, circuit))

    High=max(open_price,close_price)*(1+random.uniform(0,circuit/2))

    return open_price,High,close_price


TSAI_stock_exchange=namedtuple('TSAI_stock_exchange','name symbol Open High Close' )

TSAI_stock_exchange_db=[TSAI_stock_exchange(fake.name().split()[0],fake.name().split()[0][2],open_price(seed)[0],open_price(seed)[1],open_price(seed)[2]) for i,seed in enumerate(range(100))]

def metrics_for_stock_exchange(Database):


    W_total=0
    for ticker in Database:
        #Let's say each company issued stocks anywhere from 10k to 100k(usually the number is way high in Stock Exchanges)
        w_random=random.randint(10000,100000)
        W_total+=w_random

        #Stock market high and low should be calculated dynamically. Index is usually high when stocks with high weightage and value are high
        # or all the stocks are high at a given point( which is very rare). For the sake of brevity, let's assume that all stocks hit high during the same time

        Market_value_high_unweighted=w_random*ticker.High
        Market_value_close_unweighted=w_random*ticker.Close
        Market_value_Open_unweighted=w_random*ticker.Open

    return round(Market_value_high_unweighted/W_total,2), round(Market_value_close_unweighted/W_total,2), round(Market_value_Open_unweighted/W_total,2)

high,close,open=metrics_for_stock_exchange(TSAI_stock_exchange_db)

