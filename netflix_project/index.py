from flask import Flask, redirect, render_template, url_for, request
import querys as q

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
	tag_name = request.form.get('tag_name')
	info = q.search_by_title(tag_name)
	return render_template('search.html', info=info)

@app.route('/graphic_type', methods=['POST', 'GET'])
def stats_view_type():
	labels = ['MOVIE', 'TV SHOW']
	values = list(q.count_by_type())
	colors = ['#FFFF00', '#FFA500']
	return render_template('graphic_type.html', set=zip(values, labels, colors))

@app.route('/graphic_genre', methods=['POST', 'GET'])
def stats_view_genre():
	return render_template('graphic_genre.html')

@app.route('/graphic_rating', methods=['POST', 'GET'])
def stats_view_rating():
	return render_template('graphic_rating.html')


if __name__ == '__main__':
	app.run(debug=True)
