""" Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days """

#import calendar as c;
import datetime as d;
dateA=d.date(2014,7,2);
dateB=d.date(2014, 7, 11);
print (dateB-dateA).days;
