from application import db


class Problems(db.Model):
    __tablename__ = 'problem_table'
    id = db.Column(db.Integer, primary_key=True)
    problem_type1 = db.Column(db.String)
    problem_type2 = db.Column(db.String, nullable=False)
    problem_sentence = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    problems_model_columns = [
        'id',
        'problem_type1',
        'problem_type2',
        'problem_sentence',
        'teacher'
    ]


class Github(db.Model):
    __tablename__ = 'github_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tool = db.Column(db.String)
    star = db.Column(db.Integer, default=0)
    description = db.Column(db.String)
    tag = db.Column(db.String)
