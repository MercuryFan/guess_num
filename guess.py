#產生一個隨機整數1~100 (不要去印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話 要告訴他 比答案大或小

#延伸: 印出總共猜幾次
#延伸2: 讓使用者自行決定範圍值

import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start) #因input出來的值為字串，故使用int做型態轉換
end = int(end)
count = 0
r = random.randint(start, end)

while True:
	count += 1 # count = count + 1
	num = input('請猜猜看,一個數字:')
	num = int(num) #input會強迫答案變成字串,因此要使用型態轉換
	if num == r:
		print('終於猜對了,您一共猜了', count, '次')
		break
	elif num > r:
		print('比答案大,在往小點猜')
	elif num < r:
		print('比答案小,在往大點猜')
	print('這是你猜的第', count, '次')
	# 減少重複性，避免程式延遲

