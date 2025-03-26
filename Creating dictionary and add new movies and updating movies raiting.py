
#simple type of create dictionary and ghet operations on movie ratings and updating
# this code is easily understanfing to create a dictionary and how to operations on it 
""" Movie_collection = {
    "Jawan" : 8.9,
    "Pathan" : 9.2,
    "Krish" : 7.2,
    "chhaava" : 9.8
}
print(Movie_collection)

Movie_collection["chhaava"] = 9.9
Movie_collection["ishq"] = 9.5

print(Movie_collection)
print("Raiting of jawan movie is",Movie_collection["Pathan"],"/ 10")
print(Movie_collection.values())
print(Movie_collection.keys()) """

# GIVEN CODE IS BETTER CODE THAN ABOVE CODE 
# THIS CODE IS EXACTLY RELATABLE ON MOVIES RAITING

movies = {}

while( True):
    print("\n1. Add movie and rating")
    print("2. Update movie rating")
    print("3. Display movie name and ratings ")
    print("4. Exit program")
    
    choice = int(input(" \nEnter a choice"))

    if choice == 1:
        movie = input("\n Enetr a movie name")
        raiting = float(input(f"Enetr a raiting for {movie} (out of 10): "))
        movies[movie] = raiting
        print(f"{movie} added with raiting {raiting}:")
        
    elif choice == 2:
        movie = input("\n Eneter a name you want to update a movie raiting")
        if movie in movies:
            raiting = float(input(f"Enetr a raiting for {movie} (out of 10)"))
            movies[movie] = raiting
            print(f"Updated raiting for {movie} is {raiting}:")
        else:
            print("Movie name is not found")
            
    elif choice == 3:
        if movie in movies:
            print(f"Display all movies and raitins is : {movies}:")
        else:
            print("No any movie is present")
        
    elif choice == 4:
        print("Exit to program")
        break
        
    else:
        print("Invalid choice")
