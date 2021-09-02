from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

application = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    @application.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print(name, " ", email, " ", password)

        if form.validate():

            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('hello.html', form=form)


if __name__ == "__main__":
    application.run()
