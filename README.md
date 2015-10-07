FORMAT: 1A

# Palindrome API

## Introduction
This document is meant to give you a high level overview of the palindrome application. Please look at the table of contents for more details.

## High-level Architecture
This section is meant to give you an overview of how this application is implemented. Below you will find the app's file structure along with a table describing its main components.

        Palindrome
        |-- .elasticbeanstalk
            | -- config.yml
        |-- api
            |-- resources
                |-- message_resource.py
        |-- db
            |-- model.py
            |-- external.py
        |-- templates
        |-- application.py


Name | Description
-----:| -------------
 .elasticbeanstalk | config files for deploying with Elasticbeankstalk
/api/ | REST API definition and exception/error handling.
/db/model.py | Database model.
/db/external.py | Interface for interacting with the database.
/application.py | Main driver that starts up the application.


## Usage

1. Clone the repository.

        $ git clone git@github.com:chuo06/palindrome.git
2. Set up your Python virtualenv and activate it.

        $ virtualenv palindrome
        $ source palindrome/bin/activate

3. Install required packages to run this Flask application.

        $ pip install -r requirements.txt
4. Setup Elastic Beanstalk and deploy your environment.

        $ pip install awsebcli
        $ eb init
        $ eb create

# Group API Blueprint

## Message [/v1/message/{message_id}]

+ Parameters

    + message_id: 1 (number) - The unique identifier of the message.


### Get a Message [GET]
This action retrieves message with id 1. If found in the database, it returns a JSON representation of the message. Otherwise a 404 is returned.

+ Response 200 (application/json)

    + Body

            {"created_on": "2015-10-06T14:13:25",
            "id": 5,
            "is_palindrome": true,
            "message": "Step on no pets",
            "username": "batman"}

+ Response 404 (text/plain)

    + Body

            Message with id: `message_id` was not found.

### Delete a Message [DELETE]
This action deletes a message with id `message_id` from the database. If found in the database, it returns a JSON representation of the newly deleted message. Otherwise a 404 is returned.

+ Response 200 (application/json)

    + Body

            {"created_on": "2015-10-06T14:13:25",
            "id": 5,
            "is_palindrome": true,
            "message": "Step on no pets",
            "username": "batman"}

+ Response 404 (text/plain)

    + Body

            Message with id: `message_id` was not found.


## Messages [/v1/messages]

### List all messages [GET]
This action returns a list of JSON objects representing all the messages in the database. An empty list is returned if there are no messages to show.

+ Response 200 (application/json)

    + Body

            [
                {
                    "created_on": "2015-10-06T14:13:25",
                    "id": 1,
                    "is_palindrome": true,
                    "message": "A Santa at Nasa.",
                    "username": "Santa"
                },
                {
                    "created_on": "2015-10-06T14:58:00",
                    "id": 2,
                    "is_palindrome": true,
                    "message": "A Toyota’s a Toyota.",
                    "username": "Toyota Fan."
                }
            ]


### Post a new message [POST]
This action allows a user to create a new message. If the request is successful, a JSON representation of the newly created message is returned.

+ Parameters

    + username: Bob (string)
    + message: Acrobats stab orca. (string)

+ Request (application/json)

+ Response 200 (application/json)

    + Body

            {
                "created_on": "2015-10-06T14:58:00",
                "id": 1,
                "is_palindrome": true,
                "message": "Acrobats stab orca.",
                "username": "Bob"
            }
