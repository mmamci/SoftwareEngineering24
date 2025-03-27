from classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    supervisor = Supervisor("Moritz", "Mattes")
    subject = Subject("male", 40)
    experiment = Experiment("Leistungstest", "27.03.2025")


    print(subject.estimate_max_hr())
    print(experiment.__dict__)