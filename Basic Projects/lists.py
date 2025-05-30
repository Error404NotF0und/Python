list = ['Mango', 'Banana', 'Orange', 'Grape', 'Dragonfruit']

print("length of list", len(list))
print("First Element:", list[0])
print("Last Element:", list[-1])

list.append('Pineapple')
print("Updated List :\n", list)

list.remove('Grape')
print("Updated List :\n", list)

list.sort()
print("Sorted List:\n", list)

list.pop(1)
print("Updated List :\n", list)

list.reverse()
print("Reversed List :\n", list)

print("Multiplication on List :\n", list*2)

list = list[:4]
print("Sliced List :\n", list)

list.clear()
print("Updated List :\n", list)
