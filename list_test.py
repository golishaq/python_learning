spam = ['apples',	'bananas',	'tofu',	'cats']

def list_spell(list):
    xxx = list[0]
    berofe = list[-1]
    print(berofe)
    for word in list:
        if word != berofe:
            xxx = xxx + ", "+ word
        else:
            xxx =xxx + " and " + word
    print(xxx)
def merge(list):
  return ', '.join(list[:-1] + ['and '+list[-1]])
print(merge(spam))