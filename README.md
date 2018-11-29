# challenge-service
_Manage the challenges_

[![Build Status](https://travis-ci.org/ytbeepbeep/data-service.svg?branch=master)](https://travis-ci.org/ytbeepbeep/challenge-service)
[![Coverage Status](https://coveralls.io/repos/github/ytbeepbeep/challenge-service/badge.svg?branch=master)](https://coveralls.io/github/ytbeepbeep/challenge-service?branch=master)

_This microservice works on port 5005._

## Install
- `pip install -r requirements.txt`
- `python setup.py develop`


## Run the microservice
`python challengeservice/app.py`

**Important note:** use python 3.6.


## Docker
[![Image size](https://images.microbadger.com/badges/image/ytbeepbeep/challenge-service.svg)](https://microbadger.com/images/ytbeepbeep/challenge-service)
[![Latest version](https://images.microbadger.com/badges/version/ytbeepbeep/challenge-service.svg)](https://microbadger.com/images/ytbeepbeep/challenge-service)

A Docker Image is available on the public Docker Hub registry. You can run it with the command below.

`docker run -d --name challenge-service ytbeepbeep/challenge-service`

**Important note:** if you need to expose the service outside you Docker installation (e.g. to third part services) use the option `-p 5005:5005`

#### Locally
You can also build your own image from this repository.
- Build with `docker build -t ytbeepbeep/challenge-service .`
- Run as usually, with the commands specified above
