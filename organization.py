from aws import org_table
import hashlib
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()
SALT = os.environ["JWT_SALT"]

# Blueprints modularize code: define these routes
organization = Blueprint("organization", __name__)


@organization.get("/<string:orgName>")
def getOrganizationName(orgName):
    res = org_table.get_item(Key={"orgname":orgName})['Item']
    del res['password']
    return jsonify(res)

@organization.post("/")
def createOrganization():
    req = request.get_json()
    password_hashed = hashlib.pbkdf2_hmac(
        "sha256", req['password'].encode("utf-8"), b"SALT", 1000
    )
    tb = {"orgname": req['orgname'], "events": [],"subbed_users": [], "password": password_hashed}
    org_table.put_item(Item=tb)
    return "SUCCESS"