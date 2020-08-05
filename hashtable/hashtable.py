class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}, {self.value}"

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.store)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        loadFactor = self.count / self.get_num_slots()
        return loadFactor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # FNV_offset_basis = 1469598103934665037
        # FNV_prime = 1099511628211

        # hashed_var = FNV_offset_basis

        # string_bytes = key.encode()

        # for b in string_bytes:
        #     hashed_var = hashed_var * FNV_prime
        #     hashed_var = hashed_var ^ b
        
        # return hashed_var


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # create the node
        # entry = HashTableEntry(key, value)
        # hash the kex for the hash table index
        idx = self.hash_index(key)
        # current = self.store[idx]

        # new code to prevent collisions
        if self.store[idx] is None:
            # print("is there a val?", self.store)
            # check at the index to see if it is None
            # if yes --> insert the node with the key - value pair
            self.store[idx] = HashTableEntry(key, value)
            # print("put method new", self.store)
            self.count+=1
            return
        curr = self.store[idx] 
        self.store[idx] = HashTableEntry(key, value)
        self.store[idx].next = curr
        self.count+=1

        # Your code here
        """ Day 1 code - no collisions - naive hash table"""
        # index = self.hash_index(key)
        # self.store[index] = value
        # self.count+=1
        # return self.store[index]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        prev = None
        curr = self.store[idx]

        if curr is not None:
            while curr.key != key and curr is not None:
                prev = curr
                curr = curr.next
            if curr.key == key:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.store[idx] = curr.next
            else:
                print(f'Not found')
        else:
            print(f'Not found')
        self.get_load_factor()

        # idx = self.hash_index(key)

        # if self.store[idx] is None:
        #     return None
        
        # elif self.store[idx].next is None:
        #     deletedVal = self.store[idx].value
        #     self.store[idx] = None
        #     self.count-=1
        #     return deletedVal
        
        # else:
        #     node = self.store[idx]
        #     prev = None

        #     while node.key != key and node.next is not None:
        #         prev = node
        #         node = node.next

        #     if node.key == key:
        #         prev.next = node.next
        #         deletedVal = node.value
        #         node = None
        #         self.count-=1
        #         return deletedVal
        #     else:
        #         return None

        # Your code here
        # idx = self.hash_index(key)
        
        # if self.store[idx] is None:
        #     snapshot = self.store[idx]

        #     while snapshot is not None:
        #         if snapshot.key == key:
        #             self.store[idx] = snapshot.next
        #             snapshot.next = None
        #             self.count-=1
        #             return snapshot.value
        #         else:
        #             snapshot = snapshot.next
        #     print(f"Nothing found at key: {key}")
        # else:
        #     print(f"Nothing found at key: {key}")

        
        """ Day 1 - no collisions - naive hash table """
        # self.store[self.hash_index(key)] = None
        # self.count-=1
        # return self.store


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # print(f"get method", self.store)
        idx = self.hash_index(key)
        hash_entry = self.store[idx]

        while hash_entry is not None:
            # check to see if the values match
            if hash_entry.key == key:
                return hash_entry.value
            hash_entry = hash_entry.next
        return None


        """ Day 1 code - no collisions - naive hash table"""
        # value = self.store[self.hash_index(key)]

        # if value is None:
        #     return None
        # else:
        #     return value.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:
            if new_capacity < self.capacity * 2:
                new_capacity = self.capacity * 2
            
            new_store = [None] * new_capacity
            old_store = self.store

            self.capacity = new_capacity
            self.store = new_store

            for element in old_store:
                if element is not None:
                    node = element
                    while node is not None:
                        self.put(node.key, node.value)
                        node = node.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

# value = "test"
# hashed_value = HashTable(value)
# print(hashed_value)
# print(hashed_value.dbj2())