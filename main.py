# Write a function (or just code without a function around it) that will print into the console integer numbers from 1 to 100.
# In addition an algorithm should print in the same row as number specific word (or words) i.e.:
#a)For each number divisible by three it should print “number-that-is-divisible-by-three” and “Fizz” word (e.g: “3 – Fizz”)
#b)For each number divisible by five it should print “number-that-is-divisible-by-five” and “Buzz” word (e.g.: “5 – Buzz”)
# c)If a number is divisible by both three and five it should print “FizzBuzz” word (e.g.: “15 – FizzBuzz”)

print(range(100))

def print_all_numbers_until(last_number: int):
    for el in range(last_number):
        if el%3==0 and el%5==0:
            print('FizzBuzz',)
        elif el%3==0:
            print('Fizz')
        elif el%5==0:
            print("Buzz")
        else:
            print(str(el))
print_all_numbers_until(100)
