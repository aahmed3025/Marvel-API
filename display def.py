def display_character(character: dict) -> None:
    print('Name:', character['name'])
    print('Description:', character['description'])
    print('Thumbnail:', character['thumbnail']['path'] + '.' + character['thumbnail']['extension'])
    print('Comics:', character['comics']['available'])
    print('Series:', character['series']['available'])
    print('Stories:', character['stories']['available'])
    print('Events:', character['events']['available'])
    print('---------------------')