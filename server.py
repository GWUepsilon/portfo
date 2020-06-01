from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

print(__name__)

@app.route('/')
def index_page():
	return render_template('index.html')


@app.route('/test/<username>/<int:post_id>')
def name_claim(username = None, post_id = None):
	return render_template('index.html', name = username, post_id = post_id)


@app.route('/<string:page_name>')
def dynamic_page(page_name):
	return render_template(page_name)

#writting to database
def write_to_csv(data):
	with open('database.csv', newline = '', mode = 'a',) as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writter = csv.writer(database2, delimiter = ',', quotechar=':', quoting = csv.QUOTE_MINIMAL)
		csv_writter.writerow([email, subject, message])

@app.route('/submitted_form', methods=['POST','GET'])
def submit_form():
	if request.method=='POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thanks.html')
		except:
			return 'data didn not save to database'
	else: 
		return 'Something wrong'