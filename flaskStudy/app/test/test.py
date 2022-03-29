from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/', methods=['GET'])
def index():
    return render_template('/test/test.html', result=None, resultData=None, resultUPDATE=None)


@test.route('/insert', methods=['GET'])
def insert():
    db_class = dbModule.Database()

    sql = "insert into studydb.testTable(test) values ('%s')" %('testData')

    db_class.execute(sql)
    db_class.commit()

    return render_template('/test/test.html', result='insert is done!', resultData=None, resultUPDATE=None)


@test.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()

    sql = "select idx, test from studydb.testTable"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('/test/test.html', result=None, resultData=row[0], resultUPDATE=None)


@test.route('/update', methods=['GET'])
def update():
    db_class = dbModule.Database()

    sql = "update studydb.testTable set test='%s' where test='testData'" %('update_Data')

    db_class.execute(sql)
    db_class.commit()

    sql = "select idx, test from studydb.testTable"
    
    row = db_class.executeAll(sql)

    return render_template('/test/test.html', result=None, resultData=None, resultUPDATE=row[0])
