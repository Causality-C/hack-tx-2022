from flask import Flask, render_template, request
from auth import auth
from events import events
from organization import organization
import requests

# What we use to render a template, aka our frontend
app = Flask(__name__,template_folder="./")
app.register_blueprint(organization, url_prefix="/organization")
app.register_blueprint(events, url_prefix="/events")
app.register_blueprint(auth, url_prefix="/auth")

def getGeoLocation(location):
   query = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
   res = requests.get(query).json()
   return res

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('index.html')

@app.get("/location/<string:query_string>")
def getLocation(query_string):
   queryRes= getGeoLocation(query_string) # JSON
   response = []

   for res in queryRes:
      response.append({"lat":res['lat'],"lon":res['lon'], "display_name": res['display_name']})

   return response 