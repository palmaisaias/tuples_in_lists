#---Task 1: Formatting Flight Itineraries
#---Create a Python function that takes a list of tuples as an argument. 
#---Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
#---The function should format and return a string that lists each itinerary. 
#---For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
#---"Itinerary 1: Alice - From New York to London
#---Itinerary 2: Bob - From Tokyo to San Francisco"

import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ('Isaias', 'Los Angeles', 'Paris'), ('John', 'Dallas Fort Worth', 'Lima')]

def itin_sorter(itineraries):   #takes list 'itineraries' and formats it into a more consumable list
    print()
    itinerary_count = 0 # used this to create a clean, consecutive list of itinerary numbers
    print(Style.BRIGHT + 'Here is your list of itineraries:')
    print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
    for i in itineraries:   # for every tup in itineraries
        itinerary_count += 1    #adds 1 to itinerary_count and then I use that in my Itinerary number output
        print(f'Itinerary {itinerary_count}: {i[0]} - from {i[1]} to {i[2]}')   # formating using indexing. game changer
    print()





itin_sorter(itineraries)