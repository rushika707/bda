
Weather.txt
hadoop@ubuntu22:~$ nano weather.txt

year maxtemp mintemp
2022 35 20
2021 33 18
2020 38 22
2019 36 21
2018 37 19
2017 34 18
2016 32 17
 
cleaner.py
hadoop@ubuntu22:~$ nano cleaner.py

import re
import sys
for i in sys.stdin:
    print(re.sub(r'\s+','',i))

hadoop@ubuntu22:~$ cat weather.txt | python3 cleaner.py > weather_cleaned.txt

hadoop@ubuntu22:~$ pig -x local

grunt> weather_data = LOAD 'weather.txt' USING PigStorage(' ') AS (year:int, maxtemp:int, mintemp:int);
grunt> DUMP weather_data

grunt> filtered_weather = FILTER weather_data BY maxtemp > 35;
grunt> DUMP filtered_weather;

grunt> grouped_weather = GROUP weather_data BY year;
grunt> DUMP grouped_weather;

grunt> grouped_weather_count = FOREACH grouped_weather GENERATE group AS year, COUNT(weather_data) AS record_count;
grunt> DUMP grouped_weather_count;


