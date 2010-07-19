
# Constants for isbndbpy

APIKEY = ''

APIBASE = "http://isbndb.com/"

API = {
	'books': {
		'request': ['isbn', 'title', 'combined', 'full', 'book_id', 'person_id', 'publisher_id'
					'subject_id', 'dewey_decimal', 'lcc_number'],
		'results': ['details', 'texts', 'prices', 'pricehistory', 'subjects', 'marc', 'authors', ]
	}, 
	'subjects': {
		'request': ['name', 'category_id', 'subject_id'],
		'results': ['categories', 'structure']
	}, 
	'categories': {
		'request': ['name', 'category_id', 'parent_id'],
		'results': ['details', 'subcategories']
	}, 
	'authors': {
		'request': ['name', 'person_id'],
		'results': ['details', 'categories', 'subjects']
	}, 
	'publishers': {
		'request': ['name', 'publisher_id'],
		'results': ['details', 'categories']
	}
}


