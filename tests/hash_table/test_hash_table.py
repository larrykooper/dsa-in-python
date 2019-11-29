from hash_table import HashTable

class TestHashTable:

    def test_insert_no_collision(self):
        h = HashTable()
        h.insert(20)
        hash = h.h(20)
        assert h.slot_cardinality(hash) == 1