from sqlite3 import DatabaseError
from flask import logging
import connection_pool as cp


def find_all():
	try:
		con = cp.connection_pool()
		results = list(con.find())
		return results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
		
# searching query

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

def search_by_type_genre(type, genre):
	try:
		con = cp.connection_pool()
		results = con.find({'$and':[{'type': type}, {'listed_in': genre}]})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

# counting query

def count_by_genre(genre):
	try:
		con = cp.connection_pool()
		results = con.count({'listed_in': genre})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_duration(duration):
	try:
		con = cp.connection_pool()
		results = con.count({'duration': duration})
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_type():
	counters = {}
	try:
		con = cp.connection_pool()
		results = con.count({'type': 'Movie'})
		counters['Movie'] = results
		results = con.count({'type': 'TV Show'})
		counters['TV Show'] = results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results

def count_by_rating():
	counters = {}
	try:
		con = cp.connection_pool()
		results = con.count({'rating': 'TV-MA'})
		counters['TV-MA'] = results
		results = con.count({'rating': 'TV-14'})
		counters['TV-14'] = results
		results = con.count({'rating': 'TV-PG'})
		counters['TV-PG'] = results
		results = con.count({'rating': 'R'})
		counters['R'] = results
		results = con.count({'rating': 'PG-13'})
		counters['PG-13'] = results
	except DatabaseError as e:
		logging.warning('DB exception: %s' % e)
	return results
