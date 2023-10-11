def gradeScores(FinalGrade):
    if FinalGrade >= 90 and FinalGrade <= 100:
        return("You received an A")

    elif FinalGrade >= 80 and FinalGrade < 90:
        return("You received a B")

    elif FinalGrade >= 70 and FinalGrade < 80:
        return("You received a C")

    elif FinalGrade >= 60 and FinalGrade < 70:
        return("You received a D")

    else:
        return("You received an F")
    
    print(gradeScores(grade(testOne, testTwo, testThree, finalExam)))