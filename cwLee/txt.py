try:
    tFile = open('story.txt', encoding='UTF-8')
    print("열기 완료")

    tTextLine = tFile.readline()
    tlineNumber = 1
    print(tTextLine)

    print(".")

    for i in tFile:
        print(i)
        tlineNumber = tlineNumber + 1
    tFile.close()
except:
    print("파일 존재 안함")
