from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   adopt = list(db.adopt_dog.find({}, {'_id': False}))
   return jsonify({'inform_adopt': adopt})

@app.route('/test', methods=['POST'])
def test_post():
   name_receive = request.form['name_give']
   url_receive = request.form['url_give']
   species_receive = request.form['species_give']
   phone_receive = request.form['phone_give']

   doc = {
      'name': name_receive,
      'url': url_receive,
      'species': species_receive,
      'phone': phone_receive
   }

   db.adopt_dog.insert_one(doc)

   return jsonify({'result':'success', 'msg': '신청이 완료되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)