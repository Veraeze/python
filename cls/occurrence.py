def occurrences(word: str, replace: str, index: int):
    new_word = ""
    word_list = list(word)
    for i in range(index, len(word_list)):
        if word_list[index - 1] == word_list[i]:
            word_list[i] = replace
    for i in word_list:
        new_word += i
    return new_word

