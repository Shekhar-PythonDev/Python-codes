# Create a big_db datbase .it includes 4 small databses named as chotu_db1, chotu_db2, chotu_db3, and chotu_db4.every chotu_db datbase contains 4 movies each in it.they are all indean moivies.and perform iterations on it.and display how many actors name comes more than two times in the database.take movie name as key and value as casting of the movies.
from collections import defaultdict
big_db = {
    "chotu_db1":{
        "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi"],
        "Pathaan": ["Shah Rukh Khan", "Deepika Padukone", "John Abraham"],
        "Dangal": ["Aamir Khan", "Sakshi Tanwar", "Fatima Sana Shaikh"],
        "Lagaan": ["Aamir Khan", "Gracy Singh", "Amin Hajee"]
    },
    "chotu_db2":{
        "Kabir Singh": ["Shahid Kapoor", "kiara Advani", "Arjun Kapoor"],
        "Bajrangi Bhaijaan": ["Salman Khan", "Harshali Malotra", "Nawazuddin Siddiqui"],
        "PK": ["Amir Khan", "Anushka Sharma","Sanjay Dutt","Sushant Singh Rajput"],
        "Chhichhore": ["Sushant Singh Rajput", "Shraddha Kapoor", "Varun Sharma"]
    },
    "chotu_db3":{
        "Queen": ["Kangana Ranaut", "Rajkummar Rao", "Lisa Haydon"],
        "Tanu Weds Manu": ["Kangana Ranaut", "Madhavan", "Jimmy Shergill"],
        "Andhadhun": ["Ayushmann Khurrana", "Tabu", "Radhika Apte"],
        "Badhaai Ho": ["Ayushmann Khurrana", "Neena Gupta", "Gajraj Rao"]
    },
    "chotu_db4":{
        "Singham": ["Ajay Devgn", "Kajal Aggarwal", "Prakash Raj"],
        "Drishyam": ["Ajay Devgn", "Tabu", "Ishita Dutta"],
        "Leo": ["Vijay", "Trisha Krishnan", "Sanjay Dutt"],
        "Master": ["Vijay", "Malavika Mohanan", "Arjun Das"],
    }

}
# Function to display movies and their casts from the big_db
def display_movies_and_casts():
    for db_name, movies in big_db.items():
        print(f"\nDatabase: {db_name}")
        for movie, cast in movies.items():
            print(f"Movie: {movie}, Cast: {', '.join(cast)}")
# Function to count actor appearances across all movies in the big_db
actor_count =defaultdict(int)
for chotu_db in big_db.values():
    for movie_cast in chotu_db.values():
        for actor in movie_cast:
            actor_count[actor] += 1
  # Display actors who appear more than twice
for actor, count in actor_count.items():
    if count > 2:
        print(f"{actor} appears {count} times in the database.")   
  #Display results
display_movies_and_casts()
# Display the actor count results
print("\nActors appearing more than twice:")
for actor, count in actor_count.items():
    if count > 2:
        print(f"{actor} appears {count} times in the database.")

#OUTPUT:
Database: chotu_db1
Movie: Jawan, Cast: Shah Rukh Khan, Nayanthara, Vijay Sethupathi
Movie: Pathaan, Cast: Shah Rukh Khan, Deepika Padukone, John Abraham
Movie: Dangal, Cast: Aamir Khan, Sakshi Tanwar, Fatima Sana Shaikh
Movie: Lagaan, Cast: Aamir Khan, Gracy Singh, Amin Hajee

Database: chotu_db2
Movie: Kabir Singh, Cast: Shahid Kapoor, Kiara Advani, Arjun Kapoor
Movie: Bajrangi Bhaijaan, Cast: Salman Khan, Harshali Malotra, Nawazuddin Siddiqui
Movie: PK, Cast: Aamir Khan, Anushka Sharma, Sanjay Dutt, Sushant Singh Rajput
Movie: Chhichhore, Cast: Sushant Singh Rajput, Shraddha Kapoor, Varun Sharma

Database: chotu_db3
Movie: Queen, Cast: Kangana Ranaut, Rajkummar Rao, Lisa Haydon
Movie: Tanu Weds Manu, Cast: Kangana Ranaut, Madhavan, Jimmy Shergill
Movie: Andhadhun, Cast: Ayushmann Khurrana, Tabu, Radhika Apte
Movie: Badhaai Ho, Cast: Ayushmann Khurrana, Neena Gupta, Gajraj Rao

Database: chotu_db4
Movie: Singham, Cast: Ajay Devgn, Kajal Aggarwal, Prakash Raj
Movie: Drishyam, Cast: Ajay Devgn, Tabu, Ishita Dutta
Movie: Leo, Cast: Vijay, Trisha Krishnan, Sanjay Dutt
Movie: Master, Cast: Vijay, Malavika Mohanan, Arjun Das

Actors appearing more than twice:
Aamir Khan appears 3 times in the database.
Sanjay Dutt appears 3 times in the database.
Tabu appears 3 times in the database.
Vijay appears 3 times in the database.
Ayushmann Khurrana appears 2 times in the database.   # (just for info, below threshold)
Sushant Singh Rajput appears 2 times in the database. # (same)
...

        
            
