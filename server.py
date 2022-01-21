from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

def write_to(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt','a') as db:
        file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(db2,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./ThankYou.html')
    else:
        return 'try again'
