import re

def hashtags_to_links(text):
    # Remplace les hashtags trouvés dans la chaîne de caractères par des lien de recherche sur instagram
    def replace_hashtag(match):
        hashtag = match.group()
        link = f'<a href="https://instagram.com/search?q={hashtag}">{hashtag}</a>'
        return link
    
    return re.sub(r'#\w+', replace_hashtag, text)

text = "Je suis #Barreau Sachy #Edvaelle avec des #cheveux 4C"
result = hashtags_to_links(text)
print(result)