from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar
import csv

with open('schedule.csv', 'w', newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(["Room","Start","End"])
		
	StartDate = date(2019,1,7)
	EndDate = date(2019,1,13)
	YearEnd = date(2019,12,31)
	while EndDate < YearEnd:
		for N in range(1,5):
			csvData = "Room " +str(N), StartDate.strftime("%d %B %Y"),EndDate.strftime("%d %B %Y")
			StartDate = EndDate + timedelta(days=1)
			EndDate = StartDate + timedelta(days=6)
			writer.writerow(csvData)

