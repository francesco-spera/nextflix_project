from flask import Flask, render_template, request
import connection_pool as cp
import querys as q

app = Flask(__name__)

colors = [
    "#E74C3C", "#F1C40F", "#7FB3D5", "#C0392B",
    "#ABCDEF", "#F5B041", "#52BE80", "#AAB7B8"]

@app.route('/')
def index():
	titles = q.find_all()
	return render_template('index.html', titles=titles)

@app.route('/search', methods=['POST'])
def search():
	tag_name = request.form.get('tag_name')
	info = q.search_by_title(tag_name)
	return render_template('search.html', info=info)

@app.route("/search_advanced")
def search_advanced():
    	return render_template('search_advanced.html')

@app.route("/search_advanced", methods=['POST'])
def search_advanced_2():
    	tag_show = request.form.get('show')
    	tag_time = request.form.get('time')
    	titles = list(q.search_by_type_duraton(tag_show, tag_time))
    	return render_template('search_advanced.html', titles=titles)

@app.route("/graphic_type")
def graphic_type():
	labels = ['Movie', 'TV Show']
	values = q.count_by_type()
	return render_template('graphic_type.html', set=zip(values, labels, colors))

@app.route("/graphic_rating")
def graphic_rating():
	labels = ['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13']
	values = q.count_by_rating()
	return render_template('graphic_rating.html', set=zip(values, labels, colors))

@app.route("/graphic_covid_year")
def graphic_year():
	labels = ['2020', '2019']
	values = q.count_by_covid_year()
	return render_template('graphic_covid_year.html', set=zip(values, labels, colors))


if __name__ == '__main__':
	app.run(debug=True)

