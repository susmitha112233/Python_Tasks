"""7. Student Result Generator (Method Overloading Concept)
A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subjects"""

class Result:
    def calculate(self, a, b, c=0):
        total = a + b + c
        print("Total Marks:", total)

        if c == 0:
            print("Average:", total / 2)
        else:
            print("Average:", total / 3)


r = Result()

r.calculate(80, 90)
r.calculate(80, 90, 70)
