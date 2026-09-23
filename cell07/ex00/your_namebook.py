#!/usr/bin/env python3

def array_of_names(namebook):
    result = []
    for first, last in namebook.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
