#.Даны две последовательности. Найти элементы, различные для двух
#последовательностей и их среднее арифметическое.

def amogus(chisla1, chisla2):
    elements = set(chisla1).symmetric_difference(set(chisla2))
    aboba = sum(elements) / len(elements) if len(elements) > 0 else 0
    return list(elements), aboba

chisla1 = [1, 2, 3, 4, 5]
chisla2 = [4, 5, 6, 7, 8]

elements, aboba = amogus(chisla1, chisla2)
print("Уникальные элементы:", elements)
print("Среднее арифметическое уникальных элементов:", aboba)
