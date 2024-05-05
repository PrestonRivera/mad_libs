adjective = input("Selcet an adjective:\n")
nationality = input("Any nationality:\n")
person = input("Name a person:\n")
noun = input("Selcet a noun:\n")
adjective2 = input("Select a secondary adjective, can be the same as the first adjective if you choose:\n")
noun2 = input("Select a secondary noun, can be the same as the first noun if you choose:\n")




story = f'''
Pizza was invented by a {adjective}. {nationality} chef named {person}. To make pizza, you need to take a lump of {noun}, and make a thin, round {adjective2} {noun2}. 

'''


print(story)