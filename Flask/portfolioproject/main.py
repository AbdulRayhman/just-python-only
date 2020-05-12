import csv
from flask import render_template, request, url_for, redirect, Blueprint, Flask
from .extensions import mongo

print('portfolioproject.settings')
app = Flask(__name__, template_folder='templates')
app.config.from_object('portfolioproject.settings')
mongo.init_app(app)
# main = Blueprint('main', __name__)
# app.register_blueprint(main)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_pages(page_name: None):
    return render_template(page_name)


def write_data_to_csv(data):
    with open('database.csv', mode='a', newline='') as databaseCsv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(databaseCsv, delimiter=' ',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def write_data_to_database(data):
    try:
        portfolio_collection = mongo.db.contacts
        portfolio_collection.insert({
            'email ': data['email'],
            'subject ': data['subject'],
            'message ': data['message'],
        })
        return redirect('thank-you.html')
    except:
        return redirect('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def form_submit():
    data = request.form.to_dict()
    print(data)
    try:
        return write_data_to_database(data)
    except:
        return redirect('index.html')
