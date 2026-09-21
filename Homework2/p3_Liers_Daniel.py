"""
@author: Daniel Liers
ZNumber: 23716566
"""
import csv
def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Adds a new user to the social network."""
    try:
        if username in sn:
            return False

        sn[username] = (fullname, [])

        return True

    except Exception as e:
        print("Error adding user:", e)
        raise

def add_friend(sn: dict, user1: str, user2: str) -> bool:
    """Adds a mutual friendship between two users."""

    try:
        if user1 not in sn or user2 not in sn:
            return False
        if user1 == user2:
            return False
        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)

        return True

    except Exception as e:
        print("Error adding friend:", e)
        raise

def get_friends(sn: dict, user1: str, distance: int) -> list:
    """Returns friends of a user up to the given distance."""

    try:
        if user1 not in sn:
            return []

        if distance <= 0:
            return []

        friends = []
        visited = [user1]
        current = [user1]

        for i in range(distance):
            next_users = []

            for user in current:
                for friend in sn[user][1]:
                    if friend not in visited:
                        visited.append(friend)
                        friends.append(friend)
                        next_users.append(friend)
                    current = next_users
                

            if len(current) == 0:
                break

        return friends

    except Exception as e:
        print("Error finding friends:", e)
        raise

def save_network(filename: str, sn: dict) -> None:
    """Saves the social network to a CSV file."""

    try:
        file = open(filename, "w", newline="")
        writer = csv.writer(file)

        writer.writerow(["username", "fullname", "friends"])

        for username in sn:
            fullname = sn[username][0]
            friend_list = sn[username][1]
            friends = ",".join(friend_list)
            writer.writerow([username, fullname, friends])

        file.close()

    except Exception as e:
        print("Error saving social network:", e)
        raise

def load_network(filename: str) -> dict:
    """Loads the social network from a CSV file."""

    try:
        sn = {}

        file = open(filename, "r", newline="")
        reader = csv.reader(file)

        first_row = True

        for row in reader:
            if first_row:
                first_row = False
            else:
                username = row[0]
                fullname = row[1]

                if len(row) > 2 and row[2] != "":
                    friends = row[2].split(",")
                else:
                    friends = []
                sn[username] = (fullname, friends)

        file.close()

        return sn

    except Exception as e:
        print("Error loading social network:", e)
        raise

def main() -> None:
    """Tests the social network functions."""
    try:
        sn = {}
        print("Adding users:")
        print(add_user(sn, "alice", "Alice Smith"))
        print(add_user(sn, "maria", "Maria Cortez"))
        print(add_user(sn, "joe", "Joseph Adams"))
        print(add_user(sn, "eve", "Evelyn Cooper"))
        print(add_user(sn, "david", "David Benson"))
        print()
        print("Adding friends:")
        print(add_friend(sn, "alice", "maria"))
        print(add_friend(sn, "maria", "joe"))
        print(add_friend(sn, "joe", "eve"))
        print(add_friend(sn, "maria", "david"))
        print()
        print("Friends of alice at distance 1:")
        print(get_friends(sn, "alice", 1))
        print()
        print("Friends of alice at distance 2:")
        print(get_friends(sn, "alice", 2))
        save_network("social_network.csv", sn)
        sn = load_network("social_network.csv")
        print()
        print("Loaded social network:")
        print(sn)

    except Exception as e:
        print("An error occurred:", e)
        raise
main()