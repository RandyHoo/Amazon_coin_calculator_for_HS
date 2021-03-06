#! coding: Shift_JIS
#for Hearthstone
import math

have_coin = 0 #手持ちコイン
coinback = 0 #コインバック計算用
total_num = 0 #合計個数

#値段と個数、それぞれの要素番号が対応している必要がある
price_list	= [ 6000,	2400,	1200,	360 ]
num_list	= [ 40, 	15,  	7,  	2   ]

have_coin = int(input("手持ちコイン:"))

coinback = int(input("コインバック(%):"))
if coinback != 0:
	coinback /= 100

print("") #空行

print("手順:")
while ( have_coin / price_list[-1] ) >= 1:
	for i in range( 0, len( price_list ) ):
		if ( have_coin / price_list[i] ) >= 1:
			total_num += num_list[i]
			have_coin -= price_list[i]
			have_coin += price_list[i] * coinback
			math.ceil(have_coin)
			print("{0}パック購入".format(num_list[i]))

print("") #空行

print("合計パック:{0}".format(total_num)) #合計個数
print("余りコイン:{0}".format(int(have_coin))) #余りコイン
