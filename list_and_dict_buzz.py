def fizzbuzz(max_num):
    fizzbuzz = {
    "one"   : "FizzBuzz",
    "two"   : "Fizz",
    "three" : "Buzz",
    "four"  : "Other"
}
    """Loops through 1-max_num and prints message depending on evaluation of integer."""
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            print fizzbuzz["one"]
        elif num % 3 == 0:
            print fizzbuzz["two"]
        elif num % 5 == 0:
            print fizzbuzz["three"]
        else:
            print fizzbuzz["four"]
fizzbuzz(20)