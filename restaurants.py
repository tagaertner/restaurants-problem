def most_varied_visitor(visits):
    # Write your solution here!
    # return person name with the most restruants visted. 
    # dict key: value ["Auberon", "Elora"]
    # no tie but person can see the resturant 2 xtime but will be counted as 1
     
    unqiue_vistors_count= {} # create an empy dict to hold name , count is the fuking value
    
    # loop to iterate over the value names 
    for names in visits.values(): # loop over the value names
        unqiue_names = set(names) # creating unqui names 
    # find the name of person that vist most rest
        for name in unqiue_names: # looping over the unqiuqe names 
            unqiue_vistors_count[name] = unqiue_vistors_count.get(name, 0) +1 
    popular_num= max(unqiue_vistors_count.values())
    
    for name, count in unqiue_vistors_count.items():
        if count == popular_num:
            return name
        
      
    
# visits = {
# "Spicy City" : ["Auberon", "Elora"],
# "La Especial Norte": ["Elora", "Auberon", "Rowan"],
# "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
# "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
# "Applebee's": ["Sam", "Eliza"],
# }
# print(most_varied_visitor(visits))    
    

visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")