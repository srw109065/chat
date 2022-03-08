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
	for line in chat:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue
		if person: #如果有值才運行
			new.append(person + ':' + line)
	return new
#把轉換後的新內容寫入並調整
def write_file(filename, chat):
	with open (filename, "w") as f:
		for line in chat:
			f.write(line + '\n')
#主要完整
def main(): 
	chat = read_file("input.txt")
	chat = convert(chat)
	write_file("output.txt", chat)

main()