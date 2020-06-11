import pymysql



def chaxun(sql):
    """
        查询数据mysql数据库:只能select，不要delete update insert
    """
    # pymysql 连接数据库
    # host="192.144.148.91":数据库的ip地址 user="ljtest"：数据库登录账号, password="123456"：密码, db="ljtestdb"：数据库名字
    db = pymysql.connect(host="122.51.58.214", user="root", password="123456", db="ljtestdb")
    # 获取游标 ：查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()

    return res

#  sql = 'select * from t_admin where id = 1' 
#  a = chaxun(sql)
#  print(a)



def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    # 打开数据库
    db = pymysql.connect(host="122.51.58.214", user="root", password="123456", db="ljtestdb")
    # 获取游标 ： 查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 提交修改 
    db.commit()
    db.close()
    return True

# update
# sql = "update t_student set sname='空空' where id=2"

# insert
# sql = 'INSERT into t_student values(21, "cc", "位置", NULL, NULL, NULL, NULL)'

# delete
# sql = "delete from t_student where id=21"
# commit(sql)

