import re

tutors = ["Tim","Nicky", "Ben", "Smerity"]
lectueres = ["Sarah", "Catherine", "Katie", "Mark"]
G2 = ["Olivia", "Liz", "Zac", "Rob"]

def no_query_on_enter_state(data):
    print("I am NCSS assistant. How may I help you?")
    
def on_input_no_query(text, data):
    matchforperson = "Which group is (?P<name>\w*) in\?"
    #to find the group someone is in
    match =  re.match(matchforperson, text)
    if match:
        person = match.group('name')
        if person in G2:
            return "has_group_on_enter", person

def has_group_on_enter(person):
    print(f"{person} is in group 2.")

state =  "NO QUERY"
data = None
while state != "END":
    if state == "NO QUERY":
        no_query_on_enter_state(data)
    elif state == 
    text = input("> ")
    state, data = on_input_no_query(text, data)
    print(state, data)