from bson import ObjectId
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import c3pyo as c3
import os
import matplotlib.pyplot as plt

'''
Per avviare il server di flask:
    FLASK_APP=application_flask.py
    FLASK_ENV=development
    flask run
'''

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://Nunzia:freanat8@pythoncluster.ldlif.mongodb.net/quickstart?authSource=admin&replicaSet=atlas-d5hj2e-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo = PyMongo(app)

db_operations = mongo.db.book
#chart = c3.PieChart()

@app.route("/")
def main():
    #senza 'list' avrei un elemento di classe 'pymongo.cursor.Cursor'
    books = list(db_operations.find())
    return render_template('index.html', books=books)

@app.route('/search.html', methods=['POST'])
def search():
    tag_name = request.form.get('tag_name')
    books = list(db_operations.find({'name': tag_name}))
    #books = db_operations.archive.find()
    #output = [{'book_id':book['book_id'], 'name':book['name'], 'author':book['author']} for book in books]
    #return jsonify(output)
    return render_template('search.html', books=books)

@app.route("/graphic.html")
def graphic():
    books = list(db_operations.find())
    num_books = len(books)
    '''
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.bar(1, num_books, label='#books')
    plt.bar(2, num_books, label='#books')
    plt.title('Graphic')
    plt.xlabel('book')
    plt.ylabel('#books')
    plt.legend()
    plt.savefig(os.path.join('images/exGraph.png'), dpi=200)
    '''
    #graphs = chart.plot(num_books, label='Books')
    #chart.show()
    return render_template('graphic.html')

if __name__ == '__main__':
    app.run(debug=True)