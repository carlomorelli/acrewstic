# acrewstic
Music and media repository for your NAS, written in Python
[![Build Status](https://travis-ci.org/carlomorelli/acrewstic.svg?branch=master)](https://travis-ci.org/carlomorelli/acrewstic)
[![Coverage Status](https://coveralls.io/repos/github/carlomorelli/acrewstic/badge.svg?branch=master)](https://coveralls.io/github/carlomorelli/acrewstic?branch=master)


## About
_acrewstic_ is implemented as a RESTful API using Python3 with Flask library (http://flask.pocoo.org/).
A JS frontend will be provided in the future.

The API is implemented for POST, PUT, GET, DELETE methods. It can be triggered as follows using `curl`:

Action | Description                       | Triggering with Curl
------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------
GET    | Get the full details of all media | `curl -i http://localhost:5000/acrewstic/tasks`
GET    | Get the details of specific media | `curl -i http://localhost:5000/acrewstic/tasks/_tasknr_`
POST   | Insert new media with details     | `curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Title"}' http://localhost:5000/acrewstic/tasks`
PUT    | Modify details of specific media  | `curl -i -H "Content-Type: application/json" -X PUT -d '{"description":"Description"}' http://localhost:5000/acrewstic/tasks/_tasknr_`
DELETE | Remove all info of specific media | `curl -i -X DELETE http://localhost:5000/acrewstic/tasks/_tasknr_`

PyPI requirements for the application are listed in `requirements.txt` file:

* `flask` provides the web service library
* `redis` is the redis-py package which allows interfacing the key-value store
* `py.test` is the reference test engine


## Running with Docker and Docker-compose

A strong requirement is to install the Redis service on the system.  If Docker is installed on the system (see next section), it is possible to deploy a container of the official Redis image with a single command:

```bash
$ docker run -d redis
```
This command will download (if it is the first launch) and activate detached (parameter `-d`) the service on the background, listening on default port 6379/tcp. Run `docker ps -a` to double check. 

In the codebase a `Dockerfile` is available for also packaging the _acrewstic_ application. To create an image, and then run a container of it, run:

```bash
$ docker build -t acrewstic .
$ docker run -d -p 5000:5000 acrewstic
```

In addition to the `Dockerfile`, a `docker-compose.yml` script is also available for turning on and off both images in an orchestrated way when `docker-compose` is installed on the system (see https://github.com/docker/compose):

```bash
$ docker-compose up -d
$ docker-compose down
```

To verify that the the app is working correctly, including the bridge to Redis, launch:

```bash
$ curl -i http://localhost:5000/acrewstic/version
```


### More info
TBD

## Changelog
#### Release 0.1
- Initial release (to be released)
