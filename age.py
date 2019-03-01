
age = int(input("Print your age \n"))
def best_occupacy(age):
    if age < 6:
        return("Stay at home and sleep")
    elif age <= 16:
        return("Go to school")
    elif age <= 23:
        return("Study at Alma mater, enjoy your life!")
    elif age > 23:
        return("It's time to work till your deaf!")

my_occupacy = best_occupacy(age)
print(my_occupacy)