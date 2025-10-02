from collections.abc import Iterable

def remove_duplicates(seq):
    """
    Return a new list with duplicates removed, preserving the original order.
    Raises TypeError if input is not an iterable (except string).
    """
    if not isinstance(seq, Iterable) or isinstance(seq, str):
        raise TypeError("Input must be a non-string iterable")
    new_seq = []
    for item in seq:
        if item not in new_seq:
            new_seq.append(item)
    return new_seq


def main():
    my_seq = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    new_seq = remove_duplicates(my_seq)
    print(f"The seq with unique elements only: {new_seq}")

if __name__ == "__main__":
    main()