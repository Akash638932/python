course={
    'php':{'duration':'3 month','fees':15000},
    'java':{'duration':'2 month','fees':10000},
    'python':{'duration':'1 month','fees':12000},
    
}
#print(course)
course['java']['fees']=20000
#print(course['php'])
print(course['php']['fees'])
for k ,v in course.items():
  #print(k,v )
  print(k,v['duration'],v['fees'])
    