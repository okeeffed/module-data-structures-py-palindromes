import unittest
import palindromes


class HelloWorldTest(unittest.TestCase):
    def test_palindromes(self):
        assess = [{
            "input": "noon",
            "expectation": True
        }, {
            "input": "racecar",
            "expectation": True
        }, {
            "input": "Testing",
            "expectation": False
        }, {
            "input": "Racecar",
            "expectation": True
        }, {
            "input": "Car2rac",
            "expectation": True
        }
        ]
        for test in assess:
            self.assertEqual(palindromes.isPalindrome(
                test["input"]), test["expectation"])

    def test_handles_space(self):
        assess = [{
            "input": "racecar   ",
            "expectation": True
        }, {
            "input": "ra ce   car   ",
            "expectation": True
        }]
        for test in assess:
            self.assertEqual(palindromes.isPalindrome(
                test["input"]), test["expectation"])

    def test_handles_chars(self):
        assess = [{
            "input": "racecar  ! ! ",
            "expectation": True
        }, {
            "input": "!ra ce.   car   ",
            "expectation": True
        }, {
            "input": "!ra ctte.   car   ",
            "expectation": False
        }]
        for test in assess:
            self.assertEqual(palindromes.isPalindrome(
                test["input"]), test["expectation"])


if __name__ == '__main__':
    unittest.main()
