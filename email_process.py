from flask import Flask, request, jsonify
import email
import json


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      emailText=request.form['em']
      email_msg = email.message_from_string(emailText)
      email_data = {
         "To": email_msg['To'],
         "From": email_msg['From'],
         "Date": email_msg['date'],
         "Subject": email_msg['date'],
         "Message-ID":email_msg['Message-ID']
      }
      return jsonify(json.dumps(email_data, indent = 4))


   return '''
       <form method = "post">
         <p>Enter Text:</p>
         <p> <textarea id="em" name="em" style="width:100%; height: 70px;" maxlength="30000"></textarea> </p>
         <p><input type = "submit" value = "submit" /></p>
       </form>
   '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
