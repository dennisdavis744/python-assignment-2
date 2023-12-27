fruit=['apple','blueberry','mulberry','blackberry','strawberry','mango','orange','avacado']
print('first list :',fruit)
newfruit=[]
for E in fruit:
    if "e" in E:
        newfruit.append(E)
        print('new list :',newfruit)