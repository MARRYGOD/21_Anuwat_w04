score = int(input("Enter your score : "))
'''
>90 A Very Good !!!
>80 B Good!
>70 C Normal
>60 D Pass
<60 F Fool!!
'''
if score >= 90:
    grade = "A"
    Comment = "เอ็งนี้มันหัวหมอพ่อหนุ่ม!!"
elif score >= 80:
    grade = "B"
    Comment = "ดีมากพลทหาร"
elif score >= 70:
    grade = "C"
    Comment = "ถือว่าเอ็งยังมีความสามารถ"
elif score >= 60:
    grade = "D"
    Comment = "คาบเส้นนะไอ้หนู!!!"
else:
    grade = "F"
    Comment = "เอ็งไปตายให้หนอนขึ้นตัวเถอะ!!!"
    
print(f"คะแนน={score}")
print(f"ได้เกรด={grade}")
print(f"ความคิดเห็น={Comment}")

