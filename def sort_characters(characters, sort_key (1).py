def sort_characters(characters, sort_key):
    from typing import List

    def sort_characters(characters: List[dict], sort_key: str) -> List[dict]:
        return sorted(characters, key=lambda c: c[sort_key])