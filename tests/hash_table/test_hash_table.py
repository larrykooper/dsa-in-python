from src.hash_table.hash_table import HashTable

class TestHashTable:

    def test_insert_no_collision(self):
        h = HashTable()
        h.insert(20)
        hash = h.h(20)
        assert h.slot_cardinality(hash) == 1

    def test_insert_yes_collision(self):
        h = HashTable()
        h.insert(10)
        h.insert(33)
        hash = h.h(10)
        assert h.slot_cardinality(hash) == 2

    def test_search_when_not_found(self):
        h = HashTable()
        h.insert(33)
        res = h.search(15)
        assert res == None

    def test_search_when_found_with_chaining(self):
        h = HashTable()
        h.insert(10)
        h.insert(33)
        res = h.search(33)
        assert res == 33

    def test_delete_where_found(self):
        h = HashTable()
        h.insert(10)
        h.insert(33)
        h.insert(56)
        res = h.delete(33)
        assert res == 33
