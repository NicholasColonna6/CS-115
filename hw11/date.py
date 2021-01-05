'''
Created on 11/26/2017
@author:   Nicholas Colonna
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." ncolonna

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and self.day == d2.day
    
    def tomorrow(self):
        '''change the calling object so that it represents one calendar day after the original date'''
        if self.isLeapYear() == True and self.month == 2 and self.day == 28:
            self.month = 2
            self.day = 29
        elif 1 + self.day > DAYS_IN_MONTH[self.month]:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month +=1
        else:
            self.day += 1
    
    def yesterday(self):
        '''change the calling object so that it represents one calendar day before the original date'''
        if self.isLeapYear() == True and self.month == 3 and self.day == 1:
            self.month = 2
            self.day = 29
        elif self.day == 1:
            if self.month == 1:
                self.month = 12
                self.year -= 1
            else:
                self.month -=1
            self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
        
    def addNDays(self, N):
        '''changes calling object so that it represents N days after original date'''
        print(self)
        i = 0
        while i < N:
            self.tomorrow()
            print(self)
            i += 1
            
    def subNDays(self, N):
        '''changes calling object so that it represents N days before original date'''
        print(self)
        i = 0
        while i < N:
            self.yesterday()
            print(self)
            i += 1
            
    def isBefore(self, d2):
        '''returns True if calling object is before d2, and False if they are the same or it is after'''
        if self.year < d2.year:
            return True
        if self.year == d2.year and self.month < d2.month:
            return True
        if self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return True
        return False
    
    def isAfter(self, d2):
        '''returns True if calling object is after d2, and False if they are the same or it is before'''
        if self.year > d2.year:
            return True
        if self.year == d2.year and self.month > d2.month:
            return True
        if self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return True
        return False
    
    def diff(self,d2):
        '''returns number of days between self and d2'''
        days = 0
        d2Copy = Date.copy(d2)
        selfCopy = Date.copy(self)
        if Date.isAfter(self, d2) == True:
            while Date.isAfter(selfCopy, d2Copy) == True:
                Date.tomorrow(d2Copy)
                days += 1
        else:
            while Date.isBefore(selfCopy, d2Copy) == True:
                Date.yesterday(d2Copy)
                days -= 1
        return days
    
    def dow(self):
        '''returns string that indicates day of the week of the object'''
        baseDate = Date(11,9,2011) #this is a Wednesday
        daysDiff = self.diff(baseDate)
        dowVal = abs(daysDiff % 7)
        daysOfWeek = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        return daysOfWeek[dowVal]

'''
Testing:

d = Date(11, 9, 2011)
print(d)
print("Wednesday is", d)
d2 = Date(11, 9, 2011)
print(d2)
print(d == d2)
print(id(d))
print(id(d2))
print(d2.isLeapYear())
d3 = Date(1,1,2012)
print(d3.isLeapYear())
    
d = Date(1,1,2011)
d2 = d.copy()
print(d, d2)
print(d == d2)
print(d.equals(d2))

d = Date(12,31,2010)
print(d)
d.tomorrow()
print(d)
d2 = Date(2,28,2012)
print(d2)
d2.tomorrow()
print(d2)
            
d = Date(1,1,2011)
print(d)
d.yesterday()
print(d)
d2 = Date(3,1,2012)
print(d2)
d2.yesterday()
print(d2)
d2.yesterday()
print(d2)
            
d = Date(11, 9, 2011)
d.addNDays(3)
print(d)
d = Date(11,11,2011)
d.addNDays(1283)
print(d)

d = Date(11, 12, 2011)
d.subNDays(3)
print(d)
d = Date(5,17,2015)
d.subNDays(1283)
print(d)
    
d = Date(11,11,2011)
d2 = Date(1,1,2012)
print(d.isBefore(d2))
print(d2.isBefore(d))
print(d.isBefore(d))

print(d.isAfter(d2))
print(d2.isAfter(d))
print(d.isAfter(d))
    
d = Date(11,9,2011)
d2 = Date(12,16,2011)
print(d2.diff(d))
print(d.diff(d2))
print(d,d2)
d3 = Date(5,18,2012)
print(d3.diff(d))
print(d.diff(Date(1,1,1899)))
print(d.diff(Date(1,1,2101)))
    
d = Date(12,7,1941)
print(d.dow())
print(Date(10,28,1929).dow())
print(Date(10,19,1987).dow())
print(Date(1,1,2100).dow())'''
