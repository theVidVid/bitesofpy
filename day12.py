NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]

PY_CONTENT_CREATORS = [
    "brian okken",
    "michael kennedy",
    "trey hunner",
    "matt harrison",
    "julian sequeira",
    "dan bader",
    "michael kennedy",
    "brian okken",
    "dan bader",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = set(names)
    result = [name.title() for name in names]
    return result


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    split_names = [name.split(" ") for name in names]
    sorted_surnames = sorted(
        split_names, key=lambda split_names: split_names[1], reverse=True
    )
    results = [result for sublist in sorted_surnames for result in sublist]
    answer = iter(results)
    surname_pairs = (name + " " + next(answer, "") for name in answer)
    return list(surname_pairs)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    split_names = [name.split(" ") for name in names]
    first_names = [name[0] for name in split_names]
    return min(first_names, key=len)


print(f"Original list of Names: {PY_CONTENT_CREATORS}")
unique_titlecase_names = dedup_and_title_case_names(PY_CONTENT_CREATORS)
print(f"Unique Title Case Names: {unique_titlecase_names}")
sorted_surnames_in_desc_order = sort_by_surname_desc(unique_titlecase_names)
print(f"Surnames Sorted in Descending Order: {sorted_surnames_in_desc_order}")
shortest_name = shortest_first_name(sorted_surnames_in_desc_order)
print(f"Shortest First Name in Descending Order: {shortest_name}")
