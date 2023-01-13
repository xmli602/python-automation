import random
import pymysql
from pymysql.converters import escape_string

db = pymysql.connect(host="192.168.18.168",port=3306,user="lixiaoman",password="lxm@123!",database="business_yunyang")
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from theme_score where id like '500235_2022_08040400%'"
cursor.execute(sql)
result = cursor.fetchall()
for line in result:
    id = line['id']
    # value = random.randint(10, 19)
    value = random.uniform(1200,3000).__round__(2)
    print(id,value)
    sql_update = ''' update theme_score set value = %s where id = %s; '''
    cursor.execute(sql_update, (value,id))
    db.commit()