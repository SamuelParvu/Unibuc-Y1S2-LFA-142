import yaml, os

file_name = "NFA script - find ab.yaml"

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, file_name)

file = open(path, "r")
data = yaml.safe_load(file)
file.close()

alphabet = data["alphabet"]
EPSILON = data["EPSILON"]
states = data["states"]
transitions = data["transitions"]
initial_state = data["initial_state"]
final_states = data["final_states"]

alphabet.append(EPSILON)


# for current state
# get epsilon and add to working state?
# the full state also keep track of input pos

def get_next_move_set(move_set):
    is_accepted = False
    next_move_set = set()
    for state, word in move_set:
        symbol_map = transitions[state]    
        if(EPSILON in symbol_map):
            # next_move_list = [(next_state, input) for next_state in symbol_map[EPSILON]]
            # next_move_set.update(next_move_list)
            for next_state in symbol_map[EPSILON]:
                next_move = (next_state, word)
                next_move_set.add(next_move)
        
        if len(word) > 0:
            symbol = word[0]
            if symbol in symbol_map:  
                for next_state in symbol_map[symbol]:
                    next_move = (next_state, word[1:])
                    next_move_set.add(next_move)
        else:
            if state in final_states:
                is_accepted = True
    return (next_move_set, is_accepted)



def word_is_accepted(word):
    working_move_set = set()
    working_move_set.add((initial_state, word))
    accepted = False
    max_depth = 100000
    i = 0
    while i < max_depth and not accepted: # may go on forever so i can't really let it
        print(f"Dept: {i} move_set:{working_move_set}")
        working_move_set, accepted = get_next_move_set(working_move_set)
        i += 1
        print()
    return accepted


print("ACCEPTED" if word_is_accepted("cccabacc") else "REJECTED!")


# def get_next_state_set(state_set,symbol):
#     next_state_set = set()
#     for state in state_set:
#         symbol_map = transitions[state]    
#         if(EPSILON in symbol_map):
#             next_state_set.update(symbol_map[EPSILON])
        
#         if(symbol in symbol_map):
#             next_state_set.update(symbol_map[symbol])
            
#     return next_state_set