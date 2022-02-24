#stock = "AAPL", 123.52, 53.15, 137.98
#stock2 = ("AAPL", 123.52, 53.15, 137.98)

#print(stock)

# call it with function or object
import datetime

#tuples

def middle(stock, date):
    symbol, current, high, low = stock
    return(((high + low) / 2 ), date)


def get_high(stock):
    symbol, current, high, low = stock
    return f" High : {high}"

stock_tuple = "AAPL", 123.52, 53.15, 137.98
print(middle(stock_tuple, datetime.date.today))
print(get_high(stock_tuple))


#Named tuples via typing.NamedTuple

from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    # create methode to compute derived values of the attributes of named tuple

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2

# create a geeneric tuple

s = Stock(symbol="Apple", current=33.9, high=38, low=4.8 )

print(s.high)
print(s[2])
symbol, current, high, low = s
print(symbol, current, high, low)

# print middle
print(s.middle)
