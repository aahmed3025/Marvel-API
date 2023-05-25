from typing import List, Dict

def filter_characters(characters: List[Dict], filter_name: str) -> List[Dict]:
    filtered_characters = []
    for character in characters:
        if filter_name.lower() in character['name'].lower():
            filtered_characters.append(character)
    return filtered_characters
