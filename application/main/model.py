from application import db


class Problems(db.Model):
    __tablename__ = 'problem_table'
    id = db.Column(db.Integer, primary_key=True)
    problem_type1 = db.Column(db.String)
    problem_type2 = db.Column(db.String)
    problem_sentence = db.Column(db.String)
    teacher = db.Column(db.String)
    problems_model_columns = [
        'id',
        'problem_type1',
        'problem_type2',
        'problem_sentence',
        'teacher'
    ]
