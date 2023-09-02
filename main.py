def my_name() :
    print("my name is abdulaziz")
my_name()
def my_meal(food , drink) :
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("pizza","fanta")

def cube(number) :
    return number**3

def by_three(number):
    if number % 3 ==0 :
        return cube(number)
    else :
        return "false"
final_number = by_three(int(input("enter your number :")))
print(final_number)
