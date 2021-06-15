from flask import Flask, redirect, render_template, url_for, request
import querys as q

app = Flask(__name__)


@app.route('/')
def index():
	print(q.search_by_title('9'))
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
