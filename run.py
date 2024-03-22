from flask import Flask, render_template
import pymysql
import pandas as pd

# # 连接 MySQL 数据库
conn = pymysql.connect(
    host='127.0.0.1',  # 主机名
    port=3306,  # 端口号，MySQL默认为3306
    user='root',  # 用户名
    password='2003721gavin?',  # 密码
    database='comp3030j',  # 数据库名称
)
# # 创建游标对象
cursor = conn.cursor()
# # 执行 SQL 查询语句
cursor.execute("SELECT * FROM users")
# # # 获取查询结果
result = cursor.fetchall()
# # # 将查询结果转化为 Pandas dataframe 对象
df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])
print(df)
#打印结果
for x in cursor:
    print(x)



app = Flask(__name__,
            static_folder = "frontend/dist/assets",
            template_folder = "frontend/dist")
@app.route('/', defaults={'path': ''})
@app.route('/home')
def catch_all(path):
    return render_template("index.html")

# def hello_world():
#     return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)