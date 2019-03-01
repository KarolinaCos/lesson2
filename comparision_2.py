def two_str(one, two):
    if not isinstance(one, str) and not isinstance(two, str):
        print(0)
    elif one == two:
        print(1)
    elif one != two:
        if len(str(one)) > len(str(two)):
            print(2)
        elif two == "learn":
            print(3)

two_str(1, 2.6)
two_str("mama", "mama")
two_str("mama", "dom")
two_str("mama", "learn")
 
 