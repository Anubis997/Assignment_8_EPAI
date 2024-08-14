
from collections import namedtuple
import random
import time
from tqdm import tqdm
from faker import Faker

fake = Faker()

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

