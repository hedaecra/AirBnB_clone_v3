#!/usr/bin/python3
""" Main routes of flask app """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """ Return a status of Flask view """
    my_dict = {"status": "OK"}
    return jsonify(my_dict)


@app_views.route('/stats')
def stats():
    """ Return number of each objecs by type """
    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    })
