attempt = 0
while attempt <= 3:
    answer = input("Guess the secret numer between 1 and 10, type quit to stop: ")
    answer = int(answer)
    attempt = attempt + 1
    if answer == 8:
        print(f"good game, your answer {answer} was correct!")
        break
    elif answer < 0 or answer > 10:
        print(f"error detected: {answer} is not a value in the range")
        break
    elif attempt <= 3:
        print("incorrect, please try again")

if answer < 0 or answer > 10:
    print("next time follow the rules")
else:
    print("thanks for playing the guessing game")

#example of a while loop using break to end the loop

go_go_go = True

while go_go_go:
    text = input("please enter a word, type quit to stop: ")

    if text == "":
        continue

    if text == "quit":
        break

    print("You typed:", text)

print(f"Loop finished. you finally typed {text}!")

# example of continue and break to either skip or end the loop at the iteration

for value in range(1, 11, 1):
    if value == 5:
        # skip this iteration when value is 5
        continue

    if value == 8:
        # stop the loop completely when value is 8
        break

    print(f"the value is: {value}.")

print("Done looping.")

# example of a for loop with break and continue

# counters and totals practice

# count = tickets
# total = total of (price + count)

count = 0              # variables initialized outside of the loop
total = 0

for price in range(1, 6):
    count += 1         # variables updated inside the loop
    total += price

print(f"tickets sold: {count}. Gross Profit: ${total}.") # prints outside the loop

# for and while loops, counters and totals, class practice

count = 0
total = 20

for a in range(1, 51):
    count += 3
    total += a

print(f"we sold: {count} kits for a total of: ${total}")

apples = 0
slices = 20
oops = 3

while oops <= 5:
    apples += 1
    slices += oops
    oops += 1

print(f"i turned {apples} apples into {slices}, but i dropped {oops} slices, so there is only {slices - oops} left")

# challenge 1 for this weeks lessons
print(f"My for loop total was: {total}, my while loop total was: {slices}")

def ticket_price(age):
    if age < 13:
        return 5
    else:
        return 10

adult_ticket_price = ticket_price(20)
child_ticket_price = ticket_price(10)

print(f"Adult tickets (13 and up) cost ${adult_ticket_price}, and Children's tickets (12 and under) cost ${child_ticket_price}.")

# challenge 2

count = 0

while True:
    count = count + 1
    print("Scanned item number:", count)
    
    if count == 5:
        print("Limit reached, stopping scan.")
        break

# handling empty strings in python cleanly

user_input = input("type something: ")
clean = user_input.strip(" h")
if user_input == "":
    print("You entered nothing!")
elif user_input == "hello":
    print(f"you typed: {user_input}")
else:
    print("You entered:", clean)
print(repr(clean), repr(user_input))

# handling empty strings in python cleanly

# list slicing and indexing examples
games = ["Mario", "Zelda", "Tetris", "Pac-Man"]

print("Index 0:", games[0])
print("Index 1:", games[1])
print("Index 2:", games[2])
print("Index 3:", games[3])

print("games[-1]:", games[-1])
print("games[-2]:", games[-2])
print("games[-3]:", games[-3])
print("games[-4]:", games[-4])

games[2] = "Minecraft"
print(games)

print("Slice games[0:2]:", games[0:2])
print("Slice games[1:3]:", games[1:3])
print("Slice games[1:4]:", games[1:4])

# print("Length of games:", len(games))
# print("Trying to access games[10]:")
# print(games[10])  # this is asking for something out of the range we have, so this is why it errors? 
# !!these 3 lines cause error so i commented them out of the code!!

index = 3 

if index < len(games):
    print("Safe access:", games[index])
else:
    print("Index", index, "is out of range for this list")


# above is list slicing and indexing examples

# Lists, mastering and list iteration

games = ["Halo", "Mario", "Zelda", "Minecraft"]
for i in range(len(games)):
    print(f"Index {i}: {games[i]}")   

for game in games:
    print(f"Game: {game}")

scores = [1200, 850, 990, 1430]

for i in range(len(scores)):
    scores[i] = scores[i] + 100
    print(f"Score{i}: {scores[i]}")
print(scores)

items = ["Potion", "Shield", "Sword"]
for i in range(len(items)):
    print(f"Slot {i}: {items[i]}")  

for item in items:
    print(f"Item: {item}")

# Lists, mastering and list iteration

# append(value)
games = ["chess", "checkers"]
print("start:", games)

games.append("poker")                           # append() example
print("after append:", games)

games.append("go")
print("after second append:", games)


# insert(index, value)
newgames = ["chess", "checkers", "poker"]               
print("start:", newgames)

newgames.insert(1, "go")                         # insert() example
print("after insert at index 1:", newgames)

newgames.insert(0, "monopoly")
print("after 2nd insert:", newgames)


# extend(add multiple values separated by commas)
numbers = [1, 2, 3]
print("start:", numbers)

numbers.extend([4, 5, 6])                       # extend() example
print("after extend:", numbers)


# remove(value)
games2 = ["chess", "checkers", "poker", "go"]
print("original games_list:", games2)

games2.remove("poker")                          # remove() example
print("after remove:", games2)

# games2.remove("DOES_NOT_EXIST")          ## intentional bad use of remove when item in list doesnt exist
# print("after bad remove:", games2)


# pop(index)
scores = [10, 20, 30, 40]
print("start scores:", scores)

last_score = scores.pop()                      # pop removes the last item in the list
print("popped value:", last_score)  
print("after pop:", scores)

scores2 = [5, 15, 25, 35, 45]
print("start scores2:", scores2)

middle_score = scores2.pop(2)                  # index 2 is popped
print("popped middle_score:", middle_score)
print("after middle pop:", scores2)

# more list practice

# common methods of altering lists in python practice session with a single list. 

games = ["chess", "checkers"]
print("start:", games)

# 1) add "poker" to the end
# TODO

games.append("poker")
print("after append:", games)

# 2) insert "go" at index 1
# TODO
games.insert(1, "go")
print("after insert:", games)
# 3) extend with ["monopoly", "scrabble"]
# TODO
games.extend(["monopoly", "scrabble"])
print("after adds:", games)

# 4) remove "checkers" by value
# TODO
games.remove("checkers")
print("after remove:", games)
# 5) pop the last game into a variable called last_game
# TODO

last_game = games.pop()
print("after removals:", games)
print("last_game:", last_game)

# Ordering lists: sorted() vs. .sort()
# .sort() example

numbers = [5, 2, 9, 1]
print(f"Original list: {numbers}")

numbers.sort()
print(f"After sort:  {numbers}")

# sorted() example

numbers2 = [5, 2, 9, 1]
sorted_numbers = sorted(numbers2)

print(f"numbers after sorted():       {numbers2}")
print(f"sorted_numbers (new list):    {sorted_numbers}")

# reverse=True example

scores = [10, 50, 20, 40]
print(f"Original scores: {scores}")

scores.sort(reverse=True)

print(f"Scores sorted descending: {scores}")

# key= example

words = ["python", "is", "fun", "sometimes"]
print(f"Original words: {words}")

words_sorted_by_length = sorted(words, key=len)

print(f"Words sorted by length: {words_sorted_by_length}")

# use key= and reverse=True together

words2 = sorted(words, key=len, reverse=True)
print(f"words sorted by length in reverse order: {words2}")

names = ["Charlie", "jamie", "Richard", "vinny"]
names2 = sorted(names, key=str.lower)
print(f"Original list: {names}")
print(f"after sorting: {names2}")

words3 = ["to", "be", "or", "not", "to", "be"]
print(f"Original words: {words3}")

words_by_length = sorted(words3, key=len)
print(f"Words sorted by length: {words_by_length}")

nums = [3, 1, 3, 2, 3]
print(f"original: {nums}.")
nums_desc = sorted(nums, reverse=True) 
print(f"after the sort: {nums_desc}.")

# dictionaries, keys and values practice

person = {"name": "Alice", "age": 30}
print(person)

print(person["name"])
print(person["age"])

person["city"] = "Dallas"
print(person)
print(person["city"])

person["age"] = 31
print(person)
print(person["age"])

# more dictionary practice

data = {
    "course": "Python",
    1: "first",
    2.5: "pi-ish",
    (2025, 12, 18): "today"
}

print(data)
print(data["course"])
print(data[1])
print(data[2.5])
print(data[(2025, 12, 18)])

# intentionally using an invalid key type to see the traceback error

#bad_dict = {}
#bad_key = [1, 2, 3]

#bad_dict[bad_key] = "oops"
#print(bad_dict)

# off the top create a dictionsary with atleast 3 keys of different valid types. str int and tuple

fire = {"blaze": "Burn", "temp": 3000}

print(fire)
print(fire["blaze"])
print(fire["temp"])

fire["blaze"] = "yes"
print(fire["blaze"])

fire["temp"] = 6000
print(fire["temp"])

# dictionaries: iteration patterns

video_game_prices = {
    "Minecraft": 26.95,
    "Stardew Valley": 14.99,
    "Celeste": 19.99
}

for key in video_game_prices:   # for loop example using print(key)
    print(key)

for key in video_game_prices.keys():  # another for loop example using .key()
    print(key)

for price in video_game_prices.values():  # for loop using .values() to list the keys or games values
    print(price)

for game, price in video_game_prices.items():
    print(f"{game}, costs: ${price}.")     # made sense to use an f string to print this line given the output

# new loop that prints only the game names for games cheaper than 20

for game, price in video_game_prices.items():
    if price < 20.00:
        print(f"this game is under 20.00 dollars. Title: {game}, Cost: ${price}.")

# another practice using the keys and values of a dictionary with loops

movie_ratings = {
    "Inception": 8.8,
    "The Room": 3.7,
    "Interstellar": 8.6,
    "Cats": 2.7
}
for movie, rating in movie_ratings.items():
    print(f"{movie}\n{rating}")

for movie in movie_ratings.keys():
    print(movie)

for movie, rating in movie_ratings.items():
    if rating < 5.0:
        print(f"this movie has bad reviews: {movie}, look at the rating: {rating}")

# Updates and copy semantics- w/ list and dict.
# example
a = ["x", "y", "z"]
b = a
b.append("NEW")

# practice aliasing with numbers, variables point to the same list

numbers = [1, 2, 3]
alias = numbers               # (same object)
alias.append(4)
print("number:", numbers)
print("alias", alias)

# practice aliasing with str clean copy

colors = ["red", "green", "blue"]
colors_copy = colors[:]       # (clean copy, new object)
colors_copy.append("yellow")
print("colors:", colors)
print("colors copy:", colors_copy)

# more practice copying a list

fruits = ["apple", "banana"]
fruits_copy1 = list(fruits)   # (clean copy, new object)
fruits_copy2 = fruits.copy()  # (clean copy, new object)

fruits_copy1.append("cherry")
fruits_copy2.append("orange")

print("fruits:", fruits)
print("fruits_copy1:", fruits_copy1)
print("fruits_copy2:", fruits_copy2)

# more practice both variables point to the same dictionary

game = {"title": "Elden Ring", "price": 59.99}

game_alias = game         # (same object)
game_alias["price"] = 19.99

print("game (after alias change):", game)
print("game_alias:", game_alias)

# here we fix above with a clean copy

game2 = {"title": "Elden Ring", "price": 59.99}

game_copy1 = dict(game2)  # (clean copy, new object)
game_copy2 = game2.copy() # (clean copy, new object)

game_copy1["price"] = 39.99
game_copy2["price"] = 9.99

print("game2:", game2)
print("game_copy1:", game_copy1)
print("game_copy2:", game_copy2)

# i see the distinction, when i use game_alias = game, after defining game =, they now point to the same value/list/dict
# and in alias = numbers after defining numbers =, the same thing. this is the indicator (this = this)

# Nested structures and safe mutation

matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

print("matrix:", matrix)
print("matrix[1]:", matrix[1])        # matrix[1]- 1 = go to row [1] 
print("matrix[1][2]:", matrix[1][2])  # matrix[1][2]- 1 = go to row [1] and 2 = at this index [2] 

# {"So each pair of brackets […] is one hop deeper:
# first hop: which row
# second hop: which column"}

print("\nBefore change:", matrix)
matrix[2][1] = 99
print("After change:", matrix)
print("path → row 2, col 1:", matrix[2][1])

# nested dict

inventory = {
    "gold": 100,
    "potions": {
        "health": 3,
        "mana": 5
    },
    "weapons": {
        "sword": 1,
        "bow": 0
    }
}

print("\nFull inventory:", inventory)
print("potions sub-dict:", inventory["potions"])
print("health potions:", inventory["potions"]["health"])
print("sword count:", inventory["weapons"]["sword"])

# now we update

print("\nBefore updates:", inventory)

# gain 50 gold
inventory["gold"] += 50

# use 1 health potion
inventory["potions"]["health"] -= 1

# find a new sword
inventory["weapons"]["sword"] += 1

print("After updates:", inventory)
print("path → gold:", inventory["gold"])
print("path → potions → health:", inventory["potions"]["health"])
print("path → weapons → sword:", inventory["weapons"]["sword"])

# mix list + dict together

party = [
    {"name": "Alice", "hp": 100, "items": ["potion", "elixir"]},
    {"name": "Bob", "hp": 80, "items": ["bomb"]},
]

print("\nFull party:", party)
print("First member dict:", party[0])
print("First member name:", party[0]["name"])
print("Second member items list:", party[1]["items"])
print("First item of second member:", party[1]["items"][0])

# now we mutate this mixed structure

print("\nBefore party updates:", party)

# Alice takes 30 damage
party[0]["hp"] -= 30

# Bob gets a new item "potion"
party[1]["items"].append("potion")

print("After party updates:", party)
print("path → Alice hp:", party[0]["hp"])
print("path → Bob items:", party[1]["items"])

# safe look up with dict.get()

player = {
    "name": "Alice",
    "stats": {
        "hp": 100,
        "mp": 30
    }
}

print("\nplayer dict:", player)

stats = player.get("stats")
print("stats via get():", stats)

hp = player.get("stats", {}).get("hp", 0)
print("safe hp lookup:", hp)

energy = player.get("stats", {}).get("energy", 0)
print("safe energy lookup (missing key):", energy)

# another matrix example

print("\nAliasing demo:")

row = [1, 2, 3]
bad_matrix = [row, row]   # both rows point to the SAME inner list

print("bad_matrix before:", bad_matrix)
bad_matrix[0][0] = 99
print("bad_matrix after changing [0][0]:", bad_matrix)

# now a safer version with a copy
row2 = [1, 2, 3]
good_matrix = [row2, row2[:] ]   # second row is a shallow copy

print("\ngood_matrix before:", good_matrix)
good_matrix[0][0] = 77
print("good_matrix after changing [0][0]:", good_matrix)

# final challenge

print("\nFINAL CHALLENGE")

game = {
    "players": [
        {"name": "Alice", "hp": 100, "inventory": {"gold": 10, "items": ["potion"]}},
        {"name": "Bob", "hp": 90, "inventory": {"gold": 5, "items": []}},
    ]
}

print("Original game:", game)

# 1) Safely read Bob's gold into a variable bob_gold using get(), default 0
bob = game["players"][1]
bob_gold = bob.get("inventory", {}).get("gold", 0)
print("Bob gold (safe):", bob_gold)

# 2) Make Bob take 20 damage (mutate nested structure)
bob["hp"] -= 20

# 3) Append "elixir" to Alice's items list
alice = game["players"][0]
alice["inventory"]["items"].append("elixir")

print("Updated game:", game)
print("path → Bob hp:", game["players"][1]["hp"])
print("path → Alice items:", game["players"][0]["inventory"]["items"])

