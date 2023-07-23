# ch 27 OOP
# Containment (aggregation)

class Lesson:
    def __init__(self,t,d,r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__RequiresLab = r

    def OutputLessonDetails(self):
        print("Lesson title is:",self.__LessonTitle)
        print("Duration in min is:",self.__DurationMinutes)
        print("RequiresLab:",self.__RequiresLab)
        
class Assessment: 
    def __init__(self,t,m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m

    def OutputAssessmentDetails(self):
        print("AssessmentTitle is:",self.__AssessmentTitle)
        print("MaxMarks are: ",self.__MaxMarks)
        
class Course:
    def __init__(self, t, m): # sets up a new course
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment # Containment(aggregation)

    def AddLesson(self, t, d, r):
        self.__NumberOfLessons = self.__NumberOfLessons + 1
        self.__CourseLesson.append(Lesson(t, d, r)) # Containment(aggregation)

    def AddAssessment(self, t, m):
        self.__CourseAssessment = Assessment(t, m) # Containment(aggregation)

    def OutputCourseDetails(self):
        print("CourseTitle is:",self.__CourseTitle, "Maximum number of students:", self.__MaxStudents,"Number Of Lessons are:",self.__NumberOfLessons)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
            
        self.__CourseAssessment.OutputAssessmentDetails()
        
def main():
    MyCourse = Course("Computing", 10) # sets up a new course
    MyCourse.AddAssessment("Programming", 100) # adds an assignment
    # add 3 lessons
    MyCourse.AddLesson("Problem Solving", 60, False)
    MyCourse.AddLesson("Programming", 120, True)
    MyCourse.AddLesson("Theory", 60, False)
    # check it all works
    MyCourse.OutputCourseDetails()

main()
