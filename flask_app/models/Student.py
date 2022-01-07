from ..config.MySQLConnection import connectToMySQL

class Student:
   def __init__(self,data):
      self.id = data['id']
      self.first_name= data['first_name']
      self.last_name = data['last_name']
      self.grade = data['grade']

   def __str__(self) -> str:
      return "" + self.first_name, self.last_name, "grade:", self.grade

   @classmethod
   def get_all(cls):
      query = "SELECT * FROM students"
      students_from_db =  connectToMySQL('school').query_db(query)
      students =[]
      for s in students_from_db:     
         students.append(s)
      return students
   
   @classmethod
   def save(cls, data):
      query = "INSERT INTO students (first_name, last_name, grade) VALUES (%(first_name)s, %(last_name)s, %(grade)s);"
      return connectToMySQL('school').query_db(query, data)