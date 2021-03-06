# coding: utf-8
 
# z3-solver games

from z3 import *
 
def main(): 

    a = [1,2,3]

    s = Solver()
    x = Int('x')
    s.add(Or([x == i for i in a]))

    # Enumerate all possible solutions:
    while True:
        r = s.check()
        if r == sat:
            m = s.model()
            print(m)
            s.add(x != m[x])
        else:
            print(r)
            break

    ### approach2

    x = Int('x')
    y = Int('y')
    print(solve(x > 2, y < 10, x + 2*y == 7))
	
    person = list()

    # TODO modify for writing database as csv
    fieldnames = ["Age", "Male", "Salary (k)"]

    s = Solver()
    age = IntVector('age', 10)
    male = BoolVector('male', 10)
    salary = IntVector('salary', 10)

    s.add([18 <= age[i] for i in range(10)])
    s.add([100 >= age[i] for i in range(10)])
    s.add([20 <= salary[i] for i in range(10)])
    s.add([100 >= salary[i] for i in range(10)])

    s.add(Sum([If(And(male[i] == True, True), age[i], 0) for i in range(10)]) / (4) == 59)
    
    # Printing the mean 
    print("Mean is :", x)

    for i in range(10):
        if s.check() == sat:
            model = s.model()
            person.append([model[age[i]], model[male[i]], model[salary[i]]])
            s.add(Or(age[i] != model[age[i]], male[i] != model[male[i]], salary[i] != model[salary[i]]))

    for j in person:
        data = {fieldnames[0]: j[0]}
        data[fieldnames[1]] = j[1]
        data[fieldnames[2]] = j[2]

        print(data)
    
    print(s.check())

    return 0


if __name__ == "__main__": 
	main() 
