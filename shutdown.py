import os

# put time in seconds based on the charge there is on the phone

hours = 3

minutes = 5

total_time_in_minutes = hours*60 + minutes

total_time_in_seconds = total_time_in_minutes*60

##print(total_time_in_seconds)

os.system("shutdown /s /t " + str(total_time_in_seconds))

# the number 18000 above indicates that the time is in seconds and it is 5 hours