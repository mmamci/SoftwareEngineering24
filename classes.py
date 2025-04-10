from datetime import datetime

class Person:
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name


class Subject(Person):
    def __init__(self,first_name : str, last_name : str,  sex : str, birth_date : str):
        super().__init__(first_name,last_name)
  
        self.first_name = first_name
        self.last_name = last_name

        try:
          self.__birth_date = datetime.fromisoformat(birth_date)
        except Exception as e:
           print(e)
    
        self.sex = sex

    def estimate_max_hr(self):
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """

        # Can't find a more accurate calculation method for max heartrate.
        if self.sex == "male":
          max_hr_bpm =  223 - 0.9 * self.age_years
        elif self.sex == "female":
          max_hr_bpm = 226 - 1.0 *  self.age_years
        else:
          # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
          max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date

subject = Subject("Moritz", "Mattes", "Male", "2004-12-02")