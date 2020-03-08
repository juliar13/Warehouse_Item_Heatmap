import numpy as np
import datetime

item_num = 8000
item_list = []
warehouse_list = ["Tokyo", "Osaka", "Nagoya", "Hokkaido", "Fukuoka", "Saitama"]

for i in range(item_num):
  str_test = "itm_" + str(i)
  item_list.append(str_test)

data_num = 100000

with open('sample.csv', 'w') as f:
  print("Item Name,Warehouse Name,Date", file=f)

  for i in range(data_num):
    rand = np.random.randint(len(item_list))
    print(item_list[rand] + "," + warehouse_list[np.random.randint(5)] + "," + str(datetime.date.today()), file=f)
