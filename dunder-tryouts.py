
print("before import")
m = __import__('math')

print("before function_a")
def function_a():
    print("Function A")

print("before function_b")
def function_b():
    print("Function B {}".format(m.sqrt(100)))

print (__name__)

print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")