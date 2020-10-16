## CloudGraphr

Diagrams as Code... As A Service

Azure function that lets you draw a cloud architectures using json definitions

Basically a service wrapper for [MinGrammer](https://diagrams.mingrammer.com/)

## Docker Commands

docker build --pull --rm -f "Dockerfile" -t cloudgraphr:latest "."

docker run --name cloudgraphr -p 8000:80 cloudgraphr:latest

