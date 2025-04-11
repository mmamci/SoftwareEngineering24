from classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    supervisor = Supervisor("Moritz", "Mattes")
    subject = Subject("Linus","Torvalds", "male", "1969-04-28")
    experiment = Experiment("27.03.2025", supervisor, subject)

    subject.post()