from random import random, randint, shuffle, randrange, sample, choice, choices

print("Random 0-1 arasında değer üretir: ", random())
print("RandInt() (min-max aralığında integer değer döndürür ) int:", randint(1, 3))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Shuffle({numbers}) -> None: ")
shuffle(numbers)
print(numbers)

# stop değeri sonuca dahil edilmez randrange özelliği için
print(f"RandRange(stop) -> any: ", randrange(10))
print(f"RandRange(start,stop) -> any: ", randrange(0, 10, 1))
print(f"RandRange(start,stop,step=1) -> any: ", randrange(0, 250, 30))

print(f"Sample({numbers},k) ->: ", sample(numbers, k=5))
print(f"Choice({numbers}) -> any:", choice(numbers))
print(f"Choises({numbers},k) ->: list[any]", choices(numbers, k=5))
