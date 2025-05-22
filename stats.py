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
    
    