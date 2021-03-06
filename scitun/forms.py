from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms.fields import html5


class Student(FlaskForm):
    student_id = fields.StringField(
        "Student ID", validators=[validators.DataRequired()]
    )
    first_name = fields.StringField(
        "First Name", validators=[validators.DataRequired()]
    )
    last_name = fields.StringField("Last Name", validators=[validators.DataRequired()])

    email = html5.EmailField(
        "Email",
        validators=[validators.DataRequired()],
    )


class Lecturer(FlaskForm):

    first_name = fields.StringField(
        "First Name", validators=[validators.DataRequired()]
    )
    last_name = fields.StringField("Last Name", validators=[validators.DataRequired()])

    email = fields.StringField("Email", validators=[validators.DataRequired()])


class AssignStudent(FlaskForm):
    student = fields.SelectField("Students", choices=[])


class Scholarship(FlaskForm):
    name = fields.StringField("Name")
    description = fields.TextAreaField("Description")
    public_date = fields.DateField("Public date", default=date.today())
    close_date = fields.DateField("Close date", default=date.today())
