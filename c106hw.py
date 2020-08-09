import csv
import numpy as np

def getDataSouce(data_path):
    cup_of_coffees= []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cup_of_coffees.append(float(row['Cup of coffees']))
            hours_of_sleep.append(float(row['\t average hours of sleep (hours)']))

    return{'x': cup_of_coffees , 'y':hours_of_sleep}  

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between cups of coffe and hours of sleep \n ',correlation[0,1])

def setup():
    data_path = 'cups of coffe vs hours of sleep.csv'

    dataSource = getDataSouce(data_path)
    findCorrelation(dataSource)

setup()