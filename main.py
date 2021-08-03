from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message 

from CsuModel import CsuModel
from CsuData import CsuData
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "prathima.tangirala@gmail.com"
app.config['MAIL_PASSWORD'] = "amithareddy"
mail = Mail(app)


@app.route('/chatbot/data', methods=['POST','OPTIONS'])
def predictionDataApi():
    if request.method == 'GET':
        return jsonify({
    "test": "test",
})
    elif request.method == 'POST':
        question = request.get_json(force=True)
        print(question)
        modelresponse = csuModel.chatBotAPI(question['query'])
        print(modelresponse)
        kwargs = {
            'query': question['query'],
            'answer': modelresponse,
        }
        resp = jsonify(kwargs)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp 

    elif request.method == 'OPTIONS':
        resp = jsonify({})
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp     



@app.route('/chatbot/send-message', methods=['POST','OPTIONS'])
def sendEmailMessage():
    if request.method == 'POST':
        emailRequest = request.get_json(force=True)
        print(emailRequest)
        name = emailRequest['name']
        subject = emailRequest['subject']
        msg = emailRequest['msg']
        sender = emailRequest['sender']
        date = emailRequest['date']
        time = emailRequest['time']
        message = Message(subject, sender = sender, recipients= ['prathima.tangirala@gmail.com'])
        message.body = msg
        print(message)
        mail.send(message)
        resp = jsonify({"message":"success"})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp 

    elif request.method == 'OPTIONS':
        resp = jsonify({})
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp     

@app.route('/chatbot/submit-billing-data-request', methods=['POST','OPTIONS'])
def sendBillingDataRequest():
    if request.method == 'POST':
        dataRequest = request.get_json(force=True)
        print(dataRequest)
        csuId = dataRequest['csuId']
        optionType = dataRequest['optionType']
        if optionType == 'accountbalance':
            response = csuData.show_account_balance(csuId)
            kwargs = {
                'balance': response
            }
        elif optionType == 'payment':
            payment_method, payment_amount = csuData.show_payments_table(csuId)
            kwargs = {
                'paymentMethod': payment_method,
                'paymentAmount': payment_amount
            }
        resp = jsonify(kwargs)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp 

    elif request.method == 'OPTIONS':
        resp = jsonify({})
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp   

@app.route('/chatbot/submit-course-data-request', methods=['POST','OPTIONS'])
def sendCourseDataRequest():
    if request.method == 'POST':
        dataRequest = request.get_json(force=True)
        print(dataRequest)
        csuId = dataRequest['csuId']
        semester = dataRequest['semester']
        optionType = dataRequest['optionType']
        if optionType == 'registered_courses':
            response = csuData.show_registered_courses(csuId,semester)
        elif optionType == 'course_schedule':
            response = csuData.show_course_schedules(semester) 
        elif optionType == 'transcripts':
            response = csuData.show_latest_transcripts(csuId,semester)        
        resp = jsonify(response)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp 
    elif request.method == 'OPTIONS':
        resp = jsonify({})
        print(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST, PUT, GET, OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        return resp                    


if __name__ == '__main__':
    csuModel = CsuModel()
    csuData  = CsuData()
    content = open("./input_file/model.txt", 'r', encoding='utf-8')
    paragraph = " ".join(content.read().splitlines())
    app.run(host="0.0.0.0", port=8000)
