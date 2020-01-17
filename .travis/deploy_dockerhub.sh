#!/bin/sh
docker login --username=$DOCKER_USER --password=$DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t zelnovarsky/chbt:"$TAG" .
docker push zelnovarsky/chbt:"$TAG"