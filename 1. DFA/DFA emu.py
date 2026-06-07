import os, yaml, sys


# if len(sys.argv) > 1 :
#     path = sys.argv[1]
# else:
#     file_name = "DFA script - even length.yaml"

#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     path = os.path.join(base_dir, file_name)


file_name = "DFA script - even length.yaml"

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, file_name)

file = open(path, "r")
data = yaml.safe_load(file)
file.close()

alphabet = data["alphabet"]
states = data["states"]
transitions = data["transitions"]
initial_state = data["initial_state"]
final_states = data["final_states"]

def accepts(string):
    current_state = initial_state
    for symbol in string:
        current_state = transitions[current_state][symbol]
    return current_state in final_states


print(f'accepts("00110") -> {accepts("00110")}') # False
print(f'accepts("0000") -> {accepts("0000")}') # True