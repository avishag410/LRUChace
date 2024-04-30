
class chainItem(BaseModel):
    # key object: int
    next: int 
    prev: int

chain = {
}

last_item = None
first_item = None
MAX = 3
counter = 0

def _is_max():
    counter == MAX

def put(object: int):
        
    # enter a new object
    chain[object] = {
        prev: last_item if last_item else None  
        next: None
    }

    last_item = object
    counter += 1

    if first_item is None:
        first_item = object

    if _is_max():
        next_first_item = chain[first_item].next
        chain[first_item].pop()
        
        first_item = next_first_item

def get(object: int): 
    # init
    prev_item = chain[object].prev
    next_item = chain[object].next

    # handle prev and next items
    chain[prev_item].next = next_item
    chain[next_item].prev = prev_item

    # insert object to the end of the chain
    chain[object].prev = last_item
    chain[last_item].next = object
    chain[object].next = None

    last_item = object
    if object == first_item:
        first_item = next_item

