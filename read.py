data = []
count = 0
with open('reviews.txt','r') as f: #讀取留言紀錄文字檔

#每進入新的一則留言，計數器加1，並將留言的內容存進清單data中。
	for line in f:
		count += 1 
		data.append(line)

#以千為單位，印出目前讀到第幾筆留言
#		if count % 1000 == 0:
#			print(len(data))

#印出總共有幾筆留言
#print(len(data))
data_sum = 0
for d in data:
	data_sum += len(d)
data_ave = data_sum/len(data)
print(data_ave)	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('資料長度小於100的留言有', len(new), '則')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言有提到good的留言有', len(good), '則')

#good = [d for d in data if 'good' in d]      
wc = {} #word count
#讀取每一則留言，字與字之間用空白鍵分開，並將結果存進words
for d in data:
    words = d.split(' ')
    #計算每個字重複的次數
    for word in words:
        if word in wc:
            wc[word] += 1 #修改key的值
        else:    
            wc[word] = 1 #新增Key進wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word,wc[word])
while True:
    word = input('請輸入要查詢的字，按q離開查詢:')
    if word == 'q':
        break
    else:
        if word in wc:
            print(word,'出現的次數為:',wc[word])
        else:
            print('這個字沒有出現過喔')    
print('感謝您本使用查詢功能，歡迎再次使用')    
