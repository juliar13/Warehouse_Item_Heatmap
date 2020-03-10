import numpy as np
import datetime

data_num = 1000
# item_num = 8000
item_num = 20
item_list = []
warehouse_list = ["Tokyo", "Osaka", "Nagoya", "Hokkaido", "Fukuoka", "Saitama"]

# Create Item List
for i in range(item_num):
  str_test = "itm_" + str(i)
  item_list.append(str_test)

# Output
with open('sample2.csv', 'w') as f:
  print("Item Name,Warehouse Name,Date,Number of Records,Lot Number,Warehouse Index", file=f)

  for i in range(data_num):
    item_rand = np.random.randint(len(item_list))
    warehouse_index = np.random.randint(len(warehouse_list))
    date = datetime.date.today().replace(day=np.random.randint(1,29))
    output = item_list[item_rand] + ","
    output += warehouse_list[warehouse_index] + ","
    output += str(date) + ","
    output += str(np.random.randint(10)) + ","
    output += "00001," # Lot Number
    output += str(warehouse_index)
    print(output, file=f)
