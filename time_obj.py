# Author: Bojan G. Kalicanin
# Date: 29-Oct-2016
# Representation of the time.

import operator

class Time(object):
    """Represents a Time."""
    def __init__(self, hour=0, minute=0, second=0):
        """
        Initialization of the class attributes at object creation
        (instantiation).
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        """Special method that returns string representation of the object."""
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute,
            self.second)
            
    def __add__(self, other):
        """Overloading of the addition operator (+)."""
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
            
    def __radd__(self, other):
        """
        Right-side add. This method is invoked when a Time object
        appears on the right side of the + operator.
        """
        return self.__add__(other)
            
    def print_time(self):
        """Print time in the usual format HH:MM:SS."""
        print("{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute,
            self.second))
            
    def time_to_int(self):
        """Convert time to integer, with base of 60."""
        minutes = self.hour*60 + self.minute
        seconds = minutes*60 + self.second
        return seconds
        
    def add_time(self, other):
        """Summing two time objects."""
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
        
    def increment(self, seconds):
        """Increment a time for a given number of the seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)
        
    def is_after(self, other):
        """Check if some time is after another."""
        return self.time_to_int() > other.time_to_int()
        
    def __lt__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return operator.lt(t1, t2)
        
        
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
            
if __name__ == '__main__':
    start = Time()
    start.hour = 11
    start.minute = 59
    start.second = 30
    start.print_time()
    print(start.time_to_int())

    end = start.increment(1337)
    end.print_time()

    print(end.is_after(start))
    print(start)

    duration = Time(1, 35)
    print(start + duration)
    print(start > end)