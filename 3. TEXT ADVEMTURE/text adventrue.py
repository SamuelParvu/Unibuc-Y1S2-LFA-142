import yaml, os

# file_name = "TEXT ADVENTURE GAME v1.yaml"
# file_name = "TEXT ADVENTURE GAME v2 - POTION EDITION.yaml"
file_name = "TEXT ADVENTURE GAME v3 - POTION EDITION WITH KEY.yaml"


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

# if transition from a state is not specified we remain in that state
for state in states:
    if state not in transitions:
        transitions[state] = {}
    for symbol in alphabet:
        if symbol not in transitions[state]:
            transitions[state][symbol] = state


# print(transitions)
for t in transitions:
    print(f"{t} : {transitions[t]}")
    print()


def accepts(word):
    current_state = initial_state
    for symbol in word:
        if symbol not in transitions[current_state]:
            return False
        current_state = transitions[current_state][symbol]
    return current_state in final_states

def get_next_state(current_state,symbol):
    return transitions[current_state][symbol]
    

# game_finished = False
c_state = initial_state
while True:
    print("________________________________________________________________")
    print(f"current state: {c_state}")
    for s in alphabet:
        next_possible_state = get_next_state(c_state, s)
        if next_possible_state != c_state:
            print(f"{s} : {next_possible_state}")

    valid_coice = False
    while not valid_coice:
        symbol = input(f"where to move {alphabet}: ")
        valid_coice = symbol in alphabet
    c_state = get_next_state(c_state, symbol)
    

# o singura stare intiala,


# print(accepts('wnwnw')) # TRUE for simple game


# print(accepts(["w", "w", "pick", "e", "n", "w", "n", "w"]))# TRUE - WITH POTION
# print(accepts(["w", "w", "e", "n", "w", "n", "w"])) # FALSE - WITH POTION
