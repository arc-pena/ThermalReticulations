import csv
reader = csv.reader(['1997,Ford,E350,"Super, luxurious truck"'], skipinitialspace=True)
for r in reader:
    print(r)