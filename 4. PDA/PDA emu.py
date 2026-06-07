import os, yaml

file_name = "PDA script - equal a and b.yaml"

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, file_name)

file = open(path, "r")
data = yaml.safe_load(file)
file.close()

EPSILON = data["EPSILON"]
input_alphabet = data["input_alphabet"]
stack_alphabet = data["stack_alphabet"]
states = data["states"]
transitions = data["transitions"]
initial_state = data["initial_state"]
final_states = data["final_states"]

stack = []

def get_next(state, symbol, stack_pop):
    next_state, stack_push = transitions[state][symbol][stack_pop]
    if stack_pop != EPSILON:
        stack.pop()
    if stack_push != EPSILON:
        stack.append(stack_push)
    return next_state
        
def is_accepted(word):
    working_state = initial_state
    for symbol in word:
        if working_state not in transitions:
            return False
        if symbol not in transitions[working_state]:
            return False
        
        if EPSILON in transitions[working_state][symbol]:
            working_state = get_next(working_state,symbol,EPSILON)
        
        elif len(stack) != 0:
            if stack[-1] in transitions[working_state][symbol]:
                working_state = get_next(working_state,symbol,stack[-1])
            else:
                return False
        else:
            return False
    return working_state in final_states

print(is_accepted("aabbaabbb"))

# print(f'accepts("00110") -> {accepts("00110")}') # False
# print(f'accepts("0000") -> {accepts("0000")}') # True