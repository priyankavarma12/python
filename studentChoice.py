class Student:
    stuCount = 0

    def __init__(self, fname, lname, subject, grade):
        self.fname = fname
        self.lname = lname
        self.subject = subject
        self.grade = grade
        Student.stuCount += 1

    def displayStudentCount(self):
         print('Total Amount of Students is %d' % (Student.stuCount))

    def studentInformation(self):
         print('First Name : ' + self.fname + '\n' + 'Last Name : ' + self.lname + '\n'
               + 'Subject : '+ self.subject + '\n' + 'Grade : '+ self.grade)

print('Usage...\nq -- Quit the Program\nAdd -- Add a Student to class\nDisplay -- Display last Student Information\nstudents count -- Amount of students')

while True:
      option = input('Enter the Option you Desire: ')
      if option == 'q':
          break
      elif option == 'Add':
          first_name = input('Enter Student Name : ')
          last_name = input('Enter Students Last Name : ')
          subject = input('Enter The Subject of the Exam: ')
          mark = input('Enter Students Grade: ')
          student = Student(first_name, last_name, subject, mark)
      elif option == 'Display':
          student.studentInformation()
      elif option == 'students count':
          print('Total Amount of Students is %d '% (Student.stuCount))
    
