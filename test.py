
import assignment_8

def test_seeds_results():
    ''' Ensure that different seeds produce different results '''
    results = [open_price(seed) for seed in range(10)]
    assert len(results) == len(set(results))

def test_stock_prices_seed():
    ''' This test is to check whether all the stock prices are same for same seeds'''
    assert open_price(1)==open_price(1)
    assert open_price(1)[0]==open_price(1)[0]
    assert open_price(1)[1]==open_price(1)[1]
    assert open_price(1)[2]==open_price(1)[2]

def irrelevant_close_prices():
      '''The breakers are usually set at 10,15 & 20. The trading is paused after the circuit is broken.
      In some cases the halt goes for a few days to stabilise markets. So, if the random price generator gives a +- 20% from the open_price, it's wrong. '''
      open_p = open_price(1)[0]
      close_p = open_price(1)[2]
      assert close_p < open_p * 1.2
      assert close_p > open_p * 0.8

def irrelevant_High_prices():
    ''' Verify that the high price is within expected bounds based on open price '''
    open_p = open_price(1)[0]
    high_p = open_price(1)[1]
    assert high_p < open_p * 1.2
    assert high_p > open_p * 0.8

def irrelevant_Hi_Lo_prices():
    ''' Verify that the high price is greater than open and close prices '''
    open_p, high_p, close_p = open_price(1)
    assert high_p > open_p
    assert high_p > close_p

def irrelevant_Index_close_prices():
    ''' Verify that the average close price index is within expected bounds '''
    avg_high, avg_close, avg_open = metrics_for_stock_exchange(TSAI_stock_exchange_db)
    assert avg_close < avg_open * 1.2
    assert avg_close > avg_open * 0.8

def irrelevant_Index_High_prices():
    ''' Verify that the average high price index is within expected bounds '''
    avg_high, avg_close, avg_open = metrics_for_stock_exchange(TSAI_stock_exchange_db)
    assert avg_high < avg_open * 1.2
    assert avg_high > avg_open * 0.8

def irrelevant_Index_Hi_Lo_prices():
    ''' Verify that the average high price index is greater than average close and open prices '''
    avg_high, avg_close, avg_open = metrics_for_stock_exchange(TSAI_stock_exchange_db)
    assert avg_high > avg_close
    assert avg_high > avg_open

