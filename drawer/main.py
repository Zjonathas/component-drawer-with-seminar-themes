import random
from typing import Dict
from typing import List
from functions import menu


while True:
    members, themes = menu()
    if len(members) != len(themes):
        print('Invalid Values')
        continue
    break

drawn: List = []

members_with_themes: Dict[str, str] = {}

while True:
    if not themes and not members:
        for member, theme in members_with_themes.items():
            print(f"Name: {member} | Theme: {theme}")
        break
    drawn_number_members = random.randint(0, len(members) - 1)
    drawn_number_themes = random.randint(0, len(themes) - 1)

    members_with_themes[members[drawn_number_members]] = themes[drawn_number_themes] # noqa

    members.pop(drawn_number_members)
    themes.pop(drawn_number_themes)
