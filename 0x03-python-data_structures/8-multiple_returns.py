#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        answer_tuple = (0, None)
    else:
        str_len = len(sentence)
        first_char = sentence[0]
        answer_tuple = (str_len, first_char)
    return (answer_tuple)
