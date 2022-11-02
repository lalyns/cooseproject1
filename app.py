from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

import certifi

#성준 db
junclient = MongoClient('mongodb+srv://sparta:test@cluster0.u8xq40k.mongodb.net/Cluster0?retryWrites=true&w=majority')
jundb = junclient.dbsparta

#조운 db
jw_client = MongoClient('mongodb+srv://test:sparta@Cluster0.xtye7kw.mongodb.net/?retryWrites=true&w=majority')
jw_db = jw_client.dbsparta

#용연 db
eli_client = MongoClient('mongodb+srv://test:sparta@cluster0.iytbmso.mongodb.net/Cluster0?retryWrites=true&w=majority')
eli_db = eli_client.dbsparta

#성윤 db
syjclient = MongoClient('mongodb+srv://test:sparta@cluster0.lot5yin.mongodb.net/Cluster0?retryWrites=true&w=majority')
syjdb = syjclient.dbsparta

#남훈 db
ca = certifi.where()
nhk_client = MongoClient('mongodb+srv://test:sparta@cluster0.j4reysf.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
nhkdb = nhk_client.miniteam

@app.route('/')  #팀페이지
def home():
    return render_template('index.html')

@app.route('/jun-page')   #성준페이지
def jun_page():
    return render_template('jun-page.html')

@app.route('/jw-page')   #조운페이지
def jw_page():
    return render_template('jw-page.html')

@app.route('/elicho-page')   #용연페이지
def elicho_page():
    return render_template('elicho-page.html')

@app.route('/SYJ')   #성윤페이지
def SYJ():
    return render_template('SYJ.html')

@app.route('/nhk')    #남훈페이지
def nhk_page():
    return render_template('nhk.html')


#메인
@app.route("/coosemain", methods=["POST"])
def coose_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name':name_receive,
           'comment':comment_receive}

    nhkdb.coosemain.insert_one(doc)

    return jsonify({'msg':'메인 페이지 방명록 저장 완료!'})


@app.route("/coosemain", methods=["GET"])
def coose_get():
    comment_list = list(nhkdb.coosemain.find({}, {'_id': False}))

    return jsonify({'comment':comment_list})

#성준
@app.route("/coosejun", methods=["POST"])
def coosejun_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name':name_receive,
           'comment':comment_receive}

    jundb.coosejun.insert_one(doc)

    return jsonify({'msg':'메인 페이지 방명록 저장 완료!'})


@app.route("/coosejun", methods=["GET"])
def coosejun_get():
    comment_list = list(jundb.coosejun.find({}, {'_id': False}))

    return jsonify({'comment':comment_list})

#조운
@app.route("/kus_jw", methods=["POST"])
def jw_post():
    jw_nickname_receive = request.form['jw_nickname_give']
    jw_comment_receive = request.form['jw_comment_give']

    doc = {
        'nickname': jw_nickname_receive,
        'comment': jw_comment_receive
    }
    jw_db.tpro1.insert_one(doc)
    return jsonify({'msg': '방명록 감사합니다!'})

@app.route("/kus_jw", methods=["GET"])
def jw_show():
    jw_comment_list = list(jw_db.tpro1.find({}, {'_id': False}))
    return jsonify({'jw_comment_list': jw_comment_list})


#용연
@app.route("/cooseproject", methods=["POST"])
def cooseproject_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name':name_receive,
           'comment':comment_receive}

    eli_db.cooseproject.insert_one(doc)

    return jsonify({'msg':'등록되었습니다 :)'})


@app.route("/cooseproject", methods=["GET"])
def cooseproject_get():
    comment_list = list(eli_db.cooseproject.find({}, {'_id': False}))

    return jsonify({'comment':comment_list})


#성윤
@app.route("/cooseSYJ", methods=["POST"])
def SYJ_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name':name_receive,
           'comment':comment_receive}

    syjdb.syjcomment.insert_one(doc)

    return jsonify({'msg':'메인 페이지 방명록 저장 완료!'})

@app.route("/cooseSYJ", methods=["GET"])
def SYJ_get():
    comment_list = list(syjdb.syjcomment.find({}, {'_id': False}))

    return jsonify({'comment':comment_list, 'msg':'msg'})


#남훈
@app.route("/cus_nhk", methods=["POST"])
def nhk_post():
    nhk_nickname_receive = request.form['nhk_nickname_give']
    nhk_comment_receive = request.form['nhk_comment_give']

    doc = {
        'nickname': nhk_nickname_receive,
        'comment': nhk_comment_receive
    }
    nhkdb.nhk.insert_one(doc)
    return jsonify({'msg': '방명록 감사합니다!'})

@app.route("/cus_nhk", methods=["GET"])
def nhk_show():
    nhk_comment_list = list(nhkdb.nhk.find({}, {'_id': False}))
    return jsonify({'nhk_comment_list': nhk_comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)