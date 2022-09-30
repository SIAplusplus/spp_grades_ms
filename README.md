# spp_grades_ms
Microservice of grades.
## Requirements
### DATABASE 
* docker build -t spp_grades_db .
* docker run -d -t -i -p 3306:3306 --name spp_grades_db spp_grades_db
* docker run --name db_client -d --link spp_grades_db:db -p 8081:80 phpmyadmin
## MICROSERVICE
* docker build -t spp_grades_ms .
* docker run -p 4000:4000 -e DB_HOST=host.docker.internal -e DB_PORT=3306 -e DB_USER=admin -e DB_PASSWORD=123456 -e DB_NAME=spp_grades_db -e URL=0.0.0.0:4000 spp_grades_ms
