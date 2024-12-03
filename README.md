# restaurants-problem
Problem to be completed during Industry Prep - Interview Prep

## Problem Statement

Your goal is to write a function that determines who has visited the most restaurants. You will be given a dictionary that records restaurant visits, such as the example below:

```
visits = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
```

Each key holds the name of a restaurant, and the value is a list of restaurants visits. Each visit is represented as a string holding the name of the person who visited. Note that a person may visit the same restaurant multiple times.

In this example, Auberon has visited three different restaurants: Spicy City, La Especial Norte, and Lyon's Grocery. This is more different restaurants than anyone else in the dictionary so the function should return "Auberon".

Write a function that accepts a dictionary of restaurant visits and returns the name of the person who visited the most different restaurants. See assertions in `restaurants.py` for more test cases.