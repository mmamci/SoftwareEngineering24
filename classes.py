class Person:
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name


class Subject(Person):
    def __init__(self,first_name, last_name,  sex, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date
    
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

