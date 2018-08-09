# Setup Jenkins server for automated systems testing with CI/CD pipeline

1) Spin up Jenkins automation server
```bash
docker-compose up -d
```
2) Install system through GUI on port 8080.
2a) Use "Continue as admin" instead of creating a user
2b) Install suggested plugins
3) Setup the "command core" job
```bash
docker exec -t [DOCKER CONTAINER NAME] bash /var/jenkins_home/cuahsi/jenkins/setup.sh
```