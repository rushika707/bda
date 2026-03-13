nano dataset.csv
2000,17,13
2001,15,12
2002,11,7
2003,14,10
2004,9,5
2005,12,10
2006,11,7
2007,16,12
2008,13,9
2009,15,12
2010,12,8
2011,16,12
2012,9,5
2013,14,10
2014,15,11
2015,14,11
2016,9,5
2017,16,12
2018,13,9
2019,14,10
2020,16,12
nano wmap.py
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    year, temp_max, temp_min = map(int, line.split(','))
    print(f"{year} {temp_max}")
nano wred.py
#!/usr/bin/env python3
import sys

dmax = {}
dmin = {}

for line in sys.stdin:
    line = line.strip()
    year, temp = map(int, line.split())

    if year not in dmax:
        dmax[year] = temp
        dmin[year] = temp
    else:
        if temp > dmax[year]:
            dmax[year] = temp
        if temp < dmin[year]:
            dmin[year] = temp

for year in dmax:
    print(f"Year: {year}, Max Temp: {dmax[year]}, Min Temp: {dmin[year]}")
chmod +x wmap.py wred.py
cat dataset.csv | python3 wmap.py | python3 wred.py
start-all.sh
jps
hadoop fs -mkdir /weather
hadoop fs -put dataset.csv /weather
hadoop jar hadoop-streaming-3.3.6.jar -file wmap.py -file wred.py -mapper "python3 wmap.py" -reducer "python3 wred.py" -input /weather/dataset.csv -output /weather/output
hadoop fs -cat /weather/output/part-00000