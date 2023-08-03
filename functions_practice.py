def hello():
  print("Hello user!")

hello()


def pack(x, y, z):
  return [x, y, z]

print(pack(1, 2, 3))



def eat_lunch(foods):
  if len(foods) == 0:
    print("My lunchbox is empty!") 
  else:
    print("First I eat " + foods[0])
    for food in foods[1:]:
      print("Next I eat " + food)

eat_lunch(["sandwich", "apple", "cookie"])
eat_lunch([])


hello()
print(pack(1, 2, 3))
eat_lunch(["sandwich", "apple", "cookie"])
eat_lunch([])