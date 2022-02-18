import unittest
from online_count import count_online

class TestOnlineCount(unittest.TestCase):

    def test_count_online(self):
        
        people_status = {
            "Alice": "online",
            "Bob": "offline",
            "Eve": "online"
        }

        self.assertEqual(count_online(people_status), 2)