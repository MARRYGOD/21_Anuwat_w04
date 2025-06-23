# num_1 = 10
# num_2 = 20

# print(f"{num_1 <= num_2}")

# name_1 = "apple"
# name_2 = "banana"

# print(F"{name_1 > name_2}")

Fruits = ["apple","banana","watermelon","cherry"]
find_fruit = input(str("ใส่ชื่อผลไม้ที่ต้องการหา : "))

if find_fruit in Fruits:
    print(f"มี {find_fruit} อยู่ในรายการ")
else:
    print(f"ไม่มี {find_fruit} อยู่ในรายการ")