from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#import cv2



app = Flask(__name__)#созданияе объекта по файлу app
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
#db = SQLAlchemy(app)


#class Article(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #video = db.Column(db.File)
    #nameIll = db.Column(db.String(10), nullable=False)
    #epilepsion = db.Column(db.String(10), nullable=False)
    #text = db.Column(db.Text, nullable=False)
    #date = db.Column(db.DateTime, default=datetime.utcnow)

    #def __repr__(self):
    #    return '<Article %r>' % self.id


@app.route('/',methods=['POST','GET'])#главная страничка
@app.route('/home',methods=['POST','GET'])#главная страничка

def index():
    #if request.method == "POST":
        #video = request.form['video']
        #dalt = request.form['nameIll']
        #epil = request.form['Epilepsion']
        #article = Article(nameIll = dalt, epilepsion = epil)

        #try:
        #    db.session.add(article)
        #    db.session.commit()
        #    return redirect('/viewing')
        #except:
        #    return "При добавлении видео возникли ошибки!"

        #return render_template("viewing.html", articles=video,ar2 = dalt)
        #return redirect('/viewing')
    #else:
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


