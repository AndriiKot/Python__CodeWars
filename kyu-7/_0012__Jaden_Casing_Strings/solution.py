def to_jaden_case(string):
    return ' '.join(w.capitalize() for w in string.split())


print(to_jaden_case('string sffa dfasfs dfdasf'))