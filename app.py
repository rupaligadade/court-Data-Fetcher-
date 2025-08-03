from flask import Flask, render_template, request, redirect
from scraper import scrape_case_data
from models import db, QueryLog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///court_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    try:
        result = scrape_case_data(case_type, case_number, filing_year)

        log = QueryLog(case_type=case_type, case_number=case_number,
                       filing_year=filing_year, raw_response=str(result))
        db.session.add(log)
        db.session.commit()

        return render_template('result.html', result=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)