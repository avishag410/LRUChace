# LRUChace
changes from inital commit to last version:

- change pydantic model to class
- prev & next save the actual node instead of a copy of the key
- create utils functions: _add_to_end, _move_to_end, _pop_first & reuse them in the put & get functions
- no need to hold a counter, just run len(cache)
- in the function get() - return the item itself (if not exists return None)
- in put() function - handle another edge case - put(key) where key is already exists in the cache

# how to run?
python lrucache.py