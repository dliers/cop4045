"""
@author: Daniel Liers
ZNumber: 23716566
"""
import csv
def read_movies(filename: str) -> dict:
    """Reads a movie CSV file and returns a dictionary."""

    movie_dict = {}
    movie_file = open(filename, "r", encoding="utf-8")
    reader = csv.reader(movie_file)

    first_row = True

    for row in reader:
        if first_row:
            first_row = False
        else:
            title = row[1]
            movie_dict[title] = row

    movie_file.close()

    return movie_dict

def read_casts(filename: str) -> list:
    """Reads a cast CSV file and returns a list."""

    cast_list = []

    cast_file = open(filename, "r", encoding="utf-8")
    reader = csv.reader(cast_file)

    for row in reader:
        cast_list.append(row)
    cast_file.close()

    return cast_list

def display_top_collaborations(rated_filename: str,
                               casts_filename: str,
                               number: int = 10) -> None:

    rated_movies = read_movies(rated_filename)
    casts = read_casts(casts_filename)

    collaborations = {}

    for row in casts:
        title = row[0]

        if title in rated_movies:
            director = row[2]

            for actor in row[3:]:
                if actor != "":
                    key = (director, actor)

                    if key in collaborations:
                        collaborations[key] = collaborations[key] + 1
                    else:
                        collaborations[key] = 1

    ranking = []

    for key in collaborations:
        director = key[0]
        actor = key[1]
        count = collaborations[key]

        ranking.append((count, director, actor))

    ranking.sort(reverse=True)

    print("Top Director/Actor Collaborations:")

    count = 0

    for item in ranking:
        if count == number:
            break

        print((item[1], item[2], item[0]))
        count = count + 1

def display_top_actors(grossing_filename: str,
                       casts_filename: str,
                       number: int = 10) -> None:
    grossing_movies = read_movies(grossing_filename)
    casts = read_casts(casts_filename)

    actors = {}

    for row in casts:
        title = row[0]

        if title in grossing_movies:
            box_office = float(grossing_movies[title][3])

            for actor in row[3:]:
                if actor != "":
                    if actor in actors:
                        actors[actor] = actors[actor] + box_office
                    else:
                        actors[actor] = box_office

    ranking = []

    for actor in actors:
        ranking.append((actors[actor], actor))
    ranking.sort(reverse=True)

    print("Top Actors:")

    count = 0

    for item in ranking:
        if count == number:
            break

        print((item[1], item[0]))
        count = count + 1

def main() -> None:
    display_top_collaborations(
        "imdb-top-rated.csv",
        "imdb-top-casts.csv",
        10
    )
    print()
    display_top_actors(
        "imdb-top-grossing.csv",
        "imdb-top-casts.csv",
        10
    )
main()