import matplotlib.pyplot as plt

homework        = [10, 10, 8, 9.5, 3, 9, 0, 6]
midTerm         = [10, 10, 10, 10, 8, 5, 10, 7]
finalProject    = [9, 10, 10, 6, 10, 6, 8, 9]
numStudents     = 8
finalGrade      = []
numFailed       = 0.0
numOutstanding  = 0.0
i               = 0

##Calculates and prints grades, also calculates number of failed/outstanding
for i in range(numStudents):
        var = (0.4 * homework[i] + 0.2 * midTerm[i] + 0.4 * finalProject[i]) * 10
        finalGrade.append(var)
        print 'Student', i + 1, 'final grade:', finalGrade[i], '%'
        if var < 60:                     
            numFailed += 1
        if var > 95:                     
            numOutstanding += 1 

##Prints number of failed and fraction of outstanding
print
print 'Number of students who failed:', numFailed
for i in range(8):
        if finalGrade[i] < 60:
            print 'Student', i + 1, 'failed, final grade:', (finalGrade[i]), '%'

print 'Fraction of outstanding students:', (numOutstanding / numStudents)            

##Graphs the data in a histogram
plt.hist(finalGrade)
plt.title("Students Grades in Percentages")
plt.xlabel("Final Grade Percentage")
plt.ylabel("Number of students")
plt.savefig('ex2.png') 