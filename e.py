from datetime import datetime
from time import sleep #Yo! That's some cool auto import shit!

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59] # This is longer than my 16-hour
# flight from Dubai to Miami.

right_this_minute = datetime.today().minute

while True: # The original code didn't contain a while loop. I basically improved the first code that's in Paul Barry's "Head first into Python".
    sleep(59.9) # Yes, I know a minute is 60. Go think about it for the next 4 years.
    if right_this_minute in odds:
        print("This minute is odd.")
    else:
        print("This minute is not odd.")# No shit sherlock!
        
        # If you havent figured, this tells if the minute right now is odd or not.
