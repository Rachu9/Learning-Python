# i=0
# while i<10:
#     print(i)
#     i+=1


# i=0
# while i<=10:
#     x=0
#     while x<i:
#         print("Rachu", end='_')
#         x+=1
#     print(" ")
#     i+=1




# pin =1234
# while True:
#     pinn=int(input("Enter the pin:"))

#     if pinn==pin:
#         print("correct")
#         break
#     else:
#         print("Incorrect")

pin = 1234
trials=0
while trials<3:
    pinn = int(input(f"Trials-{trials}Enter the pin: "))
    trials+=1

    if pinn == pin:
        print("Correct")
        break
    else:
        print("Incorrect, please try again.")
