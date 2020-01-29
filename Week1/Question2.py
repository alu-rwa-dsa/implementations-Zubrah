#import a memory_profiler module
from memory_profiler import profile


#Using a for loop 
@profile
def my_func():
    a = range(1000)
    b = []
    for i in a:
        b.append(i * 2)
    return b


#using list to illustrate the memory usage
@profile
def my_second():
    a = range(1000)
    b = [i * 2 for i in a]
    return b


if __name__ == '__main__':
    my_func()
    my_second()
