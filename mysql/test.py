import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='qidi1234',
                       port=3306,
                       db='mysql',
                       charset='utf8',
                       )
cur = conn.cursor()

# 创建表格
sql_crateTB = """create table topics(
    name_id int not null auto_increment,
    last_name char(20),
    age int,
    sex char(1),
    primary key(name_id))
    """
# 插入数据
sql_insert = "insert into money(last_name,age,sex) value('de2',18,0)"
cur.execute(sql_insert)

"""
sql = "select * from user"
cur.execute(sql)
data = cur.fetchall()
for i in data[:2]:
    print(i)
"""

cur.close
conn.close
