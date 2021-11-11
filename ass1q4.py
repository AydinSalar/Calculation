
print("Please enter your test grades.")

test1 = int(input("Test 1: "))
test2 = int(input("Test 2: "))

print("Please enter your quiz grades.")

quiz1 = int(input("Quiz 1: "))
quiz2 = int(input("Quiz 2: "))
quiz3 = int(input("Quiz 3: "))

print("Please enter your homework average.")

hw_avg = float(input("Homework: "))
hw_avg = "{:.2f}".format(hw_avg)

test_avg = int(test1) + int(test2)
test_avg = int(test_avg) / 2
test_avg = "{:.2f}".format(test_avg)

quiz_avg = int(quiz1) + int(quiz2) + int(quiz3)
quiz_avg = int(quiz_avg) / 3
quiz_avg = "{:.2f}".format(quiz_avg)

w_test = float(test_avg) * 0.5
w_quiz = float(quiz_avg) * 0.3
w_hw = float(hw_avg) * 0.2

fin_grd = float(w_test) + float(w_quiz) + float(w_hw)
fin_grd = "{:.2f}".format(fin_grd)

print("Test Average: " + str(test_avg))
print("Quiz Average: " + str(quiz_avg))
print("Fina Grade: " + str(fin_grd))