best_class =[
    {
    "school_class" : "6a",
    'scores_6a' : [5, 5, 5]
    },
    {
    "worse_class" : "5c",
    'scores_5c' : [2, 2, 2]
    }
]

list_6a = best_class[0]['scores_6a']
list_5c = best_class[1]['scores_5c']
pupils_class6a = len(list_6a)
pupils_class5c = len(list_5c)   
all_pupils = pupils_class6a + pupils_class5c
print(all_pupils)

scores_6a = 0
for score in list_6a:
    scores_6a = scores_6a + score
result_6a = scores_6a / pupils_class6a
print(result_6a)

scores_5c = 0
for score in list_5c:
    scores_5c = scores_5c + score
result_5a = scores_5c / pupils_class5c
print(result_5a)

scores_all = scores_5c + scores_6a

result_all = scores_all / all_pupils
print(result_all)



