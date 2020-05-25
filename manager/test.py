class Test:

    #palaj_list is ordered and changeable
    palaj_list = list(["word", "second"])
    print(palaj_list)

    palaj_list.append("myfriend")
    print(palaj_list)

    #palaj_set is unordered and unindexed
    palaj_set = set(["1", "2", "10", "4"])
    print(palaj_set)

    palaj_set.add("15")
    print(palaj_set)

    #palaj_tuple is unchangeable
    palaj_tuple = tuple(["apple", "pineapple", "juice"])
    print(palaj_tuple)

    #palaj_dictionary
    palaj_dictionary = {
        "palaj": "very bad",
        "c++": "programming"
    }

    print(palaj_dictionary)
    print(palaj_dictionary["palaj"])

    palaj_dictionary["color"] = "black"
    print(palaj_dictionary["color"])
