def best_occupacy(age):

    if age in range(1,6):
        return("Stay at home and sleep")
    elif age in range(6,15):
        return("Go to school")
    elif age in range(16,22):
        return("Study at Alma mater, enjoy your life!")
    elif age in range(23,99):
        return("It's time to work till your deaf!")

if __name__ == "__main__":
    try: 
        age = int(input("Print your age \n"))
        my_occupacy = best_occupacy(age)
        print(my_occupacy)   
    except ValueError:
        print("It's not a number!")
    
    