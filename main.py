from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init('db/mars_explorer.db')
    app.run()


if __name__ == '__main__':
    main()
