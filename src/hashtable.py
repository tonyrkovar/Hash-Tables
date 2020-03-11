# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        new_link = LinkedPair(key, value)
        index = self._hash_mod(key)

        current_LI = self.storage[index]

        if self.storage[index] == None:
            self.storage[index] = new_link
        else:
            if current_LI.key == key:
                current_LI.value = value
            else:
                while current_LI.next is not None:
                    current_LI = current_LI.next
                    if current_LI.key == key:
                        current_LI.value = value
                current_LI.next = new_link

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]

        if current_node is None:
            print('ITEM NOT FOUND')

        elif current_node.key == key and current_node.next is None:
            print('yo')
            self.storage[index] = None
            return

        elif current_node.key == key and current_node.next is not None:
            print(self.storage[index].key, "THEY MATCH!, setting to None")
            self.storage[index] = None
            return

        elif current_node.key != key and current_node.next is not None:
            prev = current_node
            current = current_node.next
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    current = None
                    return
                prev = current
                current = current.next
            print('ITEM NOT FOUND')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Hashes the key in order to compare input to storage
        index = self._hash_mod(key)
        # Creates a variable storing the node returned from the key.
        current_node = self.storage[index]

        # Checks if the returned node is empty
        if current_node == None:
            return current_node
        # Checks the variable to see if the keys match, if they do return value
        elif current_node.key == key:
            return current_node.value
        # If the keys don't match and the node isn't empty we iterate through the linked list at index
        else:
            while current_node.next:
                # If there is a next value, set current_node to it and run the key check again
                current_node = current_node.next
                # If the key at current matches, return value
                if current_node.key == key:
                    return current_node.value
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        for item in old_storage:
            if item == None:
                pass
            elif item.next:
                self.insert(item.key, item.value)
                current_node = item
                while current_node.next is not None:
                    current_node = current_node.next
                    self.insert(current_node.key, current_node.value)
            else:
                self.insert(item.key, item.value)


if __name__ == "__main__":
    ht = HashTable(2)
    # print(dir(ht))
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
