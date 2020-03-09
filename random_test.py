import numpy as np
import datetime

# item_num = 8000
item_num = 20
item_list = []
warehouse_list = ["Tokyo", "Osaka", "Nagoya", "Hokkaido", "Fukuoka", "Saitama"]

for i in range(item_num):
  str_test = "itm_" + str(i)
  item_list.append(str_test)

data_num = 1000

with open('sample.csv', 'w') as f:
  print("Item Name,Warehouse Name,Date,Number of Records,Lot Number,Warehouse Index", file=f)

  for i in range(data_num):
    rand = np.random.randint(len(item_list))
    output = item_list[rand] + ","
    output += warehouse_list[np.random.randint(len(warehouse_list))] + ","
    output += str(datetime.date.today()) + ","
    output += "1,1,A"

    # print(item_list[rand] + "," + warehouse_list[np.random.randint(len(warehouse_list))] + "," + str(datetime.date.today()) + ",1,1,A", file=f)
    print(output, file=f)
