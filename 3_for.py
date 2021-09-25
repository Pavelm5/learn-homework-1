"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
list_scores = [
    {'school_class': '4a', 'scores': [3, 5, 4, 5, 3]},
    {'school_class': '4b', 'scores': [3, 4, 3, 2, 2]},
    {'school_class': '4c', 'scores': [5, 4, 5, 5, 2]}
]
scores_full = 0
sch_scores_sum = list_scores[0]['scores'] + list_scores[1]['scores'] + list_scores[2]['scores']
for score in sch_scores_sum:
    scores_full += score
scores_average = scores_full/len(sch_scores_sum)

print(f"Средняя оценка по школе:", scores_average)

def scores_average():
    
        for class_scores in list_scores:
            scores = class_scores['scores']
            school_class = class_scores['school_class']
            scores_sum = 0

            for score in scores:
                scores_sum += score
            scores_avg = scores_sum / len(scores)
            print(f"Средняя оценка", school_class, scores_avg)
          

     

if __name__ == "__main__":
    scores_average()
