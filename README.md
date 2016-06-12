# acrewstic
Music and media repository for your NAS, written in Python
[![Build Status](https://travis-ci.org/carlomorelli/acrewstic.svg?branch=master)](https://travis-ci.org/carlomorelli/acrewstic)

## About
_acrewstic_ is implemented as a RESTful API using Python 2.7 with Flask library (http://flask.pocoo.org/).
A JS frontend will be provided in the future.

The API is implemented for POST, PUT, GET, DELETE methods. It can be triggered as follows using `curl`:

Action | Description                       | Triggering with Curl
------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------
GET    | Get the full details of all media | curl -i http://localhost:5000/acrewstic/tasks
GET    | Get the details of specific media | curl -i http://localhost:5000/acrewstic/tasks/<task>
POST   | Insert new media with details     | curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Title"}' http://localhost:5000/acrewstic/tasks
PUT    | Modify details of specific media  | curl -i -H "Content-Type: application/json" -X PUT -d '{"description":"Description"}' http://localhost:5000/acrewstic/tasks/<task>
DELETE | Remove all info of specific media | curl -i -X DELETE http://localhost:5000/acrewstic/tasks/<task>

PyPI requirements for the application are listed in `requirements.txt` file:

# `flask` - providing the Flask web service library
# `redis` - providing the redis-py package for interfacing the key-value store
# `nose` - providing the reference test engine

Additional requirement is to install the Redis service on the system. If Docker is installed on the system, it is possible to deploy the official Redis image with a single command:

```bash
$ docker run -d redis
```

This command will download (if it is the first launch) and activate detached (parameter `-d`) the service on the background, listening on default port 6379/tcp. Run `docker ps -a` to double check. 
Finally, once dependencies are installed in the system (or in a working virtualenv), to start the application in a terminal simply launch

```bash
$ python acrewstic.py
```

### More info
TBD

## Changelog
#### Release 0.1
- Initial release (to be released)
