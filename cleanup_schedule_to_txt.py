from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main(): 
	f = open("cleanup_schedule.txt","w+")
	StartDate = date(2019,1,7)
	EndDate = date(2019,1,13)
	YearEnd = date(2019,12,31)
	#use another for loop inside while
	#For rooms and use room number to calculate the ranges
	#while date is in the limit for rooms in range 1 to for calculate start and end date
	#how to print different room numbers? N as varable and use it with "Room" in print function?

	while EndDate < YearEnd:
		for N in range(1,5):
			f.write("Room " +str(N) + ": " +StartDate.strftime("%d %B %Y") +" to "+EndDate.strftime("%d %B %Y")+"\r\n")
			StartDate = EndDate + timedelta(days=1)
			EndDate = StartDate + timedelta(days=6)

	f.close()
if __name__ == "__main__":
  main()