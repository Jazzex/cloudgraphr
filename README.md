## CloudGraphr

Diagrams as Code... As A Service

Azure function that lets you draw a cloud architectures using json definitions

Basically a service wrapper for [MinGrammer](https://diagrams.mingrammer.com/)

## Docker Commands

docker build --pull --rm -f "Dockerfile" -t allediagrams:latest "."

docker run --name allediagrams -p 8000:80 allediagrams:latest