# Author: Bojan G. Kalicanin
# Date: 29-Oct-2016
# Representation of the time.

class Time(object):
    """Represents a Time."""
    def __init__(self, hour=0, minute=0, second=0):
        """
        Initialization of the class attributes at object creation
        (instantiation).
        second: represents the seconds since midnight.
        """
        minutes = hour*60 + minute
        self.seconds = minutes*60 + second
        
    def __str__(self):
        """Special method that returns string representation of the object."""
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        time_str = "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)
        return time_str
            
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
        print(str(self))
            
    def time_to_int(self):
        """Convert time to integer, with base of 60."""
        return self.seconds
        
    def add_time(self, other):
        """Summing two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)
        
    def increment(self, seconds):
        """Increment a time for a given number of the seconds."""
        seconds += self.seconds
        return int_to_time(seconds)
        
    def is_after(self, other):
        """Check if some time is after another."""
        return self.seconds > other.seconds
        
    def is_valid(self):
        return self.seconds >= 0 and self.seconds < 24*60*60
        
def int_to_time(seconds):
    return Time(0, 0, seconds)
            
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