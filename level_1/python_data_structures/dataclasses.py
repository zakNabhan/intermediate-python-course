"""
Since Python 3.7, dataclasses let us define ordinary objects with a clean syntax for 
specifying attributes. They look – superficially – very similar to named tuples. This 
is a pleasant approach that makes it easy to understand how they work.

"""

#Here's a dataclass version of our Stock example

from dataclasses import dataclass

@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float


s = Stock(symbol="TestStock", current=494.4, high = 949.43, low= 33.1)
print(s.current)

