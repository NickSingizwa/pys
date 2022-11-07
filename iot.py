# import requests
# import csv
# import serial

# def readFile(file):
#     jsonArray = []
#     with open(file, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)
#         for row in csvReader:
#             jsonArray.append(row)
#     return jsonArray

# ser = serial.Serial(
#         port='COM7',
#         baudrate=9600,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=1
# )
# ser.flush()

# if __name__ == '__main__':
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').rstrip()
#             f=open("transactions.txt","a")
#             f.write(line)
#             f.write("\n")
#             f.close()
#             data = readFile("transactions.txt")
#             res = requests.post(
#                 'http://localhost:5050/data', json=data)
#             if res.ok:
#                 print("Data uploaded")
#                 ser.write(bytes("Data uploaded"), 'utf-8')
#                 ser.flush()


import requests
import csv

def readFile(file):
    jsonArray = []
    with open(file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    return jsonArray

data = readFile("transactions.txt")
res = requests.post(
    'http://localhost:5050/data', json=data)
if res.ok:
    print("Data Uploaded")