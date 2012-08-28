import datetime as _datetime
import sys as _sys

def p019(lower_bound, upper_bound):
	date = lower_bound
	while date.day != 1:
		date += _datetime.timedelta(days=1)
	sundays = 0
	while date <= upper_bound:
		if date.isoweekday() == 7:
			sundays += 1

		date += _datetime.timedelta(days=1)
		while date.day != 1:
			date += _datetime.timedelta(days=1)
	return sundays
		

if __name__ == '__main__':
	if len(_sys.argv) == 3:
		print(p019(_datetime.datetime.strptime(_sys.argv[1], '%m/%d/%Y'), _datetime.datetime.strptime(_sys.argv[2], '%m/%d/%Y')))
	else:
		print('Usage: p019 <date> <date>')
		_sys.exit()
