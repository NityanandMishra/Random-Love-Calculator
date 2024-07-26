import random
print("Love Calculator is calculating your score.....")
name1=input("")
name2=input("")

combined_name=name1+name2
new_name=combined_name.lower()



score=random.randint(0,100)

if score<10 or score>90:
    print(f"Your love score is {score}, you are like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your love score is {score}, dont give up you can make it.")
elif score>50 and score<=60:
    print(f"Your love score is {score}, you are cutiepies.")
elif score>60 and score<=70:
    print(f"Your love score is {score}, do you know you guys are made for each other just like Goodiemates.")
elif score>70 and score<=80:
    print(f"Your Love score is {score}, you are like penguines just made for each other soulmates.")
elif score>80 and score<=90:
    print(f"Your love score is {score}, you are lovebirds cant live without each other") 
else:
    print(f"Your love score is {score}")