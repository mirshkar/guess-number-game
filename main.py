import random

number = random. randint (1,10)

attempts=0
while attempts<3:

 guess=int(input("عددحدسی خودراواردکن "))
 attempts+=1

 if guess==number:
    print("حدس شمادرسته.")

    break
else:
    print("حدس شمااشتباه دوباره تلاش کن.")

    if attempts== 3 and guess!= number:
         print("متاسفم!تموم شدعدددرست این بود." ,number)

