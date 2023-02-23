import requests


def getDefinitions(word_id):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_id}"
    r = requests.get(url)
    res = r.json()
    if 'title' in res:
        return False
    output = {}
    deflar = []

    try:
        senses = res[0]['meanings'][0]['definitions']
        for nouns in senses:
            deflar.append(nouns["definition"])
    except:
        pass
    try:
        senses_verb = res[0]['meanings'][1]['definitions']
        for verbs in senses_verb:
            deflar.append(verbs['definition'])
    except:
        pass
    try:
        senses_adj = res[0]['meanings'][2]['definitions']
        for adjectives in senses_adj:
            deflar.append(adjectives['definition'])

    except:
        pass
    output['def'] = '\n 👉👉'.join(deflar)
    try:
        res[0]['phonetics'][0].get('audio')
        output['audio'] = res[0]['phonetics'][0]['audio']
    except:
        pass

    return output



