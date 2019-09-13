
examples = [[1,"True"], ['cat', 'cat'], ['erdd', 'learn'], ['cat', 'dog'], ['dogs', 'cat']]


def comparing_strings(first_string, second_string):
    # я не знаю, когда лучше использовать ==, а когда is
    if type(first_string) is not str or type(second_string) is not str:
        return 0
    elif first_string == second_string:
        return 1
    elif len(first_string) > len(second_string):
        return 2
    elif first_string != second_string and second_string == 'learn':
        return 3


for example in examples:
    print(comparing_strings(example[0], example[1]))

