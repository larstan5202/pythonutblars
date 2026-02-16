def test_one_vowel():
    assert count_vowels("a") == 1
    assert count_vowels("Banan") == 2

# Vokaler
def test_all_vowels():
    assert count_vowels("aeiouyåäö") == 9

# Flera förekomster av samma vokal

def test_repeated_vowels():
    assert count_vowels("aaaa") == 4
    assert count_vowels("öööööö") == 6

# Stora smä bokstäver

def test_mixed_case():
    assert count_vowels("ÅÄÖåäö") == 6
    assert count_vowels("HeLlO") == 2

def count_vowels(word):
    vowels = "aeiouyåäöAEIOUYÅÄÖ"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count