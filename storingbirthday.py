# lesson 19 storing birthday project
friend1_name = "Rahim"
friend1_birthday = "January 15"

friend2_name = "Prianka"
friend2_birthday = "March 22"

friend3_name = "Arman"
friend3_birthday = "July 8"

friend4_name = "rafi"
friend4_birthday = "October 31"

friend5_name = "ramim"
friend5_birthday = "December 5"

print("Birthdays of someone's friends:")
print(f"{friend1_name}: {friend1_birthday}")
print(f"{friend2_name}: {friend2_birthday}")
print(f"{friend3_name}: {friend3_birthday}")
print(f"{friend4_name}: {friend4_birthday}")
print(f"{friend5_name}: {friend5_birthday}")


birthdays = {
    "Rahim": "January 15",
    "Prianka": "March 22",
    "Arman": "July 8",
    "rafi": "October 31",
    "ramim": "December 5"
}

print("Birthdays of someone's friends:")
for name, date in birthdays.items():
    print(f"{name}: {date}")