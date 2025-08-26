def format_movie(movie):
    return (
        f"Title: {movie['title']}\n"
        f"Year: {movie['year']}\n"
        f"Genres: {', '.join(movie['genres'])}\n"
        f"Plot: {movie['plot']}"
    )

def get_title(m):
    if isinstance(m, dict):
        return m.get("title") or m.get("Title") or str(m)
    return str(m)


def get_meta(m):
    if isinstance(m, dict):
        year = m.get("year", "")
        genres = m.get("genres", "")
        if isinstance(genres, list):
            genres = ", ".join(genres)
        return year, genres
    return "", ""
