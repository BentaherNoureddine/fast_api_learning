from model.Person import PersonModel


class ProfessorModel(PersonModel):
    years_of_experience: int
    department: str
