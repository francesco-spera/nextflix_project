from flask import Flask, redirect, render_template, url_for, request
import connection_pool as cp
import querys as q

app = cp.app


@app.route('/')
def index():
	print(q.search_by_title('9'))
	return render_template('index.html')

@app.route('/search.html', methods=['POST'])
def search():
	tag_name = request.form.get('tag_name')
	info = q.search_by_title(tag_name)
	return render_template('search.html', info=info)


if __name__ == '__main__':
	app.run(debug=True)
