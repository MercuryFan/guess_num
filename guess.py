#產生一個隨機整數1~100 (不要去印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話 要告訴他 比答案大或小

import random

r = random.randint(1, 100)
while True:
	num = input('請猜猜看,一個數字')
	num = int(num) #input會強迫答案變成字串,因此要使用型態轉換
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('比答案大,在往小點猜')
	elif num < r:
		print('比答案小,在往大點猜')

