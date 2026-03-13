start-all.sh
jps
nano mapper.py
#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    words = re.findall(r'\b\w+\b', line.lower())
    for word in words:
        print(f"{word}\t1")

nano reducer.py
#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word == word:
    print(f"{current_word}\t{current_count}")

chmod +x mapper.py reducer.py
nano input.txt
apple banana apple
orange apple banana
apple
cat input.txt | ./mapper.py | sort -k1,1 | ./reducer.py