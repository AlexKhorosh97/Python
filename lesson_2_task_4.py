class Example(object):
 def FizzBuzz( self, n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 5 == 0 and i % 3 == 0:
            result.append('FizzBuzz')
        else:
            result.append(str(i))
    return result
object1 = Example() 
print(object1.FizzBuzz(60)) 