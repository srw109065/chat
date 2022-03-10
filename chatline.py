#讀取原始檔案
def read_file(filename):
	chat = []
	with open(filename, "r", encoding = "utf-8-sig") as r:
		for line in r:
			chat.append(line.strip())
	return chat
#轉換格式內容:在原始檔案中搜尋人名並儲存加上:及聊天內容

def convert(chat):
	new = [] #新增空清單來裝載修改的新內容
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in chat:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if name == "Allen":
			if s[2] == "貼圖":
				allen_sticker_count += 1
			elif s[2] == "圖片":
				allen_image_count += 1
			else:	
				for m in s[2:]:
					allen_word_count += len(m)	

		elif name == "Viki":
			if s[2] == "貼圖":
				viki_sticker_count += 1
			elif s[2] == "圖片":
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print("allen說了幾個字:", allen_word_count, "傳了", allen_sticker_count, "個貼圖", "傳了", allen_image_count, "個圖片")
	print("viki說了幾個字:", viki_word_count, "傳了", viki_sticker_count, "個貼圖", "傳了", viki_image_count, "個圖片")
	return new
#把轉換後的新內容寫入並調整

def write_file(filename, chat):
	with open (filename, "w") as f:
		for line in chat:
			f.write(line + '\n')
#主要完整

def main(): 
	chat = read_file("LINE-Viki.txt")
	chat = convert(chat)
	#write_file("output.txt", chat)

main()	