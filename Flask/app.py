from flask import Flask, render_template
import sqlite3
import os.path

app = Flask(__name__)


@app.route('/index')
def index():
    infos = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select * from movie order by score desc"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)
    cur.close()
    con.close()
    return render_template("index.html",infos=infos)


@app.route('/Ciyun')
def Ciyun():
    name = []
    score = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select name,score from movie_2 group by name"
    data4 = cur.execute(sql)
    for item in data4:
        name.append(item[0])
        score.append(item[1])
    return render_template("Ciyun.html", name=name, score=score)

@app.route('/Test')
def Test():
    name = []
    score = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select name,score from movie_2 group by name"
    data4 = cur.execute(sql)
    for item in data4:
        name.append(item[0])
        score.append(item[1])
    return render_template("test.html", name=name, score=score)

@app.route('/Time')
def Time():
    yeas = []
    num = []
    mon = []
    num_m = []
    avg = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql ="select yeas,count(yeas) from movie_3 group by yeas"
    data5 = cur.execute(sql)
    for item in data5:
        yeas.append(item[0])
        num.append(item[1])
    sql = "select mon,count(mon),avg(score) from movie_3 group by mon"
    data6 = cur.execute(sql)
    for item in data6:
        mon.append(item[0])
        num_m.append(item[1])
        avg.append(item[2])
    return render_template("Time.html",yeas=yeas,num=num,num_m=num_m,mon=mon,avg=avg)

@app.route('/Top100')
def Top100():
    name = []
    score = []
    yeas = []
    long_t = []
    name2 = []
    score2 = []
    yeas2 = []
    long_t2 = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select name,score,yeas,long_time from movie_3 group by yeas having long_time < 130 and long_time >100 and yeas >1999"
    data4 = cur.execute(sql)
    for item in data4:
        name.append(item[0])
        score.append(item[1])
        yeas.append(item[2])
        long_t.append(item[3])
    sql = "select name,score,yeas,long_time from movie_3 order by score desc limit 0,20"
    data5 = cur.execute(sql)
    for item in data5:
        name2.append(item[0])
        score2.append(item[1])
        yeas2.append(item[2])
        long_t2.append(item[3])

    cur.close()
    con.close()
    return render_template("Top 100.html",name=name,score=score,yeas=yeas,long_t=long_t,name2=name2,score2=score2,yeas2=yeas2,long_t2=long_t2)

#时长
@app.route('/Shichang')
def Shichang():
    long_time = []
    name = []
    score = []
    test = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select name,long_time,score from movie_2 group by name"
    data2 = cur.execute(sql)
    for item in data2:
        test.append([item[1],item[2]])

    sql = "select name,long_time from movie_2 where long_time group by long_time"
    data3 = cur.execute(sql)
    for item in data3:
        name.append(item[0])
        long_time.append(item[1])

    cur.close()
    con.close()
    return render_template("Shichang.html",name=name,long_time=long_time,score=score,test=test)

#评分
@app.route('/Pingfen')
def Pingfen():
    #评分-柱状图/圆饼图
    score = []
    num = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Movie.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select score,count(score) from movie group by score"
    data1 = cur.execute(sql)
    for item in data1:
        score.append(item[0])
        num.append(item[1])

    cur.close()
    con.close()
    return render_template("Pingfen.html",score=score,num=num)

if __name__ == '__main__':
    app.run()
