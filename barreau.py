import re

def lyen(text):
    # Remplace les hashtags trouvés dans la chaîne de caractères par des lien de recherche sur instagram
    def funhashtag(x):
        hashtag = x.group()
        link = f'<a href="https://instagram.com/search?q={hashtag}">{hashtag}</a>'
        return link
    
    return re.sub(r'#\w+', funhashtag, text)

text = "Je suis #Barreau Sachy #Edvaelle avec des #cheveux 4C"
rezilta= lyen(text)
print(rezilta)
