from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
junclient = MongoClient('mongodb+srv://sparta:test@cluster0.u8xq40k.mongodb.net/Cluster0?retryWrites=true&w=majority')
jundb = junclient.dbsparta

syjclient = MongoClient('mongodb+srv://test:sparta@cluster0.lot5yin.mongodb.net/Cluster0?retryWrites=true&w=majority')
syjdb = syjclient.dbsparta

@app.route('/')  #팀페이지
def home():
    return render_template('index.html')

@app.route('/jun-page')   #성준 개인페이지
def jun_page():
    return render_template('jun-page.html')

@app.route('/SYJ') #성윤 개인페이지
def SYJ():
    return render_template('SYJ.html')

@app.route("/coosemain", methods=["POST"])
def coose_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name':name_receive,
           'comment':comment_receive}

    jundb.coosemain.insert_one(doc)

    return jsonify({'msg':'메인 페이지 방명록 저장 완료!'})


@app.route("/coosemain", methods=["GET"])
def coose_get():
    comment_list = list(jundb.coosemain.find({}, {'_id': False}))

    return jsonify({'comment':comment_list})


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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)