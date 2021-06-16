from sqlite3 import DatabaseError
from flask import logging
import connection_pool as cp


# searching query

def find_all():
	try:
		con = cp.connection_pool()
		results = list(con.find())
		return results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)

def search_by_title(title):
	try:
		con = cp.connection_pool()
		results = list(con.find({'title': title}))
		return results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)

def search_by_type(type):
	try:
		con = cp.connection_pool()
		results = con.find({'type': type})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def search_by_release_year(year):
	try:
		con = cp.connection_pool()
		results = con.find({'release_year': year})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def search_by_rating(rating):
	try:
		con = cp.connection_pool()
		results = con.find({'rating': rating})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def search_by_duration(duration):
	try:
		con = cp.connection_pool()
		results = con.find({'duration': duration})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def search_by_title_type(title, type):
	try:
		con = cp.connection_pool()
		results = con.find({'$and':[{'Title': title}, {'Type': type}]})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def search_by_type_duraton(type, duration):
	try:
		con = cp.connection_pool()
		results = con.find({'$and':[{'type': type}, {'duration': duration}]})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

# counting query

def count_by_genre(genre):
	try:
		con = cp.connection_pool()
		results = len(list(con.find({'listed_in': genre})))
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_duration(duration):
	try:
		con = cp.connection_pool()
		results = len(list(con.find({'duration': duration})))
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_type():
	results = []
	try:
		con = cp.connection_pool()
		results_movie = len(list(con.find({'type': 'Movie'})))
		#counters['Movie'] = results
		results_show = len(list(con.find({'type': 'TV Show'})))
		#counters['TV Show'] = results
		results = [results_movie, results_show]
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_rating():
	counters = {}
	try:
		con = cp.connection_pool()
		results = len(list(con.find({'rating': 'TV-MA'})))
		counters['TV-MA'] = results
		results = len(list(con.find({'rating': 'TV-14'})))
		counters['TV-14'] = results
		results = len(list(con.find({'rating': 'TV-PG'})))
		counters['TV-PG'] = results
		results = len(list(con.find({'rating': 'R'})))
		counters['R'] = results
		results = len(list(con.find({'rating': 'PG-13'})))
		counters['PG-13'] = results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return counters

def count_by_covid_year():
	try:
		con = cp.connection_pool()
		results_2020 = len(list(con.find({'release_year': '2020'})))
		results_2019 = len(list(con.find({'release_year': '2019'})))
		counters = [results_2020, results_2019]
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return counters
