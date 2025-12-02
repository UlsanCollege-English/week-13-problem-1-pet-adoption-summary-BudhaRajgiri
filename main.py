# main.py

from collections import Counter

def summarize_adoptions(adoptions):
    """
    Summarize the number of adoptions for each type of animal.

    Parameters
    ----------
    adoptions : list of str
        A list where each element represents an adopted animal type.

    Returns
    -------
    dict
        A dictionary mapping each unique animal type to the number of times
        it appears in the adoptions list.
    """
    return dict(Counter(adoptions))


if __name__ == "__main__":
    
    sample = ["cat", "dog", "cat", "rabbit", "dog"]
    summary = summarize_adoptions(sample)
    print(summary)  # Output: {'cat': 2, 'dog': 2, 'rabbit': 1}