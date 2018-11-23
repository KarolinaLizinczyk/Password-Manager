# Password-Manager
Password-Manager is a simple, small and secure password manager application which allows you to store your credentials for various websites.

## Functionalities
* Log in with your username/password
* Add an entry
* Update an entry
* Delete an entry
* View a list of entries and their details
* Link generation with 5 minute expiration timer to access a single entry

## Built With
* Python/Flask
* HTML
* Bootstrap

## Design Notes
* I decided to develop this application with Flask framework, because it is simple and documentation as well as developer tools are excellent
* To build this application I used Flask instead of pure Python, because it helped me implement backend logic very fast in a way that it took care of all repetitve tasks.
* Django together with Flask are two the most popular frameworks, however in contrast to Django, Flask gave me the opportunity to choose modules and decide how to interact with them. Django follows a "bateries included" philosophy, which means that is gives you a lot more at the beginning.
* I decided to use PostgreSQL as it is production type of database and is popular in Python communities
* I decided to use Bootstrap for this project as it is simple, has extensive list of components as well as base styling for most of Html elements. In this project visual aspect was not the key part, so I chose bootstap because it helped me implement viusals quickly.
* To set up project folder structure I used app based structure, which means things are grouped by application. This pattern is used by default in Django.
* The application was built with accordance to the best practices for Python and follows PEP8, when sensible.

## Setup Instructions
* Use this link: https://passmngr.herokuapp.com/