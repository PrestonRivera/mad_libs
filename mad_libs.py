def user_select():
    selection = {
        "adjective": "",
        "nationality": "",
        "person": "",
        "noun": "",
        "adjective2": "",
        "noun2": "",
        "adjective3": "",
        "adjective4": "",
        "plural_noun": "",
    }
    
    for k in selection:
        selection[k] = input(f"Enter a(n) {k}:\n")

    
    return selection

words = user_select()

story = f'''
Pizza was invented by a {words["adjective"]}. {words["nationality"]} chef named {words["person"]}. To make pizza, you need to take a lump of {words["noun"]}, and make a thin, round {words["adjective2"]} {words["noun2"]}. 
Then you cover it with {words["adjective3"]} sauce, {words["adjective4"]} cheese, and fresh chopped {words["plural_noun"]}.

'''


print(story)