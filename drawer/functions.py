def menu():
    members = input(
        'Enter the names of group members separated by commas: ').strip().split(',') # noqa
    themes = input(
        'Enter the themes separated by commas: ').strip().split(',')
    return members, themes
