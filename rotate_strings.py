def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return f"{string[n:]}{string[:n]}"


rotated_phrase = "hello"
answer = rotate(rotated_phrase, -2)
print(f"Result: {answer}")
