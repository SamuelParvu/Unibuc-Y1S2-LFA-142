import yaml, os

file_name = "gen - propper square brackets.yaml"


base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, file_name)

file = open(path, "r")
data = yaml.safe_load(file)
file.close()

file = open(path, "r")
data = yaml.safe_load(file)
variable_list = data["variable_list"]
terminal_list = data["terminal_list"]
variable_start = data["variable_start"]
rule_list = data["rule_list"]
file.close()


def splice(in_text, index, remove_len, add_text):
    return in_text[:index] + add_text + in_text[index + remove_len:]    

def apply_rule_at_index(in_text, index, variable_len, sub_text):
    return splice(in_text, index, variable_len, sub_text)

def find_all_pos(txt, search_txt):
    res = []
    find_pos = txt.find(search_txt)
    while find_pos != -1:
        res.append(find_pos)
        find_pos = txt.find(search_txt, find_pos + 1)
    return res

def get_rule_child_nodes(in_text, variable, sub_text):
    res = []
    variable_len = len(variable)
    pos_list = find_all_pos(in_text,variable)
    for pos in pos_list:
        res.append(apply_rule_at_index(in_text, pos, variable_len, sub_text));
    return res

# print(generator)

# splice(ui_position_string, pos, len(pos_str), pos_str)

working_text = variable_start
while True :
    print("________________________________________________________________")
    print("________________________________________________________________")
    # GET RULE
    print("current_string:",working_text)
    print("RULES:")
    for rule_index, rule in enumerate(rule_list):
        variable = rule[0]
        sub_text = rule[1]
        print(rule_index,": ", variable, "->", sub_text)
    rule_index_selected = int(input("> Select a rule: "))
    rule = rule_list[rule_index_selected]
    variable = rule[0]
    sub_text = rule[1]

    ## GET POSITION TO APPLY RULE AT
    pos_list = find_all_pos(working_text,variable)
    if len(pos_list) == 0:
        print("choose a different rule!")
        continue

    ui_position_string = "".join([" " for x in working_text])
    for i, pos in enumerate(pos_list):
        idx_str = str(i)
        ui_position_string = splice(ui_position_string, pos, len(idx_str), idx_str)
    print()
    print(working_text)
    print(ui_position_string)
    pos_selected = pos_list[int(input("> select a position: "))]

    #APPLY RULE
    working_text = apply_rule_at_index(working_text, pos_selected, len(variable), sub_text)
    #REPEAT!
