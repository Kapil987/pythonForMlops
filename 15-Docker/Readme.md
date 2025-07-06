## Docker
Docker is a tool that helps developers build, share, run, and verify applications using containers.

### Ec2 Creation
1) Create an ec2 of `t2.small` on aws
2) ssh to the instance using ip and the keyfile
3) Create an account on `Dockerhub` and log in
```bash
cd # change dir
ls -l # list dir/files
cat filename # to view the content of the file
netstat -nptl
```
### Docker Installation
1) [Docker installation on ubuntu](https://docs.docker.com/engine/install/ubuntu/)
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

sudo usermod -aG docker $USER

sudo service docker start
sudo apt install net-tools
```
Re login on the shell

2) Once you logged in onto docker via web , you can search for images you like `nginx`
3) check the pull and other instruction for that image
4) for Docker basic commands refer to [basicDocker](./basicDocker.md)
host port can be different based on the availibility
```bash
docker -v
docker pull docker/getting-started
docker run -d -p 80:80 docker/getting-started

docker pull nginx
docker run -d -p 80:80 nginx
```
check if you can get this working on ec2 with pulic ip

5) `git clone` the 15-Docker and 115.1-Docker-flask-with-db folder on your linux ec2 machine
```bash
docker run -d -p 5000:5000 --name my-running-flask-app flaskapp
docker rm -f $(docker ps -aq)
```
6) Understand 15-Docker project
7) Understand 15.1-Docker project
8) Push the image to docker
```bash
docker login
docker push
docker tag <image_id> myrepo/myimage:tag` – Tag image
docker push
docker pull
```
9) Practice cleanup commands


