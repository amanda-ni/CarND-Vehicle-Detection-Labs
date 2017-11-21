import sliding_window
import sliding_window_solution 

windows_answer = set( sliding_window.windows )
windows_solution = set( sliding_window_solution.windows )

all_answers_in_solution = True
all_solutions_in_answer = True

print("Checking answer in solutions")
for window in windows_answer:
    if not window in windows_solution:
        all_answers_in_solution = False
        print("{} not in solution".format(window))

print("Now checking solution windows in answer")

for window in windows_solution:
    if not window in windows_answer:
        all_solutions_in_answer = False
        print("{} not in answer".format(window))
        break

if all_answers_in_solution and all_solutions_in_answers:
    print("The two implementations are equivalent")
else:
    print("These two functions do not do the same thing")
    if all_answers_in_solution:
        print("BUT your answer is a SUBSET of the solution")
    else:
       print("BUT the solution is a SUBSET of the answer")

