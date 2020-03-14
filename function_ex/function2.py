def is_valid_voter(age):
    if age >= 18:
        return True
    else:
        return False


n = int(input("Enter your age : "))
if is_valid_voter(n):
    print("You can vote")
else:
    print("tu abhi bachha hai...")
