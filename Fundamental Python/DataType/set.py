my_set={12, "shanbel", 20, True}
print(my_set)
print(type(my_set))
my_set.add("python")
my_set.pop()
my_set.add(20) # This will not add 20 again because sets do not allow duplicates
print(my_set)
my_set.remove(20)
# my_set.remove("kibre") # This will raise an error because "kibre" is not in the set
# my_set.discard(100) # This will not raise an error even if 100 is not in the set
print(my_set)
