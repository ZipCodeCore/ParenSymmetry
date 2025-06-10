class ParenSymmetry:
    
    def is_balanced(self, s):
        return None
    
    def _check_file(self, filename):
        # open file named filename
        
        # for each line in the file
            # read the line
            # print whether or not the line's parenthesis are balanced
        
        # CLOSE the file
        pass


def main():
    ps = ParenSymmetry()
    
    b0 = ps.is_balanced("()")
    print_result(b0, True)
    
    false_strings = ["(", "((", ")", "", "(()())((()))"]
    falses = True
    for str_to_test in false_strings:
        falses = ps.is_balanced(str_to_test)
    print_result(falses, False)
    
    true_strings = ["()", "(())", "(((())))", "", "(()())((()))", "(   )", "( () ( ) )"]
    trues = False
    for str_to_test in true_strings:
        trues = ps.is_balanced(str_to_test)
    print_result(trues, True)


def print_result(b0, b):
    if b0 is None:
        print("Null Failure")
        return
    if b0 == b:
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()