# epoch = a date and time from which a computer measures system time

import time

print(time.ctime())    # convert a time expressed in seconds since epoch to a readable string

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime() # local time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_object = time.gmtime() # UTC time

time_string = "On 20 April, 2020"
time_object = time.strptime(time_string, "On %d %B, %Y") # parse a string object to a time object
print(time_object)

# (year, month, day, hours, secs, #day of the week, #day of the year, day time saving)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)  # convert a tuple representation of a time object to a readable string
print(time_string)

time_string = time.mktime(time_tuple)   # convert a tuple representation of a time object to time since epoch
print(time_string)