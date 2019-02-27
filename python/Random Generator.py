
import random

first_line=["Sherlock Holmes", "Batman", "Iron Man", "Bill Gates", "Nikola Tesla", "Marie Curie", "Taylor Swift", "Blackbeard", "You", "George Washington", "Alexander Hamilton", "Elphaba", "Dorothy Gale", "Thomas Jefferson", "Abraham Lincoln"]
second_line=["Dr. Watson", "Percy Jackson", "the Doctor", "Daredevil", "Thomas Edison", "Albert Einstein", "Enrico Fermi", "Spiderman", "Capitan America", "Winston Churchill", "Annabeth Chase", "Harry Potter", "Hermione Granger", "Ron Weasely"]
third_line=["solve crimes together", "form an alliance", "are roomates", "get shipwrecked together on a deserted island","prevent robots from taking over the world", "sit next to each other on the subway", "fall in love", "are stuck on an elevator together", "are involved in a duel", "elope together", "become pirates", "are switched at birth"]


for i in range(4):
    first_random_index=random.randint(0, (len(first_line)-1))
    second_random_index=random.randint(0,(len(second_line)-1))
    third_random_index=random.randint(0, (len(third_line)-1))
    print(first_line[first_random_index])
    print("and")
    print(second_line[second_random_index])
    print(third_line[third_random_index])
    print("\n")
