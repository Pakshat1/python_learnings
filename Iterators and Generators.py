
# iteratoers are objects that can be iterated upon, meaning that you can traverse through all the values.
# An iterator is an object which implements the iterator protocol, consisting of the methods __iter__ and __next__. 
# An iterator is initialized using the iter() method, which returns an iterator object.
# A generator is a special type of iterator that is defined using a function and the yield statement.
# Generators are a simple way of creating iterators using functions.
# Example of an iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
# Example of using the iterator
my_data = [1, 2, 3, 4, 5]   
my_iterator = MyIterator(my_data)
for item in my_iterator:
    print(item)
# Output: 1 2 3 4 5 

# Example of a generator
def my_generator(data):
    for item in data:
        yield item
# output: 1 2 3 4 5

# Example of using the generator
my_data = [1, 2, 3, 4, 5]
for item in my_generator(my_data):
    print(item)
# Output: 1 2 3 4 5

# Example of a generator expression
my_data = [1, 2, 3, 4, 5]
my_generator_expr = (item for item in my_data)
for item in my_generator_expr:
    print(item)
# Output: 1 2 3 4 5

# Example of a generator with a condition
def my_conditional_generator(data):
    for item in data:
        if item % 2 == 0:  # Only yield even numbers
            yield item
# output: 2 4 

# Example of using the conditional generator
my_data = [1, 2, 3, 4, 5]
for item in my_conditional_generator(my_data):
    print(item)
# output: 2 4





    
        