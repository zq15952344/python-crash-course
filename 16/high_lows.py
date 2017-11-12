import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	print reader
	header_row = next(reader)
	print header_row
	
	dates, highs, mids, lows = [], [], [], []
	for row in reader:
		try:
			high = int(row[1])
			mid = int(row[2])
			low = int(row[3])
			
			
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
		except ValueError:
			print current_date, 'missing data'
		else:
			highs.append(high)
			mids.append(mid)
			lows.append(low)
			dates.append(current_date)
		
	print highs
	print dates
	for index, column_header in enumerate(header_row):
		print index, column_header

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
#plt.plot(dates, mid, c='yellow')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates,lows,highs,facecolor='blue', alpha=0.1)
plt.title('Daily high and low temperatures, 2014', fontsize=20)
plt.xlabel('', fontsize=10)
plt.ylabel('Temperature (F)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
fig.autofmt_xdate()
plt.show()
