def hash_string(keyword, buckets):
    sum1 = 0
    for letter in keyword:
        sum1 += ord(letter)    
    return sum1 % buckets

def test_hash_function(func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w, size)
			resutls[hv] += 1
			keys_used.append(w)
	return results
 
def make_hashtable(nbuckets):
	hashtable = []
	for i in range(0,nbuckets-1):
		hashtable.append([])
	return hashtable

def hashtable_get_bucket(htable, keyword):
    return htable[ hash_string(keyword, len(htable)) ]

def hashtable_add(htable, key, value):
	hashtable_get_bucket[htable, key].append([key, value])

def hashtable_lookup(htable, key):
	bucket = hashtable_get_bucket(htable,key)
	for entry in bucket:
		if entry[0] == key:
			return entry[1]
		return None
		
def hashtable_update(htable,key,value):
	existing_value = hashtable_lookup(htable, key)
	if existing_value and existing_value != value:
		bucket = hashtable_get_bucket(htable, key)
		for entry in bucket:
			if entry[0] == key:
				entry[1] = value
			else:
				hashtable_add(htable, key, value)
			return htable