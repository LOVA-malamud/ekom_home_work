list = ["apple","banana","kiwi","grape","melon","pear"]
def group_words_by_length(words: list) -> dict:
    result = {}
    for word in words:
        len_word = len(word)
        if len_word in result:
            result[len_word] = word
        else:
            result[len_word] = [word]
    return result
print(group_words_by_length(list))