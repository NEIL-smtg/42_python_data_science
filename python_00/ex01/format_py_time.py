import datetime
import time

startTuple = (1970, 1, 1)
start = datetime.date(*startTuple)

seconds = time.time()

today = datetime.date.today()
dayStr = today.strftime("%B %d %Y")

# dash is to get rid of leading zero
# adding , into seconds and format it to 4 decimal points
print("Seconds since {:%b %-d, %Y}: ".format(start), end="")
print("{:,.4f}".format(seconds), "or {:e}".format(seconds), end="")
print(" in scientific notation")
print(dayStr)
