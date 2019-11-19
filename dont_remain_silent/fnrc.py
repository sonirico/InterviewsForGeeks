import unittest


class QNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class UniqueCharStore:
    def __init__(self):
        self.store = {}
        self.head = None
        self.end = None

    def insert_tail(self, node):
        if self.head is None or self.end is None:
            self.head = node
            self.end = node
            return
        self.end.next = node
        node.prev = self.end
        self.end = node

    def remove_node(self, node):
        if self.head is node and self.end is node:
            # One node, being both head and end
            self.head = None
            self.end = None
            return
        if node.prev and node.next:
            # In the middle node (three or more nodes)
            node.prev.next = node.next
            node.next.prev = node.prev
            return
        if node.prev is None:
            # 2 nodes, being target the head
            node.next = None
            self.end.prev = None
            self.head = self.end
        if node.next is None:
            # 2 nodes, being target the end
            node.prev = None
            self.head.next = None
            self.end = self.head

    def set(self, char):
        if char in self.store:
            node = self.store[char]
            if node:
                self.remove_node(node)
            # Leave the char marked as seen
            self.store[char] = None
            return False
        else:
            node = QNode(char)
            self.store[char] = node
            self.insert_tail(node)
            return True

    @property
    def first_value(self):
        if self.head:
            return self.head.value
        return None


def fnrc(payload):
    store = UniqueCharStore()
    for char in payload:
        store.set(char)
    return store.first_value


class FirstNonRepeatingLetterTestCase(unittest.TestCase):
    def test_always_the_same_character(self):
        payload = "ZZZZZZZZZZZZZZZZZZZZZ"
        expected = None
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_target_is_in_last_position(self):
        payload = "ZZZZZZZZZZZZZZZZZZZZZX"
        expected = "X"
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_target_is_in_first_position(self):
        payload = "XZZZZZZZZZZZZZZZZZZZZ"
        expected = "X"
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_character_all_characters_bouncing_none(self):
        payload = "ZXZXZXZXZXZXZXZXZX"
        expected = None
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_character_bouncing_ok(self):
        payload = "ZZZZZZZZZZZZZAZZZZZZZ"
        expected = "A"
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_sequence_characters_are_repeated(self):
        payload = "ABCABCABC"	
        expected = None
        import ipdb

        ipdb.set_trace()
        actual = fnrc(payload)
        self.assertEqual(expected, actual)

    def test_any_char_is_repeated(self):
        payload = "1234567890"
        expected = "1"
        actual = fnrc(payload)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
