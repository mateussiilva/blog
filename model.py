

all_posts = {
    "0": {
        "title": "Python vs Rust",
        "tags": ["Programção", "Python", "Rust"],
        "data": "Python é tão interesante quanto Rust porem"

    },
    "1": {
        "title": "Python vs Rust",
        "tags": [],
        "data": "Python é tão interesante quanto Rust porem"

    }
}


def get_all_post():
    return all_posts


def randon_posts(num: int = 7):

    pass


if __name__ == "__main__":
    posts = get_all_post()
    print(posts)
