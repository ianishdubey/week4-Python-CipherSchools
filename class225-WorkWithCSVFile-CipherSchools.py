from csv import reader

with open('file.csv','r') as f:
    csv_reader = reader(f)
    # iterator 
    next(csv_reader)
    for now in csv_reader:
        print(csv_reader)