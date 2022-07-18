# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="localhost",user="root",passwd="81281310xjf",database="homework",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
SELECT *
FROM test
"""
# 执行SQL语句
cursor.execute(sql)
# 通过fetchall方法获得数据
data = cursor.fetchall()
#打印输出数据
print(data)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
