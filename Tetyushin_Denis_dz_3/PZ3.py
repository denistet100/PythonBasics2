#3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#.items;.keys; .values

dictionary = { "И":['Иван', 'Илья'], "Д":['Денис', 'Дима'], "М":['Марина'], "Р":['Ринат'], "П":['Пётр'], "О":['Олья']}

#print(sorted(dictionary, key = dictionary.get))

def thesaurus(wrd):

    resalt = dictionary

    for i in wrd:
        
        key = i[0].capitalize() #первая буква
        
        #if key not in resalt:
            #resalt[key] = []
        #resalt[key].append(i)
    #return resalt

    #for dictionary.keys(key):
        print(dictionary.items(key))
        #print('"', key, ': ', val)
        #for key in sonted(dictionary.key()):
            #print('"', key, '": ', val)


names = ["Иван", "Мария", "Петр", "Илья"]

#print(thesaurus(names))
thesaurus(names)
 
