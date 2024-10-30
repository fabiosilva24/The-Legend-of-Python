# Write code below 💖

credits = int(input("credits :" ))
height = int(input("height :"))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137:
    print("You are not tall enough to ride.")
elif credits < 10:
    print("You don't have enough credits.")