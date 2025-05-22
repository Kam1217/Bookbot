#Count number of words
def count_words(text):
    word_count = len(text.split())
    return word_count

#Counting characters 
def count_characters(text):
    characters_dict = {}
    characters = text.lower()
    for character in characters:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1

    return characters_dict

# { "a": 10, "b": 20 } -> [{"char": "b", "num": 20}, {"char": "a", "num": 10}]   
def sort_character_count(character_count):
    sorted_character_count = []
    
    for char in character_count: 
        num = character_count[char]
        sorted_character_count.append({"char" : char, "num" : num})

    sorted_character_count.sort(reverse=True, key=sort_on)
    return sorted_character_count

def sort_on(character_count):
    return character_count["num"]
        






    
    