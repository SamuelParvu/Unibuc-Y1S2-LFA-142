import re



file_path = "NFA/nfa test.nfa"
section_list = ["STATES", "ALPHABET", "START", "FINISH", "TRANSITIONS"]


def remove_comments(text):
    comment_pattern = r'\s*#.*'
    return re.sub(comment_pattern, "", text)  


    


with open(file_path) as file:
    text = file.read()
    text = remove_comments(text)


    # extract each section and validate individually


    # matches things like: a, b2, c_32
    pattern_list = r'/(\s*\w+,)+\s*\w+\s*/'

    # match sections:
    section_match = r'(?:A:((?:.|\n)*)(?:B:|C:|D:))|(A:(?:.|\n)*$)'

    S = 0
    for e in arr:
        S += e

    # S = functools.reduce(lambda c,b: c+b, range(100))



    for section in section_list:
        results = re.findall(section, text)
        print(results)
        print(len(results))
        print()





# only_one_section_type = 

# s = "Python is fun. python is cool."
# result = re.findall(, s, re.IGNORECASE)
# print(result)



# STATES: q0, q1, q2, q3
# ALPHABET: a,b,c
# START: q0
# FINISH: q1, q2, q3

# TRANSITIONS:
# q0,a -> q1