from aws import user_table
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()
SALT = os.environ["JWT_SALT"]

# Blueprints modularize code: define these routes
events = Blueprint("events", __name__)


@events.get("/<string:org>")
def getOrganization(org):
    return "HELLO"
    
@events.get("/<string:id>")
def getID():
    pass

@events.get("/<string:username>")
def getUsername():
    pass

@events.post("/events")
def PostResults():
    pass

@events.post("/sub/<string:id>")
def getSubList():
    pass

@events.post("/checkin/<string:id>")
def getCheckIn():
    pass

@events.delete("/<string:id>")
def deleteEvent():
    pass
