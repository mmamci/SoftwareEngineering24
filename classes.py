from datetime import datetime
from random import randint
import sys
import requests
import json

class Person:
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      self.id = self.id = last_name[0:3]+first_name[0:3]

    def post(self):
      ## Creata a new person
      # Define the URL of the API
      url = "http://127.0.0.1:5000/person/"

      # added parameter default=str as a quick and dirty fix to save datetime objects
      data_json = json.dumps(self.__dict__, default=str)

      # Send a POST request to the API
      response = requests.post(url, data=data_json)

    

      # Print the response from the server
      print(response.headers['Location'])
      print(response.text)

class Subject(Person):
    def __init__(self,first_name : str, last_name : str,  sex : str, birth_date : str):
        super().__init__(first_name,last_name)
  
        try:
          self.__birth_date = datetime.fromisoformat(birth_date)
        except Exception as e:
           print(e)
           sys.exit()
    
        self.age = datetime.now().year - self.__birth_date.year - (0 if (self.__birth_date.month, self.__birth_date.day)  < (datetime.now().month, datetime.now().day) else 1)
        self.sex = sex

    def estimate_max_hr(self):
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """

        # Can't find a calculation method which uses the exact birthday
        if self.sex == "male":
          max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
          max_hr_bpm = 226 - 1.0 *  self.age
        else:
          # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
          max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)


class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Experiment:
    def __init__(self, date, supervisor, subject, id = randint(0,100000)):
        self.date = date
        self.id = id
        self.supervisor = supervisor
        self.subject = subject