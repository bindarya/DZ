import sys
import ast

def decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        v1, v2  = int(sys.argv[2]),int(sys.argv[1])
        v3 = ast.literal_eval(sys.argv[3])    
        function_to_decorate(v1,v2,v3)
    return the_wrapper_around_the_original_function



@decorator
def swap(x, y, show=False):
    res = x / y 
    if show:
        print(res)
    return 0

swap()
