data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 # wc一開始為空清單，之後字有重複就加一
		else:
			wc[word] = 1 # 計數器先把新的字紀錄為一

for word in wc:			# word為每一個key
	if wc[word] > 100:
		print(word, wc[word])	# wc[word]為次數(value)

print(len(wc))
print(wc['Nick'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過。')

print('感謝使用本查詢功能')