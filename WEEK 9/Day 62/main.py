import csv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app=app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    cafe_loc = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time e.g 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_strength_rating = SelectField(label='Wifi Strength Rating',
                                       choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_socket_availability = SelectField(label='Power Socket Availability',
                                            choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                                            validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("Form Submitted Successfully")

        with open("cafe-data.csv", mode="a", newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow([
                form.cafe.data,
                form.cafe_loc.data,
                form.open_time.data,
                form.closing_time.data,
                form.coffee_rating.data,
                form.wifi_strength_rating.data,
                form.power_socket_availability.data
            ])

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
