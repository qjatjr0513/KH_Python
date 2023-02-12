# people = {
#     "name" : "김개똥",
#     "phone" : "010-1010-2020"
# }

# print(people["name"], people["phone"])

# books = {"Daniel Pink" : ["파는것이 인간이다.", "언제 할 것인가"], "Eric Schidt": "새로운 디지털 시대"}
# print(books["Daniel Pink"])

# books = {0: "One", False: "True"}
# print(books[0])

coffee = {"Java": 2500, "Americano": 2500, "Latte": 3000}
print(coffee["Java"])

coffee["Java"] = 3000
print(coffee["Java"])

coffee["Moca"] = 3000
print(coffee)

# del coffee ["Java"]
# print(coffee)

# coffee.pop("Latte")
# print(coffee)

print(coffee.get("Americano"))

print(coffee.keys())
print(coffee.values())
print(coffee.items())
print("Moca" in coffee)
print("Hot Latte" not in coffee)