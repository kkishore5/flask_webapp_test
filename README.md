# flask based WebApp

###  Flask Docker image to build web from scratch 
$docker build -d flask_webapp .

### Run Flask App using docker

$docker run -d -p 5000:5000 flask_webapp
