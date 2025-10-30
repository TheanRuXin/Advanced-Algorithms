class UDGraph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            if to_vertex not in self.graph[from_vertex]:
                self.graph[from_vertex].append(to_vertex)
        else:
            raise ValueError("One or both vertices not found in graph")

    def list_outgoing_adjacent_vertex(self, vertex):
        return self.graph.get(vertex, [])

    def get_user_name(self):
        return list(self.graph.keys())

    def get_followers(self,person):
        followers = []
        for vertex, neighbours in self.graph.items():
            if person in neighbours:
                followers.append(vertex)
        return followers

class Person:
    def __init__(self, name, gender, biography, privacy):
        self.name = name
        self.gender = gender
        self.bio = biography
        self.privacy = privacy

    def __str__(self):
        return self.name

p1 = Person("Alice", "Female", "Love travel.", "public")
p2 = Person("Bob", "Male", "Love game.", "private")
p3 = Person("Cathy", "Female", "Love Food", "public")
p4 = Person("David", "Male", "Love Music", "public")
p5 = Person("Eva", "Female", "Fitness trainer.", "private")

people = [p1, p2, p3, p4, p5]

social_media_app = UDGraph()

for person in people:
    social_media_app.add_vertex(person)

social_media_app.add_edge(p1, p2)
social_media_app.add_edge(p1, p3)
social_media_app.add_edge(p2, p3)
social_media_app.add_edge(p3, p1)
social_media_app.add_edge(p4, p1)
social_media_app.add_edge(p5, p4)

def display_menu():
    print("\n===== Social Media App =====")
    print("1. Display all users")
    print("2. View user profile")
    print("3. View followed accounts")
    print("4. View followers")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice


def find_person_by_name(name):
    for person in people:
        if person.name.lower() == name.lower():
            return person
    return None


while True:
    choice = display_menu()

    if choice == "1":
        print("\n--- All Users ---")
        for user in social_media_app.get_user_name():
            print(user.name)

    elif choice == "2":
        name = input("Enter user name to view profile: ")
        person = find_person_by_name(name)
        if person:
            if person.privacy == "private":
                print(f"\nName: {person.name}\nPrivacy: Private (limited view)")
            else:
                print(f"\nName: {person.name}")
                print(f"Gender: {person.gender}")
                print(f"Bio: {person.bio}")
                print(f"Privacy: {person.privacy}")
        else:
            print("User not found!")

    elif choice == "3":
        name = input("Enter user name to view followed accounts: ")
        person = find_person_by_name(name)
        if person:
            following = social_media_app.list_outgoing_adjacent_vertex(person)
            print(f"\n{person.name} follows:")
            for f in following:
                print(f"- {f.name}")
        else:
            print("User not found!")

    elif choice == "4":
        name = input("Enter user name to view followers: ")
        person = find_person_by_name(name)
        if person:
            followers = social_media_app.get_followers(person)
            print(f"\nFollowers of {person.name}:")
            for f in followers:
                print(f"- {f.name}")
        else:
            print("User not found!")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")

