name = input("What is your name?: ") 

age = input("What is your age?: ") 

city = input("What city do you live in?: ")

love = input("What do you love doing?: ")

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

print(output)
