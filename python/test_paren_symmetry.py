import unittest
from paren_symmetry import ParenSymmetry


class TestParenSymmetry(unittest.TestCase):
    
    def test_is_balanced1(self):
        input_test = "()"
        expected = True
        
        actual = ParenSymmetry().is_balanced(input_test)
        self.assertEqual(expected, actual)
    
    def test_is_balanced2(self):
        input_test = "())"
        expected = False
        
        actual = ParenSymmetry().is_balanced(input_test)
        self.assertEqual(expected, actual)
    
    def test_is_balanced3(self):
        input_test = "(("
        expected = False
        
        actual = ParenSymmetry().is_balanced(input_test)
        self.assertEqual(expected, actual)
    
    def test_is_balanced4(self):
        input_test = "()grand()illusion"
        expected = True
        
        actual = ParenSymmetry().is_balanced(input_test)
        self.assertEqual(expected, actual)
    
    def test_is_balanced_falses(self):
        false_strings = ["(", "((", ")", "(()())((()))"]
        expected = False
        
        for test_string in false_strings:
            actual = ParenSymmetry().is_balanced(test_string)
            self.assertEqual(expected, actual)
    
    def test_is_balanced_trues(self):
        true_strings = ["()", "(())", "(((())))", "", "(()())((()))", "(   )", "( () ( ) )"]
        expected = True
        
        for test_string in true_strings:
            actual = ParenSymmetry().is_balanced(test_string)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()