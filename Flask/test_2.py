# 文件读取
with open('D:\Python_big\example\movie_2.csv','rb') as f:
    data = f.read()
    print("utf-8 bytes:",data)
    data1 =data.decode('utf-8')
    print("utf-8 str:",data1)
    s = data1.encode('gb18030')
    print("gbk bytes:",s)
    s1 = s.decode('gb18030')
    print("gbk str:",s1)
