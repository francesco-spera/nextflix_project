from flask import render_template, request
import connection_pool as cp
import querys as q

app = cp.app

colors = [
    "#E74C3C", "#F1C40F", "#7FB3D5", "#C0392B",
    "#ABCDEF", "#F5B041", "#52BE80", "#AAB7B8"]

@app.route('/')
def index():
	titles = q.find_all()
	return render_template('index.html', titles=titles)

@app.route('/search.html', methods=['POST'])
def search():
	tag_name = request.form.get('tag_name')
	info = q.search_by_title(tag_name)
	return render_template('search.html', info=info)

@app.route("/search_advanced.html")
def search_advanced():
    	return render_template('search_advanced.html')

@app.route("/search_advanced.html", methods=['POST'])
def search_advanced_2():
    	tag_show = request.form.get('show')
    	tag_time = request.form.get('time')
    	titles = list(q.search_by_type_duraton(tag_show, tag_time))
    	return render_template('search_advanced.html', titles=titles)

@app.route("/graphic_type.html")
def graphic_type():
	labels = ['Movie', 'TV Show']
	values = q.count_by_type()
	return render_template('graphic_type.html', set=zip(values, labels, colors))


if __name__ == '__main__':
	app.run(debug=True)

