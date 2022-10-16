# CheckedIn Developer Guide

## What is CheckedIn?

Checkedin is a platform for organizers that enables a more decentralized check in process. Clients who are attending the event can check in once they are within a proximity of the event on a web application. As well, organizations can have a collection of events that clients can subscribe to and view.

### Image Demonstrations
![unknown1](https://user-images.githubusercontent.com/70402202/196046777-4e5787a7-3933-4e47-89f3-18a3298761e8.png)
![1unknown](https://user-images.githubusercontent.com/70402202/196046778-fd1cd704-a400-42e9-b9bc-8eb2eae77360.png)
![2unknown](https://user-images.githubusercontent.com/70402202/196046779-8639f8aa-ac81-4c3e-a960-92476d803573.png)
![3unknown](https://user-images.githubusercontent.com/70402202/196046780-7096f425-db42-480c-b417-09f16d4f281e.png)
![unknown](https://user-images.githubusercontent.com/70402202/196046781-0c900684-636c-4325-9858-80c1e15683b1.png)



## Overall Program Structure

CheckedIn is largely separated into the backend and frontend in its development. Below is an overall breakdown of the program structure

/frontend

- checkin.html: check in html webpage code
- eventCreation.html: creating event webpage for organizers
- eventInfo.html: viewing event webpage for clients
- index.html: unused code
- joinEvent.html: viewing specific event webpage for organizations
- login.html: login page webpage
- organizationPage.html: homepage for organization
- userPage.html: homepage for users

backend code (spread out in main)

- auth.py : Authentication API calls
- aws.py : API calls to AWS specifically and dynamoDB
- events.py : API calls for specifically events
- main.py: main API calls
- organization.py: Main organization API calls

## Frontend

### Overall Website Structure

![image](https://user-images.githubusercontent.com/70402202/196044901-868deed2-d5d9-41e9-ad12-a2e41bc71cec.png)


### Setup for each html

We organized webpages inside by head, body, and script codes. Scripts are written in JavaScript that handles most of the API calls.

## Backend

below is a overall implemetation of the backend system with the API calls and database sets



### API calls

**_Auth_**
POST*Login() *-> Sends a login request*

POST_register() *-> Sends a register request\_

**_Events_**
GET events/\<org> _-> list org events_

GET events/\<id> _-> returns event keyed by ID_

GET events/\<username> _-> returns events user is_ _signed up for_

POST events _-> calls create event_

POST event/sub/\<id> _-> registering to an event_

POST events/checkin/\<id> _-> check into an event_

DELETE events/\<id> _-> Delete event_


**_Organization_**
GET organization/\<orgName> *-> *returns info of* \<orgName>*

**_User_**
GET user/\<id> _-> gets user info_

---

### Database

## Environment variables
AWS_ACCESS_KEY="[AWS KEY]"

AWS_SECRET_KEY="[AWS secret KEY]"

JWT_SALT='SALT'

JWT_SALT_TWO='SALT_TWO'


## Overall Variables

**_User_**
-Email/username (KEY)

-Password

-subbed_orgs \<List>

-subbed_events \<List>


**_Organization_**
-email / organization_name

-password

-events -> [uids]

-subbed_users

**_Event_**
-Location -> (latitude, longitude)

-time_start

-time_end

-description

-organization

-users_checked_in

-uid

-prompt (after check in)

-event_name

### Noteworthy Things for Database

## Cloud Deployment

Deployment of CheckedIn to a remote server has been tested through two main sources, ngrok and google cloud

### Google Cloud

Deployment on Google Cloud can be done through a basic deployment model. The main thing is to load all the files and run remotely through the Google Cloud Shell. As well, when developing new applications, make sure to rename `app.py` to `main.py` and deploy flask using `flask --app main run`

### Ngrok

Ngrok can be used to deploy the program to any pre-existing server. Install and set up ngrok by creating an account and downloading the binaries. Then, you can use ngrok to forward one of your ports to the internet. We chose to forward port our port 4000 backend to ngrok by typing in `ngrok http 4000`.

## Known Issues

Below are some known issues that we currently have with the program

- Not all map features are figured out
- Geolocation works in theory but is not yet confirmed
- Edge cases and and error has not been fleshed out yet due to time
- Current implementation allows users to sign in multiple times
- Authentication isn't fully fledged out between users and organizations

## Future Implementation Ideas

For developers, here is some future implementation ideas we have:

- Implement SSH functions with iPhone and Android so we can use push notifications
- Have a more comprehensive event page with maybe better prompts
- Using livestreaming of people coming in and location tracking to get distances
- Pair with online purchases to automate event seating
- Mobile app development
