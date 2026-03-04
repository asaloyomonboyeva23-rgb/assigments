class TimeDuration:
    def __init__(self,hours,minutes):
        total_minutes = hours * 60 + minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60
    def __str__ (self):
        return (f"{self.hours}h {self.minutes}m")
    def __repr__(self):
        return f"TimeDuration({self.hours}, {self.minutes})"
    def __add__(self,other):
        if isinstance(other,TimeDuration):
            total_minutes = (self.hours + other.hours)*60 +(self.minutes + other.minutes)
            return TimeDuration(0,total_minutes)
        elif isinstance(other ,(int,float)):
            total_minutes = self.hours *60 + self.minutes + int(other)
            return TimeDuration(0, total_minutes)
        return NotImplemented
    def __eq__(self,other):
        if isinstance (other, TimeDuration):
            return self.hours == other.hours and self.minutes == other.minutes
        return NotImplemented
    def __bool__(self):
            return (self.hours * 60 + self.minutes) > 0

t1 = TimeDuration(1, 45)
t2 = TimeDuration(0, 30)
t3 = TimeDuration(2, 15)

print(str(t1))
print(repr(t1))
print(t1 + t2)
print(t1 + 20)
print((t1 + t2) == t3)
print(bool(TimeDuration(0, 0)))