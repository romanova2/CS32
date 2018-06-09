from binary_search import binary_search

names = ["Havard", "Sasha","Srikanth","Tomek", "Valya", "Veronica", "Will", "Zana"]
numbers = [1,2,3,4,5,6,7,8,9,246,325,1035867]

def test_person1():
    assert binary_search(names, "Srikanth") == 2 

def test_person2():
    assert binary_search(names, "Zana") == 7

def test_person3():
    assert binary_search(names, "Havard") == 0

def test_num():
    assert binary_search(numbers, 7) == 6

