def parse_words(dictionary, pieces):
    actual_words = []
    attempts = []

    for prefix in pieces:
        dict_word = dictionary.get(prefix[:2], "")
        if not dict_word:
            continue
        for suffix in pieces:
            if pieces[prefix] + pieces[suffix] != 6:
                continue
            attempt = prefix + suffix
            if attempt == dict_word:
                actual_words.append(attempt)
            else:
                attempts.append(f"{attempt} != {dict_word}")


    return actual_words, attempts

if __name__ == "__main__":
    dictionary = {"albums", "barely", "befoul", "convex", "hereby", "jigsaw", "tailor", "weaver"}
    pieces = ["al", "bums", "bar", "ely", "be", "foul", "con", "vex", "here", "by", "jig", "saw", "tail", "or", "we", "aver"]

    dictionary = {wrd[:2]: wrd for wrd in dictionary}
    pieces = {wrd: len(wrd) for wrd in pieces}

    actual_words, attempts = parse_words(dictionary, pieces)

    for word in actual_words:
        print(word)

    print()

    for attempt in attempts:
        print(attempt)

