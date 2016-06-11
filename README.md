# acrewstic
Music and media repository for your NAS, written in Python
[![Build Status](https://travis-ci.org/carlomorelli/acrewstic.svg?branch=master)](https://travis-ci.org/carlomorelli/acrewstic)

## About
_acrewstic_ is implemented as a RESTful API using Python 2.7 with Flask library (http://flask.pocoo.org/).
A JS frontend will be provided in the future.

The API is implemented for POST, PUT, GET, DELETE methods. It can be triggered as follows using curl:

Action | Description                       | Triggering with Curl
------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------
GET    | Get the full details of all media | curl -i http://localhost:5000/acrewstic/tasks
GET    | Get the details of specific media | curl -i http://localhost:5000/acrewstic/tasks/<task_nr>
POST   | Insert new media with details     | curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Title"}' http://localhost:5000/acrewstic/tasks
PUT    | Modify details of specific media  | curl -i -H "Content-Type: application/json" -X PUT -d '{"description":"Description"}' http://localhost:5000/acrewstic/tasks/<task_nr>
DELETE | Remove all info of specific media | curl -i -X DELETE http://localhost:5000/myflaskdemo/tasks/<task_nr>


Requirements for the application to run is that Flask is installed on the system (best in a virtualenv sandbox with PIP).
To start the application in a terminal, simply launch

```bash
$ python acrewstic.py
```

### More info
TBD

## Changelog
#### Release 0.1
- Initial release (to be released)
