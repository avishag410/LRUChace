class Item:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

# Initialize variables
cache = {}
first_item = None  # Least recently used item (LRU)
last_item = None   # Most recently used item (MRU)
MAX_SIZE = 3

def _add_to_end(item):
    """Add new item to the end (most recently used)"""
    global first_item, last_item
    # initialize the item
    item.next = None
    item.prev = last_item

    # update last_item pointer
    if last_item:
        last_item.next = item
    last_item = item

    # if it's the first item in the cache
    if first_item is None:
        first_item = item

def _remove_item(item):
    """Remove an item from the linked list"""
    global first_item, last_item
    if item.prev:
        item.prev.next = item.next
    
    ## if item is the first in the cache (has no prev) 
    else:
        first_item = item.next
    if item.next:
        item.next.prev = item.prev

    ## if item is the last in the cache (has no next) 
    else:
        last_item = item.prev

def _move_to_end(item):
    """Move certain item to the end (most recently used)"""
    if item == last_item:
        return
    _remove_item(item)
    _add_to_end(item)

def _pop_first():
    """Pop the least recently used item from the beginning"""
    global first_item, cache
    if first_item:
        popped_item = first_item
        _remove_item(first_item)
        del cache[popped_item.key]
        return popped_item

def put(key):
    global cache, MAX_SIZE
    item = cache.get(key, None)
    if not item:
        new_item = Item(key=key)
        cache[key] = new_item
        _add_to_end(new_item)
        # if reached the maximun capacity of the cache
        if len(cache) > MAX_SIZE:
            _pop_first()
    else:
        _move_to_end(item)

def get(key):
    item = cache.get(key, None)
    if item:
        _move_to_end(item)
    return item

# Example usage
put(1)
put(2)
put(3)
print(get(2).key)  # Accessing 2, should now be the most recently used
put(4)             # 1 should be evicted here because it's the least recently used
print(get(1))      # Trying to access 1, should return None
