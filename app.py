"""Flask app for adopt app."""

from pkg_resources import add_activation_listener
from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/', methods=['GET'])
def pets_list():
    """ Display the list of pets """
    pets = Pet.query.all()

    return render_template('pet-list.html', pets=pets)



@app.route('/add', methods=['GET',"POST"])
def pets_add():
    """ GET: Display add pet form
        TODO:
        POST: REcieve FOrm data and..."""

    form = AddPetForm()

    if form.validate_on_submit():
        # TODO: POST Route
        variable = 1

    else:
        return render_template(
            # TODO: Link html template
            "form-add-pet.html", form=form)


